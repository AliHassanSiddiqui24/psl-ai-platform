import pandas as pd

from src.config.constants import PLAYER_PROFILE_MASTER_FILE_NAME
from src.config.paths import PROCESSED_DATA_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_player_profile_master() -> pd.DataFrame:
    file_path = PROCESSED_DATA_DIR / "player_data" / PLAYER_PROFILE_MASTER_FILE_NAME
    df = pd.read_csv(file_path)
    logger.info("Loaded player profile master with shape %s", df.shape)
    return df