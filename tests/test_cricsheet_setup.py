from src.config.paths import RAW_DATA_DIR


def test_cricsheet_metadata_file_exists():
    metadata_file = RAW_DATA_DIR / "cricsheet_psl" / "download_metadata.json"
    assert metadata_file.exists()