import matplotlib.pyplot as plt
import seaborn as sns

from src.config.paths import REPORTS_DIR
from src.data.rolling_workload_loader import load_rolling_workload_features
from src.utils.logger import get_logger

logger = get_logger(__name__)

sns.set_style("whitegrid")

OUTPUT_DIR = REPORTS_DIR / "eda" / "injury" / "rolling_workload"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def plot_selected_bowler_rolling_workload(bowler_name: str):
    df = load_rolling_workload_features()
    df["match_date"] = df["match_date"].astype(str)

    bowler_df = df[df["bowler"] == bowler_name].copy()

    if bowler_df.empty:
        logger.warning("No rolling workload data found for bowler %s", bowler_name)
        return

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=bowler_df, x="match_date", y="overs_last_7_days", marker="o")
    plt.title(f"Rolling 7-Day Workload — {bowler_name}")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    safe_name = bowler_name.lower().replace(" ", "_")
    output_path = OUTPUT_DIR / f"{safe_name}_rolling_7_day_workload.png"
    plt.savefig(output_path)
    plt.close()

    logger.info("Saved plot: %s", output_path)


def plot_selected_bowler_fatigue_score(bowler_name: str):
    df = load_rolling_workload_features()
    df["match_date"] = df["match_date"].astype(str)

    bowler_df = df[df["bowler"] == bowler_name].copy()

    if bowler_df.empty:
        logger.warning("No fatigue data found for bowler %s", bowler_name)
        return

    plt.figure(figsize=(12, 6))
    sns.lineplot(data=bowler_df, x="match_date", y="fatigue_signal_score", marker="o")
    plt.title(f"Fatigue Signal Score Trend — {bowler_name}")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    safe_name = bowler_name.lower().replace(" ", "_")
    output_path = OUTPUT_DIR / f"{safe_name}_fatigue_signal_trend.png"
    plt.savefig(output_path)
    plt.close()

    logger.info("Saved plot: %s", output_path)


def main():
    sample_bowlers = [
        "Shaheen Shah Afridi",
        "Haris Rauf",
        "Shadab Khan",
    ]

    for bowler in sample_bowlers:
        plot_selected_bowler_rolling_workload(bowler)
        plot_selected_bowler_fatigue_score(bowler)

    print("Rolling workload plots generated successfully.")


if __name__ == "__main__":
    main()