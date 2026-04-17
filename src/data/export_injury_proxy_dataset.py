from src.config.paths import REPORTS_DIR
from src.data.rolling_workload_loader import load_rolling_workload_features
from src.features.injury_proxy_target import add_future_absence_proxy
from src.utils.logger import get_logger

logger = get_logger(__name__)

OUTPUT_DIR = REPORTS_DIR / "eda" / "injury" / "proxy_target"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    df = load_rolling_workload_features()
    proxy_df = add_future_absence_proxy(df)

    output_file = OUTPUT_DIR / "injury_proxy_dataset.csv"
    proxy_df.to_csv(output_file, index=False)

    logger.info("Saved injury proxy dataset to %s", output_file)
    print("Injury proxy dataset exported successfully.")
    print("\nProxy event counts:")
    print(proxy_df["injury_proxy_event"].value_counts(dropna=False))


if __name__ == "__main__":
    main()