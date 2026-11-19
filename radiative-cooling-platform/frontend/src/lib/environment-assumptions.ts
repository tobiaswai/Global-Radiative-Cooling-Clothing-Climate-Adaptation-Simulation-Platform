import type { EnvironmentAssumptions } from "@/types/simulation";

/** Mirrors the backend defaults (ADR 0009): open-ground physical environment. */
export const DEFAULT_ENVIRONMENT_ASSUMPTIONS: EnvironmentAssumptions = {
  mean_radiant_temperature_method: "ground_energy_balance",
  solar_mrt_gain_k_per_w_m2: 0.012,
  solar_mrt_gain_cap_k: 15,
  sky_temperature_method: "brutsaert_cloud",
  sky_offset_base_k: 5,
  sky_offset_humidity_range_k: 10,
  fixed_sky_offset_k: 15,
  sky_view_factor: 0.5,
  wind_speed_scaling_factor: 1,
  ground_albedo: 0.2,
  radiation_time_convention: "instantaneous_linear",
  ground_emissivity: 0.95,
  ground_soil_conductance_w_m2k: 15,
  zone_view_separation: 0.5,
};

export type EnvironmentPresetName = "open_ground_physical" | "legacy_stage1";

/** Mirrors ENVIRONMENT_PRESETS in app/schemas/environment.py. */
export const ENVIRONMENT_PRESETS: Record<
  EnvironmentPresetName,
  { label: string; overrides: Partial<EnvironmentAssumptions> }
> = {
  open_ground_physical: { label: "Open ground, physical sky and ground (default)", overrides: {} },
  legacy_stage1: {
    label: "Legacy Stage 1 proxies (reproduces stored results)",
    overrides: {
      mean_radiant_temperature_method: "air_plus_solar_linear",
      sky_temperature_method: "humidity_offset",
    },
  },
};

export function presetAssumptions(name: EnvironmentPresetName): EnvironmentAssumptions {
  return { ...DEFAULT_ENVIRONMENT_ASSUMPTIONS, ...ENVIRONMENT_PRESETS[name].overrides };
}

export function matchPreset(value: EnvironmentAssumptions): EnvironmentPresetName | "custom" {
  for (const name of Object.keys(ENVIRONMENT_PRESETS) as EnvironmentPresetName[]) {
    const preset = presetAssumptions(name);
    const keys = Object.keys(preset) as (keyof EnvironmentAssumptions)[];
    if (keys.every((key) => preset[key] === value[key])) return name;
  }
  return "custom";
}