# Line/Length Proxy Strategy

## Problem
Cricsheet ball-by-ball data does not typically provide explicit ball line and length coordinates.

## Why this matters
A true bowling line/length heatmap requires:
- tracking coordinates
- manually tagged delivery location data
- Hawkeye-style spatial data
- or computer vision-derived ball trajectory/location data

## Professional decision
We do NOT fabricate fake line/length labels.

Instead, for the current project stage, we build proxy-based weakness context heatmaps using variables that are actually available.

## Current proxy dimensions
- innings phase (powerplay, middle, death)
- wicket type
- bowler identity
- batting player
- match context
- scoring patterns
- later: bowler style / role if enriched

## Current heatmap types
1. Batter dismissal count by phase × wicket type
2. Batter dismissal count by bowler × wicket type
3. Batter dismissal count by phase × bowler
4. Batter run output by phase × bowler (later)

## Future extension
True line/length analysis can be added later using:
- manually tagged datasets
- video analysis
- computer vision ball tracking
- external tracking sources if available

## Why this is a good professional approach
- honest
- reproducible
- scientifically defensible
- extensible
- recruiter-friendly because it shows correct data reasoning