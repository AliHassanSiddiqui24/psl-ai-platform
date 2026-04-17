import pandas as pd

from src.config.paths import INTERIM_DATA_DIR, PROCESSED_DATA_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)

INPUT_FILE = INTERIM_DATA_DIR / "player_data" / "player_manual_attributes_template.csv"
OUTPUT_DIR = PROCESSED_DATA_DIR / "player_data"
OUTPUT_FILE = OUTPUT_DIR / "player_manual_attributes_clean.csv"


def clean_manual_attributes(df: pd.DataFrame) -> pd.DataFrame:
    text_columns = [
        "player_name",
        "batting_hand",
        "bowling_style",
        "player_role",
        "country",
        "notes",
    ]

    for col in text_columns:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
                .replace({"nan": pd.NA, "None": pd.NA})
            )

    if "is_overseas" in df.columns:
        df["is_overseas"] = df["is_overseas"].astype(str).str.strip().replace(
            {"True": True, "False": False, "nan": pd.NA}
        )

    if "date_of_birth" in df.columns:
        df["date_of_birth"] = pd.to_datetime(df["date_of_birth"], errors="coerce")

    df = df.drop_duplicates(subset=["player_name"], keep="first")
    return df


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(INPUT_FILE)
    clean_df = clean_manual_attributes(df)

    clean_df.to_csv(OUTPUT_FILE, index=False)
    logger.info(
        "Saved cleaned player manual attributes to %s with shape %s",
        OUTPUT_FILE,
        clean_df.shape,
    )

    print(clean_df.head())
    print("\nShape:", clean_df.shape)


if __name__ == "__main__":
    main()