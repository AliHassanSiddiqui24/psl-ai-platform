import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


def simplify_bowling_style(style: str) -> str:
    if pd.isna(style):
        return "Unknown"

    style = str(style).strip().lower()

    if "left-arm fast" in style or "left arm fast" in style:
        return "Left-arm pace"
    if "right-arm fast" in style or "right arm fast" in style:
        return "Right-arm pace"
    if "offbreak" in style or "off spin" in style or "offbreak" in style:
        return "Off-spin"
    if "legbreak" in style or "leg spin" in style or "legbreak" in style:
        return "Leg-spin"
    if "left-arm orthodox" in style or "slow left-arm orthodox" in style:
        return "Left-arm orthodox"
    if "left-arm wrist" in style or "chinaman" in style:
        return "Left-arm wrist-spin"

    return "Other"


def add_simplified_bowler_type(df: pd.DataFrame, bowling_style_col: str) -> pd.DataFrame:
    df = df.copy()
    df["bowler_type"] = df[bowling_style_col].apply(simplify_bowling_style)

    logger.info("Added simplified bowler_type column.")
    return df