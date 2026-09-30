# Stage 5 golden refresh (Dubai 2023-07-15 12:00, 2 h)

Causes (all intentional, ADR 0005-0006):
1. Absorbed solar is a source term in the clothing surface balance; the
   0.35 skin fraction is gone. Expect less solar heat reaching the skin for
   the control garment (dark, alpha = 0.6) at 5-6 m/s wind.
2. Body-incident shortwave uses the ERA5 beam/diffuse split with f_p on DNI,
   sky-diffuse and ground-reflected terms (albedo 0.2). At Dubai noon the
   incident irradiance rises from ~225 to ~280 W/m^2 (per A_D).
3. Registry key rename (effective_radiation_area_ratio -> _standing) and two
   new constants change the fingerprint even where values are unchanged.

| metric | before (3.0.0) | after (4.0.0) | delta |
|---|---|---|---|
| final_skin_temperature_improvement_c | 1.7815 | <fill> | |
| final_core_temperature_improvement_c | 1.6117 | <fill> | |
| average_skin_temperature_improvement_c | 1.0721 | <fill> | |

model_parameter_set_sha256: 5e0cbe09... -> <fill>
parameter_fingerprint: 40799058... -> <fill>
Gagge benchmark (default fixture, 60 min): unchanged (solar = 0 in the benchmark).