import { describe, expect, it } from "vitest";

import { mergeBatchProgress, progressRequiresDetailReload } from "@/lib/global-batch-progress";
import type { GlobalBatchDetail, GlobalBatchProgressEvent } from "@/types/global-batch";

const detail = {
  id: "b1",
  status: "running",
  progress: 10,
  completed_city_count: 0,
  failed_city_count: 0,
  cancelled_city_count: 0,
  request: { name: "x" },
  city_results: [
    { id: "c1", status: "running", progress: 10, monthly_results: [{ month: 1 }], checkpoint_months: [1] },
    { id: "c2", status: "queued", progress: 0, monthly_results: null, checkpoint_months: [] },
  ],
} as unknown as GlobalBatchDetail;

const event = {
  batch: { id: "b1", status: "running", progress: 35, completed_city_count: 0, failed_city_count: 0, cancelled_city_count: 0 },
  cities: [
    { id: "c1", status: "running", progress: 70, checkpoint_months: [1, 2, 3], lease_state: "live" },
  ],
} as unknown as GlobalBatchProgressEvent;

describe("mergeBatchProgress", () => {
  it("overlays progress without discarding heavy fields", () => {
    const merged = mergeBatchProgress(detail, event);

    expect(merged.progress).toBe(35);
    expect(merged.request).toEqual({ name: "x" });
    expect(merged.city_results[0].progress).toBe(70);
    expect(merged.city_results[0].checkpoint_months).toEqual([1, 2, 3]);
    expect(merged.city_results[0].monthly_results).toEqual([{ month: 1 }]);
    expect(merged.city_results[1]).toBe(detail.city_results[1]);
  });
});

describe("progressRequiresDetailReload", () => {
  it("reloads when a city reaches a terminal state or the batch finishes", () => {
    expect(progressRequiresDetailReload(null, event)).toBe(true);
    expect(progressRequiresDetailReload(detail, event)).toBe(false);

    const oneDone = { ...event, batch: { ...event.batch, completed_city_count: 1 } };
    expect(progressRequiresDetailReload(detail, oneDone)).toBe(true);

    const finished = { ...event, batch: { ...event.batch, status: "completed" as const} };
    expect(progressRequiresDetailReload(detail, finished)).toBe(true);
  });
});