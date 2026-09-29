"""Registry of every numeric constant used by the thermal model (Stage 2).

Rules
-----
* ``two_node.py``, ``clothing.py`` and ``environment_model.py`` must not
  contain bare physical constants; they bind values from here at import.
* Changing any value changes ``model_parameter_set_sha256()``, which is
  written into every simulation response and checked by the golden test.
* ``source_type == "assumed"`` marks values that still need validation
  (Stage 3 benchmark work).
"""

from __future__ import annotations

import hashlib
import json

from app.schemas.provenance import (
    ModelMetadata,
    ModelParameter,
    ModelParameterManifest,
    SourceType,
)


MODEL_PARAMETER_SET_VERSION = "2.0.0"

GAGGE_1986 = (
    "Gagge, Fobelets & Berglund (1986). A standard predictive index of "
    "human response to the thermal environment. ASHRAE Trans. 92(2B):709-731"
)
ASHRAE_FUNDAMENTALS = (
    "ASHRAE Handbook - Fundamentals (2017), Chapter 9: Thermal Comfort"
)
ISO_7730 = "ISO 7730:2005, Annex D (Fanger 1970 respiratory heat loss)"
PROTOTYPE = "Project prototype value (radiative-cooling-platform, Stage 0-1)"


def _p(
    name: str,
    value: float,
    unit: str,
    description: str,
    source_type: SourceType,
    reference: str,
    note: str | None = None,
) -> ModelParameter:
    return ModelParameter(
        name=name,
        value=value,
        unit=unit,
        description=description,
        source_type=source_type,
        reference=reference,
        note=note,
    )


_PARAMETERS: tuple[ModelParameter, ...] = (
    # --- physical constants -------------------------------------------------
    _p("stefan_boltzmann_constant", 5.670374419e-8, "W/(m^2 K^4)",
       "Stefan-Boltzmann constant", "standard", "CODATA 2018"),
    _p("magnus_a", 0.61078, "kPa",
       "Saturation vapour pressure, Tetens/Murray form: a*exp(b*T/(T+c))",
       "literature", "Murray (1967) J. Appl. Meteorol. 6:203-204"),
    _p("magnus_b", 17.2694, "-", "Saturation vapour pressure exponent factor",
       "literature", "Murray (1967) J. Appl. Meteorol. 6:203-204"),
    _p("magnus_c", 237.3, "C", "Saturation vapour pressure denominator offset",
       "literature", "Murray (1967) J. Appl. Meteorol. 6:203-204"),

    # --- body thermal mass --------------------------------------------------
    _p("core_heat_capacity", 245_000.0, "J/(m^2 K)",
       "Area-normalised effective heat capacity of the core node",
       "assumed", PROTOTYPE,
       "Core + skin = 280 kJ/(m^2 K), about 2x the lumped Gagge value for a "
       "70 kg / 1.8 m^2 person (~136 kJ/(m^2 K)). Revisit in Stage 3."),
    _p("skin_heat_capacity", 35_000.0, "J/(m^2 K)",
       "Area-normalised effective heat capacity of the skin node",
       "assumed", PROTOTYPE, "See core_heat_capacity."),

    # --- convection ---------------------------------------------------------
    _p("natural_convection_minimum_coefficient", 3.1, "W/(m^2 K)",
       "Lower bound of the convective heat transfer coefficient (still air)",
       "literature", ASHRAE_FUNDAMENTALS + ", Table 6 (seated, v < 0.2 m/s)"),
    _p("forced_convection_coefficient", 8.3, "W/(m^2 K (m/s)^-0.5)",
       "h_c = 8.3 * v^0.5",
       "literature", ASHRAE_FUNDAMENTALS + ", Table 6 (Mitchell 1974: 8.3 v^0.6)",
       "Exponent simplified from 0.6 to 0.5 in this prototype."),
    _p("linearized_radiative_coefficient", 5.5, "W/(m^2 K)",
       "Linearised radiative coefficient inside the clothing coupling factor "
       "1/(1 + R_cl (h_c + h_r))",
       "assumed", PROTOTYPE,
       "Typical h_r is 4.7-5.5 W/(m^2 K) near 30 C."),

    # --- clothing -----------------------------------------------------------
    _p("clo_to_si", 0.155, "m^2 K/(W clo)", "1 clo = 0.155 m^2 K/W",
       "standard", "ISO 9920:2007"),
    _p("lewis_relation", 16.5, "K/kPa",
       "Lewis relation h_e / h_c at sea level",
       "standard", ASHRAE_FUNDAMENTALS),
    _p("clothing_vapor_permeation_efficiency", 0.45, "-",
       "i_cl used to derive Re,cl = R_cl / (LR * i_cl) when the material "
       "does not supply a measured evaporative resistance",
       "literature", GAGGE_1986 + "; ASHRAE 55 SET procedure",
       "The Stage 1 factor 1/(1 + 0.45 clo h_c) was equivalent to "
       "i_cl ~ 0.344 (Re,cl ~ 27.3 clo m^2 Pa/W). New default gives "
       "Re,cl ~ 20.9 clo m^2 Pa/W."),
    _p("skin_emissivity", 0.95, "-",
       "Longwave emissivity of skin, used for radiation transmitted through "
       "IR-transparent textiles",
       "literature", "Steketee (1973) Phys. Med. Biol. 18:686-694"),

    # --- thermoregulation ---------------------------------------------------
    _p("core_setpoint_temperature", 36.8, "C", "Core temperature set point",
       "literature", GAGGE_1986),
    _p("skin_setpoint_temperature", 33.7, "C", "Skin temperature set point",
       "literature", GAGGE_1986),
    _p("sweating_gain_core", 170.0, "g/(h m^2 K)",
       "Regulatory sweating per K of core warm signal",
       "assumed", PROTOTYPE + " adapted from " + GAGGE_1986,
       "Gagge uses 170 g/(h m^2 K) on the body-temperature signal with an "
       "exponential skin modifier; this prototype uses separate linear gains."),
    _p("sweating_gain_skin", 200.0, "g/(h m^2 K)",
       "Regulatory sweating per K of skin warm signal",
       "assumed", PROTOTYPE),
    _p("maximum_sweat_rate", 500.0, "g/(h m^2)", "Upper bound of sweating",
       "literature", GAGGE_1986),
    _p("latent_heat_of_sweat", 0.68, "W h/g",
       "Converts g/(h m^2) to W/m^2 (h_fg 2430 kJ/kg / 3600)",
       "standard", ASHRAE_FUNDAMENTALS),
    _p("skin_diffusion_fraction", 0.06, "-",
       "Skin diffusion evaporation as a fraction of E_max",
       "literature", GAGGE_1986),
    _p("skin_blood_flow_basal", 6.3, "kg/(h m^2)", "Neutral skin blood flow",
       "literature", GAGGE_1986),
    _p("skin_blood_flow_core_gain", 75.0, "kg/(h m^2 K)",
       "Vasodilation per K of core warm signal",
       "assumed", PROTOTYPE + " adapted from " + GAGGE_1986),
    _p("skin_blood_flow_skin_gain", 20.0, "kg/(h m^2 K)",
       "Vasodilation per K of skin warm signal",
       "assumed", PROTOTYPE),
    _p("skin_blood_flow_minimum", 0.5, "kg/(h m^2)", "Lower clamp",
       "literature", GAGGE_1986),
    _p("skin_blood_flow_maximum", 90.0, "kg/(h m^2)", "Upper clamp",
       "literature", GAGGE_1986),
    _p("core_skin_conductance_basal", 5.28, "W/(m^2 K)",
       "Core-to-skin conductance without blood flow",
       "literature", GAGGE_1986),
    _p("blood_heat_capacity_per_flow", 1.163, "W h/(kg K)",
       "Blood c_p per unit flow (4186 J/(kg K) / 3600)",
       "literature", GAGGE_1986),

    # --- metabolism and respiration -----------------------------------------
    _p("metabolic_rate_per_met", 58.15, "W/m^2", "1 met",
       "standard", "ISO 7730:2005 (58.2 W/m^2); ASHRAE 55 (58.15)"),
    _p("respiratory_latent_coefficient", 1.7e-5, "1/Pa",
       "E_res = c * M * (p_ref - p_a)", "standard", ISO_7730,
       "ISO 7730 uses 1.72e-5."),
    _p("respiratory_reference_vapor_pressure", 5867.0, "Pa",
       "Reference vapour pressure in E_res", "standard", ISO_7730),
    _p("respiratory_sensible_coefficient", 0.0014, "1/K",
       "C_res = c * M * (t_ex - t_a)", "standard", ISO_7730),
    _p("exhaled_air_temperature", 34.0, "C", "t_ex in C_res",
       "standard", ISO_7730),

    # --- environment fallbacks and empirical sky models ---------------------
    _p("fallback_sky_temperature_offset", 15.0, "K",
       "Sky temperature depression used when a fixed environment supplies "
       "no sky temperature", "assumed", PROTOTYPE),
    _p("swinbank_coefficient", 0.0552, "K^-0.5",
       "Clear-sky T_sky[K] = 0.0552 * T_air[K]^1.5",
       "literature", "Swinbank (1963) Q. J. R. Meteorol. Soc. 89:339-348"),
)


MODEL_PARAMETERS: dict[str, ModelParameter] = {
    parameter.name: parameter for parameter in _PARAMETERS
}

if len(MODEL_PARAMETERS) != len(_PARAMETERS):
    raise RuntimeError("Duplicate model parameter names in registry")


def get_parameter_value(name: str) -> float:
    try:
        return MODEL_PARAMETERS[name].value
    except KeyError as error:
        raise KeyError(f"Unknown model parameter: {name}") from error


def list_model_parameters() -> list[ModelParameter]:
    return list(_PARAMETERS)


def model_parameter_set_sha256() -> str:
    serialized = json.dumps(
        [
            {"name": p.name, "value": p.value, "unit": p.unit}
            for p in _PARAMETERS
        ],
        sort_keys=True,
        separators=(",", ":"),
    )
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def build_model_metadata() -> ModelMetadata:
    return ModelMetadata(
        parameter_set_version=MODEL_PARAMETER_SET_VERSION,
        parameter_set_sha256=model_parameter_set_sha256(),
    )


def build_model_parameter_manifest() -> ModelParameterManifest:
    return ModelParameterManifest(
        **build_model_metadata().model_dump(),
        parameters=list_model_parameters(),
    )