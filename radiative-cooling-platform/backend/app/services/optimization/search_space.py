"""Decision-variable bounds and the optical energy constraints
rho_sol + tau_sol <= 1 and eps_IR + tau_IR <= 1."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from app.schemas.optimization import OptimizationCreate


OPTICAL_PAIRS: tuple[tuple[str, str], ...] = (
    ("solar_reflectance", "solar_transmittance"),
    ("infrared_emissivity", "infrared_transmittance"),
)


@dataclass(frozen=True)
class SearchSpace:
    names: tuple[str, ...]
    lower: np.ndarray
    upper: np.ndarray
    # Index pairs (i, j) with x_i + x_j <= 1 (both are decision variables).
    linear_pairs: tuple[tuple[int, int], ...]

    def index(self, name: str) -> int:
        return self.names.index(name)


def build_search_space(request: OptimizationCreate) -> SearchSpace:
    names = tuple(v.name for v in request.variables)
    lower = {v.name: v.lower for v in request.variables}
    upper = {v.name: v.upper for v in request.variables}
    base = request.base_material
    pairs: list[tuple[int, int]] = []

    for a, b in OPTICAL_PAIRS:
        has_a, has_b = a in upper, b in upper
        if has_a and has_b:
            pairs.append((names.index(a), names.index(b)))
        elif has_a:
            upper[a] = min(upper[a], 1.0 - float(getattr(base, b)))
        elif has_b:
            upper[b] = min(upper[b], 1.0 - float(getattr(base, a)))

    for a, b in OPTICAL_PAIRS:
        if a in lower and b in lower and lower[a] + lower[b] > 1.0 + 1e-9:
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
    )