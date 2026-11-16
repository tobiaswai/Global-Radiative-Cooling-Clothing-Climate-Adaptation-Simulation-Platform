"""Planck band integrals (Stage 10, ADR 0007).

F(lambda*T) = integral_0^lambda E_b,lambda d lambda / (sigma T^4).

For zeta = c2/(lambda T) >= 1 the exponential series of Siegel & Howell is
used; for zeta < 1 the Bernoulli series of integral_0^zeta u^3/(e^u-1) du.
Both are accurate to ~1e-12 in their ranges, so no table is needed.
"""

from __future__ import annotations

from math import exp, expm1, pi

from app.services.model_parameters import get_parameter_value as _param


SECOND_RADIATION_CONSTANT = _param("second_radiation_constant")  # um K
WINDOW_LOWER_UM = _param("atmospheric_window_lower_um")
WINDOW_UPPER_UM = _param("atmospheric_window_upper_um")
EMISSIVITY_REFERENCE_K = _param("emissivity_reference_temperature")

# Numerical (not physical) settings.
_NORMALIZATION = 15.0 / pi**4
_SERIES_SWITCH_ZETA = 1.0
_MAX_TERMS = 60
_OVERFLOW_ZETA = 700.0


def _lower_integral(zeta: float) -> float:
    """integral_0^zeta u^3 / (e^u - 1) du, valid for zeta < 2 pi."""
    z2 = zeta * zeta
    return zeta**3 * (
        1.0 / 3.0
        - zeta / 8.0
        + z2 / 60.0
        - z2**2 / 5040.0
        + z2**3 / 272160.0
        - z2**4 / 13305600.0
    )


def _upper_integral(zeta: float) -> float:
    """integral_zeta^inf u^3 / (e^u - 1) du."""
    total = 0.0
    for n in range(1, _MAX_TERMS + 1):
        term = exp(-n * zeta) / n * (
            zeta**3 + 3.0 * zeta**2 / n + 6.0 * zeta / n**2 + 6.0 / n**3
        )
        total += term
        if term <= 1e-16 * total:
            break
    return total


def blackbody_fraction(lambda_t_um_k: float) -> float:
    """Fraction of blackbody emission below wavelength lambda at temperature T."""
    if lambda_t_um_k <= 0.0:
        return 0.0
    zeta = SECOND_RADIATION_CONSTANT / lambda_t_um_k
    if zeta < _SERIES_SWITCH_ZETA:
        return max(0.0, 1.0 - _NORMALIZATION * _lower_integral(zeta))
    if zeta > _OVERFLOW_ZETA:
        return 0.0
    return min(1.0, _NORMALIZATION * _upper_integral(zeta))


def blackbody_fraction_slope(lambda_t_um_k: float) -> float:
    """dF/d(lambda T) in 1/(um K)."""
    if lambda_t_um_k <= 0.0:
        return 0.0
    zeta = SECOND_RADIATION_CONSTANT / lambda_t_um_k
    if zeta > _OVERFLOW_ZETA:
        return 0.0
    return _NORMALIZATION * zeta**4 / (lambda_t_um_k * expm1(zeta))


def band_fraction(
    temperature_k: float,
    lower_um: float = WINDOW_LOWER_UM,
    upper_um: float = WINDOW_UPPER_UM,
) -> float:
    return blackbody_fraction(upper_um * temperature_k) - blackbody_fraction(
        lower_um * temperature_k
    )


def band_power_k4(
    temperature_k: float,
    lower_um: float = WINDOW_LOWER_UM,
    upper_um: float = WINDOW_UPPER_UM,
) -> tuple[float, float]:
    """(band emission / sigma, d/dT of it) in K^4 and K^3."""
    t = temperature_k
    fraction = band_fraction(t, lower_um, upper_um)
    slope = (
        upper_um * blackbody_fraction_slope(upper_um * t)
        - lower_um * blackbody_fraction_slope(lower_um * t)
    )
    return fraction * t**4, 4.0 * t**3 * fraction + t**4 * slope


def outside_window_emissivity(
    broadband: float,
    window: float,
    reference_k: float = EMISSIVITY_REFERENCE_K,
) -> float:
    """eps_N such that F_W eps_W + (1 - F_W) eps_N = eps_broadband at T_ref."""
    fw = band_fraction(reference_k)
    return (broadband - fw * window) / (1.0 - fw)


def broadband_emissivity(
    window: float,
    outside: float,
    reference_k: float = EMISSIVITY_REFERENCE_K,
) -> float:
    fw = band_fraction(reference_k)
    return fw * window + (1.0 - fw) * outside


def planck_shape(wavelength_um: float, temperature_k: float) -> float:
    """Spectral emissive power up to the constant c1 (use for ratios only)."""
    zeta = SECOND_RADIATION_CONSTANT / (wavelength_um * temperature_k)
    if zeta > _OVERFLOW_ZETA:
        return 0.0
    return 1.0 / (wavelength_um**5 * expm1(zeta))