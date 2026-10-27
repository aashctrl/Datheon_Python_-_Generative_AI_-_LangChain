
# Datheon Python + Generative AI + LangChain Internship

This repository contains my implementations of Tasks 1 and 2 for the Datheon Python, Generative AI, and LangChain internship.

## Task 1: Structured LLM Prompt Pipeline & JSON Extractor

**Folder:** `task1_json_extractor/`

A Python-based information extraction pipeline that uses Google's Gemini API and Pydantic to extract structured information from resumes and invoices.

**Key features:**
- Reusable prompts for resumes and invoices
- Structured JSON generation using Gemini
- Pydantic schema validation
- Automated tests for prompts and schemas

[View Task 1 documentation](task1_json_extractor/README.md)

## Task 2: Document Q&A Assistant with RAG & Vector Embeddings

**Folder:** `task2_document_rag/`

A Retrieval-Augmented Generation (RAG) application that allows users to ask questions about PDF documents and receive answers based on retrieved document content.

**Key features:**
- PDF text extraction and page metadata
- Text splitting with overlapping chunks
- Gemini embeddings and ChromaDB vector search
- Context-based question answering
- Source page references
- Automated tests for PDF loading and text splitting

[View Task 2 documentation](task2_document_rag/README.md)

## Technology Stack

- Python
- Google Gemini API
- LangChain
- Pydantic
- ChromaDB
- PyPDF
- Pytest

## Security

- Store API credentials in a local `.env` file.
- Never commit API keys or actual `.env` files.
- Virtual environments and generated vector databases should not be committed.

## Current Status

Tasks 1 and 2 are included in this repository. The implementations and testing status are documented in their respective folders.
