from src.data.clean_ball_by_ball import clean_ball_by_ball_data
from src.utils.logger import get_logger

logger = get_logger(__name__)


def run_clean_data_pipeline():
    logger.info("Starting clean data pipeline...")
    df = clean_ball_by_ball_data()
    logger.info("Clean data pipeline completed. Final shape: %s", df.shape)


if __name__ == "__main__":
    run_clean_data_pipeline()