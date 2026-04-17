import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from src.config.paths import REPORTS_DIR
from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.dismissal_analysis import build_selected_batter_dismissal_breakdown
from src.utils.logger import get_logger

logger = get_logger(__name__)

sns.set_style("whitegrid")

OUTPUT_DIR = REPORTS_DIR / "eda" / "weakness"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def compare_batters(players: list[str]):
    df = load_clean_ball_by_ball_data()

    all_data = []

    for player in players:
        summary = build_selected_batter_dismissal_breakdown(df, player)
        if not summary.empty:
            summary["player_name"] = player
            all_data.append(summary)

    if not all_data:
        logger.warning("No dismissal comparison data found for selected players.")
        return

    comparison_df = pd.concat(all_data, ignore_index=True)

    plt.figure(figsize=(12, 6))
    sns.barplot(
        data=comparison_df,
        x="wicket_type",
        y="dismissal_count",
        hue="player_name",
    )
    plt.title("Dismissal Type Comparison Across Selected Batters")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    output_path = OUTPUT_DIR / "selected_batters_dismissal_comparison.png"
    plt.savefig(output_path)
    plt.close()

    logger.info("Saved comparison plot: %s", output_path)


def main():
    players = ["Babar Azam", "Mohammad Rizwan", "Fakhar Zaman"]
    compare_batters(players)
    print("Comparison plot generated successfully.")


if __name__ == "__main__":
    main()