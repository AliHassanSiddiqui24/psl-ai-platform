# Injury Proxy Target Interpretation Notes

## Important clarification
The current target is NOT a medically confirmed injury label.

It is a proxy event intended to capture:
- workload-related unavailability risk
- possible fatigue-related absence
- short-term post-load disappearance from match appearances

## Current proxy logic
A positive proxy event is assigned when:
- fatigue signal is high
- recent workload is high
- and the bowler does not appear again within the future short window

## What this can and cannot mean
This may reflect:
- fatigue
- rotation
- injury
- rest
- tactical non-selection

It should therefore be interpreted carefully.

## Why this still matters
Even though imperfect, this proxy allows:
- supervised modeling experimentation
- feature importance analysis
- ranking and risk scoring workflows
- future upgrade to real injury labels