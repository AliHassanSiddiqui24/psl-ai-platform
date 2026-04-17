from src.config.paths import REPORTS_DIR
from src.data.rolling_workload_loader import load_rolling_workload_features
from src.features.injury_proxy_target import add_future_absence_proxy
from src.utils.logger import get_logger

logger = get_logger(__name__)

OUTPUT_DIR = REPORTS_DIR / "eda" / "injury" / "proxy_target"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    df = load_rolling_workload_features()
    proxy_df = add_future_absence_proxy(df)

    summary = (
        proxy_df.groupby("bowler")
        .agg(
            rows=("match_id", "count"),
            proxy_events=("injury_proxy_event", "sum"),
            avg_fatigue_signal=("fatigue_signal_score", "mean"),
            max_fatigue_signal=("fatigue_signal_score", "max"),
            avg_overs_last_7_days=("overs_last_7_days", "mean"),
        )
        .reset_index()
        .sort_values("proxy_events", ascending=False)
    )

    output_file = OUTPUT_DIR / "injury_proxy_summary_by_bowler.csv"
    summary.to_csv(output_file, index=False)

    logger.info("Saved injury proxy summary to %s", output_file)
    print("Injury proxy summary exported successfully.")


if __name__ == "__main__":
    main()