import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


def build_batter_vs_bowler_type_summary(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby(["batter", "bowler_type"])
        .agg(
            balls_faced=("batter", "count"),
            runs_scored=("runs_batter", "sum"),
            dismissals=("player_out", lambda x: x.notna().sum()),
            matches=("match_id", "nunique"),
        )
        .reset_index()
    )

    grouped["strike_rate"] = (
        grouped["runs_scored"] / grouped["balls_faced"] * 100
    ).round(2)

    grouped["dismissal_rate"] = (
        grouped["dismissals"] / grouped["balls_faced"].replace(0, pd.NA)
    ).round(4)

    grouped["balls_per_dismissal"] = (
        grouped["balls_faced"] / grouped["dismissals"].replace(0, pd.NA)
    ).round(2)

    logger.info(
        "Built batter vs bowler type summary with shape %s",
        grouped.shape,
    )
    return grouped


def get_selected_batters_matchup_summary(
    df: pd.DataFrame, selected_batters: list[str]
) -> pd.DataFrame:
    summary = build_batter_vs_bowler_type_summary(df)
    filtered = summary[summary["batter"].isin(selected_batters)].copy()

    logger.info(
        "Filtered matchup summary for selected batters with shape %s",
        filtered.shape,
    )
    return filtered