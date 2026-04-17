from src.config.paths import REPORTS_DIR
from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.data.player_profile_loader import load_player_profile_master

SUMMARY_DIR = REPORTS_DIR / "eda"
SUMMARY_DIR.mkdir(parents=True, exist_ok=True)


def main():
    ball_df = load_clean_ball_by_ball_data()
    player_df = load_player_profile_master()

    phase_counts = ball_df["phase"].value_counts(dropna=False).reset_index()
    phase_counts.columns = ["phase", "count"]
    phase_counts.to_csv(SUMMARY_DIR / "phase_counts.csv", index=False)

    runs_distribution = ball_df["runs_total"].value_counts().sort_index().reset_index()
    runs_distribution.columns = ["runs_total", "count"]
    runs_distribution.to_csv(SUMMARY_DIR / "runs_distribution.csv", index=False)

    top_batters = (
        ball_df.groupby("batter")["runs_batter"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .head(20)
    )
    top_batters.to_csv(SUMMARY_DIR / "top_batters_by_runs.csv", index=False)

    top_bowlers = (
        ball_df.groupby("bowler")["wicket"]
        .sum()
        .sort_values(ascending=False)
        .reset_index()
        .head(20)
    )
    top_bowlers.to_csv(SUMMARY_DIR / "top_bowlers_by_wickets.csv", index=False)

    player_missing = player_df.isna().sum().reset_index()
    player_missing.columns = ["column", "missing_count"]
    player_missing.to_csv(SUMMARY_DIR / "player_profile_missing_summary.csv", index=False)

    print("Summary tables exported successfully.")


if __name__ == "__main__":
    main()