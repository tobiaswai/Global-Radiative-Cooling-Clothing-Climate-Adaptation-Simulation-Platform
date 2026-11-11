import type { LeaseState } from "@/types/global-batch";

/** "just now", "3 min ago", "2 h ago", "5 d ago". Future values say "in …". */
export function formatRelativeTime(value: string | null | undefined, now = new Date()): string {
  if (!value) return "—";

  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;

  const seconds = Math.round((now.getTime() - date.getTime()) / 1000);
  const abs = Math.abs(seconds);
  const suffix = seconds < 0 ? (text: string) => `in ${text}` : (text: string) => `${text} ago`;

  if (abs < 45) return seconds < 0 ? "in a few seconds" : "just now";
  if (abs < 90) return suffix("1 min");
  if (abs < 3600) return suffix(`${Math.round(abs / 60)} min`);
  if (abs < 86400) return suffix(`${Math.round(abs / 3600)} h`);
  return suffix(`${Math.round(abs / 86400)} d`);
}

export type HeartbeatHealth = "none" | "healthy" | "stale" | "expired";

/**
 * Combines the server-derived lease state with the heartbeat age so the UI
 * can warn before the lease actually expires.
 */
export function heartbeatHealth(
  leaseState: LeaseState | undefined,
  lastHeartbeatAt: string | null | undefined,
  heartbeatIntervalSeconds: number,
  now = new Date(),
): HeartbeatHealth {
  if (!leaseState || leaseState === "none") return "none";
  if (leaseState === "expired") return "expired";
  if (!lastHeartbeatAt) return "stale";

  const age = (now.getTime() - new Date(lastHeartbeatAt).getTime()) / 1000;
  return age > heartbeatIntervalSeconds * 2 ? "stale" : "healthy";
}

/** "host:pid:task-id" -> "host · 1a2b3c" for compact display. */
export function shortOwner(owner: string | null | undefined): string {
  if (!owner) return "—";
  const parts = owner.split(":");
  const host = parts[0] ?? owner;
  const tail = parts.at(-1) ?? "";
  return tail && tail !== host ? `${host} · ${tail.slice(0, 6)}` : host;
}