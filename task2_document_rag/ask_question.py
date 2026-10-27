
from pathlib import Path

from src.rag_pipeline import load_or_index_pdf, answer_question

BASE_DIR = Path(__file__).resolve().parent
PDF_PATH = BASE_DIR / "documents" / "sample_guide.pdf"
DB_PATH = BASE_DIR / "chroma_db"


def main():
    print("Indexing the PDF...")
    vector_store = load_or_index_pdf(PDF_PATH, DB_PATH)

    while True:
        question = input("\nAsk a question (or type 'exit'): ").strip()

        if question.lower() == "exit":
            break

        try:
            result = answer_question(vector_store, question)

            print("\nAnswer:")
            print(result["answer"])

            print("\nSources:")
            for source in result["sources"]:
                print(f"- {source['source']}, Page {source['page']}")

        except Exception as exc:
            print(f"Request failed: {exc}")


if __name__ == "__main__":
    main()

