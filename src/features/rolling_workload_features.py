import pandas as pd

from src.utils.logger import get_logger

logger = get_logger(__name__)


def build_rolling_workload_features(workload_df: pd.DataFrame) -> pd.DataFrame:
    df = workload_df.copy()
    df["match_date"] = pd.to_datetime(df["match_date"], errors="coerce")

    df = df.sort_values(["bowler", "match_date"]).reset_index(drop=True)

    feature_frames = []

    for bowler, group in df.groupby("bowler"):
        group = group.sort_values("match_date").copy()
        group = group.reset_index(drop=True)

        balls_last_7_days = []
        balls_last_14_days = []
        matches_last_7_days = []
        matches_last_14_days = []
        days_since_last_match = []
        back_to_back_match = []
        short_recovery_flag = []

        for idx, row in group.iterrows():
            current_date = row["match_date"]

            prev_rows = group[group["match_date"] < current_date].copy()

            prev_7 = prev_rows[
                prev_rows["match_date"] >= (current_date - pd.Timedelta(days=7))
            ]
            prev_14 = prev_rows[
                prev_rows["match_date"] >= (current_date - pd.Timedelta(days=14))
            ]

            balls_last_7_days.append(prev_7["balls_bowled"].sum())
            balls_last_14_days.append(prev_14["balls_bowled"].sum())
            matches_last_7_days.append(prev_7["match_id"].nunique())
            matches_last_14_days.append(prev_14["match_id"].nunique())

            if idx == 0:
                days_since_last_match.append(pd.NA)
                back_to_back_match.append(0)
                short_recovery_flag.append(0)
            else:
                previous_date = group.loc[idx - 1, "match_date"]
                day_gap = (current_date - previous_date).days
                days_since_last_match.append(day_gap)
                back_to_back_match.append(1 if day_gap == 1 else 0)
                short_recovery_flag.append(1 if day_gap <= 2 else 0)

        group["balls_last_7_days"] = balls_last_7_days
        group["balls_last_14_days"] = balls_last_14_days
        group["matches_last_7_days"] = matches_last_7_days
        group["matches_last_14_days"] = matches_last_14_days
        group["days_since_last_match"] = days_since_last_match
        group["back_to_back_match"] = back_to_back_match
        group["short_recovery_flag"] = short_recovery_flag

        feature_frames.append(group)

    result = pd.concat(feature_frames, ignore_index=True)
    logger.info("Built rolling workload features with shape %s", result.shape)
    return result