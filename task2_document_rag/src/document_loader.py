
from pathlib import Path

from pypdf import PdfReader
from langchain_core.documents import Document


def load_pdf(file_path: str | Path) -> list[Document]:
    """Load PDF pages and preserve source and page metadata."""

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"PDF not found: {path}")

    if path.suffix.lower() != ".pdf":
        raise ValueError("The input file must be a PDF.")

    reader = PdfReader(str(path))
    documents = []

    for page_number, page in enumerate(reader.pages):
        text = page.extract_text() or ""

        if text.strip():
            documents.append(
                Document(
                    page_content=text,
                    metadata={
                        "source": str(path.resolve()),
                        "page": page_number,
                    },
                )
            )

    if not documents:
        raise ValueError("The PDF contains no extractable text.")

    return documents
