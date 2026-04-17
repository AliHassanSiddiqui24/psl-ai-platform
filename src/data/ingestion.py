from pathlib import Path

from src.config.paths import RAW_DATA_DIR
from src.utils.exceptions import DataIngestionError
from src.utils.logger import get_logger

logger = get_logger(__name__)


class DataIngestion:
    def __init__(self, raw_data_dir: Path = RAW_DATA_DIR):
        self.raw_data_dir = raw_data_dir

    def list_raw_files(self):
        try:
            files = list(self.raw_data_dir.glob("*"))
            logger.info("Found %d raw files in %s", len(files), self.raw_data_dir)
            return files
        except Exception as e:
            logger.exception("Failed to list raw files.")
            raise DataIngestionError(f"Error listing raw files: {e}")

    def check_raw_data_directory(self):
        try:
            exists = self.raw_data_dir.exists()
            logger.info("Raw data directory exists: %s", exists)
            return exists
        except Exception as e:
            logger.exception("Failed to check raw data directory.")
            raise DataIngestionError(f"Error checking raw data directory: {e}")