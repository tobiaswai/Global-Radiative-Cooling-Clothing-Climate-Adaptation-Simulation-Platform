"""Helpers for regression ("golden") cases."""

from __future__ import annotations

from typing import Any

from app.schemas.simulation import WeatherSimulationResponse


def summarize_result_for_regression(
    result: WeatherSimulationResponse,
) -> dict[str, Any]:
    """Reduce a result to the numeric fields we want to keep stable."""
    return {
        "model_version": result.model_version,
        "city": result.city,
        "duration_minutes": result.duration_minutes,
        "summary": result.summary.model_dump(),
        "weather": {
            "point_count": len(result.weather.points),
            "payload_sha256": result.weather.source.payload_sha256,
            "quality": (
                result.weather.source.quality.model_dump(mode="json")
                if result.weather.source.quality
                else None
            ),
        },
        "control": [
            {
                "minute": p.minute,
                "core_temperature_c": p.core_temperature_c,
                "skin_temperature_c": p.skin_temperature_c,
            }
            for p in result.control.time_series
        ],
        "radiative_cooling": [
            {
                "minute": p.minute,
                "core_temperature_c": p.core_temperature_c,
                "skin_temperature_c": p.skin_temperature_c,
            }
            for p in result.radiative_cooling.time_series
        ],
    }


def compare_regression_payloads(
    expected: dict[str, Any],
    actual: dict[str, Any],
    *,
    temperature_atol: float = 1e-6,
) -> list[str]:
    """Return a list of human-readable differences (empty means identical)."""
    differences: list[str] = []

    for key in ("model_version", "city", "duration_minutes"):
        if expected.get(key) != actual.get(key):
            differences.append(f"{key}: {expected.get(key)!r} != {actual.get(key)!r}")

    for key, value in expected["summary"].items():
        if abs(value - actual["summary"][key]) > temperature_atol:
            differences.append(f"summary.{key}: {value} != {actual['summary'][key]}")

    for scenario in ("control", "radiative_cooling"):
        expected_points = expected[scenario]
        actual_points = actual[scenario]

        if len(expected_points) != len(actual_points):
            differences.append(
                f"{scenario}: {len(expected_points)} vs {len(actual_points)} points"
            )
            continue

        for index, (e, a) in enumerate(zip(expected_points, actual_points)):
            for field in ("minute", "core_temperature_c", "skin_temperature_c"):
                if abs(e[field] - a[field]) > temperature_atol:
                    differences.append(
                        f"{scenario}[{index}].{field}: {e[field]} != {a[field]}"
                    )

    if expected["weather"]["payload_sha256"] != actual["weather"]["payload_sha256"]:
        differences.append("weather payload sha256 differs")

    return differences