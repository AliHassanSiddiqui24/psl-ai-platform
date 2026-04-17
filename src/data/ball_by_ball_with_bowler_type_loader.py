import pandas as pd

from src.config.paths import PROCESSED_DATA_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_ball_by_ball_with_bowler_type() -> pd.DataFrame:
    file_path = (
        PROCESSED_DATA_DIR / "ball_by_ball" / "psl_ball_by_ball_with_bowler_type.csv"
    )
    df = pd.read_csv(file_path)
    logger.info("Loaded ball-by-ball with bowler type data with shape %s", df.shape)
    return df