# PSL Player Intelligence Platform

AI/ML-powered cricket analytics platform focused on:

- Batsman weakness detection
- Player workload and injury risk prediction
- Decision-support dashboard for cricket teams

## Project Goal
Build a professional end-to-end ML system that can be used as a strong portfolio project for cricket analytics roles in PCB, PSL franchises, and global cricket organizations.

## Initial Modules
1. Weakness Detection Engine
2. Injury Risk Prediction Engine
3. Dashboard and Reporting Layer
4. MLOps / Deployment Layer

## Tech Stack
- Python
- pandas
- scikit-learn
- XGBoost
- Streamlit
- FastAPI
- MLflow
- Docker

## Project Structure
- `data/` → raw, interim, processed data
- `notebooks/` → exploratory analysis
- `src/` → source code
- `models/` → trained model artifacts
- `reports/` → plots and PDFs
- `dashboard/` → Streamlit app
- `tests/` → tests
- `config/` → configs

## Status
Project setup in progress.
## Setup Instructions

### 1. Create virtual environment
```bash
python -m venv psl_env
psl_env\Scripts\activate

## Current Architecture

The project follows a modular source-code structure:

- `src/config/` → paths, settings, constants
- `src/data/` → ingestion, validation, loading
- `src/features/` → feature engineering logic
- `src/models/` → model training and inference
- `src/pipelines/` → runnable pipelines
- `src/utils/` → logging, exceptions, helpers

This structure is designed to support a professional ML system rather than a notebook-only workflow.
## Raw Data Source

The project uses raw cricket match data from Cricsheet.

Current raw data setup:
- Source: https://cricsheet.org/
- Competition focus: PSL
- Raw files stored in: `data/raw/cricsheet_psl/matches/`
- Metadata stored in: `data/raw/cricsheet_psl/download_metadata.json`
- File inventory stored in: `data/raw/cricsheet_psl/dataset_inventory.csv`

Raw data is kept untouched and will be parsed into structured datasets in later steps.

## Player Enrichment Layer

The project uses a professional player metadata strategy instead of relying on fragile scraping.

Current player data design includes:

1. `player_master.csv`  
   A registry of unique players observed in the dataset.

2. `player_manual_attributes_template.csv`  
   A curated template for attributes such as:
   - batting hand
   - bowling style
   - player role
   - country
   - overseas status

3. Future derived player stats  
   To be computed directly from parsed ball-by-ball Cricsheet data.

This design is more stable, maintainable, and production-friendly than using uncontrolled scraping as a core dependency.
## Parsed Ball-by-Ball Dataset

Raw Cricsheet YAML files are parsed into a structured delivery-level dataset.

Current parsed output:
- File: `data/interim/ball_by_ball/psl_ball_by_ball.csv`

Key delivery-level columns include:
- match_id
- innings_number
- batting_team
- over
- ball
- batter
- bowler
- non_striker
- runs_batter
- runs_extras
- runs_total
- wicket
- wicket_type
- player_out
- venue
- match_date

This dataset forms the core analytical base for:
- batsman weakness detection
- player workload analysis
- matchup analysis
- later feature engineering