import type {
  DecisionVariableName,
  DemandDirection,
  MetricName,
  ObjectiveName,
  ObjectiveTrend,
  OptimizationCreate,
  Sense,
} from "@/types/optimization";

export const VARIABLE_LABELS: Record<DecisionVariableName, string> = {
  solar_reflectance: "Solar reflectance ρ",
  solar_transmittance: "Solar transmittance τ_sol",
  infrared_emissivity: "IR emissivity ε (gray)",
  infrared_emissivity_window: "IR emissivity ε_W (8–13 µm)",
  infrared_emissivity_outside_window: "IR emissivity ε_N (outside window)",
  infrared_transmittance: "IR transmittance τ_IR",
  clothing_insulation_clo: "Insulation (clo)",
  evaporative_resistance_m2pa_w: "Re,cl (m²·Pa/W)",
  infrared_emissivity_ground_facing: "IR emissivity ε_g (ground-facing)",
};

/** Mirrors DEFAULT_DEMAND_DIRECTION in app/schemas/optimization.py. */
export const DEFAULT_DEMAND_DIRECTION: Record<DecisionVariableName, DemandDirection> = {
  solar_reflectance: "increasing",
  solar_transmittance: "decreasing",
  infrared_emissivity: "increasing",
  infrared_emissivity_window: "increasing",
  infrared_emissivity_outside_window: "decreasing",
  infrared_transmittance: "increasing",
  clothing_insulation_clo: "decreasing",
  evaporative_resistance_m2pa_w: "decreasing",
  infrared_emissivity_ground_facing: "decreasing",
};

export const EMISSIVITY_BAND_VARIABLES = new Set<DecisionVariableName>([
  "infrared_emissivity_window",
  "infrared_emissivity_outside_window",
]);

export const METRIC_LABELS: Record<MetricName, string> = {
  mean_skin_temperature_c: "Mean skin temperature (°C)",
  peak_skin_temperature_c: "Peak skin temperature (°C)",
  peak_core_temperature_c: "Peak core temperature (°C)",
  skin_exceedance_fraction: "Time fraction T_sk > threshold",
  core_exceedance_fraction: "Time fraction T_core > threshold",
  skin_excess_degree_hours: "Skin excess above threshold (°C·h)",
  core_excess_degree_hours: "Core excess above threshold (°C·h)",
  mean_skin_cooling_c: "Mean skin cooling vs control (°C)",
  mean_core_cooling_c: "Mean core cooling vs control (°C)",
};

export const OBJECTIVE_LABELS: Record<ObjectiveName, string> = {
  ...METRIC_LABELS,
  material_demand: "Material demand (0 = least demanding)",
};

/** Mirrors METRIC_SCALES in app/services/optimization/objective.py. */
export const METRIC_SCALES: Record<ObjectiveName, number> = {
  mean_skin_temperature_c: 1,
  peak_skin_temperature_c: 1,
  peak_core_temperature_c: 1,
  skin_exceedance_fraction: 0.1,
  core_exceedance_fraction: 0.1,
  skin_excess_degree_hours: 0.5,
  core_excess_degree_hours: 0.5,
  mean_skin_cooling_c: 1,
  mean_core_cooling_c: 1,
  material_demand: 0.1,
};

export const METRIC_OPTIONS = (Object.keys(METRIC_LABELS) as MetricName[]).map((value) => ({
  value,
  label: METRIC_LABELS[value],
}));

export const OBJECTIVE_OPTIONS = (Object.keys(OBJECTIVE_LABELS) as ObjectiveName[]).map((value) => ({
  value,
  label: OBJECTIVE_LABELS[value],
}));

export const TREND_LABELS: Record<ObjectiveTrend, string> = {
  improves: "improves as it becomes more demanding",
  worsens: "worsens as it becomes more demanding",
  flat: "flat",
  mixed: "non-monotone",
};

/** Same rule as requirement_map.map_metric on the backend. */
export function mapMetricFor(request: OptimizationCreate): { metric: MetricName; sense: Sense } {
  if (request.objective.metric !== "material_demand") {
    return { metric: request.objective.metric, sense: request.objective.sense };
  }
  const first = request.constraints[0];
  if (first) return { metric: first.metric, sense: first.operator === "<=" ? "minimize" : "maximize" };
  return { metric: "skin_excess_degree_hours", sense: "minimize" };
}

export const TERMINAL_OPTIMIZATION = new Set(["completed", "failed", "cancelled"]);