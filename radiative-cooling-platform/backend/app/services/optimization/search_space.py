"""Decision-variable bounds and optical energy constraints x_a + x_b <= 1.

Pairs
-----
* solar:   rho_sol + tau_sol <= 1                          (always)
* gray IR: eps + tau_IR <= 1                               (gray studies)
* band IR: eps_W + tau_IR <= 1 and eps_N + tau_IR <= 1     (selective studies)

A study is "selective" when a band emissivity is a decision variable or the
base garment already carries infrared_emissivity_window. The gray pair is then
implied (eps is a convex combination of eps_W and eps_N) and is not applied.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from app.schemas.optimization import EMISSIVITY_BAND_VARIABLES, OptimizationCreate
from app.services.optimization.variables import demand_direction, variable_value


SOLAR_PAIRS: tuple[tuple[str, str], ...] = (("solar_reflectance", "solar_transmittance"),)
GRAY_IR_PAIRS: tuple[tuple[str, str], ...] = (("infrared_emissivity", "infrared_transmittance"),)
BAND_IR_PAIRS: tuple[tuple[str, str], ...] = (
    ("infrared_emissivity_window", "infrared_transmittance"),
    ("infrared_emissivity_outside_window", "infrared_transmittance"),
)

LOWER_BOUND_SUM_TOLERANCE = 1e-9


@dataclass(frozen=True)
class SearchSpace:
    names: tuple[str, ...]
    lower: np.ndarray
    upper: np.ndarray
    # Index pairs (i, j) with x_i + x_j <= 1 (both are decision variables).
    linear_pairs: tuple[tuple[int, int], ...]
    directions: tuple[str, ...]

    def index(self, name: str) -> int:
        return self.names.index(name)

    def span(self, name: str) -> float:
        i = self.index(name)
        return float(self.upper[i] - self.lower[i])

    def least_demanding_bound(self, name: str) -> float:
        i = self.index(name)
        return float(self.lower[i] if self.directions[i] == "increasing" else self.upper[i])

    def most_demanding_bound(self, name: str) -> float:
        i = self.index(name)
        return float(self.upper[i] if self.directions[i] == "increasing" else self.lower[i])


def is_selective_study(request: OptimizationCreate) -> bool:
    names = {v.name for v in request.variables}
    return bool(EMISSIVITY_BAND_VARIABLES & names) or (
        request.base_material.infrared_emissivity_window is not None
    )


def optical_pairs(request: OptimizationCreate) -> tuple[tuple[str, str], ...]:
    return SOLAR_PAIRS + (BAND_IR_PAIRS if is_selective_study(request) else GRAY_IR_PAIRS)


def build_search_space(request: OptimizationCreate) -> SearchSpace:
    names = tuple(v.name for v in request.variables)
    lower = {v.name: float(v.lower) for v in request.variables}
    upper = {v.name: float(v.upper) for v in request.variables}
    base = request.base_material
    pairs: list[tuple[int, int]] = []

    for a, b in optical_pairs(request):
        has_a, has_b = a in upper, b in upper
        if has_a and has_b:
            pairs.append((names.index(a), names.index(b)))
        elif has_a:
            upper[a] = min(upper[a], 1.0 - variable_value(base, b))
        elif has_b:
            upper[b] = min(upper[b], 1.0 - variable_value(base, a))

        if has_a and has_b and lower[a] + lower[b] > 1.0 + LOWER_BOUND_SUM_TOLERANCE:
            raise ValueError(f"lower bounds of {a} and {b} already sum above 1")

    for name in names:
        if lower[name] >= upper[name]:
            raise ValueError(
                f"{name}: no feasible range left after applying the optical "
                f"energy constraint with the fixed base material "
                f"(lower {lower[name]}, effective upper {upper[name]:.4f})"
            )

    return SearchSpace(
        names=names,
        lower=np.asarray([lower[n] for n in names], dtype=float),
        upper=np.asarray([upper[n] for n in names], dtype=float),
        linear_pairs=tuple(pairs),
        directions=tuple(demand_direction(v) for v in request.variables),
    )