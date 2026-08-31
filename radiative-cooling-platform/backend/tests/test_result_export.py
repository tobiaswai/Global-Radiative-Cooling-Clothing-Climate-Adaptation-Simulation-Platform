import csv
import io
import json
from types import SimpleNamespace

import pytest

from app.services.result_export import (
    export_result_csv,
    export_result_json,
)


EXPECTED_HEADERS = [
    "minute",
    "control_core_temperature_c",
    "control_skin_temperature_c",
    "rc_core_temperature_c",
    "rc_skin_temperature_c",
    "control_convection_w_m2",
    "rc_convection_w_m2",
    "control_longwave_w_m2",
    "rc_longwave_w_m2",
    "control_evaporation_w_m2",
    "rc_evaporation_w_m2",
    "control_absorbed_solar_w_m2",
    "rc_absorbed_solar_w_m2",
]


def make_point(
    *,
    minute: float,
    core_temperature_c: float,
    skin_temperature_c: float,
    convection_w_m2: float,
    longwave_radiation_w_m2: float,
    evaporation_w_m2: float,
    absorbed_solar_w_m2: float,
):
    """Minimal time-series test objects required to create a CSV exporter."""
    return SimpleNamespace(
        minute=minute,
        core_temperature_c=core_temperature_c,
        skin_temperature_c=skin_temperature_c,
        convection_w_m2=convection_w_m2,
        longwave_radiation_w_m2=longwave_radiation_w_m2,
        evaporation_w_m2=evaporation_w_m2,
        absorbed_solar_w_m2=absorbed_solar_w_m2,
    )


def make_export_result(
    *,
    control_points=None,
    rc_points=None,
):
    """Create the minimal result object needed for CSV export."""
    if control_points is None:
        control_points = [
            make_point(
                minute=0,
                core_temperature_c=36.8,
                skin_temperature_c=33.7,
                convection_w_m2=12.5,
                longwave_radiation_w_m2=8.1,
                evaporation_w_m2=20.0,
                absorbed_solar_w_m2=100.0,
            )
        ]

    if rc_points is None:
        rc_points = [
            make_point(
                minute=0,
                core_temperature_c=36.7,
                skin_temperature_c=32.9,
                convection_w_m2=13.5,
                longwave_radiation_w_m2=10.2,
                evaporation_w_m2=18.0,
                absorbed_solar_w_m2=25.0,
            )
        ]

    return SimpleNamespace(
        control=SimpleNamespace(time_series=control_points),
        radiative_cooling=SimpleNamespace(time_series=rc_points),
    )


@pytest.mark.unit
def test_result_csv_contains_expected_headers():
    result = make_export_result()

    csv_text = export_result_csv(result)
    rows = list(csv.reader(io.StringIO(csv_text)))

    assert rows[0] == EXPECTED_HEADERS


@pytest.mark.unit
def test_result_csv_contains_control_and_rc_values():
    result = make_export_result()

    csv_text = export_result_csv(result)
    rows = list(csv.reader(io.StringIO(csv_text)))

    assert len(rows) == 2

    data_row = rows[1]

    assert float(data_row[0]) == pytest.approx(0.0)

    assert float(data_row[1]) == pytest.approx(36.8)
    assert float(data_row[2]) == pytest.approx(33.7)

    assert float(data_row[3]) == pytest.approx(36.7)
    assert float(data_row[4]) == pytest.approx(32.9)

    assert float(data_row[5]) == pytest.approx(12.5)
    assert float(data_row[6]) == pytest.approx(13.5)

    assert float(data_row[7]) == pytest.approx(8.1)
    assert float(data_row[8]) == pytest.approx(10.2)

    assert float(data_row[9]) == pytest.approx(20.0)
    assert float(data_row[10]) == pytest.approx(18.0)

    assert float(data_row[11]) == pytest.approx(100.0)
    assert float(data_row[12]) == pytest.approx(25.0)


@pytest.mark.unit
def test_result_csv_with_empty_time_series_contains_only_headers():
    result = make_export_result(
        control_points=[],
        rc_points=[],
    )

    csv_text = export_result_csv(result)
    rows = list(csv.reader(io.StringIO(csv_text)))

    assert rows == [EXPECTED_HEADERS]


@pytest.mark.unit
def test_result_csv_rejects_different_time_series_lengths():
    result = make_export_result(
        control_points=[
            make_point(
                minute=0,
                core_temperature_c=36.8,
                skin_temperature_c=33.7,
                convection_w_m2=12.5,
                longwave_radiation_w_m2=8.1,
                evaporation_w_m2=20.0,
                absorbed_solar_w_m2=100.0,
            )
        ],
        rc_points=[],
    )

    with pytest.raises(ValueError):
        export_result_csv(result)


@pytest.mark.unit
def test_result_json_serializes_model_dump_as_unicode():
    payload = {
        "city": "dubai",
        "duration_minutes": 120,
        "warning": "warning",
    }

    result = SimpleNamespace(
        model_dump=lambda *, mode: payload,
    )

    json_text = export_result_json(result)
    decoded = json.loads(json_text)

    assert decoded == payload
    assert "dubai" in json_text
    assert "warning" in json_text
    assert "\\u" not in json_text
    assert "\n" in json_text