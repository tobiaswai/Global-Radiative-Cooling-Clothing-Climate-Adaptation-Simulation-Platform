"""Golden regression case: Dubai, 2023-07-15 12:00 local, two hours.

Offline: the Open-Meteo payload is a frozen fixture. First run (or
UPDATE_GOLDEN=1) writes expected_results.json; subsequent runs compare.
"""

import json
import os
from pathlib import Path

import pytest

from app.schemas.simulation import WeatherSimulationRequest
from app.services.reproducibility import (
    compare_regression_payloads,
    summarize_result_for_regression,
)
from app.services.weather_simulation import execute_weather_simulation


FIXTURE_DIR = Path(__file__).parent / "fixtures" / "dubai_2h"
PAYLOAD_PATH = FIXTURE_DIR / "open_meteo_payload.json"
REQUEST_PATH = FIXTURE_DIR / "request.json"
EXPECTED_PATH = FIXTURE_DIR / "expected_results.json"


@pytest.mark.integration
@pytest.mark.asyncio
async def test_dubai_two_hour_golden_case(monkeypatch):
    if not PAYLOAD_PATH.exists():
        pytest.skip(
            "Fixture missing. Run: python scripts/capture_weather_fixture.py "
            "tests/fixtures/dubai_2h"
        )

    payload = json.loads(PAYLOAD_PATH.read_text(encoding="utf-8"))

    async def fake_request_open_meteo(params):
        return payload, True

    monkeypatch.setattr(
        "app.services.weather.request_open_meteo",
        fake_request_open_meteo,
    )

    request = WeatherSimulationRequest.model_validate(
        json.loads(REQUEST_PATH.read_text(encoding="utf-8"))
    )

    result = await execute_weather_simulation(request)
    actual = summarize_result_for_regression(result)

    if os.environ.get("UPDATE_GOLDEN") == "1" or not EXPECTED_PATH.exists():
        EXPECTED_PATH.write_text(
            json.dumps(actual, indent=2, sort_keys=True), encoding="utf-8"
        )
        pytest.fail(
            f"Wrote new golden file {EXPECTED_PATH}. Review, commit, and re-run."
        )

    expected = json.loads(EXPECTED_PATH.read_text(encoding="utf-8"))

    differences = compare_regression_payloads(expected, actual)

    assert not differences, "\n".join(differences)

    # Sanity: the fixture must be clean data, otherwise the case is not golden.
    quality = actual["weather"]["quality"]
    assert quality["gaps"] == []
    assert quality["duplicates_removed"] == 0