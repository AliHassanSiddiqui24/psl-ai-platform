from src.config.paths import REPORTS_DIR
from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.workload_analysis import build_match_level_bowler_workload
from src.utils.logger import get_logger

logger = get_logger(__name__)

OUTPUT_DIR = REPORTS_DIR / "eda" / "injury" / "workload_trends"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    df = load_clean_ball_by_ball_data()
    workload_df = build_match_level_bowler_workload(df)

    output_file = OUTPUT_DIR / "match_level_bowler_workload.csv"
    workload_df.to_csv(output_file, index=False)

    logger.info("Saved match-level bowler workload to %s", output_file)
    print("Match-level bowler workload exported successfully.")


if __name__ == "__main__":
    main()