# ADR 0002: adopt the Gagge (1986) thermoregulatory controllers

Context: the prototype used separate linear gains for sweating and skin blood
flow (170/200 g/(h m^2 K), 75/20 kg/(h m^2 K)) marked `assumed`. A transient
comparison with the reference cannot separate controller differences from
clothing/radiation differences while these remain arbitrary.

Decision: use the controllers of Gagge, Fobelets & Berglund (1986) as
implemented in the ASHRAE 55 SET reference procedure:
- m_rsw = 170 * WSIG_body * exp(WSIG_sk / 10.7), <= 500 g/(h m^2)
- SKBF  = (6.3 + 120 * WSIG_cr) / (1 + 0.5 * CSIG_sk), clamped [0.5, 90]
- w     = min(0.06 + 0.94 E_rsw / E_max, w_max), w_max = 0.59 v^-0.08 (clothed)
- M_shiv = 19.4 * CSIG_sk * CSIG_cr
All constants are `literature`. The platform's contribution is the clothing
optical/radiative model, not thermoregulation.

Known difference kept: when w is capped, the reference sets
E_skin = (0.06 + w_max) E_max; the prototype uses E_skin = w_max E_max.