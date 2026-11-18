from datetime import date

import pytest

from app.core.cities import get_city
from app.services.weather import build_request_params, parse_weather_points

STAGE10_HOURLY = (
    "temperature_2m,relative_humidity_2m,wind_speed_10m,shortwave_radiation,"
    "direct_radiation,diffuse_radiation,direct_normal_irradiance"
)


@pytest.mark.unit
def test_default_request_is_byte_identical_to_stage10():
    params = build_request_params(get_city("dubai"), date(2023, 7, 1), date(2023, 7, 2))
    assert params["hourly"] == STAGE10_HOURLY  # cache key and golden payload hash depend on it


@pytest.mark.unit
def test_extra_variables_are_appended_sorted():
    params = build_request_params(get_city("dubai"), date(2023, 7, 1), date(2023, 7, 2),
                                  extra_variables=("soil_temperature_0_to_7cm", "cloud_cover"))
    assert params["hourly"].endswith(",cloud_cover,soil_temperature_0_to_7cm")
    with pytest.raises(ValueError):
        build_request_params(get_city("dubai"), date(2023, 7, 1), date(2023, 7, 2),
                             extra_variables=("snowfall",))


@pytest.mark.unit
def test_parse_optional_variables_with_nulls():
    base = {name: [1.0, 2.0] for name in STAGE10_HOURLY.split(",")}
    payload = {
        "utc_offset_seconds": 14400,
        "hourly": {"time": ["2023-07-01T00:00", "2023-07-01T01:00"], **base,
                   "cloud_cover": [10.0, None], "soil_temperature_0_to_7cm": [35.0, 34.5]},
    }
    points = parse_weather_points(payload, get_city("dubai"))
    assert points[0].cloud_cover_percent == 10.0
    assert points[1].cloud_cover_percent is None
    assert points[1].soil_temperature_c == 34.5