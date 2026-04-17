from src.config.paths import REPORTS_DIR
from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.weakness_heatmaps import (
    get_player_bowler_wicket_matrix,
    get_player_phase_bowler_matrix,
    get_player_phase_wicket_matrix,
)
from src.utils.logger import get_logger

logger = get_logger(__name__)

OUTPUT_DIR = REPORTS_DIR / "eda" / "weakness" / "heatmaps"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def export_player_matrices(player_name: str):
    df = load_clean_ball_by_ball_data()
    safe_name = player_name.lower().replace(" ", "_")

    phase_wicket = get_player_phase_wicket_matrix(df, player_name)
    bowler_wicket = get_player_bowler_wicket_matrix(df, player_name)
    phase_bowler = get_player_phase_bowler_matrix(df, player_name)

    if not phase_wicket.empty:
        phase_wicket.to_csv(OUTPUT_DIR / f"{safe_name}_phase_wicket_matrix.csv")

    if not bowler_wicket.empty:
        bowler_wicket.to_csv(OUTPUT_DIR / f"{safe_name}_bowler_wicket_matrix.csv")

    if not phase_bowler.empty:
        phase_bowler.to_csv(OUTPUT_DIR / f"{safe_name}_phase_bowler_matrix.csv")

    logger.info("Exported heatmap matrices for player %s", player_name)


def main():
    sample_players = [
        "Babar Azam",
        "Mohammad Rizwan",
        "Fakhar Zaman",
    ]

    for player in sample_players:
        export_player_matrices(player)

    print("Weakness heatmap tables exported successfully.")


if __name__ == "__main__":
    main()