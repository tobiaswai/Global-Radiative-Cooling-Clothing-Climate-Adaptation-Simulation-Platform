"""Shortwave irradiance incident on the clothed body (Stage 5, ADR 0006).

Per unit DuBois area:

    I_body = f_p * DNI                          direct beam on the projected area
           + 0.5 * f_eff * F_sky * DHI          sky diffuse, upper hemisphere
           + 0.5 * f_eff * rho_g * GHI          ground reflected, lower hemisphere

This is the geometry of ASHRAE 55-2020 Normative Appendix C (Arens et al.
2015) with the measured diffuse component instead of the 0.2 * I_dir estimate,
the sky view factor limiting the sky-diffuse term, and f_bes = 1 (no shading).

Legacy path: when the beam/diffuse split is not available the whole GHI is
treated as beam on the projected area (Stage 0-4 geometry). Fixed-environment
requests that do not send DNI/DHI therefore keep their incident irradiance;
only the surface-balance treatment (ADR 0005) changes their results.

Partition at the textile (ADR 0005):
    absorbed by textile   = (1 - rho_sol - tau_sol) * I_body   -> surface balance
    transmitted to skin   = tau_sol * I_body                   -> skin node
"""

from __future__ import annotations

from dataclasses import dataclass

from app.schemas.simulation import EnvironmentInput, MaterialInput
from app.services.model_parameters import get_parameter_value


HEMISPHERE_FRACTION = get_parameter_value("diffuse_hemisphere_fraction")


@dataclass(frozen=True)
class SolarLoad:
    incident_w_m2: float
    direct_w_m2: float
    sky_diffuse_w_m2: float
    ground_reflected_w_m2: float
    absorbed_by_textile_w_m2: float
    transmitted_to_skin_w_m2: float
    split_available: bool

    @property
    def entering_system_w_m2(self) -> float:
        """Solar energy that ends up in the clothing-body system."""
        return self.absorbed_by_textile_w_m2 + self.transmitted_to_skin_w_m2


def solar_absorptance(material: MaterialInput) -> float:
    value = 1.0 - material.solar_reflectance - material.solar_transmittance
    return min(1.0, max(0.0, value))


def solar_load(
    environment: EnvironmentInput,
    material: MaterialInput,
    radiation_area_ratio: float,
) -> SolarLoad:
    ghi = max(0.0, environment.solar_radiation_w_m2)
    projected = material.projected_solar_area_factor

    dni = environment.direct_normal_irradiance_w_m2
    dhi = environment.diffuse_horizontal_irradiance_w_m2

    if dni is None or dhi is None:
        direct = projected * ghi
        sky_diffuse = 0.0
        ground_reflected = 0.0
        split_available = False
    else:
        direct = projected * max(0.0, dni)
        sky_diffuse = (
            HEMISPHERE_FRACTION
            * radiation_area_ratio
            * environment.sky_view_factor
            * max(0.0, dhi)
        )
        ground_reflected = (
            HEMISPHERE_FRACTION
            * radiation_area_ratio
            * environment.ground_albedo
            * ghi
        )
        split_available = True

    incident = direct + sky_diffuse + ground_reflected

    return SolarLoad(
        incident_w_m2=incident,
        direct_w_m2=direct,
        sky_diffuse_w_m2=sky_diffuse,
        ground_reflected_w_m2=ground_reflected,
        absorbed_by_textile_w_m2=solar_absorptance(material) * incident,
        transmitted_to_skin_w_m2=material.solar_transmittance * incident,
        split_available=split_available,
    )