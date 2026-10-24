import pytest
from pydantic import ValidationError
from src.schemas import ResumeData
from src.schemas import InvoiceData

def test_valid_resume():
    resume = ResumeData(
        name="Priya Sharma",
        email="priya@example.com",
        skills=["Python", "SQL"],
        experience_years=2,)
    assert resume.name == "Priya Sharma"
    assert resume.email == "priya@example.com"
    assert resume.skills == ["Python", "SQL"]
    assert resume.experience_years == 2

def test_missing_optional_fields():
    resume = ResumeData(name="Priya Sharma")
    assert resume.email is None
    assert resume.skills == []
    assert resume.experience_years is None

def test_negative_experience_is_rejected():
    with pytest.raises(ValidationError):
        ResumeData(
            name="Priya Sharma",
            experience_years=-2,)

def test_empty_name_is_rejected():
    with pytest.raises(ValidationError):
        ResumeData(name="   ")

def test_unknown_fields_are_rejected():
    with pytest.raises(ValidationError):
        ResumeData(
            name="Priya Sharma",
            unexpected_field="not allowed",)

def test_valid_invoice():
    invoice = InvoiceData(
        invoice_number="INV-1001",
        vendor="ABC Supplies",
        invoice_date="2026-10-20",
        currency="INR",
        total_amount=1250.50,)

    assert invoice.invoice_number == "INV-1001"
    assert invoice.vendor == "ABC Supplies"
    assert invoice.total_amount == 1250.50

def test_missing_invoice_fields():
    invoice = InvoiceData()

    assert invoice.vendor is None
    assert invoice.total_amount is None

def test_negative_invoice_total_is_rejected():
    with pytest.raises(ValidationError):
        InvoiceData(total_amount=-100)

def test_unknown_invoice_fields_are_rejected():
    with pytest.raises(ValidationError):
        InvoiceData(unexpected_field="not allowed")