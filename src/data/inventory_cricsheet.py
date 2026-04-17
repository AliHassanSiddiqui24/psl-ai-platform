from pathlib import Path
import pandas as pd

from src.config.paths import RAW_DATA_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)

CRICSHEET_PSL_DIR = RAW_DATA_DIR / "cricsheet_psl"
MATCHES_DIR = CRICSHEET_PSL_DIR / "matches"
INVENTORY_FILE = CRICSHEET_PSL_DIR / "dataset_inventory.csv"


def build_inventory():
    files = list(MATCHES_DIR.glob("*"))

    inventory_records = []
    for file_path in files:
        if file_path.is_file():
            inventory_records.append(
                {
                    "file_name": file_path.name,
                    "file_path": str(file_path),
                    "file_size_bytes": file_path.stat().st_size,
                    "file_extension": file_path.suffix.lower(),
                }
            )

    df = pd.DataFrame(inventory_records)
    logger.info("Inventory built with %d files.", len(df))
    return df


def save_inventory(df: pd.DataFrame):
    df.to_csv(INVENTORY_FILE, index=False)
    logger.info("Inventory saved to %s", INVENTORY_FILE)


def main():
    if not MATCHES_DIR.exists():
        logger.warning("Matches directory does not exist: %s", MATCHES_DIR)
        return

    df = build_inventory()
    save_inventory(df)

    print(df.head())
    print(f"\nTotal files found: {len(df)}")


if __name__ == "__main__":
    main()