import pandas as pd

from src.config.constants import CLEAN_BALL_BY_BALL_FILE_NAME
from src.config.paths import PROCESSED_DATA_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)

INPUT_FILE = PROCESSED_DATA_DIR / "ball_by_ball" / CLEAN_BALL_BY_BALL_FILE_NAME


def generate_quality_report(df: pd.DataFrame) -> dict:
    report = {
        "row_count": len(df),
        "column_count": len(df.columns),
        "missing_values": df.isna().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "unique_matches": int(df["match_id"].nunique()) if "match_id" in df.columns else None,
        "unique_batters": int(df["batter"].nunique()) if "batter" in df.columns else None,
        "unique_bowlers": int(df["bowler"].nunique()) if "bowler" in df.columns else None,
    }
    return report


def main():
    df = pd.read_csv(INPUT_FILE)
    report = generate_quality_report(df)

    print("Ball-by-Ball Quality Report")
    print("-" * 40)
    for key, value in report.items():
        print(f"{key}: {value}")


if __name__ == "__main__":
    main()