from pythermalcomfort.models import two_nodes_gagge

from app.schemas.simulation import (
    GaggeBenchmarkRequest,
    GaggeBenchmarkResponse,
    GaggeModelOutput,
    PrototypeBenchmarkOutput,
)
from app.services.two_node import simulate_material


def _to_float(value: object) -> float:
    """
    將 Python float、NumPy scalar 或單元素陣列轉為 float。
    """

    if hasattr(value, "item"):
        return float(value.item())

    return float(value)


def run_gagge_benchmark(
    request: GaggeBenchmarkRequest,
) -> GaggeBenchmarkResponse:
    """
    將自研原型與 pythermalcomfort Gagge Two-Node 比較。

    注意：
    Gagge 的標準接口不直接處理材料太陽光譜屬性，
    因此基準情景會把太陽輻射設為零。
    """

    benchmark_environment = (
        request.environment.model_copy(
            update={
                "solar_radiation_w_m2": 0.0,
            }
        )
    )

    prototype_result = simulate_material(
        duration_minutes=request.duration_minutes,
        output_interval_minutes=1,
        environment=benchmark_environment,
        person=request.person,
        material=request.material,
    )

    gagge_result = two_nodes_gagge(
        tdb=benchmark_environment.air_temperature_c,
        tr=(
            benchmark_environment
            .mean_radiant_temperature_c
        ),
        v=max(
            benchmark_environment.wind_speed_m_s,
            0.01,
        ),
        rh=(
            benchmark_environment
            .relative_humidity_percent
        ),
        met=request.person.met,
        clo=request.material.clothing_insulation_clo,
        wme=0,
        body_surface_area=(
            request.person.body_surface_area_m2
        ),
        p_atm=101325,
        position="standing",
        max_skin_blood_flow=90,
        max_sweating=500,
        round_output=False,
    )

    prototype_final_point = (
        prototype_result.time_series[-1]
    )

    gagge_core_temperature = _to_float(
        gagge_result.t_core
    )
    gagge_skin_temperature = _to_float(
        gagge_result.t_skin
    )

    return GaggeBenchmarkResponse(
        reference_model="Gagge Two-Node",
        reference_library="pythermalcomfort",
        environment_note=(
            "為確保模型邊界條件可比較，"
            "基準計算已將直接太陽輻射設為 0 W/m²。"
        ),
        prototype=PrototypeBenchmarkOutput(
            core_temperature_c=(
                prototype_result
                .final_core_temperature_c
            ),
            skin_temperature_c=(
                prototype_result
                .final_skin_temperature_c
            ),
            evaporation_w_m2=(
                prototype_final_point
                .evaporation_w_m2
            ),
            energy_residual_percent=(
                prototype_result
                .diagnostics
                .normalized_residual_percent
            ),
        ),
        gagge=GaggeModelOutput(
            core_temperature_c=(
                gagge_core_temperature
            ),
            skin_temperature_c=(
                gagge_skin_temperature
            ),
            skin_evaporation_w_m2=_to_float(
                gagge_result.e_skin
            ),
            skin_heat_loss_w_m2=_to_float(
                gagge_result.q_skin
            ),
            respiratory_heat_loss_w_m2=_to_float(
                gagge_result.q_res
            ),
            skin_blood_flow_kg_h_m2=_to_float(
                gagge_result.m_bl
            ),
            skin_wettedness=_to_float(
                gagge_result.w
            ),
            standard_effective_temperature_c=(
                _to_float(gagge_result.set)
            ),
        ),
        difference_core_temperature_c=round(
            prototype_result
            .final_core_temperature_c
            - gagge_core_temperature,
            4,
        ),
        difference_skin_temperature_c=round(
            prototype_result
            .final_skin_temperature_c
            - gagge_skin_temperature,
            4,
        ),
        warning=(
            "This is a model diagnostic comparison, not an equivalence verification."
            "The heat capacity of the self-developed prototype differs from that of the Gagge model."
            "The clothing model, blood flow control, and evaporation control equations are different."
        ),
    )