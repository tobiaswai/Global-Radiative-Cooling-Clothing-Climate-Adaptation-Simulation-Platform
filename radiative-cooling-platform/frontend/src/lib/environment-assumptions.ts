import type { EnvironmentAssumptions } from "@/types/simulation";

/** Mirrors the backend defaults (GET /api/v1/model/environment-assumptions/defaults). */
export const DEFAULT_ENVIRONMENT_ASSUMPTIONS: EnvironmentAssumptions = {
  mean_radiant_temperature_method: "air_plus_solar_linear",
  solar_mrt_gain_k_per_w_m2: 0.012,
  solar_mrt_gain_cap_k: 15,
  sky_temperature_method: "humidity_offset",
  sky_offset_base_k: 5,
  sky_offset_humidity_range_k: 10,
  fixed_sky_offset_k: 15,
  sky_view_factor: 0.5,
  wind_speed_scaling_factor: 1,
  ground_albedo: 0.2,
};