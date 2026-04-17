import pandas as pd

from src.config.paths import INTERIM_DATA_DIR
from src.data.player_validation import validate_player_attributes_schema


def test_player_manual_attributes_template_exists():
    file_path = (
        INTERIM_DATA_DIR / "player_data" / "player_manual_attributes_template.csv"
    )
    assert file_path.exists()


def test_player_manual_attributes_schema():
    file_path = (
        INTERIM_DATA_DIR / "player_data" / "player_manual_attributes_template.csv"
    )
    df = pd.read_csv(file_path)
    assert validate_player_attributes_schema(df) is True