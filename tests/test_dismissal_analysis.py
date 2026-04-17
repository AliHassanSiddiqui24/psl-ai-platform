import pandas as pd

from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.dismissal_analysis import (
    build_batsman_dismissal_summary,
    get_dismissal_rows,
)


def test_get_dismissal_rows_returns_dataframe():
    df = load_clean_ball_by_ball_data()
    dismissal_df = get_dismissal_rows(df)
    assert isinstance(dismissal_df, pd.DataFrame)


def test_dismissal_summary_has_expected_columns():
    df = load_clean_ball_by_ball_data()
    summary_df = build_batsman_dismissal_summary(df)

    expected_columns = {"player_out", "wicket_type", "dismissal_count"}
    assert expected_columns.issubset(set(summary_df.columns))