# Stage 10 golden refresh (Dubai 2023-07-15 12:00, 2 h)

Causes: four registry constants added (second_radiation_constant,
atmospheric_window_lower/upper_um, emissivity_reference_temperature);
MODEL_VERSION 0.7.0 -> 0.8.0. Both fixture garments are gray, so the selective
path is not exercised.

| metric | before (0.7.0) | after (0.8.0) | delta |
|---|---|---|---|
| final_skin_temperature_improvement_c | 2.1232 | <fill> | must be 0 |
| final_core_temperature_improvement_c | 1.9117 | <fill> | must be 0 |
| average_skin_temperature_improvement_c | 1.2876 | <fill> | must be 0 |

model_parameter_set_sha256: cab48ac8... -> <fill>
parameter_fingerprint: 10003d40... -> <fill>