"""Decision-variable semantics shared by search space, evaluator and objective.

Band emissivities
-----------------
* infrared_emissivity_window: eps in 8-13 um. Varying it alone keeps the
  out-of-window emissivity of the base garment fixed.
* infrared_emissivity_outside_window: eps outside the window. Virtual: it is
  mapped to the broadband infrared_emissivity at the reference temperature.
A gray base garment has eps_W = eps_N = infrared_emissivity.
"""

from __future__ import annotations

from app.schemas.optimization import DEFAULT_DEMAND_DIRECTION, DecisionVariable
from app.schemas.simulation import MaterialInput
from app.services.clothing import derive_evaporative_resistance_m2pa_w
from app.services.planck import broadband_emissivity, outside_window_emissivity


WINDOW = "infrared_emissivity_window"
OUTSIDE_WINDOW = "infrared_emissivity_outside_window"

PROVENANCE_RESET = {
    "material_version_id": None,
    "parameter_sources": None,
    "source_type": "derived",
    "source_reference": "optimization candidate",
}


def demand_direction(variable: DecisionVariable) -> str:
    return variable.demand_direction or DEFAULT_DEMAND_DIRECTION[variable.name]


def variable_value(material: MaterialInput, name: str) -> float:
    """Value of a decision variable on a concrete garment (handles virtual ones)."""
    if name in (WINDOW, OUTSIDE_WINDOW):
        window = material.infrared_emissivity_window
        if window is None:
            return float(material.infrared_emissivity)
        if name == WINDOW:
            return float(window)
        return float(outside_window_emissivity(material.infrared_emissivity, window))

    if name == "evaporative_resistance_m2pa_w" and material.evaporative_resistance_m2pa_w is None:
        return float(derive_evaporative_resistance_m2pa_w(material.clothing_insulation_clo))

    return float(getattr(material, name))


def candidate_material(base: MaterialInput, parameters: dict[str, float]) -> MaterialInput:
    """Validated candidate garment. Raises ValueError when physically impossible."""
    update = {name: float(value) for name, value in parameters.items()}
    outside = update.pop(OUTSIDE_WINDOW, None)

    if WINDOW in update or outside is not None:
        window = update.get(WINDOW)
        if window is None:
            window = variable_value(base, WINDOW)
        if outside is None:
            outside = variable_value(base, OUTSIDE_WINDOW)
        update[WINDOW] = window
        update["infrared_emissivity"] = broadband_emissivity(window, outside)

    return MaterialInput.model_validate({**base.model_dump(), **update, **PROVENANCE_RESET})