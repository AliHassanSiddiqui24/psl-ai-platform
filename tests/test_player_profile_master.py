import pandas as pd

from src.config.constants import PLAYER_PROFILE_MASTER_FILE_NAME
from src.config.paths import PROCESSED_DATA_DIR
from src.data.player_profile_validation import validate_player_profile_master


def test_player_profile_master_file_exists():
    file_path = PROCESSED_DATA_DIR / "player_data" / PLAYER_PROFILE_MASTER_FILE_NAME
    assert file_path.exists()


def test_player_profile_master_schema():
    file_path = PROCESSED_DATA_DIR / "player_data" / PLAYER_PROFILE_MASTER_FILE_NAME
    df = pd.read_csv(file_path)
    assert validate_player_profile_master(df) is True