from src.config.paths import REPORTS_DIR
from src.data.rolling_workload_loader import load_rolling_workload_features
from src.utils.logger import get_logger

logger = get_logger(__name__)

OUTPUT_DIR = REPORTS_DIR / "eda" / "injury" / "rolling_workload"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    df = load_rolling_workload_features()

    summary = (
        df.groupby("bowler")
        .agg(
            matches=("match_id", "nunique"),
            avg_overs_last_7_days=("overs_last_7_days", "mean"),
            max_overs_last_7_days=("overs_last_7_days", "max"),
            avg_matches_last_14_days=("matches_last_14_days", "mean"),
            total_back_to_back_matches=("back_to_back_match", "sum"),
            avg_fatigue_signal_score=("fatigue_signal_score", "mean"),
            max_fatigue_signal_score=("fatigue_signal_score", "max"),
        )
        .reset_index()
        .sort_values("max_fatigue_signal_score", ascending=False)
    )

    output_file = OUTPUT_DIR / "rolling_workload_summary_stats.csv"
    summary.to_csv(output_file, index=False)

    logger.info("Saved rolling workload summary stats to %s", output_file)
    print("Rolling workload summary stats exported successfully.")


if __name__ == "__main__":
    main()