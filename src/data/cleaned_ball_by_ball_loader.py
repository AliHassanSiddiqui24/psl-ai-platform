import pandas as pd

from src.config.constants import CLEAN_BALL_BY_BALL_FILE_NAME
from src.config.paths import PROCESSED_DATA_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_clean_ball_by_ball_data() -> pd.DataFrame:
    file_path = PROCESSED_DATA_DIR / "ball_by_ball" / CLEAN_BALL_BY_BALL_FILE_NAME
    df = pd.read_csv(file_path)
    logger.info("Loaded cleaned ball-by-ball data with shape %s", df.shape)
    return df