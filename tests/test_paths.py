from src.config.paths import RAW_DATA_DIR, PROCESSED_DATA_DIR, REPORTS_DIR


def test_paths_exist():
    assert RAW_DATA_DIR.exists()
    assert PROCESSED_DATA_DIR.exists()
    assert REPORTS_DIR.exists()