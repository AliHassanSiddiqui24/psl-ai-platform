import pandas as pd

from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.workload_analysis import build_match_level_bowler_workload
from src.features.rolling_workload_features import build_rolling_workload_features
from src.features.fatigue_signals import add_fatigue_signals


def test_rolling_workload_features_return_dataframe():
    ball_df = load_clean_ball_by_ball_data()
    workload_df = build_match_level_bowler_workload(ball_df)
    rolling_df = build_rolling_workload_features(workload_df)
    assert isinstance(rolling_df, pd.DataFrame)


def test_rolling_workload_has_expected_columns():
    ball_df = load_clean_ball_by_ball_data()
    workload_df = build_match_level_bowler_workload(ball_df)
    rolling_df = build_rolling_workload_features(workload_df)

    expected_columns = {
        "balls_last_7_days",
        "balls_last_14_days",
        "matches_last_7_days",
        "matches_last_14_days",
        "days_since_last_match",
        "back_to_back_match",
        "short_recovery_flag",
    }

    assert expected_columns.issubset(set(rolling_df.columns))


def test_fatigue_signals_added():
    ball_df = load_clean_ball_by_ball_data()
    workload_df = build_match_level_bowler_workload(ball_df)
    rolling_df = build_rolling_workload_features(workload_df)
    fatigue_df = add_fatigue_signals(rolling_df)

    expected_columns = {
        "overs_last_7_days",
        "overs_last_14_days",
        "fatigue_signal_score",
        "high_recent_workload_flag",
        "high_match_density_flag",
        "high_fatigue_flag",
    }

    assert expected_columns.issubset(set(fatigue_df.columns))