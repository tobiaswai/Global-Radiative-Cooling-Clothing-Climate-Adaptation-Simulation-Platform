export function formatNumber(
  value: number | null | undefined,
  digits = 2,
  unit = "",
): string {
  if (typeof value !== "number" || !Number.isFinite(value)) {
    return "—";
  }

  return `${value.toFixed(digits)}${unit}`;
}

export function formatSignedNumber(
  value: number | null | undefined,
  digits = 2,
  unit = "",
): string {
  if (typeof value !== "number" || !Number.isFinite(value)) {
    return "—";
  }

  const sign = value > 0 ? "+" : "";

  return `${sign}${value.toFixed(digits)}${unit}`;
}