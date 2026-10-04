import type {
  GlobalBatchDetail,
  GlobalBatchProgressEvent,
} from "@/types/global-batch";

export const TERMINAL_BATCH_STATUSES = new Set<string>([
  "completed",
  "partial_completed",
  "failed",
  "cancelled",
]);

export function isTerminalBatchStatus(status: string): boolean {
  return TERMINAL_BATCH_STATUSES.has(status);
}

/** Overlay a lightweight SSE snapshot onto the full detail without touching
 *  monthly results or analytics (those arrive via a detail reload). */
export function mergeBatchProgress(
  detail: GlobalBatchDetail,
  event: GlobalBatchProgressEvent,
): GlobalBatchDetail {
  const byId = new Map(event.cities.map((city) => [city.id, city]));

  return {
    ...detail,
    ...event.batch,
    request: detail.request,
    city_results: detail.city_results.map((city) => {
      const progress = byId.get(city.id);
      return progress ? { ...city, ...progress } : city;
    }),
  };
}

/** A full reload is needed when heavy fields (analytics, monthly results)
 *  may have changed: a city reached a terminal state or the batch did. */
export function progressRequiresDetailReload(
  previous: GlobalBatchDetail | null,
  event: GlobalBatchProgressEvent,
): boolean {
  if (!previous) return true;

  const processedBefore =
    previous.completed_city_count + previous.failed_city_count + previous.cancelled_city_count;
  const processedNow =
    event.batch.completed_city_count +
    event.batch.failed_city_count +
    event.batch.cancelled_city_count;

  return processedNow !== processedBefore || isTerminalBatchStatus(event.batch.status);
}