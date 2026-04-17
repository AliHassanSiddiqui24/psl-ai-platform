from pathlib import Path
import pandas as pd

from src.config.constants import BALL_BY_BALL_FILE_NAME
from src.config.paths import INTERIM_DATA_DIR, RAW_DATA_DIR
from src.data.cricsheet_parser import parse_match_file
from src.utils.logger import get_logger

logger = get_logger(__name__)

MATCHES_DIR = RAW_DATA_DIR / "cricsheet_psl" / "matches"
OUTPUT_DIR = INTERIM_DATA_DIR / "ball_by_ball"
OUTPUT_FILE = OUTPUT_DIR / BALL_BY_BALL_FILE_NAME


def build_ball_by_ball_dataset() -> pd.DataFrame:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    yaml_files = list(MATCHES_DIR.glob("*.yaml"))
    logger.info("Found %d YAML files to parse.", len(yaml_files))

    all_dfs = []

    for i, file_path in enumerate(yaml_files, start=1):
        try:
            logger.info("Processing file %d/%d: %s", i, len(yaml_files), file_path.name)
            match_df = parse_match_file(file_path)
            all_dfs.append(match_df)
        except Exception as e:
            logger.exception("Failed to parse file %s: %s", file_path.name, e)

    if not all_dfs:
        logger.warning("No match dataframes were created.")
        return pd.DataFrame()

    final_df = pd.concat(all_dfs, ignore_index=True)
    logger.info("Final ball-by-ball dataset shape: %s", final_df.shape)

    final_df.to_csv(OUTPUT_FILE, index=False)
    logger.info("Saved ball-by-ball dataset to %s", OUTPUT_FILE)

    return final_df


def main():
    df = build_ball_by_ball_dataset()
    print(df.head())
    print("\nFinal shape:", df.shape)


if __name__ == "__main__":
    main()