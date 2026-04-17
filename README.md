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

## Cleaned Ball-by-Ball Dataset

The parsed ball-by-ball dataset is cleaned and standardized into a processed analysis-ready dataset.

Processed output:
- `data/processed/ball_by_ball/psl_ball_by_ball_clean.csv`

Cleaning includes:
- text standardization
- numeric type fixing
- datetime conversion
- duplicate removal
- missing value handling
- derived columns such as:
  - `phase`
  - `ball_id`

This cleaned dataset is the main input for EDA, feature engineering, and model building.
## Analytical Data Model

The project now follows a fact + dimension analytical design.

### Fact Table
- `data/processed/ball_by_ball/psl_ball_by_ball_clean.csv`

### Player Dimension Tables
- `data/interim/player_data/player_master.csv`
- `data/processed/player_data/player_manual_attributes_clean.csv`
- `data/processed/player_data/player_derived_stats.csv`
- `data/processed/player_data/player_profile_master.csv`

This design is more stable and professional than creating a single giant merged table too early.
It supports:
- player profiling
- matchup analysis
- feature engineering
- model development

## Basic EDA Layer

The project includes a basic exploratory data analysis layer for both:
- cleaned ball-by-ball data
- player profile master table

Generated outputs include:
- JSON summary reports
- missing value plots
- phase distribution plots
- runs distribution plots
- player runs/wickets distributions
- exported summary CSV tables

EDA outputs are stored in:
- `reports/eda/`

## Weakness Analysis EDA — Dismissal Patterns

The first domain-specific weakness analysis step focuses on batsman dismissal patterns.

Current outputs include:
- top dismissed batters
- player-specific dismissal type breakdowns
- selected batter comparison charts
- dismissal summary CSV exports

Output folder:
- `reports/eda/weakness/`

This analysis helps identify early signals for:
- technical batting weaknesses
- pressure-related dismissal patterns
- matchup-specific vulnerability exploration

## Weakness Heatmap Foundation

Because Cricsheet ball-by-ball data does not directly contain physical bowling line and length coordinates, the project uses an honest proxy-based weakness heatmap strategy at this stage.

Current proxy heatmaps include:
- phase × wicket type
- bowler × wicket type
- phase × bowler

Outputs are stored in:
- `reports/eda/weakness/heatmaps/`

This is a professional and defensible alternative until true spatial tracking or computer vision-based delivery location data is added in later project phases.

## Weakness Analysis EDA — Phase-wise Batsman Performance

The project includes phase-wise batting analysis across:
- powerplay
- middle overs
- death overs

Current outputs include:
- phase-level batting summary tables
- strike rate by phase charts
- dismissals by phase charts
- runs by phase for top batters
- phase weakness signal exports

Output folder:
- `reports/eda/weakness/phase_analysis/`

This analysis supports early detection of:
- phase-specific weakness
- pressure sensitivity
- scoring slowdowns
- dismissal concentration by innings phase

## Weakness Analysis EDA — Batsman vs Bowler Type Matchups

The project includes tactical matchup analysis between batsmen and simplified bowler types such as:
- Left-arm pace
- Right-arm pace
- Off-spin
- Leg-spin
- Left-arm orthodox
- Left-arm wrist-spin

Current outputs include:
- batter vs bowler type summary table
- strike rate by bowler type plots
- dismissal rate by bowler type plots
- weakness signal exports

Output folder:
- `reports/eda/weakness/bowler_type_matchups/`

This analysis helps identify tactical vulnerabilities against specific bowling categories.

## Injury Module EDA — Bowler Workload Trends

The project includes a workload trend analysis layer for bowlers as the first analytical foundation for injury risk modeling.

Current outputs include:
- match-level bowler workload table
- top workload bowlers plot
- selected bowler workload trend plots
- workload summary statistics export
- interpretation notes

Output folder:
- `reports/eda/injury/workload_trends/`

This analysis supports future injury risk features such as:
- rolling workload
- fatigue index
- recent match density
- recovery window analysis