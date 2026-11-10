"use client";

import { useCallback, useEffect, useRef, useState } from "react";

import {
  cancelSimulationJob,
  getSimulationEventsUrl,
  getSimulationJob,
  getSimulationResult,
} from "@/lib/api-client";
import type { SimulationJob, WeatherSimulationResponse } from "@/types/simulation";

export type JobTransport = "sse" | "polling" | "idle";

const TERMINAL = new Set<SimulationJob["status"]>(["completed", "failed", "cancelled"]);
const POLL_MS = 3000;
const POLL_ON_ERROR_MS = 5000;

export function isTerminalJobStatus(status: string): boolean {
  return TERMINAL.has(status as SimulationJob["status"]);
}

/** Same reliability pattern as useGlobalBatch: load, stream, fall back to
 *  polling, stop at a terminal status, ignore stale snapshots. */
export function useSimulationJob(jobId: string) {
  const [job, setJob] = useState<SimulationJob | null>(null);
  const [result, setResult] = useState<WeatherSimulationResponse | null>(null);
  const [error, setError] = useState("");
  const [resultError, setResultError] = useState("");
  const [transport, setTransport] = useState<JobTransport>("idle");
  const [revision, setRevision] = useState(0);
  const updatedAtRef = useRef<number>(0);

  const applyJob = useCallback((next: SimulationJob) => {
    const stamp = new Date(next.updated_at).getTime();
    // SSE and polling race; never let an older snapshot overwrite a newer one.
    if (Number.isFinite(stamp) && stamp < updatedAtRef.current) return;
    if (Number.isFinite(stamp)) updatedAtRef.current = stamp;
    setJob((current) => (current ? { ...current, ...next } : next));
  }, []);

  const loadResult = useCallback(async () => {
    setResultError("");
    try {
      setResult(await getSimulationResult(jobId));
    } catch (caught) {
      setResultError(caught instanceof Error ? caught.message : "Failed to load simulation result");
    }
  }, [jobId]);

  const refresh = useCallback(async () => {
    const detail = await getSimulationJob(jobId);
    applyJob(detail);
    return detail;
  }, [jobId, applyJob]);

  const cancel = useCallback(async () => {
    const updated = await cancelSimulationJob(jobId);
    applyJob(updated);
  }, [jobId, applyJob]);

  const resubscribe = useCallback(() => setRevision((r) => r + 1), []);

  useEffect(() => {
    let disposed = false;
    let pollTimer: number | null = null;
    let eventSource: EventSource | null = null;

    async function load(): Promise<SimulationJob | null> {
      try {
        const detail = await getSimulationJob(jobId);
        if (!disposed) {
          applyJob(detail);
          setError("");
        }
        return detail;
      } catch (caught) {
        if (!disposed) setError(caught instanceof Error ? caught.message : "Failed to load simulation job");
        return null;
      }
    }

    function startPolling() {
      setTransport("polling");
      async function tick() {
        const detail = await load();
        if (disposed) return;
        if (detail && isTerminalJobStatus(detail.status)) {
          setTransport("idle");
          return;
        }
        pollTimer = window.setTimeout(tick, detail ? POLL_MS : POLL_ON_ERROR_MS);
      }
      pollTimer = window.setTimeout(tick, POLL_MS);
    }

    function startStream() {
      if (typeof EventSource === "undefined") return startPolling();
      try {
        eventSource = new EventSource(getSimulationEventsUrl(jobId));
      } catch {
        return startPolling();
      }
      setTransport("sse");

      const onProgress = (event: Event) => {
        if (disposed) return;
        try {
          applyJob(JSON.parse((event as MessageEvent<string>).data) as SimulationJob);
        } catch {
          setError("Failed to parse job progress data");
        }
      };

      eventSource.addEventListener("progress", onProgress);
      eventSource.addEventListener("terminal", (event) => {
        onProgress(event);
        eventSource?.close();
        eventSource = null;
        if (!disposed) setTransport("idle");
      });
      eventSource.onerror = () => {
        eventSource?.close();
        eventSource = null;
        if (!disposed) startPolling();
      };
    }

    void load().then((detail) => {
      if (disposed) return;
      if (!detail) return startPolling();
      if (isTerminalJobStatus(detail.status)) return setTransport("idle");
      startStream();
    });

    return () => {
      disposed = true;
      if (pollTimer !== null) window.clearTimeout(pollTimer);
      eventSource?.close();
    };
  }, [jobId, revision, applyJob]);

    useEffect(() => {
    if (job?.status !== "completed" || result !== null || resultError !== "") return;

    let cancelled = false;
    (async () => {
        try {
        const data = await getSimulationResult(jobId);
        if (!cancelled) setResult(data);
        } catch (caught) {
        if (!cancelled) {
            setResultError(caught instanceof Error ? caught.message : "Failed to load simulation result");
        }
        }
    })();

    return () => {
        cancelled = true;
    };
    }, [job?.status, result, resultError, jobId]);

  return { job, result, error, resultError, transport, refresh, cancel, resubscribe, retryResult: loadResult };
}