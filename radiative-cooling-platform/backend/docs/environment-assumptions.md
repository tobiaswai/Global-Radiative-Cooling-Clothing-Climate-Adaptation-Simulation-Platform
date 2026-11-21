# Environment assumptions (Stage 12 defaults, ADR 0009)

ERA5 via Open-Meteo supplies air temperature, RH, 10 m wind, GHI, DNI, DHI and,
for the default physical environment, total cloud cover and 0-7 cm soil temperature.
`app/services/environment_model.py` derives the remaining boundary conditions from
`EnvironmentAssumptions`, which is stored with every request and echoed in every result.

| field | default | controls | status |
|---|---|---|---|
| mean_radiant_temperature_method | ground_energy_balance | non-sky longwave temperature = ground surface balance | ADR 0008 |
| sky_temperature_method | brutsaert_cloud | T_sky from Brutsaert + ERA5 cloud cover | ADR 0008 |
| ground_emissivity | 0.95 | ground longwave emissivity | assumed |
| ground_soil_conductance_w_m2k | 15 | surface - 0-7 cm soil coupling | assumed |
| ground_albedo | 0.2 | reflected shortwave on body and ground absorption | assumed |
| sky_view_factor | 0.5 | sky share of the view; zone areas of two-zone garments | assumed |
| zone_view_separation | 0.5 | hemisphere separation of two-zone garments | assumed (ADR 0010) |
| wind_speed_scaling_factor | 1.0 | 10 m wind -> body height | assumed |
| radiation_time_convention | instantaneous_linear | hourly irradiance interpolation | approximation |

Presets: `open_ground_physical` (default) and `legacy_stage1`
(air_plus_solar_linear + humidity_offset). Requests stored without
`environment_assumptions` are loaded as `legacy_stage1`.

Walking (Stage 13, ADR 0012) changes the relative air speed at the body only;
the ground balance keeps using the ambient wind.

Not represented: urban canyons and shading, ground thermal inertia below 0-7 cm,
measured downwelling longwave, angle-dependent projected area factor.