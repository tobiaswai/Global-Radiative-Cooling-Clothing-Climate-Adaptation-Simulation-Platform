"""Transient comparison of the platform prototype with the Gagge two-node model.

Alignment
---------
The Gagge model has a single radiant temperature, no solar term, a fixed
clothing emissivity of 0.95 and derives Re,cl and f_cl from clo. The prototype
run is therefore configured so that both models see the same boundary
conditions; every alignment step is reported in ``alignment_applied``.
This is a diagnostic comparison, not an equivalence proof: convection
correlations, the clothing surface balance and the wettedness bookkeeping
differ by design.
"""

from __future__ import annotations

from importlib.metadata import PackageNotFoundError, version

import numpy as np
from pythermalcomfort.models import two_nodes_gagge

from app.schemas.simulation import (
    BenchmarkMetric,
    BenchmarkSeriesPoint,
    GaggeBenchmarkRequest,
    GaggeBenchmarkResponse,
    GaggeModelOutput,
    PrototypeBenchmarkOutput,
    ReferencePortParity,
)
from app.services.gagge_reference import run_gagge_reference
from app.services.two_node import simulate_material


LIBRARY_DURATION_MINUTES = 60
REFERENCE_CLOTHING_EMISSIVITY = 0.95


def _to_float(value: object) -> float:
    """Convert a Python float, NumPy scalar or single-element array to float."""
    if hasattr(value, "item"):
        return float(value.item())
    return float(value)


def _library_version() -> str:
    try:
        return version("pythermalcomfort")
    except PackageNotFoundError:
        return "unknown"


def _metric(
    prototype: np.ndarray,
    reference: np.ndarray,
    tolerance: float,
) -> BenchmarkMetric:
    difference = prototype - reference
    maximum = float(np.max(np.abs(difference)))
    return BenchmarkMetric(
        final_difference_c=round(float(difference[-1]), 4),
        maximum_absolute_difference_c=round(maximum, 4),
        root_mean_square_difference_c=round(float(np.sqrt(np.mean(difference**2))), 4),
        tolerance_c=tolerance,
        passed=maximum <= tolerance,
    )


def run_gagge_benchmark(request: GaggeBenchmarkRequest) -> GaggeBenchmarkResponse:
    alignment: list[str] = []

    # --- boundary conditions the reference model can represent ----------------
    environment = request.environment.model_copy(
        update={
            "solar_radiation_w_m2": 0.0,
            "sky_view_factor": 0.0,
            "sky_temperature_c": request.environment.mean_radiant_temperature_c,
        }
    )
    alignment.append("solar_radiation_w_m2 set to 0 (reference has no solar term)")
    alignment.append(
        "sky_view_factor set to 0 and sky temperature set equal to the mean "
        "radiant temperature (reference has a single radiant temperature)"
    )

    material = request.material.model_copy(
        update={
            "infrared_emissivity": REFERENCE_CLOTHING_EMISSIVITY,
            "infrared_transmittance": 0.0,
            "evaporative_resistance_m2pa_w": None,
            "clothing_area_factor": None,
        }
    )
    alignment.append(
        f"infrared_emissivity set to {REFERENCE_CLOTHING_EMISSIVITY} and "
        "infrared_transmittance to 0 (fixed in the reference)"
    )
    alignment.append(
        "evaporative_resistance_m2pa_w and clothing_area_factor derived from clo "
        "(the reference accepts clo only)"
    )

    # --- prototype ------------------------------------------------------------
    prototype = simulate_material(
        duration_minutes=request.duration_minutes,
        output_interval_minutes=1,
        environment=environment,
        person=request.person,
        material=material,
    )

    # --- reference trajectory (port) ------------------------------------------
    reference_kwargs = dict(
        tdb=environment.air_temperature_c,
        tr=environment.mean_radiant_temperature_c,
        v=environment.wind_speed_m_s,
        rh=environment.relative_humidity_percent,
        met=request.person.met,
        clo=material.clothing_insulation_clo,
        wme=0.0,
        body_surface_area=request.person.body_surface_area_m2,
        body_mass_kg=request.person.body_mass_kg,
        p_atm=101325.0,
        position="standing",
        max_skin_blood_flow=90.0,
        max_sweating=500.0,
    )

    reference = run_gagge_reference(
        duration_minutes=request.duration_minutes, **reference_kwargs
    )

    # --- library result: SET and port parity (60 min, 70 kg) ------------------
    library = two_nodes_gagge(
        tdb=environment.air_temperature_c,
        tr=environment.mean_radiant_temperature_c,
        v=max(environment.wind_speed_m_s, 0.01),
        rh=environment.relative_humidity_percent,
        met=request.person.met,
        clo=material.clothing_insulation_clo,
        wme=0,
        body_surface_area=request.person.body_surface_area_m2,
        p_atm=101325,
        position="standing",
        max_skin_blood_flow=90,
        max_sweating=500,
        round_output=False,
    )

    parity_reference = run_gagge_reference(
        duration_minutes=LIBRARY_DURATION_MINUTES,
        **{**reference_kwargs, "body_mass_kg": 70.0},
    ).final

    library_core = _to_float(library.t_core)
    library_skin = _to_float(library.t_skin)

    parity = ReferencePortParity(
        library_core_temperature_c=round(library_core, 4),
        port_core_temperature_c=round(parity_reference.core_temperature_c, 4),
        library_skin_temperature_c=round(library_skin, 4),
        port_skin_temperature_c=round(parity_reference.skin_temperature_c, 4),
        maximum_absolute_difference_c=round(
            max(
                abs(library_core - parity_reference.core_temperature_c),
                abs(library_skin - parity_reference.skin_temperature_c),
            ),
            4,
        ),
    )

    if request.person.body_mass_kg != 70.0:
        alignment.append(
            "reference trajectory uses body_mass_kg from the request; the library "
            "value (SET, parity) is fixed at 70 kg"
        )

    # --- align the two series minute by minute --------------------------------
    prototype_points = prototype.time_series
    reference_points = reference.points

    if len(prototype_points) != len(reference_points):
        raise RuntimeError(
            "Benchmark series length mismatch: "
            f"{len(prototype_points)} prototype vs {len(reference_points)} reference"
        )

    series = [
        BenchmarkSeriesPoint(
            minute=int(round(p.minute)),
            prototype_core_temperature_c=p.core_temperature_c,
            prototype_skin_temperature_c=p.skin_temperature_c,
            prototype_evaporation_w_m2=p.evaporation_w_m2,
            reference_core_temperature_c=round(r.core_temperature_c, 4),
            reference_skin_temperature_c=round(r.skin_temperature_c, 4),
            reference_evaporation_w_m2=round(r.skin_evaporation_w_m2, 4),
        )
        for p, r in zip(prototype_points, reference_points, strict=True)
    ]

    core_metric = _metric(
        np.asarray([s.prototype_core_temperature_c for s in series]),
        np.asarray([s.reference_core_temperature_c for s in series]),
        request.tolerances.core_temperature_c,
    )
    skin_metric = _metric(
        np.asarray([s.prototype_skin_temperature_c for s in series]),
        np.asarray([s.reference_skin_temperature_c for s in series]),
        request.tolerances.skin_temperature_c,
    )

    final_prototype = prototype_points[-1]
    final_reference = reference.final

    return GaggeBenchmarkResponse(
        reference_model="Gagge Two-Node",
        reference_library="pythermalcomfort",
        reference_library_version=_library_version(),
        environment_note=(
            "Boundary conditions were aligned to what the Gagge two-node model "
            "can represent; see alignment_applied."
        ),
        alignment_applied=alignment,
        prototype=PrototypeBenchmarkOutput(
            core_temperature_c=prototype.final_core_temperature_c,
            skin_temperature_c=prototype.final_skin_temperature_c,
            evaporation_w_m2=final_prototype.evaporation_w_m2,
            skin_wettedness=final_prototype.skin_wettedness or 0.0,
            skin_blood_flow_kg_h_m2=final_prototype.skin_blood_flow_kg_h_m2 or 0.0,
            energy_residual_percent=prototype.diagnostics.normalized_residual_percent,
        ),
        gagge=GaggeModelOutput(
            core_temperature_c=round(final_reference.core_temperature_c, 4),
            skin_temperature_c=round(final_reference.skin_temperature_c, 4),
            skin_evaporation_w_m2=round(final_reference.skin_evaporation_w_m2, 4),
            skin_heat_loss_w_m2=round(
                final_reference.skin_evaporation_w_m2
                + final_reference.sensible_heat_loss_w_m2,
                4,
            ),
            respiratory_heat_loss_w_m2=round(reference.respiratory_heat_loss_w_m2, 4),
            skin_blood_flow_kg_h_m2=round(final_reference.skin_blood_flow_kg_h_m2, 4),
            skin_wettedness=round(final_reference.skin_wettedness, 4),
            standard_effective_temperature_c=_to_float(library.set),
        ),
        difference_core_temperature_c=core_metric.final_difference_c,
        difference_skin_temperature_c=skin_metric.final_difference_c,
        core_temperature=core_metric,
        skin_temperature=skin_metric,
        passed=core_metric.passed and skin_metric.passed,
        time_series=series,
        reference_port_parity=parity,
        warning=(
            "Diagnostic comparison, not an equivalence verification. Both models "
            "share body heat capacity, the effective radiation area ratio and the "
            "Gagge 1986 controllers; they still differ in the convection "
            "correlation (8.3 v^0.5 vs 8.6 v^0.53 with a metabolic floor), the "
            "exact vs linearised radiation exchange, and the skin wettedness "
            "bookkeeping once w reaches w_max."
        ),
    )