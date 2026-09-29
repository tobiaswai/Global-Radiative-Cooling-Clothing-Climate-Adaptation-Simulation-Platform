"""Clothing dry and evaporative resistances (Stage 2).

Evaporative pathway
-------------------
E_max = (P_sk - P_a) / (Re,cl + Re,a)         [W/m^2]
Re,a  = 1 / (LR * h_c)                         [m^2 kPa/W]
Re,cl = material value, or R_cl / (LR * i_cl)  when not supplied

The clothing area factor f_cl is deliberately not applied so that the
evaporative and dry pathways stay consistent (the dry pathway also omits
it). Introducing f_cl in both pathways is Stage 3 benchmark work.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from app.schemas.simulation import MaterialInput
from app.services.model_parameters import get_parameter_value


CLO_TO_SI = get_parameter_value("clo_to_si")
LEWIS_RELATION = get_parameter_value("lewis_relation")
CLOTHING_VAPOR_PERMEATION_EFFICIENCY = get_parameter_value(
    "clothing_vapor_permeation_efficiency"
)

EvaporativeResistanceSource = Literal["material_input", "derived_from_clo"]


@dataclass(frozen=True)
class ClothingResistances:
    dry_resistance_m2k_w: float
    evaporative_resistance_m2kpa_w: float
    evaporative_resistance_source: EvaporativeResistanceSource
    infrared_transmittance: float

    @property
    def evaporative_resistance_m2pa_w(self) -> float:
        return self.evaporative_resistance_m2kpa_w * 1000.0


def derive_evaporative_resistance_m2pa_w(clothing_insulation_clo: float) -> float:
    """Re,cl = R_cl / (LR * i_cl), expressed in m^2 Pa/W."""
    dry_resistance = CLO_TO_SI * clothing_insulation_clo
    return dry_resistance / (LEWIS_RELATION * CLOTHING_VAPOR_PERMEATION_EFFICIENCY) * 1000.0


def resolve_clothing(material: MaterialInput) -> ClothingResistances:
    dry_resistance = CLO_TO_SI * material.clothing_insulation_clo

    if material.evaporative_resistance_m2pa_w is not None:
        evaporative_m2pa_w = material.evaporative_resistance_m2pa_w
        source: EvaporativeResistanceSource = "material_input"
    else:
        evaporative_m2pa_w = derive_evaporative_resistance_m2pa_w(
            material.clothing_insulation_clo
        )
        source = "derived_from_clo"

    return ClothingResistances(
        dry_resistance_m2k_w=dry_resistance,
        evaporative_resistance_m2kpa_w=evaporative_m2pa_w / 1000.0,
        evaporative_resistance_source=source,
        infrared_transmittance=material.infrared_transmittance,
    )


def air_layer_evaporative_resistance_m2kpa_w(convection_coefficient: float) -> float:
    return 1.0 / (LEWIS_RELATION * convection_coefficient)


def maximum_evaporation_w_m2(
    clothing: ClothingResistances,
    convection_coefficient: float,
    skin_vapor_pressure_kpa: float,
    ambient_vapor_pressure_kpa: float,
) -> float:
    total_resistance = (
        clothing.evaporative_resistance_m2kpa_w
        + air_layer_evaporative_resistance_m2kpa_w(convection_coefficient)
    )
    return max(
        0.0,
        (skin_vapor_pressure_kpa - ambient_vapor_pressure_kpa) / total_resistance,
    )


def assumptions_applied(clothing: ClothingResistances) -> list[str]:
    notes: list[str] = []

    if clothing.evaporative_resistance_source == "derived_from_clo":
        notes.append(
            "evaporative_resistance_m2pa_w not supplied; derived as "
            f"R_cl / (LR * i_cl) with i_cl = {CLOTHING_VAPOR_PERMEATION_EFFICIENCY} "
            f"-> {clothing.evaporative_resistance_m2pa_w:.2f} m^2 Pa/W"
        )

    if clothing.infrared_transmittance > 0.0:
        notes.append(
            "infrared_transmittance > 0: transmitted skin emission bypasses the "
            "clothing coupling factor (first-order model)"
        )

    return notes