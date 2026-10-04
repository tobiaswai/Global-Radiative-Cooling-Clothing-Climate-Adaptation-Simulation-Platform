"use client";

import { useEffect, useState } from "react";

import { getGlobalBatchCityCheckpoints } from "@/lib/api-client";
import { formatRelativeTime } from "@/lib/relative-time";
import type { CityCheckpointList } from "@/types/global-batch";

type Props = {
  batchId: string;
  cityResultId: string;
  /** Re-fetch when this changes (e.g. completed_month_count). */
  version: number;
};

export function CityCheckpointList({ batchId, cityResultId, version }: Props) {
  const [data, setData] = useState<CityCheckpointList | null>(null);
  const [error, setError] = useState("");

  useEffect(() => {
    let disposed = false;
    getGlobalBatchCityCheckpoints(batchId, cityResultId)
      .then((response) => {
        if (!disposed) {
          setData(response);
          setError("");
        }
      })
      .catch((caught: unknown) => {
        if (!disposed) setError(caught instanceof Error ? caught.message : "Unable to load checkpoints");
      });
    return () => {
      disposed = true;
    };
  }, [batchId, cityResultId, version]);

  if (error) return <p className="mt-3 text-sm text-red-300">{error}</p>;
  if (!data) return <p className="mt-3 text-sm text-slate-500">Loading checkpoints…</p>;

  const complete = data.resume_from_month > data.end_month;

  return (
    <div className="mt-8">
      <div className="flex flex-wrap items-baseline justify-between gap-3">
        <h3 className="text-lg font-semibold">Durable Checkpoints</h3>
        <p className="text-sm text-slate-400">
          {complete
            ? "All requested months checkpointed."
            : `A resumed worker would start at month ${data.resume_from_month}.`}
        </p>
      </div>

      {data.items.length === 0 ? (
        <p className="mt-3 text-sm text-slate-500">No checkpoint has been written yet.</p>
      ) : (
        <div className="mt-4 overflow-x-auto rounded-xl border border-slate-800">
          <table className="w-full min-w-[40rem] text-left text-sm">
            <thead className="bg-slate-950 text-xs uppercase tracking-wide text-slate-500">
              <tr>
                <th className="px-4 py-3">Month</th>
                <th className="px-4 py-3">Attempt</th>
                <th className="px-4 py-3">Samples</th>
                <th className="px-4 py-3">Skipped</th>
                <th className="px-4 py-3">Written</th>
                <th className="px-4 py-3">Payload SHA-256</th>
              </tr>
            </thead>
            <tbody>
              {data.items.map((item) => (
                <tr key={item.id} className="border-t border-slate-800">
                  <td className="px-4 py-3 font-medium">{item.month}</td>
                  <td className="px-4 py-3">{item.attempt}</td>
                  <td className="px-4 py-3">{item.sampled_day_count}</td>
                  <td className={`px-4 py-3 ${item.skipped_sample_count ? "text-amber-300" : ""}`}>
                    {item.skipped_sample_count}
                  </td>
                  <td className="px-4 py-3 text-slate-400" title={new Date(item.created_at).toLocaleString()}>
                    {formatRelativeTime(item.created_at)}
                  </td>
                  <td className="px-4 py-3 font-mono text-xs text-slate-400" title={item.payload_sha256}>
                    {item.payload_sha256.slice(0, 16)}…
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}