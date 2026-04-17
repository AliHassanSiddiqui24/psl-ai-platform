from src.config.paths import REPORTS_DIR
from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.workload_analysis import (
    build_match_level_bowler_workload,
    get_top_workload_bowlers,
)
from src.utils.logger import get_logger

logger = get_logger(__name__)

OUTPUT_DIR = REPORTS_DIR / "eda" / "injury" / "workload_trends"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    df = load_clean_ball_by_ball_data()
    workload_df = build_match_level_bowler_workload(df)

    workload_summary = (
        workload_df.groupby("bowler")
        .agg(
            matches=("match_id", "nunique"),
            total_balls_bowled=("balls_bowled", "sum"),
            total_overs_bowled=("overs_bowled", "sum"),
            avg_balls_per_match=("balls_bowled", "mean"),
            avg_overs_per_match=("overs_bowled", "mean"),
            total_wickets=("wickets_taken", "sum"),
        )
        .reset_index()
        .sort_values("total_balls_bowled", ascending=False)
    )

    output_file = OUTPUT_DIR / "bowler_workload_summary_stats.csv"
    workload_summary.to_csv(output_file, index=False)

    logger.info("Saved workload summary stats to %s", output_file)
    print("Bowler workload summary stats exported successfully.")


if __name__ == "__main__":
    main()