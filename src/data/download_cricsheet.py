from pathlib import Path
import json

from src.config.paths import RAW_DATA_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)

CRICSHEET_PSL_DIR = RAW_DATA_DIR / "cricsheet_psl"
MATCHES_DIR = CRICSHEET_PSL_DIR / "matches"
METADATA_FILE = CRICSHEET_PSL_DIR / "download_metadata.json"


def ensure_directories():
    CRICSHEET_PSL_DIR.mkdir(parents=True, exist_ok=True)
    MATCHES_DIR.mkdir(parents=True, exist_ok=True)
    logger.info("Cricsheet PSL directories ensured.")


def save_metadata(source_url: str = "https://cricsheet.org/"):
    metadata = {
        "source": "Cricsheet",
        "source_url": source_url,
        "competition": "PSL",
        "notes": "Raw archive downloaded manually and extracted into matches folder.",
    }

    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=4)

    logger.info("Download metadata saved to %s", METADATA_FILE)


def main():
    ensure_directories()
    save_metadata()
    logger.info("Cricsheet raw data helper setup completed.")


if __name__ == "__main__":
    main()