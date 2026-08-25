"use client";

import dynamic from "next/dynamic";

import type {
  WeatherTimeSeries,
} from "@/types/simulation";

const Plot = dynamic(
  () => import("react-plotly.js"),
  { ssr: false },
);

export function WeatherChart({
  weather,
}: {
  weather: WeatherTimeSeries;
}) {
  const points = weather.points;

  return (
    <section className="rounded-2xl border border-slate-800 bg-slate-900 p-5">
      <h2 className="text-xl font-semibold">
        Historical Weather Time Series
      </h2>

      <Plot
        data={[
          {
            x: points.map(
              (point) => point.timestamp,
            ),
            y: points.map(
              (point) =>
                point.air_temperature_c,
            ),
            name: "Air Temperature (°C)",
            type: "scatter",
            mode: "lines+markers",
            yaxis: "y",
          },
          {
            x: points.map(
              (point) => point.timestamp,
            ),
            y: points.map(
              (point) => point.ghi_w_m2,
            ),
            name: "GHI (W/m²)",
            type: "scatter",
            mode: "lines+markers",
            yaxis: "y2",
          },
          {
            x: points.map(
              (point) => point.timestamp,
            ),
            y: points.map(
              (point) =>
                point.relative_humidity_percent,
            ),
            name: "Relative Humidity (%)",
            type: "scatter",
            mode: "lines",
            yaxis: "y3",
            visible: "legendonly",
          },
        ]}
        layout={{
          autosize: true,
          height: 450,
          paper_bgcolor: "#0f172a",
          plot_bgcolor: "#0f172a",
          font: {
            color: "#cbd5e1",
          },
          margin: {
            l: 65,
            r: 70,
            t: 30,
            b: 70,
          },
          xaxis: {
            title: {
              text: "Local Time",
            },
            gridcolor: "#334155",
          },
          yaxis: {
            title: {
              text: "Air Temperature (°C)",
            },
            gridcolor: "#334155",
          },
          yaxis2: {
            title: {
              text: "GHI (W/m²)",
            },
            overlaying: "y",
            side: "right",
            gridcolor: "#334155",
          },
          yaxis3: {
            overlaying: "y",
            side: "right",
            visible: false,
          },
          hovermode: "x unified",
          legend: {
            orientation: "h",
            y: -0.25,
          },
        }}
        config={{
          responsive: true,
          displaylogo: false,
        }}
        useResizeHandler
        style={{
          width: "100%",
          height: "100%",
        }}
      />

      <div className="mt-4 border-t border-slate-800 pt-4 text-sm text-slate-400">
        <p>
          Data source:{weather.source.provider} /{" "}
          {weather.source.model}
        </p>
        <p>
          Grid Location:
          {weather.source.latitude.toFixed(4)},{" "}
          {weather.source.longitude.toFixed(4)}
        </p>
        <p>
          Cache:
          {weather.source.from_cache
            ? "Local Cache"
            : "Current API Download"}
        </p>

        <p className="mt-2">
          Weather data by Open-Meteo.com
        </p>
      </div>
    </section>
  );
}