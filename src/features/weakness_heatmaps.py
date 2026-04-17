import pandas as pd

from src.features.dismissal_analysis import get_dismissal_rows
from src.utils.logger import get_logger

logger = get_logger(__name__)


def get_player_phase_wicket_matrix(df: pd.DataFrame, player_name: str) -> pd.DataFrame:
    dismissal_df = get_dismissal_rows(df)
    player_df = dismissal_df[dismissal_df["player_out"] == player_name].copy()

    matrix = pd.pivot_table(
        player_df,
        index="phase",
        columns="wicket_type",
        values="match_id",
        aggfunc="count",
        fill_value=0,
    )

    logger.info(
        "Generated phase vs wicket_type matrix for %s with shape %s",
        player_name,
        matrix.shape,
    )
    return matrix


def get_player_bowler_wicket_matrix(
    df: pd.DataFrame, player_name: str, top_n_bowlers: int = 10
) -> pd.DataFrame:
    dismissal_df = get_dismissal_rows(df)
    player_df = dismissal_df[dismissal_df["player_out"] == player_name].copy()

    top_bowlers = player_df["bowler"].value_counts().head(top_n_bowlers).index.tolist()
    player_df = player_df[player_df["bowler"].isin(top_bowlers)].copy()

    matrix = pd.pivot_table(
        player_df,
        index="bowler",
        columns="wicket_type",
        values="match_id",
        aggfunc="count",
        fill_value=0,
    )

    logger.info(
        "Generated bowler vs wicket_type matrix for %s with shape %s",
        player_name,
        matrix.shape,
    )
    return matrix


def get_player_phase_bowler_matrix(
    df: pd.DataFrame, player_name: str, top_n_bowlers: int = 8
) -> pd.DataFrame:
    dismissal_df = get_dismissal_rows(df)
    player_df = dismissal_df[dismissal_df["player_out"] == player_name].copy()

    top_bowlers = player_df["bowler"].value_counts().head(top_n_bowlers).index.tolist()
    player_df = player_df[player_df["bowler"].isin(top_bowlers)].copy()

    matrix = pd.pivot_table(
        player_df,
        index="phase",
        columns="bowler",
        values="match_id",
        aggfunc="count",
        fill_value=0,
    )

    logger.info(
        "Generated phase vs bowler matrix for %s with shape %s",
        player_name,
        matrix.shape,
    )
    return matrix