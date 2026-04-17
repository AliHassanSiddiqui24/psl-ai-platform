import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


def add_fatigue_signals(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()

    result["overs_last_7_days"] = (result["balls_last_7_days"] / 6).round(2)
    result["overs_last_14_days"] = (result["balls_last_14_days"] / 6).round(2)

    result["fatigue_signal_score"] = (
        result["overs_last_7_days"] * 2
        + result["matches_last_14_days"] * 1.5
        + result["back_to_back_match"] * 3
        + result["short_recovery_flag"] * 2
    ).round(2)

    result["high_recent_workload_flag"] = result["overs_last_7_days"] >= 8
    result["high_match_density_flag"] = result["matches_last_14_days"] >= 3
    result["high_fatigue_flag"] = result["fatigue_signal_score"] >= 10

    logger.info("Added fatigue signals with shape %s", result.shape)
    return result