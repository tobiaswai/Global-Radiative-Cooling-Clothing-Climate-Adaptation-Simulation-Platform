import { describe, expect, it } from "vitest";

import { formatNumber, formatSignedNumber } from "@/lib/format";

describe("formatNumber", () => {
  it("renders an em dash for missing or non-finite values", () => {
    expect(formatNumber(null)).toBe("—");
    expect(formatNumber(undefined)).toBe("—");
    expect(formatNumber(Number.NaN)).toBe("—");
    expect(formatNumber(Number.POSITIVE_INFINITY)).toBe("—");
  });

  it("applies digits and unit", () => {
    expect(formatNumber(1.23456, 3, " °C")).toBe("1.235 °C");
    expect(formatNumber(2)).toBe("2.00");
  });
});

describe("formatSignedNumber", () => {
  it("prefixes positive values only", () => {
    expect(formatSignedNumber(0.5, 1)).toBe("+0.5");
    expect(formatSignedNumber(-0.5, 1)).toBe("-0.5");
    expect(formatSignedNumber(0, 1)).toBe("0.0");
  });
});