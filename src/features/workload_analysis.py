import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


def build_match_level_bowler_workload(df: pd.DataFrame) -> pd.DataFrame:
    workload_df = (
        df.groupby(["match_id", "match_date", "bowler"])
        .agg(
            balls_bowled=("bowler", "count"),
            runs_conceded=("runs_total", "sum"),
            wickets_taken=("wicket", "sum"),
        )
        .reset_index()
    )

    workload_df["overs_bowled"] = (workload_df["balls_bowled"] / 6).round(2)
    workload_df["match_date"] = pd.to_datetime(workload_df["match_date"], errors="coerce")

    logger.info(
        "Built match-level bowler workload dataset with shape %s",
        workload_df.shape,
    )
    return workload_df


def get_top_workload_bowlers(workload_df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    top_bowlers = (
        workload_df.groupby("bowler")["balls_bowled"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )
    top_bowlers.columns = ["bowler", "total_balls_bowled"]

    logger.info("Computed top %d workload bowlers.", top_n)
    return top_bowlers


def get_selected_bowler_workload_trend(
    workload_df: pd.DataFrame, bowler_name: str
) -> pd.DataFrame:
    bowler_df = workload_df[workload_df["bowler"] == bowler_name].copy()
    bowler_df = bowler_df.sort_values("match_date").reset_index(drop=True)

    logger.info(
        "Selected workload trend for bowler %s with shape %s",
        bowler_name,
        bowler_df.shape,
    )
    return bowler_df