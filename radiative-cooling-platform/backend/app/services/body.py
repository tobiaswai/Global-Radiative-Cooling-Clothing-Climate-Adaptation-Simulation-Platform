"""Body thermal mass (Stage 3, ADR 0001).

C_core = m * c_p * (1 - alpha) / A_D          [J/(m^2 K)]
C_skin = m * c_p * alpha / A_D

alpha is kept constant (Gagge 1986 initial value 0.1). Gagge lets alpha vary
with skin blood flow; a constant keeps the capacities state-independent so the
energy-balance diagnostics remain exact.
"""

from __future__ import annotations

from dataclasses import dataclass

from app.schemas.simulation import PersonInput
from app.services.model_parameters import get_parameter_value


BODY_SPECIFIC_HEAT = get_parameter_value("body_specific_heat")
SKIN_MASS_FRACTION = get_parameter_value("skin_mass_fraction")


@dataclass(frozen=True)
class BodyHeatCapacities:
    core_j_m2k: float
    skin_j_m2k: float

    @property
    def total_j_m2k(self) -> float:
        return self.core_j_m2k + self.skin_j_m2k


def body_heat_capacities(person: PersonInput) -> BodyHeatCapacities:
    total = BODY_SPECIFIC_HEAT * person.body_mass_kg / person.body_surface_area_m2
    return BodyHeatCapacities(
        core_j_m2k=total * (1.0 - SKIN_MASS_FRACTION),
        skin_j_m2k=total * SKIN_MASS_FRACTION,
    )