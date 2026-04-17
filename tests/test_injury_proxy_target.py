import pandas as pd

from src.data.rolling_workload_loader import load_rolling_workload_features
from src.features.injury_correlation_analysis import compute_correlation_matrix
from src.features.injury_proxy_target import add_future_absence_proxy


def test_correlation_matrix_returns_dataframe():
    df = load_rolling_workload_features()
    corr_df = compute_correlation_matrix(df)
    assert isinstance(corr_df, pd.DataFrame)


def test_proxy_target_column_added():
    df = load_rolling_workload_features()
    proxy_df = add_future_absence_proxy(df)
    assert "injury_proxy_event" in proxy_df.columns


def test_proxy_target_is_binary():
    df = load_rolling_workload_features()
    proxy_df = add_future_absence_proxy(df)
    unique_vals = set(proxy_df["injury_proxy_event"].dropna().unique())
    assert unique_vals.issubset({0, 1})