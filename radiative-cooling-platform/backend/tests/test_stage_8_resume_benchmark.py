"""Stage 8 acceptance: resuming from monthly checkpoints is exact and cheap.

Fully offline. ``get_historical_weather_range`` is replaced by a deterministic
synthetic provider so the only cost measured is the thermal model.

Assertions
1. The uninterrupted run fetches one weather range per month.
2. A run that crashes after month N leaves exactly N checkpoints.
3. The resumed run fetches only the missing 12 - N months and reproduces the
   uninterrupted result exactly (monthly results and every annual metric).

Set RECORD_BENCHMARK=1 to write timings to docs/acceptance/stage-8-observability/.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
from datetime import datetime, timedelta
from pathlib import Path
from time import perf_counter
from zoneinfo import ZoneInfo

import pytest

from app.core.cities import CityConfig
from app.schemas.global_batch import GlobalBatchCreate, MonthlyAdaptationResult
from app.schemas.weather import (
    WeatherPoint,
    WeatherQualityReport,
    WeatherSourceMetadata,
    WeatherTimeSeries,
)
from app.services import climate_adaptation
from app.services.climate_adaptation import analyze_city_climate_adaptation
from app.services.weather import city_to_response, normalize_local_datetime, to_utc


RECORD_PATH = (
    Path(__file__).resolve().parents[1]
    / "docs" / "acceptance" / "stage-8-observability" / "resume-benchmark.json"
)

CRASH_AFTER_MONTH = 4

ANNUAL_METRIC_KEYS = (
    "climate_adaptation_rate_percent",
    "exposure_coverage_percent",
    "annual_average_skin_improvement_c",
    "annual_average_core_improvement_c",
    "maximum_skin_improvement_c",
    "effective_cooling_hours",
    "sampled_day_count",
    "eligible_sample_count",
    "evaluated_weighted_days",
    "beneficial_weighted_days",
    "completed_month_count",
    "skin_improvement_p50_c",
    "skin_improvement_p90_c",
    "skin_improvement_p95_c",
    "core_improvement_p50_c",
    "core_improvement_p90_c",
    "core_improvement_p95_c",
    "heatwave_event_count",
    "longest_heatwave_days",
    "heatwave_events",
)


class SyntheticWeatherProvider:
    """Deterministic hourly weather with a clear diurnal cycle. Counts calls."""

    def __init__(self) -> None:
        self.calls = 0

    async def __call__(
        self,
        *,
        city: CityConfig,
        start_time_local: datetime,
        end_time_local: datetime,
        padding_hours: int = 1,
        require_window_coverage: bool = True,
    ) -> WeatherTimeSeries:
        self.calls += 1

        tz = ZoneInfo(city.timezone)
        start = normalize_local_datetime(start_time_local, city.timezone)
        end = normalize_local_datetime(end_time_local, city.timezone)

        cursor = to_utc(start - timedelta(hours=padding_hours)).replace(minute=0, second=0, microsecond=0)
        stop = to_utc(end + timedelta(hours=padding_hours + 1))

        points: list[WeatherPoint] = []
        while cursor <= stop:
            local = cursor.astimezone(tz)
            hour = local.hour + local.minute / 60.0
            day_of_year = local.timetuple().tm_yday

            seasonal = 6.0 * math.sin(2.0 * math.pi * (day_of_year - 110) / 365.0)
            diurnal = 5.0 * math.sin(2.0 * math.pi * (hour - 9.0) / 24.0)
            temperature = 31.0 + seasonal + diurnal

            daylight = 6.0 <= hour <= 18.0
            ghi = 950.0 * math.sin(math.pi * (hour - 6.0) / 12.0) if daylight else 0.0

            points.append(
                WeatherPoint(
                    timestamp=local,
                    air_temperature_c=round(temperature, 3),
                    relative_humidity_percent=40.0,
                    wind_speed_m_s=2.5,
                    ghi_w_m2=round(ghi, 2),
                    direct_radiation_w_m2=round(ghi * 0.75, 2),
                    diffuse_radiation_w_m2=round(ghi * 0.25, 2),
                    dni_w_m2=round(ghi * 0.8, 2),
                )
            )
            cursor += timedelta(hours=1)

        digest = hashlib.sha256(f"{city.id}|{start.isoformat()}|{end.isoformat()}".encode()).hexdigest()

        return WeatherTimeSeries(
            city=city_to_response(city),
            requested_start_time=start,
            requested_end_time=end,
            points=points,
            source=WeatherSourceMetadata(
                provider="synthetic",
                dataset="stage-8-benchmark",
                model="synthetic",
                latitude=city.latitude,
                longitude=city.longitude,
                elevation_m=city.elevation_m,
                timezone=city.timezone,
                downloaded_at=start,
                from_cache=True,
                attribution="synthetic",
                payload_sha256=digest,
                quality=WeatherQualityReport(expected_step_seconds=3600, point_count=len(points)),
            ),
        )


def make_request(person, control_material, rc_material) -> GlobalBatchCreate:
    return GlobalBatchCreate(
        name="Stage 8 resume benchmark",
        city_ids=["dubai"],
        year=2023,
        start_month=1,
        end_month=12,
        analysis_resolution="representative",
        sample_days_per_month=1,
        local_start_hour=12,
        duration_minutes=60,
        output_interval_minutes=10,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
    )


@pytest.mark.benchmark
@pytest.mark.asyncio
async def test_resume_recomputes_only_missing_months_and_matches_uninterrupted(
    monkeypatch, person, control_material, rc_material
):
    provider = SyntheticWeatherProvider()
    monkeypatch.setattr(climate_adaptation, "get_historical_weather_range", provider)

    request = make_request(person, control_material, rc_material)

    # --- 1. uninterrupted reference run -------------------------------------
    started = perf_counter()
    full = await analyze_city_climate_adaptation(city_id="dubai", request=request)
    full_seconds = perf_counter() - started

    assert provider.calls == 12
    assert full["completed_month_count"] == 12

    # --- 2. crash after CRASH_AFTER_MONTH -----------------------------------
    saved: list[MonthlyAdaptationResult] = []

    def checkpoint_then_crash(monthly, completed_month, _completed_sample_count):
        saved[:] = [m.model_copy(deep=True) for m in monthly]
        if completed_month == CRASH_AFTER_MONTH:
            raise RuntimeError("simulated worker crash")

    provider.calls = 0
    with pytest.raises(RuntimeError, match="simulated worker crash"):
        await analyze_city_climate_adaptation(
            city_id="dubai", request=request, checkpoint_callback=checkpoint_then_crash
        )

    assert provider.calls == CRASH_AFTER_MONTH
    assert [m.month for m in saved] == list(range(1, CRASH_AFTER_MONTH + 1))

    # --- 3. resume from the saved checkpoints -------------------------------
    provider.calls = 0
    stages: list[str] = []
    started = perf_counter()
    resumed = await analyze_city_climate_adaptation(
        city_id="dubai",
        request=request,
        initial_monthly_results=saved,
        progress_callback=lambda _progress, stage: stages.append(stage),
    )
    resumed_seconds = perf_counter() - started

    assert provider.calls == 12 - CRASH_AFTER_MONTH, "resume must not refetch checkpointed months"
    assert sum(s.startswith("restored_checkpoint_") for s in stages) == CRASH_AFTER_MONTH

    # Exactness: resumed == uninterrupted, month by month and metric by metric.
    assert resumed["monthly_results"] == full["monthly_results"]
    for key in ANNUAL_METRIC_KEYS:
        assert resumed[key] == full[key], key

    # Known Stage 7 limitation, documented: restored months carry no weather
    # payload hash because no weather was fetched for them.
    restored_hashes = resumed["data_quality"]["monthly_weather_payload_sha256"]
    assert set(restored_hashes) == {f"{m:02d}" for m in range(CRASH_AFTER_MONTH + 1, 13)}

    # Cost: the resumed run should scale with the missing months, not the year.
    expected_fraction = (12 - CRASH_AFTER_MONTH) / 12
    assert resumed_seconds < full_seconds * (expected_fraction + 0.35), (
        f"resume took {resumed_seconds:.2f}s vs full {full_seconds:.2f}s"
    )

    if os.environ.get("RECORD_BENCHMARK") == "1":
        RECORD_PATH.parent.mkdir(parents=True, exist_ok=True)
        RECORD_PATH.write_text(
            json.dumps(
                {
                    "recorded_at": datetime.now().astimezone().isoformat(),
                    "crash_after_month": CRASH_AFTER_MONTH,
                    "full_run_seconds": round(full_seconds, 3),
                    "resumed_run_seconds": round(resumed_seconds, 3),
                    "months_restored": CRASH_AFTER_MONTH,
                    "months_computed": 12 - CRASH_AFTER_MONTH,
                    "weather_fetches_full": 12,
                    "weather_fetches_resumed": 12 - CRASH_AFTER_MONTH,
                    "resumed_equals_full": True,
                },
                indent=2,
            ),
            encoding="utf-8",
        )