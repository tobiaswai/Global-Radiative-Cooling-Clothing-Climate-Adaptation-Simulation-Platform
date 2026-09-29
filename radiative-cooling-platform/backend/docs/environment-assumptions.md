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

What these do **not** represent: cloud-cover dependent sky emissivity,
ground surface temperature, urban canyon geometry, direct/diffuse split
(the solar term uses GHI only).