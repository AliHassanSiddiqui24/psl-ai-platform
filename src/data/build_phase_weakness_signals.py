import pandas as pd

from src.config.paths import REPORTS_DIR
from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.phase_analysis import build_batsman_phase_summary
from src.utils.logger import get_logger

logger = get_logger(__name__)

OUTPUT_DIR = REPORTS_DIR / "eda" / "weakness" / "phase_analysis"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def build_phase_weakness_signals(df: pd.DataFrame) -> pd.DataFrame:
    summary = build_batsman_phase_summary(df)

    summary["dismissal_rate"] = (
        summary["dismissals"] / summary["balls_faced"].replace(0, pd.NA)
    ).round(4)

    summary["low_strike_rate_flag"] = summary["strike_rate"] < 110
    summary["high_dismissal_rate_flag"] = summary["dismissal_rate"] > 0.05

    return summary


def main():
    df = load_clean_ball_by_ball_data()
    signals_df = build_phase_weakness_signals(df)

    output_file = OUTPUT_DIR / "batsman_phase_weakness_signals.csv"
    signals_df.to_csv(output_file, index=False)

    logger.info("Saved phase weakness signals to %s", output_file)
    print("Phase weakness signals exported successfully.")


if __name__ == "__main__":
    main()