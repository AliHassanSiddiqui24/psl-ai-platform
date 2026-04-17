import pandas as pd

from src.config.paths import REPORTS_DIR
from src.data.ball_by_ball_with_bowler_type_loader import load_ball_by_ball_with_bowler_type
from src.features.batter_vs_bowler_type_analysis import build_batter_vs_bowler_type_summary
from src.utils.logger import get_logger

logger = get_logger(__name__)

OUTPUT_DIR = REPORTS_DIR / "eda" / "weakness" / "bowler_type_matchups"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_bowler_type_weakness_signals(df: pd.DataFrame) -> pd.DataFrame:
    summary = build_batter_vs_bowler_type_summary(df)

    summary["low_strike_rate_flag"] = summary["strike_rate"] < 110
    summary["high_dismissal_rate_flag"] = summary["dismissal_rate"] > 0.05
    summary["small_sample_flag"] = summary["balls_faced"] < 20

    return summary


def main():
    df = load_ball_by_ball_with_bowler_type()
    signals_df = build_bowler_type_weakness_signals(df)

    output_file = OUTPUT_DIR / "batter_vs_bowler_type_weakness_signals.csv"
    signals_df.to_csv(output_file, index=False)

    logger.info("Saved bowler type weakness signals to %s", output_file)
    print("Bowler type weakness signals exported successfully.")


if __name__ == "__main__":
    main()