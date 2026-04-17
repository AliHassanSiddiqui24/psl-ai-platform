import pandas as pd

from src.data.ball_by_ball_with_bowler_type_loader import load_ball_by_ball_with_bowler_type
from src.features.batter_vs_bowler_type_analysis import build_batter_vs_bowler_type_summary


def test_batter_vs_bowler_type_summary_returns_dataframe():
    df = load_ball_by_ball_with_bowler_type()
    summary = build_batter_vs_bowler_type_summary(df)
    assert isinstance(summary, pd.DataFrame)


def test_batter_vs_bowler_type_summary_has_expected_columns():
    df = load_ball_by_ball_with_bowler_type()
    summary = build_batter_vs_bowler_type_summary(df)

    expected_columns = {
        "batter",
        "bowler_type",
        "balls_faced",
        "runs_scored",
        "dismissals",
        "strike_rate",
        "dismissal_rate",
    }

    assert expected_columns.issubset(set(summary.columns))