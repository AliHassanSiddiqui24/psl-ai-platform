from src.config.paths import REPORTS_DIR
from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.phase_analysis import build_batsman_phase_summary
from src.utils.logger import get_logger

logger = get_logger(__name__)

OUTPUT_DIR = REPORTS_DIR / "eda" / "weakness" / "phase_analysis"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    df = load_clean_ball_by_ball_data()
    phase_summary = build_batsman_phase_summary(df)

    output_file = OUTPUT_DIR / "batsman_phase_summary.csv"
    phase_summary.to_csv(output_file, index=False)

    logger.info("Saved batsman phase summary to %s", output_file)
    print("Batsman phase summary exported successfully.")


if __name__ == "__main__":
    main()