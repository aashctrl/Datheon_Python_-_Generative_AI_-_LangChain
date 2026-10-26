
import pytest
from langchain_core.documents import Document

from src.text_splitter import split_documents


def test_splitting_creates_smaller_chunks():
    document = Document(
        page_content="Python is useful. " * 100,
        metadata={"source": "sample.pdf", "page": 0},
    )

    chunks = split_documents(
        [document],
        chunk_size=100,
        chunk_overlap=20,
    )

    assert len(chunks) > 1
    assert all(len(chunk.page_content) <= 100 for chunk in chunks)


def test_metadata_is_preserved():
    document = Document(
        page_content="Python programming and data analysis.",
        metadata={"source": "sample.pdf", "page": 2},
    )

    chunks = split_documents([document])

    assert chunks
    assert all(chunk.metadata["source"] == "sample.pdf" for chunk in chunks)
    assert all(chunk.metadata["page"] == 2 for chunk in chunks)


def test_start_index_is_added():
    document = Document(
        page_content="Python programming. " * 30,
        metadata={"page": 0},
    )

    chunks = split_documents([document])

    assert all("start_index" in chunk.metadata for chunk in chunks)


def test_invalid_chunk_size_is_rejected():
    document = Document(page_content="Python")

    with pytest.raises(ValueError):
        split_documents([document], chunk_size=0)


def test_invalid_overlap_is_rejected():
    document = Document(page_content="Python")

    with pytest.raises(ValueError):
        split_documents([document], chunk_size=100, chunk_overlap=100)
