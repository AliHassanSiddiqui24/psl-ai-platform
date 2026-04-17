from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from src.utils.logger import get_logger

logger = get_logger(__name__)

sns.set_style("whitegrid")


def save_bar_plot(data, x, y, title, output_path, figsize=(10, 6), rotate_x=False):
    plt.figure(figsize=figsize)
    sns.barplot(data=data, x=x, y=y)
    plt.title(title)
    if rotate_x:
        plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    logger.info("Saved bar plot to %s", output_path)


def save_count_plot(data, x, title, output_path, figsize=(10, 6), rotate_x=False):
    plt.figure(figsize=figsize)
    sns.countplot(data=data, x=x)
    plt.title(title)
    if rotate_x:
        plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    logger.info("Saved count plot to %s", output_path)


def save_histogram(data, column, title, output_path, figsize=(10, 6), bins=30):
    plt.figure(figsize=figsize)
    sns.histplot(data[column].dropna(), bins=bins, kde=True)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    logger.info("Saved histogram to %s", output_path)


def save_missing_values_plot(df: pd.DataFrame, output_path: Path):
    missing = df.isna().sum().sort_values(ascending=False)
    missing = missing[missing > 0]

    if missing.empty:
        logger.info("No missing values found. Skipping missing values plot.")
        return

    plt.figure(figsize=(12, 6))
    sns.barplot(x=missing.index, y=missing.values)
    plt.title("Missing Values by Column")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
    logger.info("Saved missing values plot to %s", output_path)