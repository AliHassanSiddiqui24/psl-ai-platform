import pandas as pd

from src.config.paths import INTERIM_DATA_DIR
from src.config.constants import BALL_BY_BALL_FILE_NAME
from src.data.ball_by_ball_validation import validate_ball_by_ball_schema


def test_ball_by_ball_file_exists():
    file_path = INTERIM_DATA_DIR / "ball_by_ball" / BALL_BY_BALL_FILE_NAME
    assert file_path.exists()


def test_ball_by_ball_schema():
    file_path = INTERIM_DATA_DIR / "ball_by_ball" / BALL_BY_BALL_FILE_NAME
    df = pd.read_csv(file_path)
    assert validate_ball_by_ball_schema(df) is True