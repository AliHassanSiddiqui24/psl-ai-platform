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