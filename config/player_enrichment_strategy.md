# Player Enrichment Strategy

## Objective
Create a robust and professional player-level metadata layer for the PSL AI Platform without relying on fragile web scraping.

## Approach
We use a 3-layer player data strategy:

### 1. Player Master
A unique list of players observed in the dataset.

Fields:
- player_name
- source
- first_seen_match_id
- last_seen_match_id
- notes

### 2. Manual Attributes
Curated or manually collected player attributes not directly available in ball-by-ball data.

Fields:
- batting_hand
- bowling_style
- player_role
- country
- is_overseas
- date_of_birth
- notes

### 3. Derived Stats
Stats computed directly from parsed Cricsheet ball-by-ball data.

Examples:
- matches_played
- innings_batted
- runs_scored
- wickets_taken
- balls_faced
- overs_bowled

## Why this approach?
- More stable than scraping
- Reproducible
- Easier to maintain
- Better for professional ML/data engineering workflow
- Keeps external dependencies low

## External enrichment
Optional external sources may be used later, but only in a controlled, documented, and non-fragile way.