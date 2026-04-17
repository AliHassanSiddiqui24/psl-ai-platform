from pathlib import Path
from typing import Any, Dict, List

import pandas as pd
import yaml

from src.utils.logger import get_logger

logger = get_logger(__name__)


def load_yaml_file(file_path: Path) -> Dict[str, Any]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data


def extract_match_info(data: Dict[str, Any]) -> Dict[str, Any]:
    info = data.get("info", {})

    dates = info.get("dates", [])
    match_date = dates[0] if dates else None

    teams = info.get("teams", [None, None])
    team1 = teams[0] if len(teams) > 0 else None
    team2 = teams[1] if len(teams) > 1 else None

    toss = info.get("toss", {})
    toss_winner = toss.get("winner")
    toss_decision = toss.get("decision")

    return {
        "match_date": match_date,
        "city": info.get("city"),
        "venue": info.get("venue"),
        "team1": team1,
        "team2": team2,
        "toss_winner": toss_winner,
        "toss_decision": toss_decision,
    }


def parse_deliveries(
    innings_data: List[Dict[str, Any]],
    match_id: str,
    match_info: Dict[str, Any],
) -> List[Dict[str, Any]]:
    rows = []

    for innings_index, innings_entry in enumerate(innings_data, start=1):
        innings_name = list(innings_entry.keys())[0]
        innings_content = innings_entry[innings_name]

        batting_team = innings_content.get("team")
        deliveries = innings_content.get("deliveries", [])

        for delivery in deliveries:
            delivery_key = list(delivery.keys())[0]
            delivery_data = delivery[delivery_key]

            over_ball = str(delivery_key).split(".")
            over = int(over_ball[0]) if len(over_ball) > 0 else None
            ball = int(over_ball[1]) if len(over_ball) > 1 else None

            batter = delivery_data.get("batter")
            bowler = delivery_data.get("bowler")
            non_striker = delivery_data.get("non_striker")

            runs = delivery_data.get("runs", {})
            runs_batter = runs.get("batter", 0)
            runs_extras = runs.get("extras", 0)
            runs_total = runs.get("total", 0)

            extras = delivery_data.get("extras", {})
            extras_type = ",".join(extras.keys()) if extras else None

            wickets = delivery_data.get("wickets", [])
            wicket = 1 if wickets else 0

            wicket_type = None
            player_out = None
            fielders_involved = None

            if wickets:
                first_wicket = wickets[0]
                wicket_type = first_wicket.get("kind")
                player_out = first_wicket.get("player_out")

                fielders = first_wicket.get("fielders", [])
                if fielders:
                    fielder_names = []
                    for fielder in fielders:
                        if isinstance(fielder, dict):
                            name = fielder.get("name")
                            if name:
                                fielder_names.append(name)
                        elif isinstance(fielder, str):
                            fielder_names.append(fielder)
                    fielders_involved = ", ".join(fielder_names) if fielder_names else None

            row = {
                "match_id": match_id,
                "innings_number": innings_index,
                "batting_team": batting_team,
                "over": over,
                "ball": ball,
                "batter": batter,
                "bowler": bowler,
                "non_striker": non_striker,
                "runs_batter": runs_batter,
                "runs_extras": runs_extras,
                "runs_total": runs_total,
                "extras_type": extras_type,
                "wicket": wicket,
                "wicket_type": wicket_type,
                "player_out": player_out,
                "fielders_involved": fielders_involved,
                **match_info,
            }

            rows.append(row)

    return rows


def parse_match_file(file_path: Path) -> pd.DataFrame:
    logger.info("Parsing match file: %s", file_path)

    data = load_yaml_file(file_path)
    match_info = extract_match_info(data)

    innings_data = data.get("innings", [])
    match_id = file_path.stem

    rows = parse_deliveries(innings_data, match_id, match_info)
    df = pd.DataFrame(rows)

    logger.info("Parsed match %s with shape %s", match_id, df.shape)
    return df