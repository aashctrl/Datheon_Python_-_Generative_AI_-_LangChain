
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, ValidationError

from src.prompts import (
    INVOICE_SYSTEM_PROMPT,
    SYSTEM_PROMPT,
    build_invoice_prompt,
    build_resume_prompt,
)
from src.schemas import InvoiceData, ResumeData


load_dotenv()


def _prepare_gemini_schema(schema: dict) -> dict:
    """Remove schema keywords unsupported by our Gemini request."""

    cleaned_schema = {}

    for key, value in schema.items():
        if key == "additionalProperties":
            continue

        if isinstance(value, dict):
            cleaned_schema[key] = _prepare_gemini_schema(value)
        elif isinstance(value, list):
            cleaned_schema[key] = [
                _prepare_gemini_schema(item)
                if isinstance(item, dict)
                else item
                for item in value
            ]
        else:
            cleaned_schema[key] = value

    return cleaned_schema


def _generate_structured_data(
    text: str,
    system_prompt: str,
    schema_model: type[BaseModel],
) -> BaseModel:
    """Generate structured data with Gemini and validate it locally."""

    api_key = os.getenv("GEMINI_API_KEY")
    model = os.getenv("GEMINI_MODEL")

    if not api_key or not model:
        raise RuntimeError(
            "Check GEMINI_API_KEY and GEMINI_MODEL in your .env file."
        )

    client = genai.Client(api_key=api_key)

    gemini_schema = _prepare_gemini_schema(
        schema_model.model_json_schema()
    )

    response = client.models.generate_content(
        model=model,
        contents=text,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            response_mime_type="application/json",
            response_schema=gemini_schema,
            temperature=0,
        ),
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response.")

    try:
        return schema_model.model_validate_json(response.text)
    except ValidationError as exc:
        raise RuntimeError(
            "Gemini returned data that failed validation."
        ) from exc


def extract_resume(resume_text: str) -> ResumeData:
    """Extract and validate structured information from a resume."""

    if not resume_text.strip():
        raise ValueError("Resume text cannot be empty.")

    prompt = build_resume_prompt(resume_text)

    result = _generate_structured_data(
        text=prompt,
        system_prompt=SYSTEM_PROMPT,
        schema_model=ResumeData,
    )

    return result


def extract_invoice(invoice_text: str) -> InvoiceData:
    """Extract and validate structured information from an invoice."""

    if not invoice_text.strip():
        raise ValueError("Invoice text cannot be empty.")

    prompt = build_invoice_prompt(invoice_text)

    result = _generate_structured_data(
        text=prompt,
        system_prompt=INVOICE_SYSTEM_PROMPT,
        schema_model=InvoiceData,
    )

    return result
