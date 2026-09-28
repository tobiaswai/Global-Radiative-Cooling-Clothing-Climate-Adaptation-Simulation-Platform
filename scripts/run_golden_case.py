"""Run the Dubai two-hour golden case offline and export CSV + metadata.

Usage (from backend/):
    python scripts/run_golden_case.py tests/fixtures/dubai_2h out/
"""

import asyncio
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.schemas.simulation import WeatherSimulationRequest  # noqa: E402
from app.services import weather as weather_service  # noqa: E402
from app.services.reproducibility import (  # noqa: E402
    summarize_result_for_regression,
)
from app.services.result_export import export_result_csv  # noqa: E402
from app.services.weather_simulation import (  # noqa: E402
    execute_weather_simulation,
)


def git_commit() -> str | None:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], text=True
        ).strip()
    except Exception:  # noqa: BLE001
        return None


async def main(fixture_dir: Path, out_dir: Path) -> None:
    payload = json.loads(
        (fixture_dir / "open_meteo_payload.json").read_text(encoding="utf-8")
    )

    async def offline_request(params):
        return payload, True

    weather_service.request_open_meteo = offline_request  # type: ignore[assignment]

    request = WeatherSimulationRequest.model_validate(
        json.loads((fixture_dir / "request.json").read_text(encoding="utf-8"))
    )

    result = await execute_weather_simulation(request)

    out_dir.mkdir(parents=True, exist_ok=True)

    (out_dir / "results.csv").write_text(
        export_result_csv(result), encoding="utf-8-sig"
    )

    regression = summarize_result_for_regression(result)

    metadata = {
        "run_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": git_commit(),
        "model_version": result.model_version,
        "request": request.model_dump(mode="json"),
        "weather_payload_sha256": regression["weather"]["payload_sha256"],
        "weather_quality": regression["weather"]["quality"],
        "summary": regression["summary"],
    }

    (out_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(json.dumps(metadata["summary"], indent=2))


if __name__ == "__main__":
    asyncio.run(main(Path(sys.argv[1]), Path(sys.argv[2])))