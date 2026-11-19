"""Uniform vs two-zone RC garment on one hot day (Stage 12 L1).

Usage (from backend/): python scripts/inspect_zoned_garment.py dubai 2023-07-15
"""

from __future__ import annotations

import argparse
import asyncio
import csv
from datetime import datetime
from pathlib import Path

from app.core.cities import get_city
from app.schemas.environment import EnvironmentAssumptions
from app.schemas.simulation import MaterialInput, PersonInput
from app.services.environment_model import required_weather_variables
from app.services.exposure_statistics import time_weighted_mean
from app.services.two_node import simulate_material_with_weather
from app.services.weather import get_historical_weather

OUT = Path("docs/acceptance/stage-12-defaults-zones")
PERSON = PersonInput(met=2.6)
BASE = dict(name="RC", clothing_insulation_clo=0.4, solar_reflectance=0.92, infrared_emissivity=0.95)


def mean(result, attribute: str) -> float:
    points = [(p.minute, getattr(p, attribute)) for p in result.time_series]
    return round(time_weighted_mean([m for m, _ in points], [v for _, v in points]), 3)


async def main(city_id: str, day: str) -> None:
    city = get_city(city_id)
    rows = []
    for s in (0.0, 0.25, 0.5, 0.75, 1.0):
        assumptions = EnvironmentAssumptions(zone_view_separation=s)
        weather = await get_historical_weather(
            city, datetime.fromisoformat(f"{day}T12:00"), 120,
            extra_variables=required_weather_variables(assumptions),
        )
        for label, ground in (("uniform", None), ("eps_g 0.5", 0.5), ("eps_g 0.1", 0.1)):
            material = MaterialInput(**BASE, infrared_emissivity_ground_facing=ground)
            result = simulate_material_with_weather(120, 5, weather, PERSON, material, assumptions)
            rows.append({
                "separation": s, "garment": label,
                "mean_skin_c": mean(result, "skin_temperature_c"),
                "final_core_c": result.final_core_temperature_c,
                "mean_clothing_surface_c": mean(result, "clothing_surface_temperature_c"),
                "mean_surround_c": mean(result, "surround_temperature_c"),
                "mean_sky_c": mean(result, "sky_temperature_c"),
            })
            print(rows[-1])

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"l1-{city_id}-{day}.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("city")
    parser.add_argument("date")
    args = parser.parse_args()
    asyncio.run(main(args.city, args.date))