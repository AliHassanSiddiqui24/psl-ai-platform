import pandas as pd

from src.config.paths import INTERIM_DATA_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_player_manual_attributes() -> pd.DataFrame:
    file_path = INTERIM_DATA_DIR / "player_data" / "player_manual_attributes_template.csv"
    df = pd.read_csv(file_path)
    logger.info("Loaded player manual attributes with shape %s", df.shape)
    return df


def load_player_master() -> pd.DataFrame:
    file_path = INTERIM_DATA_DIR / "player_data" / "player_master.csv"
    df = pd.read_csv(file_path)
    logger.info("Loaded player master with shape %s", df.shape)
    return df