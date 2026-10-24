import json
from pathlib import Path
from src.extractor import extract_resume

def main():
    project_dir = Path(__file__).resolve().parent.parent
    resume_path = project_dir / "examples" / "sample_resume.txt"
    resume_text = resume_path.read_text(encoding="utf-8")
    try:
        result = extract_resume(resume_text)
        print("\nExtracted resume data:\n")
        print(json.dumps(result.model_dump(), indent=4))
    except (ValueError, RuntimeError) as exc:
        print(f"Extraction failed: {exc}")

if __name__ == "__main__":
    main()
