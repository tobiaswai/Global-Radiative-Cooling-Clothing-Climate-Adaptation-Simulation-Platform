import { describe, expect, it } from "vitest";

import { formatRelativeTime, heartbeatHealth, shortOwner } from "@/lib/relative-time";

const NOW = new Date("2026-01-01T12:00:00Z");

describe("formatRelativeTime", () => {
  it("handles missing and invalid input", () => {
    expect(formatRelativeTime(null, NOW)).toBe("—");
    expect(formatRelativeTime("nope", NOW)).toBe("nope");
  });

  it("scales units", () => {
    expect(formatRelativeTime("2026-01-01T11:59:50Z", NOW)).toBe("just now");
    expect(formatRelativeTime("2026-01-01T11:58:00Z", NOW)).toBe("2 min ago");
    expect(formatRelativeTime("2026-01-01T09:00:00Z", NOW)).toBe("3 h ago");
    expect(formatRelativeTime("2025-12-29T12:00:00Z", NOW)).toBe("3 d ago");
    expect(formatRelativeTime("2026-01-01T12:05:00Z", NOW)).toBe("in 5 min");
  });
});

describe("heartbeatHealth", () => {
  it("is none without a lease and expired when the server says so", () => {
    expect(heartbeatHealth("none", "2026-01-01T11:59:59Z", 30, NOW)).toBe("none");
    expect(heartbeatHealth(undefined, null, 30, NOW)).toBe("none");
    expect(heartbeatHealth("expired", "2026-01-01T11:59:59Z", 30, NOW)).toBe("expired");
  });

  it("flags a live lease whose heartbeat is older than two intervals", () => {
    expect(heartbeatHealth("live", "2026-01-01T11:59:40Z", 30, NOW)).toBe("healthy");
    expect(heartbeatHealth("live", "2026-01-01T11:58:00Z", 30, NOW)).toBe("stale");
    expect(heartbeatHealth("live", null, 30, NOW)).toBe("stale");
  });
});

describe("shortOwner", () => {
  it("compacts host:pid:task", () => {
    expect(shortOwner("worker-a:4242:0f1e2d3c4b5a")).toBe("worker-a · 0f1e2d");
    expect(shortOwner("single")).toBe("single");
    expect(shortOwner(null)).toBe("—");
  });
});