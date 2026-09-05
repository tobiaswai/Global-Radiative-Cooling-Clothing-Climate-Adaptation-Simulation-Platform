"use client";

import dynamic from "next/dynamic";
import { useEffect, useState } from "react";
import { useParams } from "next/navigation";

import {
  cancelGlobalBatch,
  getGlobalBatch,
  getGlobalBatchGeoJson,
} from "@/lib/api-client";

import type {
  GeoJsonFeatureCollection,
  GlobalBatchDetail,
} from "@/types/global-batch";

const GlobalAdaptationMap = dynamic(
  () => import("@/components/global-adaptation-map"),
  {
    ssr: false,
  },
);

const terminalStatuses = new Set([
  "completed",
  "partial_completed",
  "failed",
  "cancelled",
]);

export default function GlobalBatchPage() {
  const parameters = useParams<{
    batchId: string;
  }>();

  const [batch, setBatch] =
    useState<GlobalBatchDetail | null>(null);

  const [geoJson, setGeoJson] =
    useState<GeoJsonFeatureCollection | null>(null);

  const [error, setError] = useState("");

  useEffect(() => {
    let timer: number | null = null;

    async function load() {
      try {
        const response = await getGlobalBatch(
          parameters.batchId,
        );

        setBatch(response);
        setError("");

        if (response.completed_city_count > 0) {
          const mapData = await getGlobalBatchGeoJson(
            parameters.batchId,
          );

          setGeoJson(mapData);
        }

        if (!terminalStatuses.has(response.status)) {
          timer = window.setTimeout(load, 3000);
        }
      } catch (caughtError) {
        setError(
          caughtError instanceof Error
            ? caughtError.message
            : "Unable to load the analysis batch",
        );
      }
    }

    void load();

    return () => {
      if (timer !== null) {
        window.clearTimeout(timer);
      }
    };
  }, [parameters.batchId]);

  async function cancelBatch() {
    try {
      setError("");

      await cancelGlobalBatch(parameters.batchId);

      const updated = await getGlobalBatch(
        parameters.batchId,
      );

      setBatch(updated);
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "Unable to cancel the analysis batch",
      );
    }
  }

  if (!batch) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        {error || "Loading global analysis..."}
      </main>
    );
  }

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header className="flex flex-wrap items-start justify-between gap-5">
          <div>
            <p className="text-sm text-cyan-400">
              Global Analysis Batch
            </p>

            <h1 className="mt-2 text-3xl font-bold">
              Global Climate Adaptation Results
            </h1>

            <p className="mt-2 text-sm text-slate-400">
              Batch ID: {batch.id}
            </p>
          </div>

          {!terminalStatuses.has(batch.status) && (
            <button
              type="button"
              onClick={cancelBatch}
              className="rounded-lg border border-red-800 px-5 py-2 text-red-300 transition-colors hover:bg-red-950"
            >
              Cancel Batch
            </button>
          )}
        </header>

        <section className="mt-8 grid gap-4 md:grid-cols-4">
          <Metric
            label="Status"
            value={formatStatus(batch.status)}
          />

          <Metric
            label="Overall Progress"
            value={`${batch.progress}%`}
          />

          <Metric
            label="Completed Cities"
            value={
              `${batch.completed_city_count}` +
              ` / ${batch.total_city_count}`
            }
          />

          <Metric
            label="Failed Cities"
            value={String(batch.failed_city_count)}
          />
        </section>

        <div className="mt-5 h-3 overflow-hidden rounded-full bg-slate-800">
          <div
            className="h-full bg-cyan-400 transition-all"
            style={{
              width: `${batch.progress}%`,
            }}
          />
        </div>

        {geoJson && geoJson.features.length > 0 && (
          <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-4">
            <GlobalAdaptationMap data={geoJson} />
          </section>
        )}

        <section className="mt-8 overflow-x-auto rounded-2xl border border-slate-800">
          <table className="w-full min-w-200 text-left">
            <thead className="bg-slate-900 text-sm text-slate-400">
              <tr>
                <th className="px-4 py-4">
                  City
                </th>

                <th className="px-4 py-4">
                  Status
                </th>

                <th className="px-4 py-4">
                  Adaptation Rate
                </th>

                <th className="px-4 py-4">
                  Average Skin Cooling
                </th>

                <th className="px-4 py-4">
                  Maximum Skin Cooling
                </th>
              </tr>
            </thead>

            <tbody>
              {batch.city_results.map((result) => (
                <tr
                  key={result.id}
                  className="border-t border-slate-800"
                >
                  <td className="px-4 py-4">
                    <p className="font-medium">
                      {result.city_name}
                    </p>

                    <p className="text-xs text-slate-500">
                      {result.country}
                    </p>
                  </td>

                  <td className="px-4 py-4">
                    {formatStatus(result.status)}

                    <div className="mt-1 text-xs text-slate-500">
                      {result.progress}%
                    </div>
                  </td>

                  <td className="px-4 py-4 text-cyan-300">
                    {formatNumber(
                      result.climate_adaptation_rate_percent,
                      "%",
                    )}
                  </td>

                  <td className="px-4 py-4">
                    {formatNumber(
                      result.annual_average_skin_improvement_c,
                      " °C",
                    )}
                  </td>

                  <td className="px-4 py-4">
                    {formatNumber(
                      result.maximum_skin_improvement_c,
                      " °C",
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>

        {error && (
          <div className="mt-6 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">
            {error}
          </div>
        )}
      </div>
    </main>
  );
}

function Metric({
  label,
  value,
}: {
  label: string;
  value: string;
}) {
  return (
    <div className="rounded-xl border border-slate-800 bg-slate-900 p-5">
      <p className="text-sm text-slate-400">
        {label}
      </p>

      <p className="mt-2 text-xl font-semibold text-cyan-300">
        {value}
      </p>
    </div>
  );
}

function formatNumber(
  value: number | null,
  suffix: string,
): string {
  if (value === null) {
    return "—";
  }

  return `${value.toFixed(2)}${suffix}`;
}

function formatStatus(status: string): string {
  return status
    .split("_")
    .map(
      (word) =>
        word.charAt(0).toUpperCase() +
        word.slice(1),
    )
    .join(" ");
}