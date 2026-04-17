import pandas as pd

from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.phase_analysis import build_batsman_phase_summary


def test_phase_summary_returns_dataframe():
    df = load_clean_ball_by_ball_data()
    summary = build_batsman_phase_summary(df)
    assert isinstance(summary, pd.DataFrame)


def test_phase_summary_has_expected_columns():
    df = load_clean_ball_by_ball_data()
    summary = build_batsman_phase_summary(df)

    expected_columns = {
        "batter",
        "phase",
        "balls_faced",
        "runs_scored",
        "dismissals",
        "matches",
        "strike_rate",
    }

    assert expected_columns.issubset(set(summary.columns))