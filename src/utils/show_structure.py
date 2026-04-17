from src.config.paths import (
    ROOT_DIR,
    DATA_DIR,
    RAW_DATA_DIR,
    INTERIM_DATA_DIR,
    PROCESSED_DATA_DIR,
    MODELS_DIR,
    REPORTS_DIR,
    LOGS_DIR,
)


def main():
    print("Project structure paths:")
    print(f"ROOT_DIR: {ROOT_DIR}")
    print(f"DATA_DIR: {DATA_DIR}")
    print(f"RAW_DATA_DIR: {RAW_DATA_DIR}")
    print(f"INTERIM_DATA_DIR: {INTERIM_DATA_DIR}")
    print(f"PROCESSED_DATA_DIR: {PROCESSED_DATA_DIR}")
    print(f"MODELS_DIR: {MODELS_DIR}")
    print(f"REPORTS_DIR: {REPORTS_DIR}")
    print(f"LOGS_DIR: {LOGS_DIR}")


if __name__ == "__main__":
    main()