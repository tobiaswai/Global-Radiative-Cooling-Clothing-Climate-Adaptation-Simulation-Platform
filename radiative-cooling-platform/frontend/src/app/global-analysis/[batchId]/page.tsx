"use client";

import Link from "next/link";
import dynamic from "next/dynamic";
import { useParams } from "next/navigation";
import { useEffect, useMemo, useState } from "react";

import { BatchReliabilityPanel } from "@/components/global/batch-reliability-panel";
import { CheckpointTimeline } from "@/components/global/checkpoint-timeline";
import { CityCheckpointList } from "@/components/global/city-checkpoint-list";
import { DataQualityPanel } from "@/components/global/data-quality-panel";
import { LeaseBadge } from "@/components/global/lease-badge";
import {
  cancelGlobalBatch,
  getGlobalBatchExportUrl,
  getGlobalBatchGeoJson,
  retryFailedGlobalBatchCities,
} from "@/lib/api-client";
import { isTerminalBatchStatus } from "@/lib/global-batch-progress";
import { useGlobalBatch } from "@/lib/use-global-batch";
import type {
  GeoJsonFeatureCollection,
  GlobalCityResult,
  HeatwaveEvent,
} from "@/types/global-batch";


const GlobalAdaptationMap = dynamic(
  () =>
    import(
      "@/components/global-adaptation-map"
    ),
  {
    ssr: false,

    loading: () => (
      <div className="flex h-[35rem] items-center justify-center rounded-2xl bg-slate-950 text-slate-400">
        Loading global map...
      </div>
    ),
  },
);

export default function GlobalBatchPage() {
  const parameters = useParams<{ batchId: string }>();
  const batchId = parameters.batchId;

  const { batch, error, setError, transport, refresh, resubscribe } = useGlobalBatch(batchId);

  const [geoJson, setGeoJson] = useState<GeoJsonFeatureCollection | null>(null);
  const [selectedCityId, setSelectedCityId] = useState<string | null>(null);
  const [isCancelling, setIsCancelling] = useState(false);
  const [isRetrying, setIsRetrying] = useState(false);

  const completedCityCount = batch?.completed_city_count ?? 0;

  // Synchronise with the GeoJSON endpoint. Re-runs only when a city completes
  // (keyed on the count, not on every heartbeat). The only setState here is in
  // the fetch callback, i.e. after the external system answered.
  useEffect(() => {
    if (completedCityCount === 0) {
      return;
    }

    let disposed = false;

    getGlobalBatchGeoJson(batchId)
      .then((data) => {
        if (!disposed) setGeoJson(data);
      })
      .catch((caught: unknown) => {
        if (!disposed) setError(getErrorMessage(caught, "Unable to load global map data."));
      });

    return () => {
      disposed = true;
    };
  }, [batchId, completedCityCount, setError]);

  const mapData = completedCityCount > 0 ? geoJson : null;

  const selectedCity = useMemo(
    () => batch?.city_results.find((result) => result.id === selectedCityId) ?? null,
    [batch, selectedCityId],
  );

  const completedResults = useMemo(
    () => batch?.city_results.filter((result) => result.status === "completed") ?? [],
    [batch],
  );

  const aggregateMetrics = useMemo(
    () => ({
      meanExposureCoverage: calculateMean(completedResults.map((r) => r.exposure_coverage_percent)),
      meanAdaptationRate: calculateMean(completedResults.map((r) => r.climate_adaptation_rate_percent)),
      meanSkinCooling: calculateMean(completedResults.map((r) => r.annual_average_skin_improvement_c)),
      meanSkinP90: calculateMean(completedResults.map((r) => r.skin_improvement_p90_c)),
      totalHeatwaveEvents: completedResults.reduce((t, r) => t + (r.heatwave_event_count ?? 0), 0),
    }),
    [completedResults],
  );

  async function cancelBatch() {
    if (isCancelling) return;
    try {
      setIsCancelling(true);
      setError("");
      await cancelGlobalBatch(batchId);
      await refresh();
    } catch (caught) {
      setError(getErrorMessage(caught, "Unable to cancel the analysis batch."));
    } finally {
      setIsCancelling(false);
    }
  }

  async function retryFailedCities() {
    if (isRetrying) return;
    try {
      setIsRetrying(true);
      setError("");
      await retryFailedGlobalBatchCities(batchId);
      await refresh();
      resubscribe(); // batch left its terminal state; reopen the stream
    } catch (caught) {
      setError(getErrorMessage(caught, "Unable to retry failed cities."));
    } finally {
      setIsRetrying(false);
    }
  }

  if (!batch) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        <div className="mx-auto max-w-7xl">
          {error ? (
            <div className="rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">{error}</div>
          ) : (
            <p className="text-slate-400">Loading global analysis...</p>
          )}
        </div>
      </main>
    );
  }

  const isTerminal = isTerminalBatchStatus(batch.status);
  const canRetry =
    isTerminal &&
    batch.failed_city_count > 0 &&
    (batch.status === "partial_completed" || batch.status === "failed");

  const analysisResolution = batch.request.analysis_resolution ?? "representative";
  const analysisResolutionLabel = analysisResolution === "daily" ? "Daily" : "Representative Days";
  const samplingLabel =
    analysisResolution === "daily"
      ? `Every ${batch.request.daily_stride_days ?? 1} day(s)`
      : `${batch.request.sample_days_per_month ?? 1} day(s) per month`;
  const heatwaveAvailable =
    batch.request.enable_heatwave_analysis &&
    analysisResolution === "daily" &&
    (batch.request.daily_stride_days ?? 1) === 1;

  const startMonth = batch.request.start_month ?? 1;
  const endMonth = batch.request.end_month ?? 12;

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-[95rem] px-6 py-10">
        <nav className="mb-4 flex items-center gap-2 text-sm text-slate-400">
          <Link href="/global-analysis" className="hover:text-slate-100">Global Analysis</Link>
          <span>/</span>
          <Link href="/global-analysis/batches" className="hover:text-slate-100">Batches</Link>
          <span>/</span>
          <span className="text-slate-200">Batch Result</span>
        </nav>

        <header className="flex flex-wrap items-start justify-between gap-5">
          <div>
            <p className="text-sm font-medium text-cyan-400">Global Analysis</p>
            <h1 className="mt-2 text-3xl font-bold">{batch.request.name}</h1>
            <p className="mt-3 text-sm text-slate-400">
              Batch ID: <span className="font-mono text-slate-300">{batch.id}</span>
            </p>
            <p className="mt-1 text-sm text-slate-500">Created {formatDateTime(batch.created_at)}</p>
          </div>

          <div className="flex flex-wrap gap-3">
            {canRetry && (
              <button
                type="button"
                onClick={retryFailedCities}
                disabled={isRetrying}
                className="rounded-lg border border-amber-700 px-5 py-2 text-amber-300 transition-colors hover:bg-amber-950 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {isRetrying ? "Submitting Retry..." : "Retry Failed Cities"}
              </button>
            )}

            <a
              href={getGlobalBatchExportUrl(batch.id)}
              className="rounded-lg border border-cyan-700 px-5 py-2 text-cyan-300 transition-colors hover:bg-cyan-950"
            >
              Download Export
            </a>

            {!isTerminal && (
              <button
                type="button"
                onClick={cancelBatch}
                disabled={isCancelling || Boolean(batch.cancel_requested_at)}
                className="rounded-lg border border-red-800 px-5 py-2 text-red-300 transition-colors hover:bg-red-950 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {batch.cancel_requested_at
                  ? "Cancel requested – finishing current month"
                  : isCancelling
                    ? "Cancelling..."
                    : "Cancel Batch"}
              </button>
            )}
          </div>
        </header>

        <section className="mt-8 grid gap-4 md:grid-cols-2 lg:grid-cols-4 xl:grid-cols-8">
          <Metric label="Status" value={formatLabel(batch.status)} />
          <Metric label="Overall Progress" value={`${batch.progress}%`} />
          <Metric label="Completed Cities" value={`${batch.completed_city_count} / ${batch.total_city_count}`} />
          <Metric label="Failed Cities" value={String(batch.failed_city_count)} />
          <Metric label="Cancelled Cities" value={String(batch.cancelled_city_count)} />
          <Metric label="Resolution" value={analysisResolutionLabel} />
          <Metric label="Sampling" value={samplingLabel} />
          <Metric label="Execution Profile" value={formatLabel(batch.request.execution_profile ?? "auto")} />
        </section>

        <div className="mt-5 h-3 overflow-hidden rounded-full bg-slate-800">
          <div
            className="h-full bg-cyan-400 transition-all duration-500"
            style={{ width: `${clampProgress(batch.progress)}%` }}
          />
        </div>

        <BatchReliabilityPanel batch={batch} transport={transport} />

        <section className="mt-6 grid gap-4 md:grid-cols-2 lg:grid-cols-5">
          <Metric label="Mean Exposure Coverage" value={formatNumber(aggregateMetrics.meanExposureCoverage, "%")} />
          <Metric label="Mean Adaptation Rate" value={formatNumber(aggregateMetrics.meanAdaptationRate, "%")} />
          <Metric label="Mean Skin Cooling" value={formatNumber(aggregateMetrics.meanSkinCooling, " °C")} />
          <Metric label="Mean P90 Skin Cooling" value={formatNumber(aggregateMetrics.meanSkinP90, " °C")} />
          <Metric
            label="Detected Heatwaves"
            value={heatwaveAvailable ? String(aggregateMetrics.totalHeatwaveEvents) : "Unavailable"}
          />
        </section>

        {batch.error_message && (
          <div className="mt-6 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">
            <p className="font-semibold">Batch Error</p>
            <p className="mt-2 text-sm">{batch.error_message}</p>
          </div>
        )}

        {error && (
          <div className="mt-6 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">{error}</div>
        )}

        <section className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-5">
          <div className="mb-5">
            <h2 className="text-xl font-semibold">Global Adaptation Map</h2>
            <p className="mt-2 text-sm text-slate-400">Completed cities are colored by climate adaptation rate.</p>
          </div>

          {mapData && mapData.features.length > 0 ? (
            <GlobalAdaptationMap data={mapData} />
          ) : (
            <div className="flex h-80 items-center justify-center rounded-xl bg-slate-950 text-slate-500">
              Map data will appear after at least one city completes.
            </div>
          )}
        </section>

        <section className="mt-8 overflow-hidden rounded-2xl border border-slate-800 bg-slate-900">
          <div className="border-b border-slate-800 p-5">
            <h2 className="text-xl font-semibold">City Results</h2>
            <p className="mt-2 text-sm text-slate-400">
              Select a city to inspect monthly, percentile, checkpoint, data-quality and heatwave results.
            </p>
          </div>

          <div className="overflow-x-auto">
            <table className="min-w-[100rem] w-full text-left text-sm">
              <thead className="bg-slate-950 text-xs uppercase tracking-wide text-slate-500">
                <tr>
                  <th className="px-4 py-4">City</th>
                  <th className="px-4 py-4">Status</th>
                  <th className="px-4 py-4">Lease</th>
                  <th className="px-4 py-4">Checkpoints</th>
                  <th className="px-4 py-4">Attempts</th>
                  <th className="px-4 py-4">Exposure</th>
                  <th className="px-4 py-4">Adaptation</th>
                  <th className="px-4 py-4">Mean Skin</th>
                  <th className="px-4 py-4">P90 Skin</th>
                  <th className="px-4 py-4">P95 Skin</th>
                  <th className="px-4 py-4">Heatwaves</th>
                  <th className="px-4 py-4">Samples</th>
                </tr>
              </thead>

              <tbody>
                {batch.city_results.map((result) => (
                  <CityResultRow
                    key={result.id}
                    result={result}
                    startMonth={startMonth}
                    endMonth={endMonth}
                    selected={selectedCityId === result.id}
                    onSelect={() => setSelectedCityId(result.id)}
                  />
                ))}
              </tbody>
            </table>
          </div>
        </section>

        {selectedCity && (
          <CityDetailPanel
            batchId={batch.id}
            result={selectedCity}
            startMonth={startMonth}
            endMonth={endMonth}
            heatwaveAvailable={heatwaveAvailable}
            onClose={() => setSelectedCityId(null)}
          />
        )}
      </div>
    </main>
  );
}

function CityResultRow({
  result,
  startMonth,
  endMonth,
  selected,
  onSelect,
}: {
  result: GlobalCityResult;
  startMonth: number;
  endMonth: number;
  selected: boolean;
  onSelect: () => void;
}) {
  const checkpointMonths = result.checkpoint_months ?? [];

  return (
    <tr
      className={[
        "cursor-pointer border-t border-slate-800 align-top transition",
        selected ? "bg-cyan-950/50" : "hover:bg-slate-800/50",
      ].join(" ")}
      onClick={onSelect}
    >
      <td className="px-4 py-4">
        <p className="font-medium">{result.city_name}</p>
        <p className="text-xs text-slate-500">{result.country}</p>
        {result.error_message && (
          <p className="mt-2 max-w-xs text-xs leading-5 text-red-400">{result.error_message}</p>
        )}
      </td>

      <td className="px-4 py-4">
        <StatusBadge status={result.status} />
        <p className="mt-2 text-xs text-slate-500">{result.progress}%</p>
        <p className="mt-1 max-w-44 break-words text-xs text-slate-600">{formatLabel(result.stage)}</p>
      </td>

      <td className="px-4 py-4">
        <LeaseBadge
          leaseState={result.lease_state}
          leaseOwner={result.lease_owner}
          lastHeartbeatAt={result.last_heartbeat_at}
          leaseExpiresAt={result.lease_expires_at}
        />
      </td>

      <td className="px-4 py-4">
        <CheckpointTimeline
          startMonth={startMonth}
          endMonth={endMonth}
          checkpointMonths={checkpointMonths}
          status={result.status}
          compact
        />
        <p className="mt-2 text-xs text-slate-500">
          {result.completed_month_count} / {endMonth - startMonth + 1} month(s)
          {result.last_checkpoint_month ? ` · last ${result.last_checkpoint_month}` : ""}
        </p>
        {result.resumed_from_checkpoint && (
          <span className="mt-2 inline-flex rounded-full border border-violet-800 bg-violet-950 px-2 py-1 text-xs text-violet-300">
            Resumed
          </span>
        )}
      </td>

      <td className="px-4 py-4">
        <p className={result.retry_count > 0 ? "text-amber-300" : ""}>{result.retry_count + 1}</p>
        {result.retry_count > 0 && (
          <p className="mt-1 text-xs text-slate-500">{result.retry_count} retr{result.retry_count === 1 ? "y" : "ies"}</p>
        )}
      </td>

      <td className="px-4 py-4">
        {formatNumber(result.exposure_coverage_percent, "%")}
        {result.evaluated_weighted_days !== null && (
          <p className="mt-1 text-xs text-slate-500">{result.evaluated_weighted_days} weighted days</p>
        )}
      </td>

      <td className="px-4 py-4 text-cyan-300">
        {result.climate_adaptation_rate_percent === null ? (
          <span className="text-slate-500">No qualifying exposure</span>
        ) : (
          formatNumber(result.climate_adaptation_rate_percent, "%")
        )}
      </td>

      <td className="px-4 py-4">{formatNumber(result.annual_average_skin_improvement_c, " °C")}</td>
      <td className="px-4 py-4">{formatNumber(result.skin_improvement_p90_c, " °C")}</td>
      <td className="px-4 py-4">{formatNumber(result.skin_improvement_p95_c, " °C")}</td>

      <td className="px-4 py-4">
        {result.heatwave_event_count ?? "—"}
        {result.longest_heatwave_days !== null && (
          <p className="mt-1 text-xs text-slate-500">Longest: {result.longest_heatwave_days} days</p>
        )}
      </td>

      <td className="px-4 py-4">
        {result.sampled_day_count ?? "—"}
        {result.eligible_sample_count !== null && (
          <p className="mt-1 text-xs text-slate-500">{result.eligible_sample_count} eligible</p>
        )}
      </td>
    </tr>
  );
}

function CityDetailPanel({
  batchId,
  result,
  startMonth,
  endMonth,
  heatwaveAvailable,
  onClose,
}: {
  batchId: string;
  result: GlobalCityResult;
  startMonth: number;
  endMonth: number;
  heatwaveAvailable: boolean;
  onClose: () => void;
}) {
  return (
    <section className="mt-8 rounded-2xl border border-cyan-900 bg-slate-900 p-6">
      <div className="flex flex-wrap items-start justify-between gap-4">
        <div>
          <p className="text-sm font-medium text-cyan-400">City Analytics</p>
          <h2 className="mt-1 text-2xl font-semibold">
            {result.city_name}, {result.country}
          </h2>
          <p className="mt-2 text-sm text-slate-500">
            {result.latitude.toFixed(4)}, {result.longitude.toFixed(4)}
          </p>
        </div>

        <div className="flex flex-col items-end gap-3">
          <LeaseBadge
            leaseState={result.lease_state}
            leaseOwner={result.lease_owner}
            lastHeartbeatAt={result.last_heartbeat_at}
            leaseExpiresAt={result.lease_expires_at}
          />
          <button
            type="button"
            onClick={onClose}
            className="rounded-lg border border-slate-700 px-4 py-2 text-sm text-slate-300 hover:bg-slate-800"
          >
            Close
          </button>
        </div>
      </div>

      <div className="mt-6">
        <CheckpointTimeline
          startMonth={startMonth}
          endMonth={endMonth}
          checkpointMonths={result.checkpoint_months ?? []}
          status={result.status}
        />
      </div>

      <div className="mt-6 grid gap-4 md:grid-cols-2 lg:grid-cols-4">
        <Metric label="Skin Cooling P50" value={formatNumber(result.skin_improvement_p50_c, " °C")} />
        <Metric label="Skin Cooling P90" value={formatNumber(result.skin_improvement_p90_c, " °C")} />
        <Metric label="Skin Cooling P95" value={formatNumber(result.skin_improvement_p95_c, " °C")} />
        <Metric label="Maximum Skin Cooling" value={formatNumber(result.maximum_skin_improvement_c, " °C")} />
        <Metric label="Core Cooling P50" value={formatNumber(result.core_improvement_p50_c, " °C")} />
        <Metric label="Core Cooling P90" value={formatNumber(result.core_improvement_p90_c, " °C")} />
        <Metric label="Core Cooling P95" value={formatNumber(result.core_improvement_p95_c, " °C")} />
        <Metric label="Effective Cooling" value={formatNumber(result.effective_cooling_hours, " hours")} />
      </div>

      <MonthlyResultsTable result={result} />

      <CityCheckpointList
        batchId={batchId}
        cityResultId={result.id}
        version={result.completed_month_count}
      />

      <DataQualityPanel result={result} />

      <HeatwaveResults events={result.heatwave_events ?? []} available={heatwaveAvailable} />
    </section>
  );
}

function MonthlyResultsTable({
  result,
}: {
  result: GlobalCityResult;
}) {
  const monthlyResults =
    result.monthly_results ?? [];

  return (
    <div className="mt-8">
      <h3 className="text-lg font-semibold">
        Monthly Results
      </h3>

      {monthlyResults.length === 0 ? (
        <p className="mt-3 text-sm text-slate-500">
          No monthly results are available.
        </p>
      ) : (
        <div className="mt-4 overflow-x-auto rounded-xl border border-slate-800">
          <table className="min-w-[70rem] w-full text-left text-sm">
            <thead className="bg-slate-950 text-xs uppercase tracking-wide text-slate-500">
              <tr>
                <th className="px-4 py-3">
                  Month
                </th>

                <th className="px-4 py-3">
                  Samples
                </th>

                <th className="px-4 py-3">
                  Eligible
                </th>

                <th className="px-4 py-3">
                  Exposure
                </th>

                <th className="px-4 py-3">
                  Adaptation
                </th>

                <th className="px-4 py-3">
                  Average Skin
                </th>

                <th className="px-4 py-3">
                  Average Core
                </th>

                <th className="px-4 py-3">
                  Maximum Skin
                </th>

                <th className="px-4 py-3">
                  Weighted Days
                </th>
              </tr>
            </thead>

            <tbody>
              {monthlyResults.map(
                (month) => (
                  <tr
                    key={month.month}
                    className="border-t border-slate-800"
                  >
                    <td className="px-4 py-3 font-medium">
                      {formatMonth(
                        month.month,
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {
                        month.sampled_day_count
                      }
                    </td>

                    <td className="px-4 py-3">
                      {
                        month.eligible_sample_count
                      }
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        month
                          .exposure_coverage_percent,
                        "%",
                      )}
                    </td>

                    <td className="px-4 py-3 text-cyan-300">
                      {formatNumber(
                        month
                          .climate_adaptation_rate_percent,
                        "%",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        month
                          .average_skin_improvement_c,
                        " °C",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        month
                          .average_core_improvement_c,
                        " °C",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        month
                          .maximum_skin_improvement_c,
                        " °C",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {
                        month.evaluated_weighted_days
                      }{" "}
                      /{" "}
                      {
                        month.total_weighted_days
                      }
                    </td>
                  </tr>
                ),
              )}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}


function HeatwaveResults({
  events,
  available,
}: {
  events: HeatwaveEvent[];
  available: boolean;
}) {
  return (
    <div className="mt-8">
      <h3 className="text-lg font-semibold">
        Heatwave Events
      </h3>

      {!available ? (
        <p className="mt-3 text-sm text-amber-300">
          Heatwave analysis is unavailable for
          this sampling configuration.
        </p>
      ) : events.length === 0 ? (
        <p className="mt-3 text-sm text-slate-500">
          No qualifying heatwave event was
          detected.
        </p>
      ) : (
        <div className="mt-4 overflow-x-auto rounded-xl border border-slate-800">
          <table className="min-w-[65rem] w-full text-left text-sm">
            <thead className="bg-slate-950 text-xs uppercase tracking-wide text-slate-500">
              <tr>
                <th className="px-4 py-3">
                  Start
                </th>

                <th className="px-4 py-3">
                  End
                </th>

                <th className="px-4 py-3">
                  Duration
                </th>

                <th className="px-4 py-3">
                  Mean Maximum Air
                </th>

                <th className="px-4 py-3">
                  Peak Air
                </th>

                <th className="px-4 py-3">
                  Mean Skin Cooling
                </th>

                <th className="px-4 py-3">
                  P90 Skin Cooling
                </th>

                <th className="px-4 py-3">
                  Beneficial Days
                </th>
              </tr>
            </thead>

            <tbody>
              {events.map(
                (event, index) => (
                  <tr
                    key={
                      `${event.start_date_local}-` +
                      `${event.end_date_local}-` +
                      index
                    }
                    className="border-t border-slate-800"
                  >
                    <td className="px-4 py-3">
                      {formatDate(
                        event.start_date_local,
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {formatDate(
                        event.end_date_local,
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {event.duration_days} days
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        event
                          .mean_maximum_air_temperature_c,
                        " °C",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        event
                          .peak_air_temperature_c,
                        " °C",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        event
                          .mean_skin_improvement_c,
                        " °C",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {formatNumber(
                        event
                          .p90_skin_improvement_c,
                        " °C",
                      )}
                    </td>

                    <td className="px-4 py-3">
                      {
                        event.beneficial_day_count
                      }
                    </td>
                  </tr>
                ),
              )}
            </tbody>
          </table>
        </div>
      )}
    </div>
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

      <p className="mt-2 break-words text-xl font-semibold text-cyan-300">
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
  return (
    <span
      className={
        "inline-flex rounded-full border " +
        "px-2.5 py-1 text-xs font-medium " +
        getStatusColorClass(status)
      }
    >
      {formatLabel(status)}
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


function formatLabel(
  value: string,
): string {
  if (!value) {
    return "—";
  }

  return value
    .split("_")
    .map(
      (word) =>
        word.charAt(0).toUpperCase() +
        word.slice(1),
    )
    .join(" ");
}


function formatMonth(
  month: number,
): string {
  if (
    !Number.isInteger(month) ||
    month < 1 ||
    month > 12
  ) {
    return String(month);
  }

  return new Intl.DateTimeFormat(
    "en-US",
    {
      month: "long",
      timeZone: "UTC",
    },
  ).format(
    new Date(
      Date.UTC(2023, month - 1, 1),
    ),
  );
}


function formatDate(
  value: string | null,
): string {
  if (!value) {
    return "—";
  }

  const date = new Date(value);

  if (
    Number.isNaN(date.getTime())
  ) {
    return value;
  }

  return new Intl.DateTimeFormat(
    "en-US",
    {
      year: "numeric",
      month: "short",
      day: "numeric",
    },
  ).format(date);
}


function formatDateTime(
  value: string | null,
): string {
  if (!value) {
    return "—";
  }

  const date = new Date(value);

  if (
    Number.isNaN(date.getTime())
  ) {
    return value;
  }

  return new Intl.DateTimeFormat(
    "en-US",
    {
      year: "numeric",
      month: "short",
      day: "numeric",
      hour: "2-digit",
      minute: "2-digit",
      second: "2-digit",
    },
  ).format(date);
}


function calculateMean(
  values: Array<
    number | null | undefined
  >,
): number | null {
  const validValues = values.filter(
    (value): value is number =>
      value !== null &&
      value !== undefined &&
      Number.isFinite(value),
  );

  if (validValues.length === 0) {
    return null;
  }

  return (
    validValues.reduce(
      (total, value) =>
        total + value,
      0,
    ) / validValues.length
  );
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


function getErrorMessage(
  error: unknown,
  fallback: string,
): string {
  return error instanceof Error
    ? error.message
    : fallback;
}