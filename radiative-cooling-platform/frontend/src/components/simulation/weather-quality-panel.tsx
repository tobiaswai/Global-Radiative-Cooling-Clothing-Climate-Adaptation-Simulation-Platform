import { formatRelativeTime } from "@/lib/relative-time";
import type { WeatherTimeSeries } from "@/types/simulation";

export function WeatherQualityPanel({ weather }: { weather: WeatherTimeSeries }) {
  const quality = weather.source.quality ?? null;

  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="text-xl font-semibold">Weather Data Quality</h2>
      <p className="mt-2 text-sm text-slate-400">
        Provenance and timeline audit of the ERA5 series that drove this run.
      </p>

      <dl className="mt-5 grid gap-4 text-sm sm:grid-cols-2 lg:grid-cols-4">
        <Item label="Payload SHA-256">
          <span className="font-mono" title={weather.source.payload_sha256 ?? undefined}>
            {weather.source.payload_sha256 ? `${weather.source.payload_sha256.slice(0, 16)}…` : "—"}
          </span>
        </Item>
        <Item label="Cache">{weather.source.from_cache ? "Local cache" : "Downloaded"}</Item>
        <Item label="Downloaded">{formatRelativeTime(weather.source.downloaded_at)}</Item>
        <Item label="Points in window">{weather.points.length}</Item>
      </dl>

      {quality ? (
        <dl className="mt-5 grid gap-4 text-sm sm:grid-cols-2 lg:grid-cols-4">
          <Item label="Expected step">{quality.expected_step_seconds} s</Item>
          <Item label="Sorted on arrival">{quality.was_sorted ? "Yes" : "No (sorted)"}</Item>
          <Item label="Duplicates removed">{quality.duplicates_removed}</Item>
          <Item label="Gaps">
            <span className={quality.gaps.length ? "text-amber-300" : ""}>{quality.gaps.length}</span>
          </Item>
        </dl>
      ) : (
        <p className="mt-5 text-sm text-slate-500">
          No quality report was stored with this result (recorded before Stage 1 PR-1).
        </p>
      )}

      {quality && quality.notes.length > 0 && (
        <ul className="mt-4 list-inside list-disc space-y-1 text-xs text-slate-400">
          {quality.notes.map((note) => <li key={note}>{note}</li>)}
        </ul>
      )}
    </section>
  );
}

function Item({ label, children }: { label: string; children: React.ReactNode }) {
  return (
    <div>
      <dt className="text-slate-500">{label}</dt>
      <dd className="mt-1 text-slate-200">{children}</dd>
    </div>
  );
}