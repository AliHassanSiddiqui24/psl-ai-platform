import pandas as pd
from pathlib import Path

from src.utils.exceptions import DataValidationError
from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_csv(file_path: Path) -> pd.DataFrame:
    try:
        if not file_path.exists():
            raise DataValidationError(f"CSV file not found: {file_path}")

        df = pd.read_csv(file_path)
        logger.info("CSV loaded successfully from %s with shape %s", file_path, df.shape)
        return df
    except Exception as e:
        logger.exception("Failed to load CSV file.")
        raise