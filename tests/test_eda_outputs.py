from src.config.paths import REPORTS_DIR


def test_basic_eda_summary_file_exists():
    summary_file = REPORTS_DIR / "eda" / "ball_by_ball_basic_summary.json"
    assert summary_file.exists()