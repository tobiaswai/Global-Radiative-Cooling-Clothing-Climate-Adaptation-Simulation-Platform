/**
 * Planck band fractions, mirroring app/services/planck.py (Stage 10, ADR 0007).
 * Constants mirror the backend registry; keep them in sync.
 */
export const SECOND_RADIATION_CONSTANT = 14387.768775; // um K
export const WINDOW_LOWER_UM = 8;
export const WINDOW_UPPER_UM = 13;
export const EMISSIVITY_REFERENCE_K = 305;

const NORMALIZATION = 15 / Math.PI ** 4;

function lowerIntegral(z: number): number {
  const z2 = z * z;
  return z ** 3 * (1 / 3 - z / 8 + z2 / 60 - z2 ** 2 / 5040 + z2 ** 3 / 272160 - z2 ** 4 / 13305600);
}

function upperIntegral(z: number): number {
  let total = 0;
  for (let n = 1; n <= 60; n += 1) {
    const term = (Math.exp(-n * z) / n) * (z ** 3 + (3 * z ** 2) / n + (6 * z) / n ** 2 + 6 / n ** 3);
    total += term;
    if (term <= 1e-16 * total) break;
  }
  return total;
}

export function blackbodyFraction(lambdaT: number): number {
  if (lambdaT <= 0) return 0;
  const z = SECOND_RADIATION_CONSTANT / lambdaT;
  if (z < 1) return Math.max(0, 1 - NORMALIZATION * lowerIntegral(z));
  if (z > 700) return 0;
  return Math.min(1, NORMALIZATION * upperIntegral(z));
}

export function bandFraction(temperatureK = EMISSIVITY_REFERENCE_K): number {
  return blackbodyFraction(WINDOW_UPPER_UM * temperatureK) - blackbodyFraction(WINDOW_LOWER_UM * temperatureK);
}

export function outsideWindowEmissivity(broadband: number, windowValue: number): number {
  const fw = bandFraction();
  return (broadband - fw * windowValue) / (1 - fw);
}

export function broadbandEmissivity(windowValue: number, outside: number): number {
  const fw = bandFraction();
  return fw * windowValue + (1 - fw) * outside;
}

export type SpectralCheck = { outside: number; error: string | null };

/** Same rule as the backend validator _check_spectral_emissivity. */
export function checkSpectralEmissivity(
  broadband: number,
  windowValue: number,
  transmittance: number,
): SpectralCheck {
  const outside = outsideWindowEmissivity(broadband, windowValue);
  if (windowValue + transmittance > 1 + 1e-6) {
    return { outside, error: "ε_W + τ_IR must not exceed 1." };
  }
  if (outside < -1e-6 || outside + transmittance > 1 + 1e-6) {
    return {
      outside,
      error: `Broadband ε and ε_W imply an out-of-window emissivity of ${outside.toFixed(3)}, outside [0, 1 − τ_IR].`,
    };
  }
  return { outside, error: null };
}