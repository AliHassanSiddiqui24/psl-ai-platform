from src.config.paths import REPORTS_DIR
from src.data.ball_by_ball_with_bowler_type_loader import load_ball_by_ball_with_bowler_type
from src.features.batter_vs_bowler_type_analysis import build_batter_vs_bowler_type_summary
from src.utils.logger import get_logger

logger = get_logger(__name__)

OUTPUT_DIR = REPORTS_DIR / "eda" / "weakness" / "bowler_type_matchups"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    df = load_ball_by_ball_with_bowler_type()
    summary = build_batter_vs_bowler_type_summary(df)

    output_file = OUTPUT_DIR / "batter_vs_bowler_type_summary.csv"
    summary.to_csv(output_file, index=False)

    logger.info("Saved batter vs bowler type summary to %s", output_file)
    print("Batter vs bowler type summary exported successfully.")


if __name__ == "__main__":
    main()