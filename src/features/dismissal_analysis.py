import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


def get_dismissal_rows(df: pd.DataFrame) -> pd.DataFrame:
    dismissal_df = df[df["wicket"] == 1].copy()
    dismissal_df = dismissal_df[dismissal_df["player_out"].notna()].copy()

    logger.info("Filtered dismissal rows with shape %s", dismissal_df.shape)
    return dismissal_df


def build_batsman_dismissal_summary(df: pd.DataFrame) -> pd.DataFrame:
    dismissal_df = get_dismissal_rows(df)

    summary = (
        dismissal_df.groupby(["player_out", "wicket_type"])
        .size()
        .reset_index(name="dismissal_count")
        .sort_values(["player_out", "dismissal_count"], ascending=[True, False])
    )

    logger.info("Built batsman dismissal summary with shape %s", summary.shape)
    return summary


def get_top_dismissed_batters(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    dismissal_df = get_dismissal_rows(df)

    top_batters = (
        dismissal_df["player_out"]
        .value_counts()
        .head(top_n)
        .reset_index()
    )

    top_batters.columns = ["player_name", "dismissal_count"]

    logger.info("Computed top %d dismissed batters.", top_n)
    return top_batters


def build_selected_batter_dismissal_breakdown(
    df: pd.DataFrame, player_name: str
) -> pd.DataFrame:
    dismissal_df = get_dismissal_rows(df)

    player_df = dismissal_df[dismissal_df["player_out"] == player_name].copy()

    summary = (
        player_df["wicket_type"]
        .value_counts(dropna=False)
        .reset_index()
    )
    summary.columns = ["wicket_type", "dismissal_count"]

    logger.info(
        "Built dismissal breakdown for player %s with shape %s",
        player_name,
        summary.shape,
    )
    return summary