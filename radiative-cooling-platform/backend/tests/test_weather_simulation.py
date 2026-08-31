from datetime import datetime
from types import SimpleNamespace

import pytest

from app.schemas.simulation import (
    WeatherSimulationRequest,
)
from app.services import weather_simulation


class FakeWeatherSimulationResponse(
    SimpleNamespace
):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


@pytest.mark.unit
@pytest.mark.asyncio
async def test_execute_weather_simulation(
    monkeypatch,
    person,
    control_material,
    rc_material,
):
    request = WeatherSimulationRequest(
        city_id="dubai",
        start_time_local=datetime(
            2025,
            7,
            15,
            10,
            0,
        ),
        duration_minutes=120,
        output_interval_minutes=1,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
    )

    city = SimpleNamespace(
        id="dubai",
        name="Dubai",
    )
    weather = object()

    control_result = SimpleNamespace(
        time_series=[
            SimpleNamespace(
                skin_temperature_c=35.0,
            ),
            SimpleNamespace(
                skin_temperature_c=36.0,
            ),
        ],
        final_skin_temperature_c=36.0,
        final_core_temperature_c=38.0,
    )

    rc_result = SimpleNamespace(
        time_series=[
            SimpleNamespace(
                skin_temperature_c=33.0,
            ),
            SimpleNamespace(
                skin_temperature_c=34.0,
            ),
        ],
        final_skin_temperature_c=34.0,
        final_core_temperature_c=37.5,
    )

    get_city_calls = []
    weather_calls = []
    simulation_calls = []

    def fake_get_city(city_id):
        get_city_calls.append(city_id)
        return city

    async def fake_get_historical_weather(
        *,
        city,
        start_time_local,
        duration_minutes,
    ):
        weather_calls.append(
            {
                "city": city,
                "start_time_local": (
                    start_time_local
                ),
                "duration_minutes": (
                    duration_minutes
                ),
            }
        )
        return weather

    def fake_simulate_material_with_weather(
        *,
        duration_minutes,
        output_interval_minutes,
        weather,
        person,
        material,
    ):
        simulation_calls.append(material.name)

        if material.name == control_material.name:
            return control_result

        return rc_result

    monkeypatch.setattr(
        weather_simulation,
        "get_city",
        fake_get_city,
    )
    monkeypatch.setattr(
        weather_simulation,
        "get_historical_weather",
        fake_get_historical_weather,
    )
    monkeypatch.setattr(
        weather_simulation,
        "simulate_material_with_weather",
        fake_simulate_material_with_weather,
    )
    monkeypatch.setattr(
        weather_simulation,
        "WeatherSimulationResponse",
        FakeWeatherSimulationResponse,
    )

    progress_events = []

    result = await (
        weather_simulation
        .execute_weather_simulation(
            request,
            progress_callback=lambda progress, stage: (
                progress_events.append(
                    (progress, stage)
                )
            ),
        )
    )

    assert get_city_calls == ["dubai"]

    assert len(weather_calls) == 1
    assert (
        weather_calls[0]["duration_minutes"]
        == 120
    )

    assert simulation_calls == [
        control_material.name,
        rc_material.name,
    ]

    assert progress_events == [
        (10, "downloading_weather"),
        (
            30,
            "running_control_simulation",
        ),
        (
            65,
            "running_radiative_cooling_simulation",
        ),
        (90, "generating_summary"),
    ]

    assert result.city == "Dubai"
    assert result.control is control_result
    assert (
        result.radiative_cooling
        is rc_result
    )

    assert (
        result.summary
        .final_skin_temperature_improvement_c
        == pytest.approx(2.0)
    )
    assert (
        result.summary
        .final_core_temperature_improvement_c
        == pytest.approx(0.5)
    )
    assert (
        result.summary
        .average_skin_temperature_improvement_c
        == pytest.approx(2.0)
    )


@pytest.mark.unit
@pytest.mark.asyncio
async def test_execute_weather_simulation_without_callback(
    monkeypatch,
    person,
    control_material,
    rc_material,
):
    request = WeatherSimulationRequest(
        city_id="dubai",
        start_time_local=datetime(
            2025,
            7,
            15,
            10,
            0,
        ),
        duration_minutes=1,
        output_interval_minutes=1,
        person=person,
        control_material=control_material,
        rc_material=rc_material,
    )

    city = SimpleNamespace(
        id="dubai",
        name="Dubai",
    )
    weather = object()

    scenario = SimpleNamespace(
        time_series=[
            SimpleNamespace(
                skin_temperature_c=34.0,
            )
        ],
        final_skin_temperature_c=34.0,
        final_core_temperature_c=37.0,
    )

    monkeypatch.setattr(
        weather_simulation,
        "get_city",
        lambda city_id: city,
    )

    async def fake_weather(**kwargs):
        return weather

    monkeypatch.setattr(
        weather_simulation,
        "get_historical_weather",
        fake_weather,
    )
    monkeypatch.setattr(
        weather_simulation,
        "simulate_material_with_weather",
        lambda **kwargs: scenario,
    )
    monkeypatch.setattr(
        weather_simulation,
        "WeatherSimulationResponse",
        FakeWeatherSimulationResponse,
    )

    result = await (
        weather_simulation
        .execute_weather_simulation(
            request,
            progress_callback=None,
        )
    )

    assert result.city == "Dubai"
    assert (
        result.summary
        .final_skin_temperature_improvement_c
        == 0
    )