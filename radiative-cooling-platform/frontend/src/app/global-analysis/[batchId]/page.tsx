"use client";

import dynamic from "next/dynamic";
import { useParams } from "next/navigation";
import {
  useEffect,
  useState,
} from "react";

import {
  cancelGlobalBatch,
  getGlobalBatch,
  getGlobalBatchExportUrl,
  getGlobalBatchGeoJson,
  retryFailedGlobalBatchCities,
} from "@/lib/api-client";

import type {
  GeoJsonFeatureCollection,
  GlobalBatchDetail,
} from "@/types/global-batch";


const GlobalAdaptationMap = dynamic(
  () =>
    import(
      "@/components/global-adaptation-map"
    ),
  {
    ssr: false,

    loading: () => (
      <div className="flex h-140 items-center justify-center rounded-2xl bg-slate-950 text-slate-400">
        Loading global map...
      </div>
    ),
  },
);


const terminalStatuses =
  new Set<string>([
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
    useState<GlobalBatchDetail | null>(
      null,
    );

  const [geoJson, setGeoJson] =
    useState<
      GeoJsonFeatureCollection | null
    >(null);

  const [error, setError] =
    useState("");

  const [
    pollingRevision,
    setPollingRevision,
  ] = useState(0);

  const [
    isCancelling,
    setIsCancelling,
  ] = useState(false);

  const [
    isRetrying,
    setIsRetrying,
  ] = useState(false);

  useEffect(() => {
    let timer: number | null = null;
    let disposed = false;

    async function load() {
      try {
        const response =
          await getGlobalBatch(
            parameters.batchId,
          );

        if (disposed) {
          return;
        }

        setBatch(response);
        setError("");

        if (
          response.completed_city_count > 0
        ) {
          try {
            const mapData =
              await getGlobalBatchGeoJson(
                parameters.batchId,
              );

            if (!disposed) {
              setGeoJson(mapData);
            }
          } catch (mapError) {
            if (!disposed) {
              setError(
                mapError instanceof Error
                  ? mapError.message
                  : (
                      "Unable to load " +
                      "global map data"
                    ),
              );
            }
          }
        } else if (!disposed) {
          setGeoJson(null);
        }

        if (
          !disposed &&
          !terminalStatuses.has(
            response.status,
          )
        ) {
          timer = window.setTimeout(
            load,
            3000,
          );
        }
      } catch (caughtError) {
        if (disposed) {
          return;
        }

        setError(
          caughtError instanceof Error
            ? caughtError.message
            : (
                "Unable to load the " +
                "analysis batch"
              ),
        );

        /*
         * 暫時性網路錯誤不應永久停止輪詢。
         */
        timer = window.setTimeout(
          load,
          5000,
        );
      }
    }

    void load();

    return () => {
      disposed = true;

      if (timer !== null) {
        window.clearTimeout(timer);
      }
    };
  }, [
    parameters.batchId,
    pollingRevision,
  ]);

  async function refreshBatch() {
    const updated =
      await getGlobalBatch(
        parameters.batchId,
      );

    setBatch(updated);

    if (
      updated.completed_city_count > 0
    ) {
      const mapData =
        await getGlobalBatchGeoJson(
          parameters.batchId,
        );

      setGeoJson(mapData);
    }

    return updated;
  }

  async function cancelBatch() {
    if (isCancelling) {
      return;
    }

    try {
      setIsCancelling(true);
      setError("");

      await cancelGlobalBatch(
        parameters.batchId,
      );

      await refreshBatch();
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : (
              "Unable to cancel the " +
              "analysis batch"
            ),
      );
    } finally {
      setIsCancelling(false);
    }
  }

  async function retryFailedCities() {
    if (isRetrying) {
      return;
    }

    try {
      setIsRetrying(true);
      setError("");

      await retryFailedGlobalBatchCities(
        parameters.batchId,
      );

      await refreshBatch();

      /*
       * 原本的輪詢在 terminal status 時已停止。
       * 增加 revision 重新啟動 useEffect 輪詢。
       */
      setPollingRevision(
        (current) => current + 1,
      );
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : (
              "Unable to retry failed " +
              "cities"
            ),
      );
    } finally {
      setIsRetrying(false);
    }
  }

  if (!batch) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        <div className="mx-auto max-w-7xl">
          {error ? (
            <div className="rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">
              {error}
            </div>
          ) : (
            <p className="text-slate-400">
              Loading global analysis...
            </p>
          )}
        </div>
      </main>
    );
  }

  const isTerminal =
    terminalStatuses.has(batch.status);

  const canRetry =
    isTerminal &&
    batch.failed_city_count > 0 &&
    (
      batch.status ===
        "partial_completed" ||
      batch.status === "failed"
    );

  const sampleDaysPerMonth =
    batch.request
      .sample_days_per_month ?? 1;

  const meanExposureCoverage =
    readSummaryNumber(
      batch.summary,
      "mean_exposure_coverage_percent",
    );

  const meanAdaptationRate =
    readSummaryNumber(
      batch.summary,
      "mean_climate_adaptation_rate_percent",
    );

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header className="flex flex-wrap items-start justify-between gap-5">
          <div>
            <p className="text-sm text-cyan-400">
              Global Analysis Batch
            </p>

            <h1 className="mt-2 text-3xl font-bold">
              Global Climate Adaptation
              Results
            </h1>

            <p className="mt-2 text-sm text-slate-400">
              Batch ID: {batch.id}
            </p>

            <p className="mt-1 text-sm text-slate-500">
              Stage:{" "}
              {formatStatus(batch.stage)}
            </p>
          </div>

          <div className="flex flex-wrap gap-3">
            {canRetry && (
              <button
                type="button"
                onClick={
                  retryFailedCities
                }
                disabled={isRetrying}
                className="rounded-lg border border-amber-700 px-5 py-2 text-amber-300 transition-colors hover:bg-amber-950 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {isRetrying
                  ? "Submitting Retry..."
                  : "Retry Failed Cities"}
              </button>
            )}

            <a
              href={getGlobalBatchExportUrl(
                batch.id,
              )}
              className="rounded-lg border border-cyan-700 px-5 py-2 text-cyan-300 transition-colors hover:bg-cyan-950"
            >
              Download Export
            </a>

            {!isTerminal && (
              <button
                type="button"
                onClick={cancelBatch}
                disabled={isCancelling}
                className="rounded-lg border border-red-800 px-5 py-2 text-red-300 transition-colors hover:bg-red-950 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {isCancelling
                  ? "Cancelling..."
                  : "Cancel Batch"}
              </button>
            )}
          </div>
        </header>

        <section className="mt-8 grid gap-4 md:grid-cols-2 lg:grid-cols-5">
          <Metric
            label="Status"
            value={formatStatus(
              batch.status,
            )}
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
            value={String(
              batch.failed_city_count,
            )}
          />

          <Metric
            label="Samples per Month"
            value={String(
              sampleDaysPerMonth,
            )}
          />
        </section>

        <div className="mt-5 h-3 overflow-hidden rounded-full bg-slate-800">
          <div
            className="h-full bg-cyan-400 transition-all duration-500"
            style={{
              width: `${
                clampProgress(
                  batch.progress,
                )
              }%`,
            }}
          />
        </div>

        {(meanExposureCoverage !== null ||
          meanAdaptationRate !== null) && (
          <section className="mt-6 grid gap-4 md:grid-cols-2">
            <Metric
              label="Mean Exposure Coverage"
              value={formatNumber(
                meanExposureCoverage,
                "%",
              )}
            />

            <Metric
              label="Mean Climate Adaptation Rate"
              value={formatNumber(
                meanAdaptationRate,
                "%",
              )}
            />
          </section>
        )}

        {batch.error_message && (
          <div className="mt-6 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">
            <p className="font-semibold">
              Batch error
            </p>

            <p className="mt-1 text-sm">
              {batch.error_message}
            </p>
          </div>
        )}

        {geoJson &&
          geoJson.features.length > 0 && (
            <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-4">
              <div className="mb-4">
                <h2 className="text-xl font-semibold">
                  Global Adaptation Map
                </h2>

                <p className="mt-1 text-sm text-slate-400">
                  Circle color represents
                  climate adaptation rate.
                  Grey circles have no
                  qualifying heat-exposure
                  samples.
                </p>
              </div>

              <GlobalAdaptationMap
                data={geoJson}
              />
            </section>
          )}

        <section className="mt-8 overflow-hidden rounded-2xl border border-slate-800">
          <div className="border-b border-slate-800 bg-slate-900 px-5 py-4">
            <h2 className="text-xl font-semibold">
              City Results
            </h2>

            <p className="mt-1 text-sm text-slate-400">
              Exposure coverage shows how
              much of the weighted sampling
              period satisfied the configured
              heat-exposure thresholds.
            </p>
          </div>

          <div className="overflow-x-auto">
            <table className="w-full min-w-[1150px] text-left">
              <thead className="bg-slate-900 text-sm text-slate-400">
                <tr>
                  <th className="px-4 py-4">
                    City
                  </th>

                  <th className="px-4 py-4">
                    Status
                  </th>

                  <th className="px-4 py-4">
                    Exposure Coverage
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

                  <th className="px-4 py-4">
                    Samples
                  </th>
                </tr>
              </thead>

              <tbody>
                {batch.city_results.map(
                  (result) => (
                    <tr
                      key={result.id}
                      className="border-t border-slate-800 align-top"
                    >
                      <td className="px-4 py-4">
                        <p className="font-medium">
                          {result.city_name}
                        </p>

                        <p className="text-xs text-slate-500">
                          {result.country}
                        </p>

                        {result.error_message && (
                          <p className="mt-2 max-w-xs text-xs leading-5 text-red-400">
                            {
                              result.error_message
                            }
                          </p>
                        )}
                      </td>

                      <td className="px-4 py-4">
                        <StatusBadge
                          status={
                            result.status
                          }
                        />

                        <div className="mt-2 text-xs text-slate-500">
                          {result.progress}%
                        </div>

                        <div className="mt-1 max-w-44 break-words text-xs text-slate-600">
                          {formatStatus(
                            result.stage,
                          )}
                        </div>
                      </td>

                      <td className="px-4 py-4">
                        {formatNumber(
                          result
                            .exposure_coverage_percent,
                          "%",
                        )}

                        {result
                          .evaluated_weighted_days !==
                          null && (
                          <div className="mt-1 text-xs text-slate-500">
                            {
                              result
                                .evaluated_weighted_days
                            }{" "}
                            weighted days
                          </div>
                        )}
                      </td>

                      <td className="px-4 py-4 text-cyan-300">
                        {result
                          .climate_adaptation_rate_percent ===
                        null
                          ? (
                            <span className="text-slate-500">
                              No qualifying
                              exposure
                            </span>
                          )
                          : formatNumber(
                              result
                                .climate_adaptation_rate_percent,
                              "%",
                            )}

                        {result
                          .beneficial_weighted_days !==
                          null && (
                          <div className="mt-1 text-xs text-slate-500">
                            {
                              result
                                .beneficial_weighted_days
                            }{" "}
                            beneficial days
                          </div>
                        )}
                      </td>

                      <td className="px-4 py-4">
                        {formatNumber(
                          result
                            .annual_average_skin_improvement_c,
                          " °C",
                        )}
                      </td>

                      <td className="px-4 py-4">
                        {formatNumber(
                          result
                            .maximum_skin_improvement_c,
                          " °C",
                        )}
                      </td>

                      <td className="px-4 py-4">
                        <div>
                          {
                            result
                              .eligible_sample_count ??
                            0
                          }
                          {" / "}
                          {
                            result
                              .sampled_day_count ??
                            0
                          }
                        </div>

                        <div className="mt-1 text-xs text-slate-500">
                          Eligible / total
                        </div>

                        {result.retry_count >
                          0 && (
                          <div className="mt-2 text-xs text-amber-400">
                            Retried{" "}
                            {
                              result.retry_count
                            }
                            {result.retry_count ===
                            1
                              ? " time"
                              : " times"}
                          </div>
                        )}
                      </td>
                    </tr>
                  ),
                )}

                {batch.city_results.length ===
                  0 && (
                  <tr>
                    <td
                      colSpan={7}
                      className="px-4 py-10 text-center text-slate-500"
                    >
                      No city results are
                      available.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
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


function StatusBadge({
  status,
}: {
  status: string;
}) {
  const colorClass =
    getStatusColorClass(status);

  return (
    <span
      className={
        "inline-flex rounded-full border " +
        "px-2.5 py-1 text-xs font-medium " +
        colorClass
      }
    >
      {formatStatus(status)}
    </span>
  );
}


function getStatusColorClass(
  status: string,
): string {
  switch (status) {
    case "completed":
      return (
        "border-emerald-800 " +
        "bg-emerald-950 " +
        "text-emerald-300"
      );

    case "running":
      return (
        "border-cyan-800 " +
        "bg-cyan-950 " +
        "text-cyan-300"
      );

    case "queued":
      return (
        "border-slate-700 " +
        "bg-slate-900 " +
        "text-slate-300"
      );

    case "failed":
      return (
        "border-red-800 " +
        "bg-red-950 " +
        "text-red-300"
      );

    case "cancelled":
      return (
        "border-slate-700 " +
        "bg-slate-950 " +
        "text-slate-400"
      );

    default:
      return (
        "border-amber-800 " +
        "bg-amber-950 " +
        "text-amber-300"
      );
  }
}


function formatNumber(
  value: number | null | undefined,
  suffix: string,
): string {
  if (
    value === null ||
    value === undefined ||
    !Number.isFinite(value)
  ) {
    return "—";
  }

  return `${value.toFixed(2)}${suffix}`;
}


function formatStatus(
  status: string,
): string {
  if (!status) {
    return "—";
  }

  return status
    .split("_")
    .map(
      (word) =>
        word.charAt(0).toUpperCase() +
        word.slice(1),
    )
    .join(" ");
}


function clampProgress(
  value: number,
): number {
  if (!Number.isFinite(value)) {
    return 0;
  }

  return Math.max(
    0,
    Math.min(100, value),
  );
}


function readSummaryNumber(
  summary: Record<
    string,
    unknown
  > | null,
  key: string,
): number | null {
  if (!summary) {
    return null;
  }

  const value = summary[key];

  if (
    value === null ||
    value === undefined ||
    value === ""
  ) {
    return null;
  }

  const numericValue =
    Number(value);

  if (!Number.isFinite(numericValue)) {
    return null;
  }

  return numericValue;
}