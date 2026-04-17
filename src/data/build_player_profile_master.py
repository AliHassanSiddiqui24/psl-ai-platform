import pandas as pd

from src.config.constants import PLAYER_PROFILE_MASTER_FILE_NAME
from src.config.paths import INTERIM_DATA_DIR, PROCESSED_DATA_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)

PLAYER_MASTER_FILE = INTERIM_DATA_DIR / "player_data" / "player_master.csv"
PLAYER_DERIVED_FILE = PROCESSED_DATA_DIR / "player_data" / "player_derived_stats.csv"
PLAYER_MANUAL_FILE = PROCESSED_DATA_DIR / "player_data" / "player_manual_attributes_clean.csv"

OUTPUT_DIR = PROCESSED_DATA_DIR / "player_data"
OUTPUT_FILE = OUTPUT_DIR / PLAYER_PROFILE_MASTER_FILE_NAME


def build_player_profile_master() -> pd.DataFrame:
    player_master = pd.read_csv(PLAYER_MASTER_FILE)
    player_derived = pd.read_csv(PLAYER_DERIVED_FILE)
    player_manual = pd.read_csv(PLAYER_MANUAL_FILE)

    df = pd.merge(player_master, player_derived, on="player_name", how="left")
    df = pd.merge(df, player_manual, on="player_name", how="left")

    return df


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    df = build_player_profile_master()
    df.to_csv(OUTPUT_FILE, index=False)

    logger.info("Saved player profile master to %s with shape %s", OUTPUT_FILE, df.shape)

    print(df.head())
    print("\nShape:", df.shape)


if __name__ == "__main__":
    main()