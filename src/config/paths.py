from pathlib import Path

# Project root
ROOT_DIR = Path(__file__).resolve().parents[2]

# Main directories
DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

NOTEBOOKS_DIR = ROOT_DIR / "notebooks"
SRC_DIR = ROOT_DIR / "src"
MODELS_DIR = ROOT_DIR / "models"
REPORTS_DIR = ROOT_DIR / "reports"
FIGURES_DIR = REPORTS_DIR / "figures"
PDFS_DIR = REPORTS_DIR / "pdfs"
DASHBOARD_DIR = ROOT_DIR / "dashboard"
TESTS_DIR = ROOT_DIR / "tests"
CONFIG_DIR = ROOT_DIR / "config"
LOGS_DIR = ROOT_DIR / "logs"

# Create directories if they don't exist
DIRECTORIES_TO_CREATE = [
    DATA_DIR,
    RAW_DATA_DIR,
    INTERIM_DATA_DIR,
    PROCESSED_DATA_DIR,
    NOTEBOOKS_DIR,
    SRC_DIR,
    MODELS_DIR,
    REPORTS_DIR,
    FIGURES_DIR,
    PDFS_DIR,
    DASHBOARD_DIR,
    TESTS_DIR,
    CONFIG_DIR,
    LOGS_DIR,
]

for directory in DIRECTORIES_TO_CREATE:
    directory.mkdir(parents=True, exist_ok=True)
