import json

import pandas as pd

from src.config.paths import PROCESSED_DATA_DIR, REPORTS_DIR
from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.utils.logger import get_logger
from src.visualization.eda_utils import (
    save_count_plot,
    save_histogram,
    save_missing_values_plot,
)

logger = get_logger(__name__)

EDA_DIR = REPORTS_DIR / "eda"
EDA_DIR.mkdir(parents=True, exist_ok=True)

SUMMARY_FILE = EDA_DIR / "ball_by_ball_basic_summary.json"


def generate_basic_summary(df: pd.DataFrame) -> dict:
    summary = {
        "row_count": int(len(df)),
        "column_count": int(len(df.columns)),
        "unique_matches": int(df["match_id"].nunique()),
        "unique_batters": int(df["batter"].nunique()),
        "unique_bowlers": int(df["bowler"].nunique()),
        "unique_venues": int(df["venue"].nunique()) if "venue" in df.columns else None,
        "total_runs": int(df["runs_total"].sum()),
        "total_wickets": int(df["wicket"].sum()),
        "phase_distribution": df["phase"].value_counts(dropna=False).to_dict(),
    }
    return summary


def main():
    df = load_clean_ball_by_ball_data()

    summary = generate_basic_summary(df)

    with open(SUMMARY_FILE, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4, default=str)

    logger.info("Saved basic summary to %s", SUMMARY_FILE)

    save_missing_values_plot(df, EDA_DIR / "ball_by_ball_missing_values.png")
    save_count_plot(
        df,
        x="phase",
        title="Distribution of Deliveries by Phase",
        output_path=EDA_DIR / "phase_distribution.png",
    )
    save_histogram(
        df,
        column="runs_total",
        title="Distribution of Runs per Delivery",
        output_path=EDA_DIR / "runs_total_distribution.png",
    )

    print("Ball-by-ball basic EDA completed.")
    print(summary)


if __name__ == "__main__":
    main()