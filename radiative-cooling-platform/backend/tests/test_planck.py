import pytest

from app.services.planck import (
    SECOND_RADIATION_CONSTANT,
    band_fraction,
    band_power_k4,
    blackbody_fraction,
    blackbody_fraction_slope,
    broadband_emissivity,
    outside_window_emissivity,
)


@pytest.mark.unit
@pytest.mark.parametrize(
    ("lambda_t", "expected"),
    [(1000.0, 0.00032), (2898.0, 0.2501), (5000.0, 0.6337), (10000.0, 0.9142)],
)
def test_blackbody_fraction_matches_tables(lambda_t, expected):
    assert blackbody_fraction(lambda_t) == pytest.approx(expected, abs=5e-4)


@pytest.mark.unit
def test_series_are_continuous_at_the_switch():
    below = blackbody_fraction(SECOND_RADIATION_CONSTANT * (1 + 1e-9))
    above = blackbody_fraction(SECOND_RADIATION_CONSTANT * (1 - 1e-9))
    assert below == pytest.approx(above, abs=1e-9)


@pytest.mark.unit
def test_fraction_limits_and_monotonicity():
    values = [blackbody_fraction(x) for x in (100, 1000, 3000, 10000, 1e5, 1e7)]
    assert values == sorted(values)
    assert values[0] == pytest.approx(0.0, abs=1e-12)
    assert values[-1] == pytest.approx(1.0, abs=1e-9)


@pytest.mark.unit
def test_slope_matches_finite_difference():
    x, h = 4000.0, 1e-3
    numeric = (blackbody_fraction(x + h) - blackbody_fraction(x - h)) / (2 * h)
    assert blackbody_fraction_slope(x) == pytest.approx(numeric, rel=1e-6)


@pytest.mark.unit
def test_window_band_fraction_near_300_k():
    assert band_fraction(300.0) == pytest.approx(0.32, abs=0.01)


@pytest.mark.unit
def test_band_power_derivative():
    t, h = 305.0, 1e-3
    numeric = (band_power_k4(t + h)[0] - band_power_k4(t - h)[0]) / (2 * h)
    assert band_power_k4(t)[1] == pytest.approx(numeric, rel=1e-6)


@pytest.mark.unit
def test_band_split_round_trip():
    broadband = broadband_emissivity(0.9, 0.3)
    assert outside_window_emissivity(broadband, 0.9) == pytest.approx(0.3, abs=1e-12)
    assert outside_window_emissivity(0.7, 0.7) == pytest.approx(0.7, abs=1e-12)