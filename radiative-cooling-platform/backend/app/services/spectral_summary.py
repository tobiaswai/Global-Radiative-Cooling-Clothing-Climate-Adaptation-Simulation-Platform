"""Planck-weighted band averages of uploaded IR spectra (Stage 10)."""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np

from app.schemas.material import SpectrumBandSummary
from app.services.planck import (
    WINDOW_LOWER_UM,
    WINDOW_UPPER_UM,
    blackbody_fraction,
    planck_shape,
)

GRID_POINTS = 401  # numerical: dense sub-grid so the Planck weight is well resolved


@dataclass(frozen=True)
class BandIntegral:
    weighted: float   # integral eps * B
    weight: float     # integral B
    coverage: float   # covered blackbody fraction / target blackbody fraction

    @property
    def average(self) -> float | None:
        return self.weighted / self.weight if self.weight > 0 else None


def band_integral(
    wavelengths: np.ndarray,
    values: np.ndarray,
    lower_um: float,
    upper_um: float,
    temperature_k: float,
) -> BandIntegral:
    lo = max(lower_um, float(wavelengths[0]))
    hi = min(upper_um, float(wavelengths[-1]))
    target = blackbody_fraction(upper_um * temperature_k) - blackbody_fraction(
        lower_um * temperature_k
    )

    if hi <= lo or target <= 0:
        return BandIntegral(0.0, 0.0, 0.0)

    inside = wavelengths[(wavelengths > lo) & (wavelengths < hi)]
    grid = np.unique(np.concatenate([np.linspace(lo, hi, GRID_POINTS), inside]))
    eps = np.interp(grid, wavelengths, values)
    weight = np.asarray([planck_shape(float(w), temperature_k) for w in grid])

    covered = blackbody_fraction(hi * temperature_k) - blackbody_fraction(lo * temperature_k)

    return BandIntegral(
        weighted=float(np.trapezoid(eps * weight, grid)),
        weight=float(np.trapezoid(weight, grid)),
        coverage=covered / target,
    )


def summarize_ir_spectrum(
    points: list[dict],
    *,
    spectrum_type: str,
    temperature_k: float,
) -> SpectrumBandSummary:
    wavelengths = np.asarray([p["wavelength_um"] for p in points], dtype=float)
    values = np.asarray([p["value"] for p in points], dtype=float)

    window = band_integral(wavelengths, values, WINDOW_LOWER_UM, WINDOW_UPPER_UM, temperature_k)
    measured = band_integral(wavelengths, values, 0.0, math.inf, temperature_k)

    outside_weight = measured.weight - window.weight
    outside = (
        (measured.weighted - window.weighted) / outside_weight
        if outside_weight > 1e-12 * max(measured.weight, 1e-300)
        else None
    )

    def rounded(value: float | None) -> float | None:
        return None if value is None else round(value, 5)

    return SpectrumBandSummary(
        spectrum_type=spectrum_type,
        temperature_k=temperature_k,
        window_lower_um=WINDOW_LOWER_UM,
        window_upper_um=WINDOW_UPPER_UM,
        measured_lower_um=float(wavelengths[0]),
        measured_upper_um=float(wavelengths[-1]),
        window_average=rounded(window.average),
        window_coverage=round(window.coverage, 5),
        broadband_average=rounded(measured.average),
        broadband_coverage=round(measured.coverage, 5),
        outside_window_average=rounded(outside),
    )