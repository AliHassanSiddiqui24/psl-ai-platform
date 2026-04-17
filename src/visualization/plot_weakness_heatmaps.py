import matplotlib.pyplot as plt
import seaborn as sns

from src.config.paths import REPORTS_DIR
from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.weakness_heatmaps import (
    get_player_bowler_wicket_matrix,
    get_player_phase_bowler_matrix,
    get_player_phase_wicket_matrix,
)
from src.utils.logger import get_logger

logger = get_logger(__name__)

sns.set_style("whitegrid")

OUTPUT_DIR = REPORTS_DIR / "eda" / "weakness" / "heatmaps"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def save_heatmap(matrix, title, output_path, figsize=(10, 6)):
    if matrix.empty:
        logger.warning("Empty matrix for plot: %s", title)
        return

    plt.figure(figsize=figsize)
    sns.heatmap(matrix, annot=True, fmt="g", cmap="Reds")
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

    logger.info("Saved heatmap to %s", output_path)


def generate_heatmaps_for_player(player_name: str):
    df = load_clean_ball_by_ball_data()

    phase_wicket = get_player_phase_wicket_matrix(df, player_name)
    bowler_wicket = get_player_bowler_wicket_matrix(df, player_name)
    phase_bowler = get_player_phase_bowler_matrix(df, player_name)

    safe_name = player_name.lower().replace(" ", "_")

    save_heatmap(
        phase_wicket,
        title=f"{player_name} — Phase vs Wicket Type",
        output_path=OUTPUT_DIR / f"{safe_name}_phase_wicket_heatmap.png",
    )

    save_heatmap(
        bowler_wicket,
        title=f"{player_name} — Bowler vs Wicket Type",
        output_path=OUTPUT_DIR / f"{safe_name}_bowler_wicket_heatmap.png",
        figsize=(12, 6),
    )

    save_heatmap(
        phase_bowler,
        title=f"{player_name} — Phase vs Bowler",
        output_path=OUTPUT_DIR / f"{safe_name}_phase_bowler_heatmap.png",
        figsize=(12, 6),
    )


def main():
    sample_players = [
        "Babar Azam",
        "Mohammad Rizwan",
        "Fakhar Zaman",
    ]

    for player in sample_players:
        generate_heatmaps_for_player(player)

    print("Weakness proxy heatmaps generated successfully.")


if __name__ == "__main__":
    main()