import json

import pandas as pd

from src.config.paths import PROCESSED_DATA_DIR, REPORTS_DIR
from src.data.player_profile_loader import load_player_profile_master
from src.utils.logger import get_logger
from src.visualization.eda_utils import save_histogram, save_missing_values_plot

logger = get_logger(__name__)

EDA_DIR = REPORTS_DIR / "eda"
EDA_DIR.mkdir(parents=True, exist_ok=True)

SUMMARY_FILE = EDA_DIR / "player_profile_basic_summary.json"


def generate_player_summary(df: pd.DataFrame) -> dict:
    summary = {
        "row_count": int(len(df)),
        "column_count": int(len(df.columns)),
        "players_with_batting_stats": int(df["batting_runs_scored"].notna().sum())
        if "batting_runs_scored" in df.columns
        else 0,
        "players_with_bowling_stats": int(df["bowling_wickets"].notna().sum())
        if "bowling_wickets" in df.columns
        else 0,
        "players_with_manual_role": int(df["player_role"].notna().sum())
        if "player_role" in df.columns
        else 0,
        "countries_present": (
            df["country"].dropna().value_counts().to_dict()
            if "country" in df.columns
            else {}
        ),
    }
    return summary


def main():
    df = load_player_profile_master()

    summary = generate_player_summary(df)

    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4, default=str)

    logger.info("Saved player profile summary to %s", SUMMARY_FILE)

    save_missing_values_plot(df, EDA_DIR / "player_profile_missing_values.png")

    if "batting_runs_scored" in df.columns:
        save_histogram(
            df,
            column="batting_runs_scored",
            title="Distribution of Player Runs Scored",
            output_path=EDA_DIR / "player_runs_distribution.png",
        )

    if "bowling_wickets" in df.columns:
        save_histogram(
            df,
            column="bowling_wickets",
            title="Distribution of Player Wickets",
            output_path=EDA_DIR / "player_wickets_distribution.png",
        )

    print("Player profile basic EDA completed.")
    print(summary)


if __name__ == "__main__":
    main()