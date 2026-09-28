"""Download one Open-Meteo payload and freeze it as a test fixture.

Usage (from backend/):
    python scripts/capture_weather_fixture.py tests/fixtures/dubai_2h
"""

import asyncio
import hashlib
import json
import sys
from datetime import datetime, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.core.cities import get_city  # noqa: E402
from app.schemas.simulation import WeatherSimulationRequest  # noqa: E402
from app.services.weather import (  # noqa: E402
    build_request_params,
    download_open_meteo_payload,
    normalize_local_datetime,
)


async def main(fixture_dir: Path) -> None:
    request = WeatherSimulationRequest.model_validate(
        json.loads((fixture_dir / "request.json").read_text(encoding="utf-8"))
    )

    city = get_city(request.city_id)

    start = normalize_local_datetime(request.start_time_local, city.timezone)
    end = start + timedelta(minutes=request.duration_minutes)

    params = build_request_params(
        city=city,
        start_date=(start - timedelta(hours=1)).date(),
        end_date=(end + timedelta(hours=1)).date(),
    )

    payload = await download_open_meteo_payload(params)

    raw = json.dumps(payload, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
    (fixture_dir / "open_meteo_payload.json").write_text(raw, encoding="utf-8")
    (fixture_dir / "open_meteo_payload.sha256").write_text(
        hashlib.sha256(raw.encode("utf-8")).hexdigest() + "\n", encoding="utf-8"
    )
    (fixture_dir / "request_params.json").write_text(
        json.dumps(params, indent=2, sort_keys=True), encoding="utf-8"
    )

    print(f"captured {len(payload['hourly']['time'])} hourly points into {fixture_dir}")
    print(f"captured at {datetime.utcnow().isoformat()}Z")


if __name__ == "__main__":
    asyncio.run(main(Path(sys.argv[1])))