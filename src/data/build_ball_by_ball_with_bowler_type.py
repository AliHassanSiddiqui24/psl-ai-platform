import pandas as pd

from src.config.paths import PROCESSED_DATA_DIR
from src.features.bowler_type_mapping import add_simplified_bowler_type
from src.utils.logger import get_logger

logger = get_logger(__name__)

BALL_FILE = PROCESSED_DATA_DIR / "ball_by_ball" / "psl_ball_by_ball_clean.csv"
PLAYER_FILE = PROCESSED_DATA_DIR / "player_data" / "player_manual_attributes_clean.csv"

OUTPUT_DIR = PROCESSED_DATA_DIR / "ball_by_ball"
OUTPUT_FILE = OUTPUT_DIR / "psl_ball_by_ball_with_bowler_type.csv"


def main():
    ball_df = pd.read_csv(BALL_FILE)
    player_df = pd.read_csv(PLAYER_FILE)

    bowler_meta = player_df[["player_name", "bowling_style"]].copy()
    bowler_meta = bowler_meta.rename(columns={"player_name": "bowler"})

    bowler_meta = add_simplified_bowler_type(bowler_meta, "bowling_style")

    merged_df = pd.merge(ball_df, bowler_meta, on="bowler", how="left")
    merged_df["bowler_type"] = merged_df["bowler_type"].fillna("Unknown")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    merged_df.to_csv(OUTPUT_FILE, index=False)

    logger.info(
        "Saved ball-by-ball with bowler type to %s with shape %s",
        OUTPUT_FILE,
        merged_df.shape,
    )

    print(merged_df.head())
    print("\nShape:", merged_df.shape)
    print("\nBowler type counts:")
    print(merged_df["bowler_type"].value_counts(dropna=False))


if __name__ == "__main__":
    main()