import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


def add_future_absence_proxy(
    df: pd.DataFrame,
    future_window_days: int = 7,
    fatigue_threshold: float = 10.0,
    recent_workload_threshold: float = 8.0,
) -> pd.DataFrame:
    result = df.copy()
    result["match_date"] = pd.to_datetime(result["match_date"], errors="coerce")
    result = result.sort_values(["bowler", "match_date"]).reset_index(drop=True)

    proxy_flags = []

    for bowler, group in result.groupby("bowler"):
        group = group.sort_values("match_date").copy()
        group_flags = []

        for idx, row in group.iterrows():
            current_date = row["match_date"]
            future_cutoff = current_date + pd.Timedelta(days=future_window_days)

            future_rows = group[
                (group["match_date"] > current_date)
                & (group["match_date"] <= future_cutoff)
            ]

            no_future_appearance = future_rows.empty
            high_fatigue = row.get("fatigue_signal_score", 0) >= fatigue_threshold
            high_recent_workload = row.get("overs_last_7_days", 0) >= recent_workload_threshold

            proxy_event = int(no_future_appearance and high_fatigue and high_recent_workload)
            group_flags.append(proxy_event)

        group["injury_proxy_event"] = group_flags
        proxy_flags.append(group)

    final_df = pd.concat(proxy_flags, ignore_index=True)
    logger.info("Added injury proxy event column with shape %s", final_df.shape)
    return final_df