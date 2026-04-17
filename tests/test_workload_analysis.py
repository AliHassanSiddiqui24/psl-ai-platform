import pandas as pd

from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.workload_analysis import build_match_level_bowler_workload


def test_workload_analysis_returns_dataframe():
    df = load_clean_ball_by_ball_data()
    workload_df = build_match_level_bowler_workload(df)
    assert isinstance(workload_df, pd.DataFrame)


def test_workload_analysis_has_expected_columns():
    df = load_clean_ball_by_ball_data()
    workload_df = build_match_level_bowler_workload(df)

    expected_columns = {
        "match_id",
        "match_date",
        "bowler",
        "balls_bowled",
        "runs_conceded",
        "wickets_taken",
        "overs_bowled",
    }

    assert expected_columns.issubset(set(workload_df.columns))