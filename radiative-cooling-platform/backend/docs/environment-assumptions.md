# Environment assumptions

ERA5 (via Open-Meteo) supplies air temperature, RH, 10 m wind and GHI.
Everything else the two-node model needs is derived by
`app/services/environment_model.py` using `EnvironmentAssumptions`, which is
part of every weather-driven request and echoed in every response.

| field | default | what it controls | status |
|---|---|---|---|
| mean_radiant_temperature_method | air_plus_solar_linear | T_mrt = T_air + min(cap, gain·GHI) | assumed (Stage 1 prototype) |
| solar_mrt_gain_k_per_w_m2 / solar_mrt_gain_cap_k | 0.012 / 15 | slope and cap above | assumed |
| sky_temperature_method | humidity_offset | T_sky = T_air − (5 + 10·(1−RH)) | assumed |
| sky_temperature_method = swinbank | — | clear-sky T_sky = 0.0552·T_air[K]^1.5 (Swinbank 1963) | literature |
| sky_view_factor | 0.5 | share of view occupied by sky | assumed; open site |
| wind_speed_scaling_factor | 1.0 | 10 m → body height | assumed; 0.67 ≈ log profile to 1.1 m |
| ground_albedo | 0.2 | reflected-diffuse shortwave term (ADR 0006) | assumed |

What these do **not** represent: cloud-cover dependent sky emissivity, 
ground surface temperature, urban canyon geometry, solar-altitude dependent f_p
(the solar term uses GHI only).

Selective emitters (infrared_emissivity_window set, ADR 0007): the sky is split
into the 8-13 um window, whose emissivity is back-calculated from T_sky above,
and the rest of the spectrum, treated as a blackbody at T_air. The non-sky part
of the view is a blackbody at T_mrt in every band. With the default
air_plus_solar_linear rule, T_mrt can exceed T_air by up to 15 K, which favours
low out-of-window emissivity; repeat key results with equal_to_air.

# ADR 0008: physical sky and ground temperatures

## Context
Since Stage 5 the body-incident shortwave (beam, sky diffuse, ground reflected)
is computed explicitly. The legacy rule T_mrt = T_air + min(15 K, 0.012 GHI)
still raises the longwave temperature of the non-sky view with GHI, so the
sun is counted twice and the surroundings act as a hot longwave source.
Stage 10 experiment G was designed to expose the consequence: optimizers
favour low (out-of-window) emissivity in Dubai.

## Decision
New, opt-in methods using ERA5 variables available from Open-Meteo:
- sky_temperature_method = brutsaert_cloud:
  eps = c + (1 - c) 1.24 (e_a[hPa]/T_a[K])^(1/7), T_sky = eps^(1/4) T_a,
  c = ERA5 total cloud cover. Consistent with ADR 0007: overcast -> T_sky = T_air.
- mean_radiant_temperature_method = ground_energy_balance: the non-sky view is
  the ground surface at the root of
  (1 - rho_g) GHI + eps_g sigma T_sky^4 = eps_g sigma T_g^4 + h_g (T_g - T_a) + K (T_g - T_soil),
  h_g = 2.8 + 3.0 v (Watmuff 1977), T_soil = ERA5 0-7 cm layer.
- Extra Open-Meteo variables are requested only when these methods are active;
  default requests, caches and payload hashes are byte-identical.
- Time series record the sky and surroundings temperatures used.

## Consequences
- MODEL_PARAMETER_SET_VERSION 6.0.0 (4 constants), MODEL_VERSION 0.9.0.
  Default trajectories unchanged; fingerprints and checkpoint request hashes change.
- Defaults are NOT switched. Switching is a Stage 12 decision gated by experiment K.

## Limitations
- Steady ground balance: no thermal inertia beyond the 0-7 cm layer, so the
  afternoon peak is reached too early and the evening ground is too cool.
- K (surface-soil conductance) is assumed; experiment K4 quantifies its effect.
- Horizontal open ground only; walls, shading and urban canyons are not modelled.
- Using ERA5 total cloud cover as the Crawford-Duchon cloud fraction is an approximation.