import matplotlib.pyplot as plt
import seaborn as sns

from src.config.paths import REPORTS_DIR
from src.data.ball_by_ball_with_bowler_type_loader import load_ball_by_ball_with_bowler_type
from src.features.batter_vs_bowler_type_analysis import get_selected_batters_matchup_summary
from src.utils.logger import get_logger

logger = get_logger(__name__)

sns.set_style("whitegrid")

OUTPUT_DIR = REPORTS_DIR / "eda" / "weakness" / "bowler_type_matchups"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def plot_selected_batters_strike_rate(selected_batters: list[str]):
    df = load_ball_by_ball_with_bowler_type()
    summary = get_selected_batters_matchup_summary(df, selected_batters)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=summary, x="bowler_type", y="strike_rate", hue="batter")
    plt.title("Strike Rate vs Bowler Type for Selected Batters")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    output_path = OUTPUT_DIR / "selected_batters_strike_rate_vs_bowler_type.png"
    plt.savefig(output_path)
    plt.close()

    logger.info("Saved plot: %s", output_path)


def plot_selected_batters_dismissal_rate(selected_batters: list[str]):
    df = load_ball_by_ball_with_bowler_type()
    summary = get_selected_batters_matchup_summary(df, selected_batters)

    plt.figure(figsize=(12, 6))
    sns.barplot(data=summary, x="bowler_type", y="dismissal_rate", hue="batter")
    plt.title("Dismissal Rate vs Bowler Type for Selected Batters")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()

    output_path = OUTPUT_DIR / "selected_batters_dismissal_rate_vs_bowler_type.png"
    plt.savefig(output_path)
    plt.close()

    logger.info("Saved plot: %s", output_path)


def main():
    selected_batters = ["Babar Azam", "Mohammad Rizwan", "Fakhar Zaman"]

    plot_selected_batters_strike_rate(selected_batters)
    plot_selected_batters_dismissal_rate(selected_batters)

    print("Batter vs bowler type plots generated successfully.")


if __name__ == "__main__":
    main()