import pandas as pd

from src.config.constants import PLAYER_MASTER_FILE_NAME
from src.config.paths import INTERIM_DATA_DIR, PROCESSED_DATA_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)

INPUT_FILE = PROCESSED_DATA_DIR / "ball_by_ball" / "psl_ball_by_ball_clean.csv"
OUTPUT_DIR = INTERIM_DATA_DIR / "player_data"
OUTPUT_FILE = OUTPUT_DIR / PLAYER_MASTER_FILE_NAME


def extract_unique_players(df: pd.DataFrame) -> pd.DataFrame:
    batter_df = df[["batter", "match_id"]].rename(columns={"batter": "player_name"})
    bowler_df = df[["bowler", "match_id"]].rename(columns={"bowler": "player_name"})
    non_striker_df = df[["non_striker", "match_id"]].rename(
        columns={"non_striker": "player_name"}
    )

    combined = pd.concat([batter_df, bowler_df, non_striker_df], ignore_index=True)
    combined = combined.dropna(subset=["player_name"])

    player_summary = (
        combined.groupby("player_name")
        .agg(
            first_seen_match_id=("match_id", "min"),
            last_seen_match_id=("match_id", "max"),
        )
        .reset_index()
    )

    player_summary["source"] = "cricsheet_parsed"
    player_summary["notes"] = pd.NA

    player_summary = player_summary[
        ["player_name", "source", "first_seen_match_id", "last_seen_match_id", "notes"]
    ].sort_values("player_name").reset_index(drop=True)

    return player_summary


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(INPUT_FILE)
    player_master_df = extract_unique_players(df)

    player_master_df.to_csv(OUTPUT_FILE, index=False)
    logger.info("Saved player master to %s with shape %s", OUTPUT_FILE, player_master_df.shape)

    print(player_master_df.head())
    print("\nShape:", player_master_df.shape)


if __name__ == "__main__":
    main()