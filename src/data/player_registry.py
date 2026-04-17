from pathlib import Path
import pandas as pd

from src.config.paths import INTERIM_DATA_DIR, PROCESSED_DATA_DIR
from src.config.constants import (
    PLAYER_MASTER_FILE_NAME,
    PLAYER_MANUAL_ATTRIBUTES_FILE_NAME,
)
from src.utils.logger import get_logger

logger = get_logger(__name__)

PLAYER_DATA_INTERIM_DIR = INTERIM_DATA_DIR / "player_data"
PLAYER_DATA_PROCESSED_DIR = PROCESSED_DATA_DIR / "player_data"

PLAYER_MASTER_PATH = PLAYER_DATA_INTERIM_DIR / PLAYER_MASTER_FILE_NAME
PLAYER_MANUAL_ATTRIBUTES_PATH = PLAYER_DATA_INTERIM_DIR / PLAYER_MANUAL_ATTRIBUTES_FILE_NAME


def ensure_player_data_directories():
    PLAYER_DATA_INTERIM_DIR.mkdir(parents=True, exist_ok=True)
    PLAYER_DATA_PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    logger.info("Player data directories ensured.")


def create_empty_player_master():
    columns = [
        "player_name",
        "source",
        "first_seen_match_id",
        "last_seen_match_id",
        "notes",
    ]
    df = pd.DataFrame(columns=columns)
    df.to_csv(PLAYER_MASTER_PATH, index=False)
    logger.info("Empty player master created at %s", PLAYER_MASTER_PATH)
    return df


def create_manual_attributes_template():
    columns = [
        "player_name",
        "batting_hand",
        "bowling_style",
        "player_role",
        "country",
        "is_overseas",
        "date_of_birth",
        "notes",
    ]
    df = pd.DataFrame(columns=columns)
    df.to_csv(PLAYER_MANUAL_ATTRIBUTES_PATH, index=False)
    logger.info(
        "Player manual attributes template created at %s",
        PLAYER_MANUAL_ATTRIBUTES_PATH,
    )
    return df


def main():
    ensure_player_data_directories()

    if not PLAYER_MASTER_PATH.exists():
        create_empty_player_master()

    if not PLAYER_MANUAL_ATTRIBUTES_PATH.exists():
        create_manual_attributes_template()

    logger.info("Player registry scaffold setup completed.")


if __name__ == "__main__":
    main()