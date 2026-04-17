from pathlib import Path

from src.utils.exceptions import DataValidationError
from src.utils.logger import get_logger

logger = get_logger(__name__)


class DataValidator:
    def validate_file_exists(self, file_path: Path) -> bool:
        try:
            if not file_path.exists():
                raise DataValidationError(f"File does not exist: {file_path}")

            logger.info("Validated file exists: %s", file_path)
            return True
        except Exception as e:
            logger.exception("File validation failed.")
            raise DataValidationError(str(e))

    def validate_directory_has_files(self, directory_path: Path) -> bool:
        try:
            if not directory_path.exists():
                raise DataValidationError(f"Directory does not exist: {directory_path}")

            files = list(directory_path.glob("*"))
            if len(files) == 0:
                raise DataValidationError(f"No files found in directory: {directory_path}")

            logger.info("Validated directory has %d files: %s", len(files), directory_path)
            return True
        except Exception as e:
            logger.exception("Directory validation failed.")
            raise DataValidationError(str(e))