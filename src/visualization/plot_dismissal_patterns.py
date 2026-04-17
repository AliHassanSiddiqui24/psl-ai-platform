from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns

from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.dismissal_analysis import (
    build_selected_batter_dismissal_breakdown,
    get_top_dismissed_batters,
)
from src.config.paths import REPORTS_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)

sns.set_style("whitegrid")

OUTPUT_DIR = REPORTS_DIR / "eda" / "weakness"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def plot_top_dismissed_batters():
    df = load_clean_ball_by_ball_data()
    summary = get_top_dismissed_batters(df, top_n=15)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=summary, x="player_name", y="dismissal_count")
    plt.title("Top 15 Most Dismissed Batters")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    output_path = OUTPUT_DIR / "top_15_most_dismissed_batters.png"
    plt.savefig(output_path)
    plt.close()

    logger.info("Saved plot: %s", output_path)


def plot_selected_batter_dismissal_breakdown(player_name: str):
    df = load_clean_ball_by_ball_data()
    summary = build_selected_batter_dismissal_breakdown(df, player_name)

    if summary.empty:
        logger.warning("No dismissal breakdown found for player: %s", player_name)
        return

    plt.figure(figsize=(10, 6))
    sns.barplot(data=summary, x="wicket_type", y="dismissal_count")
    plt.title(f"Dismissal Pattern for {player_name}")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    safe_name = player_name.lower().replace(" ", "_")
    output_path = OUTPUT_DIR / f"{safe_name}_dismissal_pattern.png"
    plt.savefig(output_path)
    plt.close()

    logger.info("Saved plot: %s", output_path)


def main():
    plot_top_dismissed_batters()

    sample_players = [
        "Babar Azam",
        "Mohammad Rizwan",
        "Fakhar Zaman",
    ]

    for player in sample_players:
        plot_selected_batter_dismissal_breakdown(player)

    print("Dismissal pattern plots generated successfully.")


if __name__ == "__main__":
    main()