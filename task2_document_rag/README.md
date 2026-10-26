
# Task 2: Document Q&A Assistant with RAG & Vector Embeddings

## Overview

This project implements a Retrieval-Augmented Generation (RAG) pipeline that allows users to ask questions about information stored in PDF documents. It extracts document text, divides it into smaller chunks, converts the chunks into vector embeddings, and retrieves relevant content to help a Gemini language model generate context-based answers.

The application also provides source references, including the document name and page number, to make answers easier to verify.

## Features

- **PDF Loading:** Extracts text from PDF documents using PyPDF.
- **Text Splitting:** Divides documents into smaller, overlapping chunks while preserving metadata.
- **Vector Embeddings:** Uses Google's Gemini embedding model to represent text as vectors.
- **Vector Database:** Stores and retrieves document chunks using ChromaDB.
- **Semantic Search:** Retrieves relevant chunks based on the user's question.
- **Context-Based Answers:** Uses Google Gemini to generate answers from retrieved document content.
- **Source References:** Displays the PDF filename and relevant page numbers.
- **Persistent Indexing:** Reuses an existing vector database to avoid unnecessary re-indexing.
- **Input Validation and Tests:** Includes automated tests for document loading and text splitting.

## Technology Stack

- Python
- LangChain
- Google Gemini API
- ChromaDB
- PyPDF
- `langchain-google-genai`
- `langchain-text-splitters`
- `python-dotenv`
- Pytest
- ReportLab for generating the sample PDF

## Project Structure

```text
task2_document_rag/
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── document_loader.py
│   ├── text_splitter.py
│   ├── vector_store.py
│   └── rag_pipeline.py
├── documents/
│   └── sample_guide.pdf
├── tests/
│   ├── test_document_loader.py
│   └── test_text_splitter.py
├── chroma_db/
├── ask_question.py
├── create_sample_pdf.py
├── .env.example
├── requirements.txt
└── README.md
```

*Note: `chroma_db/` is generated when the vector index is created. Its contents do not need to be committed to GitHub.*

## How It Works

1. **Load:** Extracts text and page metadata from the selected PDF.
2. **Split:** Divides the text into overlapping chunks to preserve context.
3. **Embed:** Converts document chunks into numerical vectors using Gemini embeddings.
4. **Store:** Saves vectors and document metadata in ChromaDB.
5. **Retrieve:** Searches for relevant chunks based on the user's question.
6. **Generate:** Passes retrieved context to Gemini to generate a document-grounded answer.
7. **Cite:** Displays source filenames and page numbers for the retrieved chunks.

## Setup and Installation

### 1. Navigate to the Project Directory

```bash
cd D:\Datheon\task2_document_rag
```

### 2. Activate the Virtual Environment

If your virtual environment is in the parent `D:\Datheon` directory:

```bash
..\.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the Gemini API

The project currently reads its Gemini API configuration from the Task 1 `.env` file:

`D:\Datheon\task1_json_extractor\.env`

Ensure it contains the following settings, using your own valid API key:

```dotenv
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.7-flash
GEMINI_EMBEDDING_MODEL=gemini-embedding-001
```

The model names should match the models configured and supported by your Gemini API access.

**Security:** Never commit your `.env` file or expose your API key publicly.

### 5. Generate the Sample PDF (If Needed)

```bash
python create_sample_pdf.py
```

This creates `documents/sample_guide.pdf` for testing.

## Running the Application

From the `task2_document_rag` directory, run:

```bash
python ask_question.py
```

Enter a question when prompted. The application retrieves relevant document content, generates an answer, and displays its sources.

Example questions:

- What is a variable in Python?
- How do lists work in Python?
- What is a function?

Type `exit` to close the application.

## Running Tests

Execute the automated tests using:

```bash
python -m pytest -v
```

The current tests cover PDF loading, text extraction, page metadata, invalid file handling, text chunking, metadata preservation, chunk start indices, and invalid chunking parameters.

## Limitations

- Answer quality depends on the content and text extractability of the PDF.
- Scanned PDFs may require OCR, which is not currently implemented.
- A valid Gemini API key and internet connection are required for embeddings and answer generation.
- Temporary Gemini API errors or rate limits can interrupt answer generation.
- Source references identify retrieved document pages but do not guarantee that every generated statement is correct.

## Future Improvements

- Add support for multiple PDF documents.
- Improve relevance filtering to reject unrelated retrieved chunks.
- Expand tests for retrieval, answer generation, and source references.
- Add a Streamlit interface for an interactive user experience.
- Improve error handling and retry behaviour for temporary API failures.

## Conclusion

This project demonstrates an end-to-end RAG workflow combining PDF processing, text chunking, vector embeddings, semantic retrieval, and LLM-based answer generation. It provides a foundation for building document-grounded question-answering applications.
