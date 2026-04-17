import pandas as pd

from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.features.weakness_heatmaps import get_player_phase_wicket_matrix


def test_phase_wicket_matrix_returns_dataframe():
    df = load_clean_ball_by_ball_data()
    matrix = get_player_phase_wicket_matrix(df, "Babar Azam")
    assert isinstance(matrix, pd.DataFrame)