import matplotlib.pyplot as plt
import seaborn as sns

from src.config.paths import REPORTS_DIR
from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.phase_analysis import (
    get_selected_batters_phase_summary,
    get_top_batters_by_runs,
)
from src.utils.logger import get_logger

logger = get_logger(__name__)

sns.set_style("whitegrid")

OUTPUT_DIR = REPORTS_DIR / "eda" / "weakness" / "phase_analysis"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def plot_selected_batters_strike_rate_by_phase(selected_batters: list[str]):
    df = load_clean_ball_by_ball_data()
    summary = get_selected_batters_phase_summary(df, selected_batters)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=summary, x="phase", y="strike_rate", hue="batter")
    plt.title("Strike Rate by Phase for Selected Batters")
    plt.tight_layout()

    output_path = OUTPUT_DIR / "selected_batters_strike_rate_by_phase.png"
    plt.savefig(output_path)
    plt.close()

    logger.info("Saved plot: %s", output_path)


def plot_selected_batters_dismissals_by_phase(selected_batters: list[str]):
    df = load_clean_ball_by_ball_data()
    summary = get_selected_batters_phase_summary(df, selected_batters)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=summary, x="phase", y="dismissals", hue="batter")
    plt.title("Dismissals by Phase for Selected Batters")
    plt.tight_layout()

    output_path = OUTPUT_DIR / "selected_batters_dismissals_by_phase.png"
    plt.savefig(output_path)
    plt.close()

    logger.info("Saved plot: %s", output_path)


def plot_top_batters_phase_runs():
    df = load_clean_ball_by_ball_data()
    top_batters = get_top_batters_by_runs(df, top_n=8)
    summary = get_selected_batters_phase_summary(df, top_batters)

    plt.figure(figsize=(14, 6))
    sns.barplot(data=summary, x="phase", y="runs_scored", hue="batter")
    plt.title("Runs Scored by Phase for Top Batters")
    plt.tight_layout()

    output_path = OUTPUT_DIR / "top_batters_runs_by_phase.png"
    plt.savefig(output_path)
    plt.close()

    logger.info("Saved plot: %s", output_path)


def main():
    selected_batters = ["Babar Azam", "Mohammad Rizwan", "Fakhar Zaman"]

    plot_selected_batters_strike_rate_by_phase(selected_batters)
    plot_selected_batters_dismissals_by_phase(selected_batters)
    plot_top_batters_phase_runs()

    print("Phase analysis plots generated successfully.")


if __name__ == "__main__":
    main()