"use client";

import Link from "next/link";
import { useParams } from "next/navigation";
import { useEffect, useState } from "react";

import { LeaseBadge } from "@/components/global/lease-badge";
import { ConvergenceChart } from "@/components/optimization/convergence-chart";
import { RequirementMapChart } from "@/components/optimization/requirement-map-chart";
import { cancelOptimization, getOptimization } from "@/lib/api-client";
import { formatNumber, formatSignedNumber } from "@/lib/format";
import {
  METRIC_LABELS,
  OBJECTIVE_LABELS,
  TERMINAL_OPTIMIZATION,
  TREND_LABELS,
  VARIABLE_LABELS,
  mapMetricFor,
} from "@/lib/optimization-labels";
import type {
  CandidateEvaluation,
  DecisionVariableName,
  MetricName,
  OptimizationCreate,
  OptimizationJobDetail,
  OptimizationResult,
  RequirementMapResult,
} from "@/types/optimization";

export default function OptimizationDetailPage() {
  const { optimizationId } = useParams<{ optimizationId: string }>();
  const [job, setJob] = useState<OptimizationJobDetail | null>(null);
  const [error, setError] = useState("");
  const [revision, setRevision] = useState(0);
  const [cancelling, setCancelling] = useState(false);

  useEffect(() => {
    let disposed = false;
    let timer: number | null = null;

    async function load() {
      try {
        const detail = await getOptimization(optimizationId);
        if (disposed) return;
        setJob(detail);
        setError("");
        if (!TERMINAL_OPTIMIZATION.has(detail.status)) timer = window.setTimeout(load, 3000);
      } catch (caught) {
        if (disposed) return;
        setError(caught instanceof Error ? caught.message : "Unable to load optimization");
        timer = window.setTimeout(load, 5000);
      }
    }

    void load();
    return () => {
      disposed = true;
      if (timer !== null) window.clearTimeout(timer);
    };
  }, [optimizationId, revision]);

  async function handleCancel() {
    setCancelling(true);
    try {
      await cancelOptimization(optimizationId);
      setRevision((r) => r + 1);
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Unable to cancel");
    } finally {
      setCancelling(false);
    }
  }

  if (!job) {
    return (
      <main className="min-h-screen bg-slate-950 p-10 text-white">
        {error ? <div className="rounded-lg border border-red-900 bg-red-950 p-4 text-red-300">{error}</div>
               : <p className="text-slate-400">Loading…</p>}
      </main>
    );
  }

  const objective = job.request.objective.metric;
  const result = job.result;
  const terminal = TERMINAL_OPTIMIZATION.has(job.status);

  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl space-y-8 px-6 py-10">
        <nav className="text-sm text-slate-400">
          <Link href="/optimizations" className="hover:text-white">Inverse Design</Link> /{" "}
          <span className="text-slate-200">{job.name}</span>
        </nav>

        <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
          <div className="flex flex-wrap items-start justify-between gap-4">
            <div>
              <h1 className="text-2xl font-bold">{job.name}</h1>
              <p className="mt-1 text-sm text-slate-400">
                {job.city_id} · months {job.request.months.join(", ")} · {job.request.variables.length} variable(s) ·
                objective: {job.request.objective.sense} {OBJECTIVE_LABELS[objective]}
              </p>
            </div>
            <div className="flex items-center gap-4">
              <LeaseBadge leaseState={job.lease_state} leaseOwner={job.lease_owner}
                lastHeartbeatAt={job.last_heartbeat_at} leaseExpiresAt={job.lease_expires_at} />
              {!terminal && (
                <button type="button" onClick={handleCancel} disabled={cancelling || job.status === "cancelling"}
                  className="rounded-lg border border-red-800 px-4 py-2 text-red-300 disabled:opacity-50">
                  {job.status === "cancelling" ? "Cancel requested…" : "Cancel"}
                </button>
              )}
            </div>
          </div>
          <div className="mt-5 h-3 overflow-hidden rounded-full bg-slate-800">
            <div className="h-full bg-cyan-400 transition-all" style={{ width: `${job.progress}%` }} />
          </div>
          <p className="mt-2 text-sm text-slate-400">
            {job.status} · {job.stage} · {job.evaluation_count} evaluations · {job.progress}%
          </p>
          {job.error_message && <p className="mt-3 text-sm text-red-300">{job.error_message}</p>}
          {error && <p className="mt-3 text-sm text-red-300">{error}</p>}
        </section>

        {result && <VerdictCard result={result} />}
        {result && (result.warnings?.length ?? 0) > 0 && <WarningsPanel warnings={result.warnings!} />}
        {job.history.length > 0 && <ConvergenceChart history={job.history} metric={objective} />}
        {result && <CandidateTable result={result} request={job.request} />}
        {result && (result.sensitivities?.length ?? 0) > 0 && <SensitivityTable result={result} request={job.request} />}
        {result?.requirement_map && (
          <RequirementMapChart map={result.requirement_map} metric={mapMetricFor(job.request).metric} />
        )}
        {result && <RunRecord result={result} />}
      </div>
    </main>
  );
}

function VerdictCard({ result }: { result: OptimizationResult }) {
  const tone = result.verdict === "infeasible"
    ? "border-red-800 bg-red-950/40 text-red-200"
    : "border-emerald-800 bg-emerald-950/40 text-emerald-200";
  const map = result.requirement_map;

  return (
    <section className={`rounded-2xl border p-6 ${tone}`}>
      <p className="text-sm uppercase tracking-wide opacity-70">Verdict</p>
      <p className="mt-1 text-3xl font-bold">{result.verdict.toUpperCase()}</p>
      <p className="mt-3 max-w-4xl">{result.message}</p>
      {map && <RequirementReadings map={map} />}
    </section>
  );
}

function RequirementReadings({ map }: { map: RequirementMapResult }) {
  const step = (values: number[]) => (values.length > 1 ? Math.abs(values[1] - values[0]) : 0);
  const rows = [
    { variable: map.x_variable, value: map.required_x_at_best_y ?? map.minimum_x_at_max_y,
      direction: map.x_demand_direction ?? "increasing", trend: map.objective_trend_x, step: step(map.x_values) },
    { variable: map.y_variable, value: map.required_y_at_best_x ?? map.minimum_y_at_max_x,
      direction: map.y_demand_direction ?? "increasing", trend: map.objective_trend_y, step: step(map.y_values) },
  ];

  return (
    <div className="mt-5 grid gap-4 sm:grid-cols-2">
      {rows.map((row) => (
        <div key={row.variable} className="rounded-xl border border-slate-700 bg-slate-950/60 p-4">
          <p className="text-sm text-slate-400">Requirement on {VARIABLE_LABELS[row.variable]}</p>
          <p className="mt-1 text-2xl font-semibold text-white">
            {row.value === null || row.value === undefined
              ? "not reachable"
              : `${row.direction === "increasing" ? "≥" : "≤"} ${row.value.toFixed(3)}`}
          </p>
          <p className="mt-1 text-xs text-slate-500">
            Least demanding feasible value anywhere on the map (± {row.step.toFixed(3)} grid step).
            {row.trend && ` Metric ${TREND_LABELS[row.trend]} along this axis.`}
          </p>
        </div>
      ))}
    </div>
  );
}

function WarningsPanel({ warnings }: { warnings: string[] }) {
  return (
    <section className="rounded-2xl border border-amber-800 bg-amber-950/30 p-6">
      <h2 className="text-lg font-semibold text-amber-200">Interpretation warnings</h2>
      <ul className="mt-3 list-inside list-disc space-y-2 text-sm text-amber-100">
        {warnings.map((warning) => <li key={warning}>{warning}</li>)}
      </ul>
    </section>
  );
}

function CandidateTable({ result, request }: { result: OptimizationResult; request: OptimizationCreate }) {
  const columns: [string, CandidateEvaluation | null | undefined][] = [
    ["Baseline", result.baseline],
    ["Best found", result.best],
    ["Best corner", result.best_corner],
    ["Most demanding", result.optical_upper_bound],
  ];
  const parameterNames = Object.keys(result.best.parameters) as DecisionVariableName[];
  const metricNames = Object.keys(METRIC_LABELS) as MetricName[];
  const highlighted = new Set<string>([request.objective.metric, ...request.constraints.map((c) => c.metric)]);
  const constraintLabels = Object.keys(result.best.constraint_excess ?? {});

  return (
    <section className="overflow-x-auto rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="text-xl font-semibold">Candidates</h2>
      <table className="mt-4 w-full min-w-[56rem] text-left text-sm">
        <thead className="border-b border-slate-700 text-slate-400">
          <tr>
            <th className="px-3 py-2">Quantity</th>
            {columns.map(([label]) => <th key={label} className="px-3 py-2">{label}</th>)}
          </tr>
        </thead>
        <tbody>
          {parameterNames.map((name) => (
            <tr key={name} className="border-b border-slate-800">
              <td className="px-3 py-2 text-slate-300">{VARIABLE_LABELS[name]}</td>
              {columns.map(([label, c]) => <td key={label} className="px-3 py-2 font-mono">{formatNumber(c?.parameters[name], 3)}</td>)}
            </tr>
          ))}
          <tr className="border-b border-slate-800">
            <td className="px-3 py-2 text-slate-300">Material demand</td>
            {columns.map(([label, c]) => <td key={label} className="px-3 py-2">{formatNumber(c?.material_demand, 3)}</td>)}
          </tr>
          {metricNames.map((name) => (
            <tr key={name} className={`border-b border-slate-800 ${highlighted.has(name) ? "bg-cyan-950/30" : ""}`}>
              <td className="px-3 py-2 text-slate-300">{METRIC_LABELS[name]}</td>
              {columns.map(([label, c]) => <td key={label} className="px-3 py-2">{formatNumber(c?.metrics?.[name], 3)}</td>)}
            </tr>
          ))}
          {constraintLabels.map((label) => (
            <tr key={label} className="border-b border-slate-800">
              <td className="px-3 py-2 font-mono text-xs text-slate-300">excess: {label}</td>
              {columns.map(([column, c]) => {
                const value = c?.constraint_excess?.[label];
                return (
                  <td key={column} className={`px-3 py-2 ${value !== undefined && value > 0 ? "text-red-300" : "text-emerald-300"}`}>
                    {formatSignedNumber(value, 4)}
                  </td>
                );
              })}
            </tr>
          ))}
          <tr>
            <td className="px-3 py-2 text-slate-300">Constraints satisfied</td>
            {columns.map(([label, c]) => (
              <td key={label} className={`px-3 py-2 ${c?.feasible ? "text-emerald-300" : "text-red-300"}`}>
                {c ? (c.metrics ? (c.feasible ? "yes" : `no (normalised ${formatNumber(c.constraint_violation, 3)})`) : "impossible") : "—"}
              </td>
            ))}
          </tr>
        </tbody>
      </table>
    </section>
  );
}

function SensitivityTable({ result, request }: { result: OptimizationResult; request: OptimizationCreate }) {
  const metrics = Array.from(new Set<MetricName>([
    ...(request.objective.metric === "material_demand" ? [] : [request.objective.metric as MetricName]),
    ...request.constraints.map((c) => c.metric),
    "mean_skin_temperature_c",
  ]));

  return (
    <section className="overflow-x-auto rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="text-xl font-semibold">Sensitivity at the reported optimum</h2>
      <p className="mt-1 text-sm text-slate-400">
        Change of each metric if the variable swept its whole search range (central difference,
        linearised). Compare with the constraint excess to see whether a target is reachable at all.
      </p>
      <table className="mt-4 w-full min-w-[48rem] text-left text-sm">
        <thead className="border-b border-slate-700 text-slate-400">
          <tr>
            <th className="px-3 py-2">Variable</th>
            {metrics.map((m) => <th key={m} className="px-3 py-2">{METRIC_LABELS[m]}</th>)}
          </tr>
        </thead>
        <tbody>
          {result.sensitivities!.map((s) => (
            <tr key={s.name} className="border-b border-slate-800">
              <td className="px-3 py-2 text-slate-300">{VARIABLE_LABELS[s.name]}</td>
              {metrics.map((m) => <td key={m} className="px-3 py-2 font-mono">{formatSignedNumber(s.full_range_effects[m], 4)}</td>)}
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}

function RunRecord({ result }: { result: OptimizationResult }) {
  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6 text-sm text-slate-400">
      <h2 className="text-lg font-semibold text-slate-200">Run record</h2>
      <p className="mt-2">
        {result.sample_count} sample day(s), {result.skipped_samples.length} skipped ·{" "}
        {result.evaluation_count} garment evaluations · {result.simulation_count} thermal simulations ·{" "}
        {result.generations} generations · {result.elapsed_seconds.toFixed(1)} s
      </p>
      <p className="mt-1">
        Objective normalised as (value − {formatNumber(result.objective_reference, 4)}) / {formatNumber(result.objective_scale, 3)}.
      </p>
      <p className="mt-1 font-mono text-xs">
        model {result.model_version} · fingerprint {result.parameter_fingerprint.slice(0, 16)}… · {result.algorithm_message}
      </p>
    </section>
  );
}