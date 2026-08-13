import csv
import io
import json

from app.schemas.simulation import (
    WeatherSimulationResponse,
)


def export_result_csv(
    result: WeatherSimulationResponse,
) -> str:
    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow(
        [
            "minute",
            "control_core_temperature_c",
            "control_skin_temperature_c",
            "rc_core_temperature_c",
            "rc_skin_temperature_c",
            "control_convection_w_m2",
            "rc_convection_w_m2",
            "control_longwave_w_m2",
            "rc_longwave_w_m2",
            "control_evaporation_w_m2",
            "rc_evaporation_w_m2",
            "control_absorbed_solar_w_m2",
            "rc_absorbed_solar_w_m2",
        ]
    )

    control_points = (
        result.control.time_series
    )
    rc_points = (
        result.radiative_cooling.time_series
    )

    for control, rc in zip(
        control_points,
        rc_points,
        strict=True,
    ):
        writer.writerow(
            [
                control.minute,
                control.core_temperature_c,
                control.skin_temperature_c,
                rc.core_temperature_c,
                rc.skin_temperature_c,
                control.convection_w_m2,
                rc.convection_w_m2,
                control.longwave_radiation_w_m2,
                rc.longwave_radiation_w_m2,
                control.evaporation_w_m2,
                rc.evaporation_w_m2,
                control.absorbed_solar_w_m2,
                rc.absorbed_solar_w_m2,
            ]
        )

    return output.getvalue()


def export_result_json(
    result: WeatherSimulationResponse,
) -> str:
    return json.dumps(
        result.model_dump(mode="json"),
        ensure_ascii=False,
        indent=2,
    )