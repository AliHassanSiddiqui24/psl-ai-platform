from src.config.paths import REPORTS_DIR
from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.dismissal_analysis import (
    build_batsman_dismissal_summary,
    get_top_dismissed_batters,
)
from src.utils.logger import get_logger

logger = get_logger(__name__)

OUTPUT_DIR = REPORTS_DIR / "eda" / "weakness"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    df = load_clean_ball_by_ball_data()

    full_summary = build_batsman_dismissal_summary(df)
    full_summary.to_csv(OUTPUT_DIR / "batsman_dismissal_summary.csv", index=False)

    top_batters = get_top_dismissed_batters(df, top_n=20)
    top_batters.to_csv(OUTPUT_DIR / "top_dismissed_batters.csv", index=False)

    logger.info("Dismissal summary exports completed.")
    print("Dismissal summary CSV files exported successfully.")


if __name__ == "__main__":
    main()