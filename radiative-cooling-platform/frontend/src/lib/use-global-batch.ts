"use client";

import { useCallback, useEffect, useRef, useState } from "react";

import { getGlobalBatch, getGlobalBatchEventsUrl } from "@/lib/api-client";
import {
  isTerminalBatchStatus,
  mergeBatchProgress,
  progressRequiresDetailReload,
} from "@/lib/global-batch-progress";
import type { GlobalBatchDetail, GlobalBatchProgressEvent } from "@/types/global-batch";

export type BatchTransport = "sse" | "polling" | "idle";

const POLL_INTERVAL_MS = 3000;
const POLL_INTERVAL_ON_ERROR_MS = 5000;

export function useGlobalBatch(batchId: string) {
  const [batch, setBatch] = useState<GlobalBatchDetail | null>(null);
  const [error, setError] = useState("");
  const [transport, setTransport] = useState<BatchTransport>("idle");
  const [revision, setRevision] = useState(0);
  const batchRef = useRef<GlobalBatchDetail | null>(null);

  useEffect(() => {
    batchRef.current = batch;
  }, [batch]);

  const refresh = useCallback(async () => {
    const detail = await getGlobalBatch(batchId);
    setBatch(detail);
    setError("");
    return detail;
  }, [batchId]);

  /** Restart the subscription (after retry, for example). */
  const resubscribe = useCallback(() => setRevision((current) => current + 1), []);

  useEffect(() => {
    let disposed = false;
    let pollTimer: number | null = null;
    let eventSource: EventSource | null = null;

    function message(caught: unknown, fallback: string) {
      return caught instanceof Error ? caught.message : fallback;
    }

    async function loadDetail(): Promise<GlobalBatchDetail | null> {
      try {
        const detail = await getGlobalBatch(batchId);
        if (!disposed) {
          setBatch(detail);
          setError("");
        }
        return detail;
      } catch (caught) {
        if (!disposed) setError(message(caught, "Unable to load the global analysis."));
        return null;
      }
    }

    function stopPolling() {
      if (pollTimer !== null) {
        window.clearTimeout(pollTimer);
        pollTimer = null;
      }
    }

    function startPolling() {
      setTransport("polling");

      async function tick() {
        const detail = await loadDetail();
        if (disposed) return;
        if (detail && isTerminalBatchStatus(detail.status)) {
          setTransport("idle");
          return;
        }
        pollTimer = window.setTimeout(tick, detail ? POLL_INTERVAL_MS : POLL_INTERVAL_ON_ERROR_MS);
      }

      pollTimer = window.setTimeout(tick, POLL_INTERVAL_MS);
    }

    function startStream() {
      if (typeof EventSource === "undefined") {
        startPolling();
        return;
      }

      try {
        eventSource = new EventSource(getGlobalBatchEventsUrl(batchId));
      } catch {
        startPolling();
        return;
      }

      setTransport("sse");

      eventSource.addEventListener("progress", (event) => {
        if (disposed) return;
        try {
          const parsed = JSON.parse((event as MessageEvent<string>).data) as GlobalBatchProgressEvent;
          const needsReload = progressRequiresDetailReload(batchRef.current, parsed);
          setBatch((current) => (current ? mergeBatchProgress(current, parsed) : current));
          if (needsReload) void loadDetail();
        } catch {
          setError("Failed to parse batch progress data.");
        }
      });

      eventSource.addEventListener("terminal", () => {
        eventSource?.close();
        eventSource = null;
        void loadDetail().then(() => {
          if (!disposed) setTransport("idle");
        });
      });

      eventSource.onerror = () => {
        // Proxy without SSE support, network blip, or server restart: fall back.
        eventSource?.close();
        eventSource = null;
        if (!disposed) startPolling();
      };
    }

    void loadDetail().then((detail) => {
      if (disposed || !detail) {
        if (!disposed) startPolling();
        return;
      }
      if (isTerminalBatchStatus(detail.status)) {
        setTransport("idle");
        return;
      }
      startStream();
    });

    return () => {
      disposed = true;
      stopPolling();
      eventSource?.close();
    };
  }, [batchId, revision]);

  return { batch, error, setError, transport, refresh, resubscribe };
}