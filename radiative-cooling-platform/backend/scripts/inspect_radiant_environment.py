"""Hour-by-hour sky and surroundings temperatures, legacy vs physical (Stage 11 K1).

Usage (from backend/): python scripts/inspect_radiant_environment.py dubai 2023-07-15
Writes docs/acceptance/stage-11-radiant/k1-<city>-<date>.csv and prints checks.
"""

from __future__ import annotations

import argparse
import asyncio
import csv
from datetime import datetime
from pathlib import Path

from app.core.cities import get_city
from app.schemas.environment import EnvironmentAssumptions
from app.services.environment_model import required_weather_variables
from app.services.weather import get_historical_weather
from app.services.weather_interpolation import WeatherInterpolator

LEGACY = EnvironmentAssumptions()
PHYSICAL = EnvironmentAssumptions(
    mean_radiant_temperature_method="ground_energy_balance",
    sky_temperature_method="brutsaert_cloud",
)
OUT = Path("docs/acceptance/stage-11-radiant")


async def main(city_id: str, day: str) -> None:
    city = get_city(city_id)
    weather = await get_historical_weather(
        city, datetime.fromisoformat(f"{day}T00:00"), 1380,
        extra_variables=required_weather_variables(PHYSICAL),
    )
    legacy = WeatherInterpolator.from_series(weather, assumptions=LEGACY)
    physical = WeatherInterpolator.from_series(weather, assumptions=PHYSICAL)

    rows = []
    for hour in range(0, 24):
        t = hour * 3600.0
        if t > physical.t_max:
            break
        a, b = legacy.environment_at(t), physical.environment_at(t)
        cloud = float(physical.cloud_values[(abs(physical.relative_seconds - t)).argmin()])
        rows.append({
            "hour": hour, "air_c": round(b.air_temperature_c, 2), "rh": round(b.relative_humidity_percent, 1),
            "ghi": round(b.solar_radiation_w_m2, 0), "cloud_pct": round(cloud, 0),
            "sky_legacy_c": round(a.sky_temperature_c, 2), "sky_physical_c": round(b.sky_temperature_c, 2),
            "surround_legacy_c": round(a.mean_radiant_temperature_c, 2),
            "surround_physical_c": round(b.mean_radiant_temperature_c, 2),
        })

    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"k1-{city_id}-{day}.csv"
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    def check(label: str, ok: bool) -> None:
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")

    night = [r for r in rows if r["hour"] <= 5]
    sunny = [r for r in rows if r["ghi"] >= 600]
    clear = [r for r in rows if r["cloud_pct"] <= 10]
    overcast = [r for r in rows if r["cloud_pct"] >= 90]
    check("night: |T_ground - T_air| <= 6 K",
          all(abs(r["surround_physical_c"] - r["air_c"]) <= 6 for r in night))
    check("sunny hours: T_ground > T_air", all(r["surround_physical_c"] > r["air_c"] for r in sunny))
    check("clear hours: sky depression 8-35 K",
          all(8 <= r["air_c"] - r["sky_physical_c"] <= 35 for r in clear) if clear else True)
    check("overcast hours: sky depression <= 6 K",
          all(r["air_c"] - r["sky_physical_c"] <= 6 for r in overcast) if overcast else True)
    print(f"wrote {path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("city")
    parser.add_argument("date")
    args = parser.parse_args()
    asyncio.run(main(args.city, args.date))