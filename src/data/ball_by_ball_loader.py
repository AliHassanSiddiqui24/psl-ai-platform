import pandas as pd

from src.config.paths import INTERIM_DATA_DIR
from src.config.constants import BALL_BY_BALL_FILE_NAME
from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_ball_by_ball_data() -> pd.DataFrame:
    file_path = INTERIM_DATA_DIR / "ball_by_ball" / BALL_BY_BALL_FILE_NAME
    df = pd.read_csv(file_path)
    logger.info("Loaded ball-by-ball data with shape %s", df.shape)
    return df