
from pathlib import Path

from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document

from src.config import EMBEDDING_MODEL, GEMINI_API_KEY


def create_embeddings() -> GoogleGenerativeAIEmbeddings:
    """Create the Google Gemini embedding model."""

    if not GEMINI_API_KEY:
        raise RuntimeError("GEMINI_API_KEY is not configured.")

    return GoogleGenerativeAIEmbeddings(
        model=EMBEDDING_MODEL,
        google_api_key=GEMINI_API_KEY,
    )


def build_vector_store(
    chunks: list[Document],
    persist_directory: str | Path = "chroma_db",
) -> Chroma:
    """Embed document chunks and store them in ChromaDB."""

    if not chunks:
        raise ValueError("Cannot build a vector store with no chunks.")

    embeddings = create_embeddings()

    return Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(persist_directory),
        collection_name="document_qa",
    )
