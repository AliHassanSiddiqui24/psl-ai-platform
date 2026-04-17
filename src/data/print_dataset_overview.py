from src.data.cleaned_ball_by_ball_loader import load_clean_ball_by_ball_data
from src.data.player_profile_loader import load_player_profile_master


def main():
    ball_df = load_clean_ball_by_ball_data()
    player_df = load_player_profile_master()

    print("=" * 60)
    print("PSL AI PLATFORM — DATASET OVERVIEW")
    print("=" * 60)

    print("\n[Ball-by-Ball Data]")
    print(f"Shape: {ball_df.shape}")
    print(f"Matches: {ball_df['match_id'].nunique()}")
    print(f"Batters: {ball_df['batter'].nunique()}")
    print(f"Bowlers: {ball_df['bowler'].nunique()}")
    print(f"Venues: {ball_df['venue'].nunique()}")
    print(f"Runs: {ball_df['runs_total'].sum()}")
    print(f"Wickets: {ball_df['wicket'].sum()}")

    print("\n[Phase Distribution]")
    print(ball_df["phase"].value_counts(dropna=False))

    print("\n[Player Profile Data]")
    print(f"Shape: {player_df.shape}")
    print(f"Unique players: {player_df['player_name'].nunique()}")

    if "player_role" in player_df.columns:
        print("\nPlayer roles available:")
        print(player_df["player_role"].value_counts(dropna=False).head(10))

    print("=" * 60)


if __name__ == "__main__":
    main()