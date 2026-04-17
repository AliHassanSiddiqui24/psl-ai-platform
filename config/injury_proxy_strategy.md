# Injury Proxy Strategy

## Problem
The project does not currently have access to true medical injury labels such as:
- confirmed injury dates
- injury type
- recovery duration
- missed matches explicitly due to injury

## Why this matters
A true supervised injury prediction model requires reliable labels.
Without valid labels, any direct "injury prediction" claim would be scientifically weak.

## Professional decision
We do NOT fabricate fake medical injury labels.

Instead, we define a defensible workload-related proxy event.

## Selected proxy concept
A row may be marked as a proxy risk event if:
1. the bowler has elevated recent workload / fatigue
2. and the bowler is absent from the next short future window (e.g. next 7 or 14 days)

## What this proxy means
This is NOT a confirmed injury.
It is better interpreted as:
- post-load absence risk
- workload-related unavailability proxy
- possible fatigue/injury/rotation risk event

## Why this is acceptable for this stage
- transparent
- reproducible
- consistent with available data
- extensible once true labels are available

## Future upgrade path
This proxy target can later be replaced or refined using:
- official injury reports
- manually curated injury labels
- external verified injury databases
- team availability data    