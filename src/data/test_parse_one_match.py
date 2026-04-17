from pathlib import Path

from src.data.cricsheet_parser import parse_match_file
from src.utils.logger import get_logger

logger = get_logger(__name__)


def main():
    matches_dir = Path("data/raw/cricsheet_psl/matches")
    yaml_files = list(matches_dir.glob("*.yaml"))

    if not yaml_files:
        print("No YAML files found in data/raw/cricsheet_psl/matches")
        return

    sample_file = yaml_files[0]
    print(f"Parsing sample file: {sample_file.name}")

    df = parse_match_file(sample_file)
    print(df.head())
    print("\nShape:", df.shape)
    print("\nColumns:", df.columns.tolist())


if __name__ == "__main__":
    main()