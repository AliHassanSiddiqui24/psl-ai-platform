import pandas as pd

from src.config.paths import REPORTS_DIR
from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_rolling_workload_features() -> pd.DataFrame:
    file_path = (
        REPORTS_DIR
        / "eda"
        / "injury"
        / "rolling_workload"
        / "bowler_rolling_workload_features.csv"
    )
    df = pd.read_csv(file_path)
    logger.info("Loaded rolling workload features with shape %s", df.shape)
    return df