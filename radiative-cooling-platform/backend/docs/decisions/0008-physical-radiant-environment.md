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