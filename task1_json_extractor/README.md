# Task 1: Structured LLM Prompt Pipeline & JSON Extractor

## Overview

This project implements a Python-based information extraction pipeline using Google's Gemini API and Pydantic. It converts unstructured resume and invoice text into structured JSON data that can be validated and used by other applications.

The project demonstrates prompt engineering, few-shot prompting, LLM API integration, structured output generation, schema validation, and automated testing.

## Features

- Extract structured information from resumes and invoices.
- Use reusable prompt templates and extraction instructions.
- Generate JSON responses using the Gemini API.
- Validate responses using Pydantic models.
- Handle missing information without intentionally inventing values.
- Reject invalid fields and negative numerical values.
- Keep API credentials in environment variables.
- Run automated tests without requiring a live API call for every test.

## Technology Stack

- Python
- Google Gemini API (`google-genai`)
- Pydantic
- python-dotenv
- pytest

## Project Structure

```text
task1_json_extractor/
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── schemas.py
│   ├── prompts.py
│   └── extractor.py
├── tests/
│   ├── test_schemas.py
│   └── test_prompts.py
├── examples/
│   ├── sample_resume.txt
│   └── sample_invoice.txt
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Install Python

Install a compatible Python version and ensure Python and pip are available from your terminal.

### 2. Install dependencies

From the `task1_json_extractor` directory, run:

```bash
pip install -r requirements.txt
```

### 3. Configure the Gemini API

Create a Gemini API key through Google AI Studio.

Copy `.env.example` to `.env` and configure:

```dotenv
GEMINI_API_KEY=your_actual_api_key
GEMINI_MODEL=your_available_gemini_model
```

Replace the placeholders with valid values. Never commit the actual `.env` file or expose your API key.

### 4. Run resume extraction

From the `task1_json_extractor` directory, run:

```bash
python -m src.main
```

The program reads `examples/sample_resume.txt`, calls Gemini, validates the response, and prints the resulting JSON.

### 5. Run invoice extraction

Use the sample invoice with the extraction function:

```bash
python -c "from pathlib import Path; from src.extractor import extract_invoice; print(extract_invoice(Path('examples/sample_invoice.txt').read_text(encoding='utf-8')).model_dump_json(indent=2))"
```

The result includes the invoice number, vendor, date, currency, and total amount when those fields can be extracted.

### 6. Run automated tests

From the `task1_json_extractor` directory, execute:

```bash
python -m pytest tests -v
```

The test suite covers schema validation, optional fields, invalid values, unexpected fields, and prompt construction. These tests do not require live Gemini calls.

## Example Output

A successful resume extraction may return:

```json
{
  "name": "Priya Sharma",
  "email": "priya@example.com",
  "skills": [
    "Python",
    "SQL",
    "Flask",
    "Pandas",
    "NumPy",
    "Git"
  ],
  "experience_years": 2.0
}
```

## Implementation Workflow

1. Accept unstructured resume or invoice text.
2. Build a document-specific prompt.
3. Send the prompt to Gemini with a JSON response schema.
4. Parse the generated JSON.
5. Validate the result using the corresponding Pydantic model.
6. Return the validated structured data or report an error.

## Limitations

- Extraction accuracy depends on the quality and completeness of the input text.
- LLM-generated values should be reviewed for important business decisions.
- The current invoice schema captures selected fields and does not calculate or independently verify invoice totals.
- Schema validation ensures data structure and configured constraints, but does not prove that every extracted value is factually correct.
- A valid Gemini API key, model access, and available API quota are required for live extraction.

## Future Improvements

- Add document upload support.
- Expand invoice field coverage.
- Add retry strategies for transient API failures.
- Improve email and date validation.
- Add structured logging and extraction evaluation metrics.
- Integrate the extractor into a Streamlit application.

## Internship

**Program:** Python + Generative AI + LangChain Internship  
**Task:** Structured LLM Prompt Pipeline & JSON Extractor  
**Provider:** Google Gemini API