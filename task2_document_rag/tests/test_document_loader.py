
from pathlib import Path

import pytest

from src.document_loader import load_pdf


DOCUMENTS_DIR = Path(__file__).resolve().parents[1] / "documents"
SAMPLE_PDF = DOCUMENTS_DIR / "sample_guide.pdf"


def test_pdf_loads_three_pages():
    pages = load_pdf(SAMPLE_PDF)

    assert len(pages) == 3


def test_page_metadata_is_preserved():
    pages = load_pdf(SAMPLE_PDF)

    assert pages[0].metadata["page"] == 0
    assert pages[1].metadata["page"] == 1
    assert pages[2].metadata["page"] == 2


def test_page_content_is_extracted():
    pages = load_pdf(SAMPLE_PDF)

    assert "Variables" in pages[0].page_content
    assert "Lists" in pages[1].page_content
    assert "Functions" in pages[2].page_content


def test_missing_pdf_raises_error():
    with pytest.raises(FileNotFoundError):
        load_pdf(DOCUMENTS_DIR / "missing.pdf")


def test_non_pdf_file_is_rejected(tmp_path):
    text_file = tmp_path / "guide.txt"
    text_file.write_text("Not a PDF", encoding="utf-8")

    with pytest.raises(ValueError):
        load_pdf(text_file)
