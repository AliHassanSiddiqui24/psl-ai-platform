from src.data.ingestion import DataIngestion
from src.utils.logger import get_logger

logger = get_logger(__name__)


def run_data_pipeline():
    logger.info("Starting data pipeline...")

    ingestion = DataIngestion()

    directory_exists = ingestion.check_raw_data_directory()
    raw_files = ingestion.list_raw_files()

    logger.info("Raw data directory exists: %s", directory_exists)
    logger.info("Number of raw files found: %d", len(raw_files))

    logger.info("Data pipeline completed successfully.")


if __name__ == "__main__":
    run_data_pipeline()