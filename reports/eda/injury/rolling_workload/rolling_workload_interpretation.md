# Rolling Workload Interpretation Notes

## Objective
Capture recent workload and recovery patterns for bowlers as a stronger proxy for injury risk.

## Features included
- balls_last_7_days
- balls_last_14_days
- matches_last_7_days
- matches_last_14_days
- days_since_last_match
- back_to_back_match
- short_recovery_flag
- fatigue_signal_score

## Why these are useful
Injury risk is usually more linked to recent accumulated load and recovery insufficiency than to a single isolated match workload.

## Current fatigue signal
The current fatigue signal is heuristic and designed as an engineering proxy, not a medical diagnosis.

It increases with:
- high recent overs
- high recent match density
- back-to-back matches
- short recovery windows

## Future improvement
These features can later be:
- validated against injury proxies
- used in ML models
- refined with domain expert feedback