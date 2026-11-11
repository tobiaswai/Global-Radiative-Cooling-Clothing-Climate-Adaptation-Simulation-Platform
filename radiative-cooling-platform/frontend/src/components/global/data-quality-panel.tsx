"use client";

import type { GlobalCityResult } from "@/types/global-batch";

export function DataQualityPanel({ result }: { result: GlobalCityResult }) {
  const quality = result.data_quality ?? null;
  const definitions = result.metric_definitions ?? {};

  if (!quality) {
    return (
      <p className="text-sm text-slate-500">
        Data-quality metadata is not available for this result.
      </p>
    );
  }

  const reasons = Object.entries(quality?.skip_reasons ?? {});
  const hashes = Object.entries(quality?.monthly_weather_payload_sha256 ?? {});

  return (
    <div className="mt-8 grid gap-6 lg:grid-cols-2">
      {quality && (
        <section className="rounded-xl border border-slate-800 bg-slate-950/60 p-5">
          <h3 className="text-lg font-semibold">Data Quality</h3>

          <dl className="mt-3 grid grid-cols-2 gap-3 text-sm">
            <div>
              <dt className="text-slate-500">Skipped samples</dt>
              <dd className={quality.skipped_sample_count ? "text-amber-300" : "text-slate-200"}>
                {quality.skipped_sample_count ?? 0}
              </dd>
            </div>
            <div>
              <dt className="text-slate-500">Skipped weighted days</dt>
              <dd className="text-slate-200">{quality.skipped_weighted_days ?? 0}</dd>
            </div>
          </dl>

          {reasons.length > 0 && (
            <ul className="mt-3 space-y-1 text-xs text-slate-400">
              {reasons.map(([code, count]) => (
                <li key={code}>
                  <span className="font-mono text-amber-300">{code}</span> × {count}
                </li>
              ))}
            </ul>
          )}

          {hashes.length > 0 && (
            <details className="mt-3 text-xs text-slate-500">
              <summary className="cursor-pointer">Weather payload SHA-256 per month ({hashes.length})</summary>
              <ul className="mt-2 space-y-1 font-mono">
                {hashes.map(([month, digest]) => (
                  <li key={month}>
                    {month}: {digest ? `${digest.slice(0, 16)}…` : "— (restored from checkpoint)"}
                  </li>
                ))}
              </ul>
            </details>
          )}
        </section>
      )}

      {Object.keys(definitions).length > 0 && (
        <section className="rounded-xl border border-slate-800 bg-slate-950/60 p-5">
          <h3 className="text-lg font-semibold">Metric Definitions</h3>
          <dl className="mt-3 space-y-3 text-sm">
            {Object.entries(definitions).map(([key, definition]) => (
              <div key={key}>
                <dt className="font-mono text-cyan-300">{key}</dt>
                <dd className="mt-1 text-slate-300">{definition.display_name}</dd>
                {definition.formula && (
                  <dd className="mt-1 font-mono text-xs text-slate-400">{definition.formula}</dd>
                )}
                {definition.interpretation && (
                  <dd className="mt-1 text-xs leading-5 text-slate-500">{definition.interpretation}</dd>
                )}
              </div>
            ))}
          </dl>
        </section>
      )}
    </div>
  );
}