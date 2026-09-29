# Stage 3 golden refresh (Dubai 2023-07-15 12:00, 2 h)

Causes (all intentional, see ADR 0001-0003):
1. Heat capacities 280 -> 135.7 kJ/(m^2 K) (70 kg / 1.8 m^2). Transients are
   roughly twice as fast; the 2 h case is closer to steady state.
2. Explicit clothing surface temperature with f_cl = 1 + 0.15 clo replaces the
   linearised coupling factor.
3. Gagge 1986 controllers replace the prototype's linear gains.

| metric | before (2.0.0) | after (3.0.0) | delta |
|---|---|---|---|
| final_skin_temperature_improvement_c | 0.7846 | <fill> | |
| final_core_temperature_improvement_c | 0.1362 | <fill> | |
| average_skin_temperature_improvement_c | 0.43 | <fill> | |

model_parameter_set_sha256: ebc0c642... -> <fill>
Gagge benchmark (default fixture, 60 min): core max|dT| = <fill> C, skin max|dT| = <fill> C
Reference port parity (60 min, 70 kg): max|dT| = <fill> C