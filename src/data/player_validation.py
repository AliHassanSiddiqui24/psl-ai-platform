import pandas as pd

from src.utils.exceptions import DataValidationError
from src.utils.logger import get_logger

logger = get_logger(__name__)


REQUIRED_PLAYER_ATTRIBUTE_COLUMNS = [
    "player_name",
    "batting_hand",
    "bowling_style",
    "player_role",
    "country",
    "is_overseas",
    "date_of_birth",
    "notes",
]


def validate_player_attributes_schema(df: pd.DataFrame) -> bool:
    missing_columns = [
        col for col in REQUIRED_PLAYER_ATTRIBUTE_COLUMNS if col not in df.columns
    ]

    if missing_columns:
        logger.error("Missing columns in player attributes file: %s", missing_columns)
        raise DataValidationError(
            f"Missing columns in player attributes file: {missing_columns}"
        )

    logger.info("Player attributes schema validated successfully.")
    return True