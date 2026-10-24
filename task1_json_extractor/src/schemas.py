from pydantic import BaseModel, ConfigDict, Field, field_validator

class ResumeData(BaseModel):
    """Structured information extracted from a resume."""
    model_config = ConfigDict(extra="forbid")
    name: str = Field(description="Full name of the candidate")
    email: str | None = Field(default=None, description="Email address, or null if unavailable")
    skills: list[str] = Field(default_factory=list, description="Technical and professional skills")
    experience_years: float | None = Field(default=None,ge=0,description="Years of professional experience, or null if unknown")

    @field_validator("name")
    @classmethod
    def name_must_not_be_empty(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Name cannot be empty")
        return value

    @field_validator("email")
    @classmethod
    def normalize_email(cls, value: str | None) -> str | None:
        if value is None:
            return None
        value = value.strip()
        return value or None

class InvoiceData(BaseModel):
    """Structured information extracted from an invoice."""
    model_config = ConfigDict(extra="forbid")
    invoice_number: str | None = Field(
        default=None,
        description="Invoice identifier, or null if unavailable",)
    vendor: str | None = Field(
        default=None,
        description="Vendor or supplier name, or null if unavailable",)
    invoice_date: str | None = Field(
        default=None,
        description="Invoice date as written in the document",)
    currency: str | None = Field(
        default=None,
        description="Currency code, such as INR or USD, if identifiable",)
    total_amount: float | None = Field(
        default=None,
        ge=0,
        description="Final invoice total, or null if unavailable",)