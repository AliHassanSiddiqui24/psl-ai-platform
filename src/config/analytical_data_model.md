# Analytical Data Model

## Fact Table
### Cleaned Ball-by-Ball Data
File:
- `data/processed/ball_by_ball/psl_ball_by_ball_clean.csv`

This is the core delivery-level fact table.

## Dimension Tables

### Player Master
File:
- `data/interim/player_data/player_master.csv`

Unique player registry extracted from the ball-by-ball data.

### Player Manual Attributes
File:
- `data/processed/player_data/player_manual_attributes_clean.csv`

Curated player metadata such as:
- batting hand
- bowling style
- role
- country
- overseas status

### Player Derived Stats
File:
- `data/processed/player_data/player_derived_stats.csv`

Computed directly from ball-by-ball data.

### Player Profile Master
File:
- `data/processed/player_data/player_profile_master.csv`

Integrated player-level analytical table.

## Design Principle
Use a fact + dimension style analytical design instead of building one giant denormalized table too early.

This is:
- more maintainable
- easier to debug
- more scalable
- closer to professional analytics workflows