import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


def get_numeric_workload_features(df: pd.DataFrame) -> pd.DataFrame:
    candidate_columns = [
        "balls_bowled",
        "overs_bowled",
        "balls_last_7_days",
        "balls_last_14_days",
        "matches_last_7_days",
        "matches_last_14_days",
        "days_since_last_match",
        "back_to_back_match",
        "short_recovery_flag",
        "overs_last_7_days",
        "overs_last_14_days",
        "fatigue_signal_score",
    ]

    available_columns = [col for col in candidate_columns if col in df.columns]
    numeric_df = df[available_columns].copy()

    logger.info("Prepared numeric workload feature set with shape %s", numeric_df.shape)
    return numeric_df


def compute_correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    numeric_df = get_numeric_workload_features(df)
    corr_df = numeric_df.corr(numeric_only=True)

    logger.info("Computed correlation matrix with shape %s", corr_df.shape)
    return corr_df