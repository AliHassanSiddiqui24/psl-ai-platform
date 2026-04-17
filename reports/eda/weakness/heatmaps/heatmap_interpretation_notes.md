# Weakness Heatmap Interpretation Notes

## Important clarification
These are NOT true bowling line/length heatmaps.

They are proxy-based weakness context heatmaps built from available Cricsheet data.

## Current heatmaps include
- phase × wicket type
- bowler × wicket type
- phase × bowler

## What they tell us
These heatmaps help answer questions such as:
- In which innings phase does a batter get dismissed most often?
- Which wicket types are most common for a batter?
- Which bowlers have dismissed the batter repeatedly?
- Which bowlers are more effective in certain phases?

## Why this is useful
Even without physical ball tracking data, these matrices provide:
- tactical matchup insights
- early weakness signals
- feature engineering ideas
- scouting/reporting value

## Future upgrade path
True spatial line/length heatmaps can be added later using:
- computer vision
- manual delivery tagging
- tracking data