from src.config.paths import REPORTS_DIR
from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.workload_analysis import build_match_level_bowler_workload
from src.features.rolling_workload_features import build_rolling_workload_features
from src.features.fatigue_signals import add_fatigue_signals
from src.utils.logger import get_logger

logger = get_logger(__name__)

OUTPUT_DIR = REPORTS_DIR / "eda" / "injury" / "rolling_workload"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    ball_df = load_clean_ball_by_ball_data()
    workload_df = build_match_level_bowler_workload(ball_df)
    rolling_df = build_rolling_workload_features(workload_df)
    fatigue_df = add_fatigue_signals(rolling_df)

    output_file = OUTPUT_DIR / "bowler_rolling_workload_features.csv"
    fatigue_df.to_csv(output_file, index=False)

    logger.info("Saved rolling workload features to %s", output_file)
    print("Rolling workload features exported successfully.")


if __name__ == "__main__":
    main()