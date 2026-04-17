import pandas as pd

from src.utils.exceptions import DataValidationError
from src.utils.logger import get_logger

logger = get_logger(__name__)

REQUIRED_BALL_BY_BALL_COLUMNS = [
    "match_id",
    "innings_number",
    "batting_team",
    "over",
    "ball",
    "batter",
    "bowler",
    "non_striker",
    "runs_batter",
    "runs_extras",
    "runs_total",
    "wicket",
    "match_date",
    "venue",
]


def validate_ball_by_ball_schema(df: pd.DataFrame) -> bool:
    missing_columns = [
        col for col in REQUIRED_BALL_BY_BALL_COLUMNS if col not in df.columns
    ]

    if missing_columns:
        logger.error("Missing required columns: %s", missing_columns)
        raise DataValidationError(f"Missing required columns: {missing_columns}")

    logger.info("Ball-by-ball schema validated successfully.")
    return True