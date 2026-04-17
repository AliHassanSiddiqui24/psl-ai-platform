import matplotlib.pyplot as plt
import seaborn as sns

from src.config.paths import REPORTS_DIR
from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.workload_analysis import (
    build_match_level_bowler_workload,
    get_selected_bowler_workload_trend,
    get_top_workload_bowlers,
)
from src.utils.logger import get_logger

logger = get_logger(__name__)

sns.set_style("whitegrid")

OUTPUT_DIR = REPORTS_DIR / "eda" / "injury" / "workload_trends"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def plot_top_workload_bowlers():
    df = load_clean_ball_by_ball_data()
    workload_df = build_match_level_bowler_workload(df)
    top_bowlers = get_top_workload_bowlers(workload_df, top_n=12)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=top_bowlers, x="bowler", y="total_balls_bowled")
    plt.title("Top 12 Bowlers by Total Balls Bowled")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    output_path = OUTPUT_DIR / "top_12_workload_bowlers.png"
    plt.savefig(output_path)
    plt.close()

    logger.info("Saved plot: %s", output_path)


def plot_selected_bowler_trend(bowler_name: str):
    df = load_clean_ball_by_ball_data()
    workload_df = build_match_level_bowler_workload(df)
    bowler_df = get_selected_bowler_workload_trend(workload_df, bowler_name)

    if bowler_df.empty:
        logger.warning("No workload data found for bowler %s", bowler_name)
        return

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=bowler_df, x="match_date", y="overs_bowled", marker="o")
    plt.title(f"Workload Trend — {bowler_name}")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    safe_name = bowler_name.lower().replace(" ", "_")
    output_path = OUTPUT_DIR / f"{safe_name}_workload_trend.png"
    plt.savefig(output_path)
    plt.close()

    logger.info("Saved plot: %s", output_path)


def main():
    plot_top_workload_bowlers()

    sample_bowlers = [
        "Shaheen Shah Afridi",
        "Haris Rauf",
        "Shadab Khan",
    ]

    for bowler in sample_bowlers:
        plot_selected_bowler_trend(bowler)

    print("Workload trend plots generated successfully.")


if __name__ == "__main__":
    main()