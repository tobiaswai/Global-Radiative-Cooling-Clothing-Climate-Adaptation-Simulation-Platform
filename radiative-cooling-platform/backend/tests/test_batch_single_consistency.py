"""Stage 0: the annual pipeline and a single weather run must agree on the
same exposure window (same weather slice, same materials, same summary)."""

from datetime import datetime, timedelta

import pytest

from app.core.cities import get_city
from app.schemas.simulation import WeatherSimulationRequest
from app.services import climate_adaptation
from app.services.climate_adaptation import analyze_city_climate_adaptation
from app.services.weather import slice_weather_time_series
from app.services.weather_simulation import execute_weather_simulation_with_weather
from tests.test_stage_8_resume_benchmark import SyntheticWeatherProvider, make_request


@pytest.mark.integration
@pytest.mark.asyncio
async def test_batch_sample_matches_single_run(monkeypatch, person, control_material, rc_material):
    provider = SyntheticWeatherProvider()
    monkeypatch.setattr(climate_adaptation, "get_historical_weather_range", provider)

    request = make_request(person, control_material, rc_material).model_copy(
        update={"start_month": 7, "end_month": 7}
    )
    annual = await analyze_city_climate_adaptation(city_id="dubai", request=request)
    sample = annual["monthly_results"][0]["samples"][0]
    start = datetime.fromisoformat(sample["sample_date_local"]).replace(tzinfo=None)

    city = get_city("dubai")
    month_weather = await provider(
        city=city,
        start_time_local=datetime(2023, 7, 1),
        end_time_local=datetime(2023, 8, 1) + timedelta(
            hours=request.local_start_hour, minutes=request.duration_minutes
        ),
        padding_hours=1,
        require_window_coverage=False,
    )
    sliced = slice_weather_time_series(
        weather=month_weather, start_time_local=start,
        duration_minutes=request.duration_minutes, padding_hours=1,
    )
    single = execute_weather_simulation_with_weather(
        request=WeatherSimulationRequest(
            city_id="dubai", start_time_local=start,
            duration_minutes=request.duration_minutes,
            output_interval_minutes=request.output_interval_minutes,
            person=person, control_material=control_material, rc_material=rc_material,
            environment_assumptions=request.environment_assumptions,
        ),
        weather=sliced, city_name="Dubai",
    )

    assert sample["average_skin_improvement_c"] == pytest.approx(
        single.summary.average_skin_temperature_improvement_c, abs=1e-4
    )
    assert sample["final_skin_improvement_c"] == pytest.approx(
        single.summary.final_skin_temperature_improvement_c, abs=1e-4
    )