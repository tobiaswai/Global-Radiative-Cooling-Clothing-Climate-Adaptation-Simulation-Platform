"""Constants duplicated in the frontend must equal the backend values."""

import re
from pathlib import Path

import pytest

from app.schemas.environment import EnvironmentAssumptions
from app.services.model_parameters import get_parameter_value

FRONTEND = Path(__file__).resolve().parents[2] / "frontend" / "src" / "lib"


def _read(name: str) -> str:
    path = FRONTEND / name
    if not path.exists():
        pytest.skip("frontend sources not available")
    return path.read_text(encoding="utf-8")


@pytest.mark.unit
def test_planck_constants_match_registry():
    text = _read("planck.ts")
    expected = {
        "SECOND_RADIATION_CONSTANT": get_parameter_value("second_radiation_constant"),
        "WINDOW_LOWER_UM": get_parameter_value("atmospheric_window_lower_um"),
        "WINDOW_UPPER_UM": get_parameter_value("atmospheric_window_upper_um"),
        "EMISSIVITY_REFERENCE_K": get_parameter_value("emissivity_reference_temperature"),
    }
    for name, value in expected.items():
        match = re.search(rf"export const {name} = ([0-9.]+)", text)
        assert match, name
        assert float(match.group(1)) == pytest.approx(value), name


@pytest.mark.unit
def test_environment_defaults_match_schema():
    text = _read("environment-assumptions.ts")
    pairs = dict(re.findall(r"^\s*(\w+):\s*\"?([\w.]+)\"?,?\s*$", text, flags=re.M))
    for key, value in EnvironmentAssumptions().model_dump().items():
        assert key in pairs, f"{key} missing in DEFAULT_ENVIRONMENT_ASSUMPTIONS"
        if isinstance(value, (int, float)):
            assert float(pairs[key]) == pytest.approx(value), key
        else:
            assert pairs[key] == value, key