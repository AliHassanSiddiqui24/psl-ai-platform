import pandas as pd

from src.utils.exceptions import DataValidationError
from src.utils.logger import get_logger

logger = get_logger(__name__)

REQUIRED_PLAYER_PROFILE_COLUMNS = [
    "player_name",
    "source",
    "first_seen_match_id",
    "last_seen_match_id",
]


def validate_player_profile_master(df: pd.DataFrame) -> bool:
    missing_columns = [
        col for col in REQUIRED_PLAYER_PROFILE_COLUMNS if col not in df.columns
    ]

    if missing_columns:
        logger.error("Missing player profile columns: %s", missing_columns)
        raise DataValidationError(
            f"Missing player profile columns: {missing_columns}"
        )

    logger.info("Player profile master schema validated successfully.")
    return True