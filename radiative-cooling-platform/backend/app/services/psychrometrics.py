"""Psychrometric helpers shared by the body model and the environment model."""

from __future__ import annotations

from math import exp

from app.services.model_parameters import get_parameter_value as _param


MAGNUS_A = _param("magnus_a")
MAGNUS_B = _param("magnus_b")
MAGNUS_C = _param("magnus_c")


def saturation_vapor_pressure_kpa(temperature_c: float) -> float:
    return MAGNUS_A * exp(MAGNUS_B * temperature_c / (temperature_c + MAGNUS_C))


def vapor_pressure_kpa(temperature_c: float, relative_humidity_percent: float) -> float:
    return relative_humidity_percent / 100.0 * saturation_vapor_pressure_kpa(temperature_c)
