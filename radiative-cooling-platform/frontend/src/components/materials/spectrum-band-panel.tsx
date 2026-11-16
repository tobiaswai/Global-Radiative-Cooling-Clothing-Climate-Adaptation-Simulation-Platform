"use client";

import Link from "next/link";
import { useState } from "react";

import { getSpectrumBandSummary } from "@/lib/api-client";
import { formatNumber } from "@/lib/format";
import { broadbandEmissivity } from "@/lib/planck";
import type { SpectrumBandSummary } from "@/types/material";

const MINIMUM_COVERAGE = 0.95;

export function SpectrumBandPanel({
  materialId,
  versionId,
  versionNumber,
}: {
  materialId: string;
  versionId: string;
  versionNumber: number;
}) {
  const [summary, setSummary] = useState<SpectrumBandSummary | null>(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function load() {
    setLoading(true);
    setError("");
    try {
      setSummary(await getSpectrumBandSummary(versionId, "mir_emissivity"));
    } catch (caught) {
      setError(caught instanceof Error ? caught.message : "Unable to summarise spectrum");
    } finally {
      setLoading(false);
    }
  }

  const windowValue = summary?.window_average ?? null;
  const outside = summary?.outside_window_average ?? null;
  const broadband = windowValue !== null && outside !== null ? broadbandEmissivity(windowValue, outside) : null;
  const usable = summary !== null && windowValue !== null && broadband !== null && summary.window_coverage >= MINIMUM_COVERAGE;

  const href =
    usable && broadband !== null && windowValue !== null
      ? `/materials/${materialId}/versions/new?ir_window=${windowValue.toFixed(4)}` +
        `&ir_broadband=${broadband.toFixed(4)}&from_version=${versionNumber}&t=${summary!.temperature_k}`
      : null;

  return (
    <div className="mt-3 rounded-lg border border-slate-800 bg-slate-950 p-4 text-sm">
      <button type="button" onClick={() => void load()} disabled={loading}
        className="rounded-lg border border-cyan-800 px-3 py-1.5 text-cyan-300 disabled:opacity-50">
        {loading ? "Integrating…" : "Derive band emissivities (Planck-weighted)"}
      </button>

      {error && <p className="mt-2 text-red-300">{error}</p>}

      {summary && (
        <>
          <dl className="mt-3 grid gap-3 sm:grid-cols-4">
            <Pair label={`ε_W (${summary.window_lower_um}–${summary.window_upper_um} µm)`} value={formatNumber(windowValue, 3)} />
            <Pair label="ε_N (measured, outside window)" value={formatNumber(outside, 3)} />
            <Pair label={`Broadband ε (${summary.temperature_k} K)`} value={formatNumber(broadband, 3)} />
            <Pair label="Window / total coverage"
              value={`${(summary.window_coverage * 100).toFixed(1)} % / ${(summary.broadband_coverage * 100).toFixed(1)} %`} />
          </dl>
          {summary.window_coverage < MINIMUM_COVERAGE && (
            <p className="mt-2 text-amber-300">
              The spectrum covers less than {MINIMUM_COVERAGE * 100} % of the window&apos;s blackbody emission; values are not used.
            </p>
          )}
          {summary.broadband_coverage < MINIMUM_COVERAGE && (
            <p className="mt-2 text-xs text-slate-500">
              Broadband ε assumes the measured out-of-window average also holds outside{" "}
              {summary.measured_lower_um}–{summary.measured_upper_um} µm.
            </p>
          )}
          {href && (
            <Link href={href} className="mt-3 inline-block text-cyan-300 underline">
              Create a new version with these values →
            </Link>
          )}
        </>
      )}
    </div>
  );
}

function Pair({ label, value }: { label: string; value: string }) {
  return (
    <div>
      <dt className="text-xs text-slate-500">{label}</dt>
      <dd className="mt-1 font-mono text-cyan-300">{value}</dd>
    </div>
  );
}