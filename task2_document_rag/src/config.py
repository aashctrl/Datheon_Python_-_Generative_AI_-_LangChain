
import os
from pathlib import Path

from dotenv import load_dotenv


# D:\Datheon
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# D:\Datheon\task1_json_extractor\.env
TASK1_ENV = PROJECT_ROOT / "task1_json_extractor" / ".env"

load_dotenv(TASK1_ENV, override=False)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
CHAT_MODEL = os.getenv("GEMINI_MODEL")
EMBEDDING_MODEL = os.getenv(
    "GEMINI_EMBEDDING_MODEL",
    "gemini-embedding-001",
)


def validate_config() -> None:
    if not GEMINI_API_KEY:
        raise RuntimeError(
            f"GEMINI_API_KEY was not found. Check: {TASK1_ENV}"
        )

    if not CHAT_MODEL:
        raise RuntimeError(
            "GEMINI_MODEL is missing from the Task 1 .env file."
        )
