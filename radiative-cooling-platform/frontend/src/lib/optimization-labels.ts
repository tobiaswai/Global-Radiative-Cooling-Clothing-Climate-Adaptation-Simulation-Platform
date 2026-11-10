import type { DecisionVariableName, MetricName } from "@/types/optimization";

export const VARIABLE_LABELS: Record<DecisionVariableName, string> = {
  solar_reflectance: "Solar reflectance ρ",
  solar_transmittance: "Solar transmittance τ_sol",
  infrared_emissivity: "IR emissivity ε",
  infrared_transmittance: "IR transmittance τ_IR",
  clothing_insulation_clo: "Insulation (clo)",
  evaporative_resistance_m2pa_w: "Re,cl (m²·Pa/W)",
};

export const METRIC_LABELS: Record<MetricName, string> = {
  mean_skin_temperature_c: "Mean skin temperature (°C)",
  peak_skin_temperature_c: "Peak skin temperature (°C)",
  peak_core_temperature_c: "Peak core temperature (°C)",
  skin_exceedance_fraction: "Time fraction T_sk > threshold",
  core_exceedance_fraction: "Time fraction T_core > threshold",
  mean_skin_cooling_c: "Mean skin cooling vs control (°C)",
  mean_core_cooling_c: "Mean core cooling vs control (°C)",
};

export const METRIC_OPTIONS = (Object.keys(METRIC_LABELS) as MetricName[]).map((value) => ({
  value,
  label: METRIC_LABELS[value],
}));

export const TERMINAL_OPTIMIZATION = new Set(["completed", "failed", "cancelled"]);