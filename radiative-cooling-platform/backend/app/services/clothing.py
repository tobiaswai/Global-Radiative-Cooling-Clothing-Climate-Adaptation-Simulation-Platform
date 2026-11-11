"""Clothing dry and evaporative resistances and area factor (Stage 3).

Dry pathway (see two_node.clothing_surface_temperature_c)
    (T_sk - T_cl) / R_cl = f_cl * [h_c (T_cl - T_a) + eps_cl sigma (T_cl^4 - T_env^4)]

Evaporative pathway
    E_max = (P_sk - P_a) / (Re,cl + Re,a)          [W/m^2]
    Re,a  = 1 / (LR * f_cl * h_c)                  [m^2 kPa/W]
    Re,cl = material value, or R_cl / (LR * i_cl)  when not supplied

f_cl = material value, or 1 + clothing_area_factor_slope * clo.
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
CLOTHING_AREA_FACTOR_SLOPE = get_parameter_value("clothing_area_factor_slope")

ParameterSourceLabel = Literal["material_input", "derived_from_clo"]


@dataclass(frozen=True)
class ClothingResistances:
    dry_resistance_m2k_w: float
    evaporative_resistance_m2kpa_w: float
    evaporative_resistance_source: ParameterSourceLabel
    infrared_transmittance: float
    area_factor: float
    area_factor_source: ParameterSourceLabel

    @property
    def evaporative_resistance_m2pa_w(self) -> float:
        return self.evaporative_resistance_m2kpa_w * 1000.0

    @property
    def is_nude(self) -> bool:
        return self.dry_resistance_m2k_w <= 0.0


def derive_evaporative_resistance_m2pa_w(clothing_insulation_clo: float) -> float:
    """Re,cl = R_cl / (LR * i_cl), expressed in m^2 Pa/W."""
    dry_resistance = CLO_TO_SI * clothing_insulation_clo
    return (
        dry_resistance
        / (LEWIS_RELATION * CLOTHING_VAPOR_PERMEATION_EFFICIENCY)
        * 1000.0
    )


def derive_clothing_area_factor(clothing_insulation_clo: float) -> float:
    """f_cl = 1 + slope * clo."""
    return 1.0 + CLOTHING_AREA_FACTOR_SLOPE * clothing_insulation_clo


def resolve_clothing(material: MaterialInput) -> ClothingResistances:
    dry_resistance = CLO_TO_SI * material.clothing_insulation_clo

    if material.evaporative_resistance_m2pa_w is not None:
        evaporative_m2pa_w = material.evaporative_resistance_m2pa_w
        evaporative_source: ParameterSourceLabel = "material_input"
    else:
        evaporative_m2pa_w = derive_evaporative_resistance_m2pa_w(
            material.clothing_insulation_clo
        )
        evaporative_source = "derived_from_clo"

    if material.clothing_area_factor is not None:
        area_factor = material.clothing_area_factor
        area_factor_source: ParameterSourceLabel = "material_input"
    else:
        area_factor = derive_clothing_area_factor(material.clothing_insulation_clo)
        area_factor_source = "derived_from_clo"

    return ClothingResistances(
        dry_resistance_m2k_w=dry_resistance,
        evaporative_resistance_m2kpa_w=evaporative_m2pa_w / 1000.0,
        evaporative_resistance_source=evaporative_source,
        infrared_transmittance=material.infrared_transmittance,
        area_factor=area_factor,
        area_factor_source=area_factor_source,
    )


def air_layer_evaporative_resistance_m2kpa_w(
    convection_coefficient: float,
    area_factor: float,
) -> float:
    return 1.0 / (LEWIS_RELATION * area_factor * convection_coefficient)


def maximum_evaporation_w_m2(
    clothing: ClothingResistances,
    convection_coefficient: float,
    skin_vapor_pressure_kpa: float,
    ambient_vapor_pressure_kpa: float,
) -> float:
    total_resistance = (
        clothing.evaporative_resistance_m2kpa_w
        + air_layer_evaporative_resistance_m2kpa_w(
            convection_coefficient, clothing.area_factor
        )
    )
    return max(
        0.0,
        (skin_vapor_pressure_kpa - ambient_vapor_pressure_kpa) / total_resistance,
    )


def assumptions_applied(
    clothing: ClothingResistances,
    *,
    solar_split_available: bool = False,
) -> list[str]:
    notes: list[str] = []

    if clothing.evaporative_resistance_source == "derived_from_clo":
        notes.append(
            "evaporative_resistance_m2pa_w not supplied; derived as "
            f"R_cl / (LR * i_cl) with i_cl = {CLOTHING_VAPOR_PERMEATION_EFFICIENCY} "
            f"-> {clothing.evaporative_resistance_m2pa_w:.2f} m^2 Pa/W"
        )

    if clothing.area_factor_source == "derived_from_clo":
        notes.append(
            "clothing_area_factor not supplied; derived as "
            f"1 + {CLOTHING_AREA_FACTOR_SLOPE} * clo -> {clothing.area_factor:.4f}"
        )

    if clothing.infrared_transmittance > 0.0:
        notes.append(
            "infrared_transmittance > 0: transmitted skin emission is a parallel "
            "path that bypasses the clothing surface balance (first-order model)"
        )

    notes.append(
        "solar radiation absorbed by the textile enters the clothing surface "
        "balance; transmitted solar reaches the skin node directly. "
        "absorbed_solar_to_body_fraction is ignored (ADR 0005)"
    )

    if solar_split_available:
        notes.append(
            "body-incident shortwave = f_p * DNI + 0.5 f_eff F_sky DHI "
            "+ 0.5 f_eff rho_g GHI (ASHRAE 55 Appendix C geometry, ADR 0006)"
        )
    else:
        notes.append(
            "no beam/diffuse split supplied; GHI treated as beam on the "
            "projected area (legacy Stage 0-4 geometry, ADR 0006)"
        )

    return notes