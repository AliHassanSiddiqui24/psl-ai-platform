import pandas as pd

from src.config.constants import CLEAN_BALL_BY_BALL_FILE_NAME
from src.config.paths import PROCESSED_DATA_DIR
from src.data.cleaned_ball_by_ball_validation import validate_clean_ball_by_ball_schema


def test_clean_ball_by_ball_file_exists():
    file_path = PROCESSED_DATA_DIR / "ball_by_ball" / CLEAN_BALL_BY_BALL_FILE_NAME
    assert file_path.exists()


def test_clean_ball_by_ball_schema():
    file_path = PROCESSED_DATA_DIR / "ball_by_ball" / CLEAN_BALL_BY_BALL_FILE_NAME
    df = pd.read_csv(file_path)
    assert validate_clean_ball_by_ball_schema(df) is True


def test_no_duplicate_rows_in_cleaned_data():
    file_path = PROCESSED_DATA_DIR / "ball_by_ball" / CLEAN_BALL_BY_BALL_FILE_NAME
    df = pd.read_csv(file_path)
    assert df.duplicated().sum() == 0