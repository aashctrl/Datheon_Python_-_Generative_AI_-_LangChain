import pytest

from src.prompts import (
    build_invoice_prompt,
    build_resume_prompt,
)


def test_resume_prompt_contains_input():
    prompt = build_resume_prompt(
        "Priya Sharma knows Python and SQL."
    )

    assert "Priya Sharma" in prompt
    assert "Python and SQL" in prompt


def test_invoice_prompt_contains_input():
    prompt = build_invoice_prompt(
        "Invoice INV-1001, total INR 1250."
    )

    assert "INV-1001" in prompt
    assert "INR 1250" in prompt


def test_empty_resume_is_rejected():
    with pytest.raises(ValueError):
        build_resume_prompt("   ")


def test_empty_invoice_is_rejected():
    with pytest.raises(ValueError):
        build_invoice_prompt("")
