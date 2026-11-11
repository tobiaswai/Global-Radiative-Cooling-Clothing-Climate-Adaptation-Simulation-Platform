"use client";

import dynamic from "next/dynamic";
import type { Data } from "plotly.js";

import { hasOptionalSeries, pluckOptionalSeries } from "@/lib/time-series";
import type { SimulationResponse } from "@/types/simulation";

const Plot = dynamic(() => import("react-plotly.js"), {
  ssr: false,
  loading: () => (
    <div className="flex h-96 items-center justify-center text-slate-400">
      Loading charts...
    </div>
  ),
});

type TemperatureChartProps = {
  result: SimulationResponse;
};

export function TemperatureChart({ result }: TemperatureChartProps) {
  const control = result.control.time_series;
  const rc = result.radiative_cooling.time_series;

  const controlMinutes = control.map((point) => point.minute);
  const rcMinutes = rc.map((point) => point.minute);

  const hasClothingSurface =
    hasOptionalSeries(control, "clothing_surface_temperature_c") ||
    hasOptionalSeries(rc, "clothing_surface_temperature_c");

  const data: Data[] = [
    {
      x: controlMinutes,
      y: control.map((point) => point.skin_temperature_c),
      type: "scatter",
      mode: "lines",
      name: "Standard Clothing: Skin Temperature",
      line: { color: "#f97316", width: 3 },
    },
    {
      x: rcMinutes,
      y: rc.map((point) => point.skin_temperature_c),
      type: "scatter",
      mode: "lines",
      name: "Radiative Cooling: Skin Temperature",
      line: { color: "#22d3ee", width: 3 },
    },
    {
      x: controlMinutes,
      y: control.map((point) => point.core_temperature_c),
      type: "scatter",
      mode: "lines",
      name: "Standard Clothing: Core Temperature",
      line: { color: "#ef4444", width: 2, dash: "dot" },
    },
    {
      x: rcMinutes,
      y: rc.map((point) => point.core_temperature_c),
      type: "scatter",
      mode: "lines",
      name: "Radiative Cooling: Core Temperature",
      line: { color: "#3b82f6", width: 2, dash: "dot" },
    },
  ];

  if (hasClothingSurface) {
    data.push(
      {
        x: controlMinutes,
        y: pluckOptionalSeries(control, "clothing_surface_temperature_c"),
        type: "scatter",
        mode: "lines",
        name: "Standard Clothing: Clothing Surface",
        line: { color: "#fdba74", width: 2, dash: "dashdot" },
        visible: "legendonly",
      },
      {
        x: rcMinutes,
        y: pluckOptionalSeries(rc, "clothing_surface_temperature_c"),
        type: "scatter",
        mode: "lines",
        name: "Radiative Cooling: Clothing Surface",
        line: { color: "#67e8f9", width: 2, dash: "dashdot" },
        visible: "legendonly",
      },
    );
  }

  return (
    <div className="overflow-hidden rounded-2xl border border-slate-800 bg-slate-900 p-4">
      <h2 className="mb-4 text-xl font-semibold">
        Human Body Temperature Dynamics
      </h2>

      <Plot
        data={data}
        layout={{
          autosize: true,
          height: 480,
          paper_bgcolor: "#0f172a",
          plot_bgcolor: "#0f172a",
          font: { color: "#cbd5e1" },
          margin: { l: 65, r: 30, t: 20, b: 60 },
          xaxis: { title: { text: "Time (min)" }, gridcolor: "#334155" },
          yaxis: { title: { text: "Temperature (°C)" }, gridcolor: "#334155" },
          legend: { orientation: "h", y: -0.25 },
          hovermode: "x unified",
        }}
        config={{
          responsive: true,
          displaylogo: false,
          toImageButtonOptions: {
            format: "png",
            filename: "temperature-comparison",
            scale: 2,
          },
        }}
        useResizeHandler
        style={{ width: "100%", height: "100%" }}
      />

      {hasClothingSurface && (
        <p className="mt-3 text-sm text-slate-400">
          Clothing surface temperature is hidden by default. Click its legend
          entry to overlay it on the skin and core curves.
        </p>
      )}
    </div>
  );
}