from src.config.paths import RAW_DATA_DIR
from src.data.ingestion import DataIngestion
from src.data.validation import DataValidator
from src.utils.logger import get_logger

logger = get_logger(__name__)


def run_data_pipeline():
    logger.info("Starting data pipeline...")

    ingestion = DataIngestion()
    validator = DataValidator()

    raw_data_root_exists = ingestion.check_raw_data_directory()
    raw_root_files = ingestion.list_raw_files()

    logger.info("Raw data root exists: %s", raw_data_root_exists)
    logger.info("Raw data root contains %d items.", len(raw_root_files))

    cricsheet_matches_dir = RAW_DATA_DIR / "cricsheet_psl" / "matches"

    try:
        validator.validate_directory_has_files(cricsheet_matches_dir)
        logger.info("Cricsheet PSL matches directory is ready for parsing.")
    except Exception as e:
        logger.warning("Validation warning: %s", e)

    logger.info("Data pipeline completed successfully.")


if __name__ == "__main__":
    run_data_pipeline()