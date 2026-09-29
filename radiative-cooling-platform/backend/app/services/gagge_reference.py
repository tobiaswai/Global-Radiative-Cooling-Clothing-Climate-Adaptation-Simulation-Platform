"""Minute-by-minute Gagge two-node reference model.

This is a port of the algorithm used by ``pythermalcomfort.models.two_nodes_gagge``
(Tartarini & Schiavon 2020, MIT licence), which itself follows Gagge, Fobelets &
Berglund (1986) and the ASHRAE 55 SET reference procedure. The library returns
only the state after 60 minutes for a fixed 70 kg body; this port exposes the
full trajectory, the exposure duration and the body mass so the platform
prototype can be compared minute by minute.

Parity with the library at 60 minutes and 70 kg is enforced by
``tests/test_gagge_reference.py``. Do not "improve" the physics here: the value
of this module is that it reproduces the reference exactly, quirks included.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import exp
from typing import Literal


BodyPosition = Literal["standing", "sitting"]

MET_FACTOR_W_M2 = 58.2
STEFAN_BOLTZMANN = 5.6697e-8
SWEATING_COEFFICIENT = 170.0
VASODILATION_COEFFICIENT = 120.0
VASOCONSTRICTION_COEFFICIENT = 0.5
SKIN_NEUTRAL_C = 33.7
CORE_NEUTRAL_C = 36.8
SKIN_BLOOD_FLOW_NEUTRAL = 6.3
BODY_SPECIFIC_HEAT_WH_KGK = 0.97
CLOTHING_EMISSIVITY = 0.95
SURFACE_ITERATION_LIMIT = 150


def saturation_vapor_pressure_torr(temperature_c: float) -> float:
    return exp(18.6686 - 4030.183 / (temperature_c + 235.0))


@dataclass(frozen=True)
class GaggeReferencePoint:
    minute: int
    core_temperature_c: float
    skin_temperature_c: float
    skin_evaporation_w_m2: float
    sensible_heat_loss_w_m2: float
    skin_blood_flow_kg_h_m2: float
    skin_wettedness: float


@dataclass(frozen=True)
class GaggeReferenceResult:
    points: list[GaggeReferencePoint]
    respiratory_heat_loss_w_m2: float
    maximum_skin_wettedness: float

    @property
    def final(self) -> GaggeReferencePoint:
        return self.points[-1]


def run_gagge_reference(
    *,
    tdb: float,
    tr: float,
    v: float,
    rh: float,
    met: float,
    clo: float,
    wme: float = 0.0,
    body_surface_area: float = 1.8258,
    body_mass_kg: float = 70.0,
    p_atm: float = 101325.0,
    position: BodyPosition = "standing",
    max_skin_blood_flow: float = 90.0,
    max_sweating: float = 500.0,
    duration_minutes: int = 60,
    w_max: float | None = None,
) -> GaggeReferenceResult:
    if duration_minutes < 1:
        raise ValueError("duration_minutes must be at least 1")

    air_speed = max(v, 0.1)
    vapor_pressure = rh * saturation_vapor_pressure_torr(tdb) / 100.0  # torr

    alfa = 0.1
    body_neutral_c = alfa * SKIN_NEUTRAL_C + (1.0 - alfa) * CORE_NEUTRAL_C

    t_skin = SKIN_NEUTRAL_C
    t_core = CORE_NEUTRAL_C
    m_bl = SKIN_BLOOD_FLOW_NEUTRAL

    e_skin = 0.1 * met  # library initialisation (kept for parity)
    q_sensible = 0.0
    w = 0.0

    pressure_atm = p_atm / 101325.0
    r_clo = 0.155 * clo
    f_a_cl = 1.0 + 0.15 * clo
    lr = 2.2 / pressure_atm  # Lewis ratio, C/torr
    rm = (met - wme) * MET_FACTOR_W_M2
    m = met * MET_FACTOR_W_M2

    i_cl = 0.45 if clo > 0 else 1.0

    if w_max is None:
        w_max = (
            0.59 * air_speed ** -0.08 if clo > 0 else 0.38 * air_speed ** -0.29
        )

    h_cc = 3.0 * pressure_atm ** 0.53
    h_fc = 8.600001 * (air_speed * pressure_atm) ** 0.53
    h_cc = max(h_cc, h_fc)
    if met > 0.85:
        h_cc = max(h_cc, 5.66 * (met - 0.85) ** 0.39)

    h_r = 4.7
    h_t = h_r + h_cc
    r_a = 1.0 / (f_a_cl * h_t)
    t_op = (h_r * tr + h_cc * tdb) / h_t

    q_res = 0.0023 * m * (44.0 - vapor_pressure)
    c_res = 0.0014 * m * (34.0 - tdb)

    radiation_area_ratio = 0.7 if position == "sitting" else 0.73

    points = [
        GaggeReferencePoint(
            minute=0,
            core_temperature_c=t_core,
            skin_temperature_c=t_skin,
            skin_evaporation_w_m2=e_skin,
            sensible_heat_loss_w_m2=q_sensible,
            skin_blood_flow_kg_h_m2=m_bl,
            skin_wettedness=w,
        )
    ]

    for minute in range(1, duration_minutes + 1):
        # Clothing surface temperature with a temperature-dependent h_r.
        t_cl = (r_a * t_skin + r_clo * t_op) / (r_a + r_clo)
        for _ in range(SURFACE_ITERATION_LIMIT):
            h_r = (
                4.0 * CLOTHING_EMISSIVITY * STEFAN_BOLTZMANN
                * ((t_cl + tr) / 2.0 + 273.15) ** 3.0
                * radiation_area_ratio
            )
            h_t = h_r + h_cc
            r_a = 1.0 / (f_a_cl * h_t)
            t_op = (h_r * tr + h_cc * tdb) / h_t
            t_cl_new = (r_a * t_skin + r_clo * t_op) / (r_a + r_clo)
            converged = abs(t_cl_new - t_cl) <= 0.01
            t_cl = t_cl_new
            if converged:
                break
        else:
            raise RuntimeError("Gagge reference: clothing temperature did not converge")

        q_sensible = (t_skin - t_op) / (r_a + r_clo)
        hf_cs = (t_core - t_skin) * (5.28 + 1.163 * m_bl)
        s_core = m - hf_cs - q_res - c_res - wme
        s_skin = hf_cs - q_sensible - e_skin

        tc_sk = BODY_SPECIFIC_HEAT_WH_KGK * alfa * body_mass_kg
        tc_cr = BODY_SPECIFIC_HEAT_WH_KGK * (1.0 - alfa) * body_mass_kg
        t_skin += s_skin * body_surface_area / (tc_sk * 60.0)
        t_core += s_core * body_surface_area / (tc_cr * 60.0)
        t_body = alfa * t_skin + (1.0 - alfa) * t_core

        sk_sig = t_skin - SKIN_NEUTRAL_C
        warm_sk = max(sk_sig, 0.0)
        colds = max(-sk_sig, 0.0)
        c_reg_sig = t_core - CORE_NEUTRAL_C
        c_warm = max(c_reg_sig, 0.0)
        c_cold = max(-c_reg_sig, 0.0)
        warm_b = max(t_body - body_neutral_c, 0.0)

        m_bl = (SKIN_BLOOD_FLOW_NEUTRAL + VASODILATION_COEFFICIENT * c_warm) / (
            1.0 + VASOCONSTRICTION_COEFFICIENT * colds
        )
        m_bl = min(max(m_bl, 0.5), max_skin_blood_flow)

        m_rsw = min(SWEATING_COEFFICIENT * warm_b * exp(warm_sk / 10.7), max_sweating)
        e_rsw = 0.68 * m_rsw

        r_ea = 1.0 / (lr * f_a_cl * h_cc)
        r_ecl = r_clo / (lr * i_cl)
        e_max = (saturation_vapor_pressure_torr(t_skin) - vapor_pressure) / (r_ea + r_ecl)
        if e_max == 0.0:
            e_max = 0.001  # library guard against division by zero

        p_rsw = e_rsw / e_max
        w = 0.06 + 0.94 * p_rsw
        e_diff = w * e_max - e_rsw
        if w > w_max:
            w = w_max
            p_rsw = w_max / 0.94
            e_rsw = p_rsw * e_max
            e_diff = 0.06 * (1.0 - p_rsw) * e_max
        if e_max < 0.0:
            e_diff = 0.0
            e_rsw = 0.0
            w = w_max

        e_skin = e_rsw + e_diff
        met_shivering = 19.4 * colds * c_cold
        m = rm + met_shivering
        alfa = 0.0417737 + 0.7451833 / (m_bl + 0.585417)

        points.append(
            GaggeReferencePoint(
                minute=minute,
                core_temperature_c=t_core,
                skin_temperature_c=t_skin,
                skin_evaporation_w_m2=e_skin,
                sensible_heat_loss_w_m2=q_sensible,
                skin_blood_flow_kg_h_m2=m_bl,
                skin_wettedness=w,
            )
        )

    return GaggeReferenceResult(
        points=points,
        respiratory_heat_loss_w_m2=q_res + c_res,
        maximum_skin_wettedness=w_max,
    )