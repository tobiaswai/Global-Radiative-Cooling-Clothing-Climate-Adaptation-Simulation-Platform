"""Scrambled Sobol sampling of material variables (ADR 0011)."""

from __future__ import annotations

import math
from dataclasses import dataclass

import numpy as np
from scipy.stats import qmc

from app.schemas.simulation import MaterialInput
from app.schemas.surrogate import SurrogateDatasetCreate
from app.services.optimization.variables import candidate_material

PARAMETER_DECIMALS = 6


@dataclass(frozen=True)
class SampledMaterial:
    index: int
    parameters: dict[str, float]
    material: MaterialInput


def _sobol(dimension: int, seed: int) -> qmc.Sobol:
    try:  # SciPy >= 1.15
        return qmc.Sobol(d=dimension, scramble=True, rng=np.random.default_rng(seed))
    except TypeError:
        return qmc.Sobol(d=dimension, scramble=True, seed=seed)


def sample_materials(spec: SurrogateDatasetCreate) -> tuple[list[SampledMaterial], int]:
    """(valid materials, rejected count). Deterministic for a given spec."""
    names = spec.variable_names
    lower = np.asarray([v.lower for v in spec.variables], dtype=float)
    upper = np.asarray([v.upper for v in spec.variables], dtype=float)

    unit = _sobol(len(names), spec.seed).random_base2(m=int(math.log2(spec.material_count)))
    points = qmc.scale(unit, lower, upper)

    valid: list[SampledMaterial] = []
    rejected = 0
    for index, row in enumerate(points):
        parameters = {name: round(float(value), PARAMETER_DECIMALS) for name, value in zip(names, row)}
        try:
            material = candidate_material(spec.base_material, parameters)
        except ValueError:
            rejected += 1
            continue
        valid.append(SampledMaterial(index=index, parameters=parameters, material=material))
    return valid, rejected