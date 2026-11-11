import type { TimeSeriesPoint } from "@/types/simulation";

/** Series that may be null on the wire or absent on pre-Stage-3 results. */
export type OptionalSeriesKey =
  | "maximum_evaporation_w_m2"
  | "skin_wettedness"
  | "clothing_surface_temperature_c"
  | "skin_blood_flow_kg_h_m2"
  | "solar_incident_w_m2"
  | "solar_absorbed_by_textile_w_m2"
  | "solar_transmitted_w_m2";

export function hasOptionalSeries(
  points: TimeSeriesPoint[],
  key: OptionalSeriesKey,
): boolean {
  return points.some((point) => typeof point[key] === "number");
}

export function pluckOptionalSeries(
  points: TimeSeriesPoint[],
  key: OptionalSeriesKey,
): Array<number | null> {
  return points.map((point) => {
    const value = point[key];

    return typeof value === "number" && Number.isFinite(value) ? value : null;
  });
}