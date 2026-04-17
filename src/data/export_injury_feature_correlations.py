import matplotlib.pyplot as plt
import seaborn as sns

from src.config.paths import REPORTS_DIR
from src.data.rolling_workload_loader import load_rolling_workload_features
from src.features.injury_correlation_analysis import compute_correlation_matrix
from src.utils.logger import get_logger

logger = get_logger(__name__)

OUTPUT_DIR = REPORTS_DIR / "eda" / "injury" / "correlation_analysis"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def main():
    df = load_rolling_workload_features()
    corr_df = compute_correlation_matrix(df)

    csv_file = OUTPUT_DIR / "injury_feature_correlation_matrix.csv"
    corr_df.to_csv(csv_file)

    plt.figure(figsize=(12, 8))
    sns.heatmap(corr_df, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix — Workload and Fatigue Features")
    plt.tight_layout()

    plot_file = OUTPUT_DIR / "injury_feature_correlation_heatmap.png"
    plt.savefig(plot_file)
    plt.close()

    logger.info("Saved correlation matrix CSV to %s", csv_file)
    logger.info("Saved correlation heatmap to %s", plot_file)

    print("Injury feature correlation analysis exported successfully.")


if __name__ == "__main__":
    main()