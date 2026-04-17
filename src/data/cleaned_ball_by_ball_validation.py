import pandas as pd

from src.utils.exceptions import DataValidationError
from src.utils.logger import get_logger

logger = get_logger(__name__)

REQUIRED_CLEAN_COLUMNS = [
    "match_id",
    "match_date",
    "venue",
    "innings_number",
    "batting_team",
    "over",
    "ball",
    "ball_id",
    "batter",
    "bowler",
    "non_striker",
    "runs_batter",
    "runs_extras",
    "runs_total",
    "wicket",
    "phase",
]


def validate_clean_ball_by_ball_schema(df: pd.DataFrame) -> bool:
    missing_columns = [col for col in REQUIRED_CLEAN_COLUMNS if col not in df.columns]

    if missing_columns:
        logger.error("Missing columns in cleaned dataset: %s", missing_columns)
        raise DataValidationError(
            f"Missing columns in cleaned dataset: {missing_columns}"
        )

    logger.info("Cleaned ball-by-ball schema validated successfully.")
    return True