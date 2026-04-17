import pandas as pd

from src.config.constants import (
    BALL_BY_BALL_FILE_NAME,
    CLEAN_BALL_BY_BALL_FILE_NAME,
)
from src.config.paths import INTERIM_DATA_DIR, PROCESSED_DATA_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)

INPUT_FILE = INTERIM_DATA_DIR / "ball_by_ball" / BALL_BY_BALL_FILE_NAME
OUTPUT_DIR = PROCESSED_DATA_DIR / "ball_by_ball"
OUTPUT_FILE = OUTPUT_DIR / CLEAN_BALL_BY_BALL_FILE_NAME


def load_raw_parsed_data() -> pd.DataFrame:
    df = pd.read_csv(INPUT_FILE)
    logger.info("Loaded raw parsed ball-by-ball data with shape %s", df.shape)
    return df


def standardize_text_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    for col in columns:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
                .replace({"nan": pd.NA, "None": pd.NA})
            )
    return df


def fix_data_types(df: pd.DataFrame) -> pd.DataFrame:
    numeric_columns = [
        "innings_number",
        "over",
        "ball",
        "runs_batter",
        "runs_extras",
        "runs_total",
        "wicket",
    ]

    for col in numeric_columns:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "match_date" in df.columns:
        df["match_date"] = pd.to_datetime(df["match_date"], errors="coerce")

    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    # Fill optional columns with NA where missing
    optional_text_cols = [
        "city",
        "venue",
        "extras_type",
        "wicket_type",
        "player_out",
        "fielders_involved",
        "toss_winner",
        "toss_decision",
    ]

    for col in optional_text_cols:
        if col in df.columns:
            df[col] = df[col].fillna(pd.NA)

    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    logger.info("Removed %d duplicate rows.", before - after)
    return df


def add_derived_columns(df: pd.DataFrame) -> pd.DataFrame:
    # innings phase
    def get_phase(over):
        if pd.isna(over):
            return pd.NA
        if 0 <= over <= 5:
            return "powerplay"
        elif 6 <= over <= 14:
            return "middle"
        elif 15 <= over <= 19:
            return "death"
        return pd.NA

    if "over" in df.columns:
        df["phase"] = df["over"].apply(get_phase)

    # legal ball id helper
    if "over" in df.columns and "ball" in df.columns:
        df["ball_id"] = df["over"].astype("Int64").astype(str) + "." + df["ball"].astype("Int64").astype(str)

    return df


def sort_dataset(df: pd.DataFrame) -> pd.DataFrame:
    sort_cols = [col for col in ["match_date", "match_id", "innings_number", "over", "ball"] if col in df.columns]
    if sort_cols:
        df = df.sort_values(sort_cols).reset_index(drop=True)
    return df


def clean_ball_by_ball_data() -> pd.DataFrame:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = load_raw_parsed_data()

    df = standardize_text_columns(
        df,
        [
            "match_id",
            "city",
            "venue",
            "team1",
            "team2",
            "toss_winner",
            "toss_decision",
            "batting_team",
            "batter",
            "bowler",
            "non_striker",
            "extras_type",
            "wicket_type",
            "player_out",
            "fielders_involved",
        ],
    )

    df = fix_data_types(df)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = add_derived_columns(df)
    df = sort_dataset(df)

    logger.info("Cleaned dataset shape: %s", df.shape)

    df.to_csv(OUTPUT_FILE, index=False)
    logger.info("Saved cleaned ball-by-ball dataset to %s", OUTPUT_FILE)

    return df


def main():
    df = clean_ball_by_ball_data()
    print(df.head())
    print("\nShape:", df.shape)
    print("\nDtypes:")
    print(df.dtypes)


if __name__ == "__main__":
    main()