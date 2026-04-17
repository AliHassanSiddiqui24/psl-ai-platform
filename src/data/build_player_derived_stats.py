import pandas as pd

from src.config.constants import PLAYER_DERIVED_STATS_FILE_NAME
from src.config.paths import PROCESSED_DATA_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)

INPUT_FILE = PROCESSED_DATA_DIR / "ball_by_ball" / "psl_ball_by_ball_clean.csv"
OUTPUT_DIR = PROCESSED_DATA_DIR / "player_data"
OUTPUT_FILE = OUTPUT_DIR / PLAYER_DERIVED_STATS_FILE_NAME


def build_batting_stats(df: pd.DataFrame) -> pd.DataFrame:
    batting = (
        df.groupby("batter")
        .agg(
            batting_balls_faced=("batter", "count"),
            batting_runs_scored=("runs_batter", "sum"),
            batting_total_runs=("runs_total", "sum"),
            batting_dismissals=("player_out", lambda x: x.notna().sum()),
            batting_matches_played=("match_id", "nunique"),
        )
        .reset_index()
        .rename(columns={"batter": "player_name"})
    )

    batting["batting_strike_rate"] = (
        batting["batting_runs_scored"] / batting["batting_balls_faced"] * 100
    ).round(2)

    batting["batting_average"] = (
        batting["batting_runs_scored"] / batting["batting_dismissals"].replace(0, pd.NA)
    ).round(2)

    return batting


def build_bowling_stats(df: pd.DataFrame) -> pd.DataFrame:
    bowling = (
        df.groupby("bowler")
        .agg(
            bowling_balls=("bowler", "count"),
            bowling_runs_conceded=("runs_total", "sum"),
            bowling_wickets=("wicket", "sum"),
            bowling_matches_played=("match_id", "nunique"),
        )
        .reset_index()
        .rename(columns={"bowler": "player_name"})
    )

    bowling["bowling_overs"] = (bowling["bowling_balls"] / 6).round(2)
    bowling["bowling_economy"] = (
        bowling["bowling_runs_conceded"] / bowling["bowling_overs"].replace(0, pd.NA)
    ).round(2)

    return bowling


def build_player_derived_stats(df: pd.DataFrame) -> pd.DataFrame:
    batting = build_batting_stats(df)
    bowling = build_bowling_stats(df)

    merged = pd.merge(batting, bowling, on="player_name", how="outer")
    return merged


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(INPUT_FILE)
    derived_df = build_player_derived_stats(df)

    derived_df.to_csv(OUTPUT_FILE, index=False)
    logger.info(
        "Saved player derived stats to %s with shape %s", OUTPUT_FILE, derived_df.shape
    )

    print(derived_df.head())
    print("\nShape:", derived_df.shape)


if __name__ == "__main__":
    main()