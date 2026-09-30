import csv
import io
import json
from typing import Any

from app.schemas.simulation import WeatherSimulationResponse


CSV_HEADERS = [
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
    # Stage 2 / 3 diagnostics; blank for results stored before they existed.
    "control_maximum_evaporation_w_m2",
    "rc_maximum_evaporation_w_m2",
    "control_skin_wettedness",
    "rc_skin_wettedness",
    "control_clothing_surface_temperature_c",
    "rc_clothing_surface_temperature_c",
    # Stage 5
    "control_solar_incident_w_m2",
    "rc_solar_incident_w_m2",
]


def _optional(point: Any, name: str) -> Any:
    value = getattr(point, name, None)
    return "" if value is None else value


def export_result_csv(result: WeatherSimulationResponse) -> str:
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(CSV_HEADERS)

    for control, rc in zip(
        result.control.time_series,
        result.radiative_cooling.time_series,
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
                _optional(control, "maximum_evaporation_w_m2"),
                _optional(rc, "maximum_evaporation_w_m2"),
                _optional(control, "skin_wettedness"),
                _optional(rc, "skin_wettedness"),
                _optional(control, "clothing_surface_temperature_c"),
                _optional(rc, "clothing_surface_temperature_c"),
                _optional(control, "solar_incident_w_m2"),
                _optional(rc, "solar_incident_w_m2"),
            ]
        )

    return output.getvalue()


def export_result_json(result: WeatherSimulationResponse) -> str:
    return json.dumps(result.model_dump(mode="json"), ensure_ascii=False, indent=2)