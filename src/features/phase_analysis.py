import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


def build_batsman_phase_summary(df: pd.DataFrame) -> pd.DataFrame:
    grouped = (
        df.groupby(["batter", "phase"])
        .agg(
            balls_faced=("batter", "count"),
            runs_scored=("runs_batter", "sum"),
            total_runs=("runs_total", "sum"),
            dismissals=("player_out", lambda x: x.notna().sum()),
            matches=("match_id", "nunique"),
        )
        .reset_index()
    )

    grouped["strike_rate"] = (
        grouped["runs_scored"] / grouped["balls_faced"] * 100
    ).round(2)

    grouped["balls_per_dismissal"] = (
        grouped["balls_faced"] / grouped["dismissals"].replace(0, pd.NA)
    ).round(2)

    grouped["runs_per_match"] = (
        grouped["runs_scored"] / grouped["matches"].replace(0, pd.NA)
    ).round(2)

    logger.info("Built batsman phase summary with shape %s", grouped.shape)
    return grouped


def get_selected_batters_phase_summary(
    df: pd.DataFrame, selected_batters: list[str]
) -> pd.DataFrame:
    summary = build_batsman_phase_summary(df)
    filtered = summary[summary["batter"].isin(selected_batters)].copy()

    logger.info(
        "Filtered phase summary for selected batters with shape %s",
        filtered.shape,
    )
    return filtered


def get_top_batters_by_runs(df: pd.DataFrame, top_n: int = 10) -> list[str]:
    top_batters = (
        df.groupby("batter")["runs_batter"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .index.tolist()
    )

    logger.info("Computed top %d batters by runs.", top_n)
    return top_batters