"use client";

import {
  useEffect,
  useRef,
} from "react";

import type * as GeoJSON from "geojson";
import * as maplibregl from "maplibre-gl";

import type {
  GeoJsonFeatureCollection,
} from "@/types/global-batch";


type Props = {
  data: GeoJsonFeatureCollection;
};


const ADAPTATION_SOURCE_ID =
  "adaptation";

const ADAPTATION_LAYER_ID =
  "adaptation-circles";


export default function GlobalAdaptationMap({
  data,
}: Props) {
  const containerRef =
    useRef<HTMLDivElement | null>(null);

  const mapRef =
    useRef<maplibregl.Map | null>(null);

  /*
   * useRef 的 initialValue 只會在第一次 render 時使用。
   * 後續資料更新會在下方的 useEffect 中同步。
   */
  const dataRef =
    useRef<GeoJsonFeatureCollection>(data);

  useEffect(() => {
    if (!containerRef.current) {
      return;
    }

    const map = new maplibregl.Map({
      container: containerRef.current,

      style: {
        version: 8,

        sources: {
          openstreetmap: {
            type: "raster",

            tiles: [
              "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
            ],

            tileSize: 256,

            attribution:
              "© OpenStreetMap contributors",
          },
        },

        layers: [
          {
            id: "openstreetmap",
            type: "raster",
            source: "openstreetmap",
          },
        ],
      },

      center: [20, 15],
      zoom: 1.2,
      minZoom: 1,
      maxZoom: 12,
    });

    mapRef.current = map;

    map.addControl(
      new maplibregl.NavigationControl({
        showCompass: true,
        showZoom: true,
        visualizePitch: true,
      }),
      "top-right",
    );

    map.addControl(
      new maplibregl.FullscreenControl(),
      "top-right",
    );

    map.on("load", () => {
      /*
       * load callback 可能延後執行，因此從 dataRef
       * 取得當時最新的 GeoJSON，而不是使用初次 render
       * 捕獲的 data。
       */
      map.addSource(
        ADAPTATION_SOURCE_ID,
        {
          type: "geojson",

          data:
            dataRef.current as GeoJSON.FeatureCollection,
        },
      );

      map.addLayer({
        id: ADAPTATION_LAYER_ID,
        type: "circle",
        source: ADAPTATION_SOURCE_ID,

        paint: {
          /*
           * 沒有 qualifying exposure 時 adaptation rate 為 null。
           * coalesce 將 null 視為 0，只用於決定圓形尺寸。
           */
          "circle-radius": [
            "interpolate",
            ["linear"],

            [
              "coalesce",

              [
                "get",
                "climate_adaptation_rate_percent",
              ],

              0,
            ],

            0,
            7,

            100,
            18,
          ],

          /*
           * null 代表城市沒有符合門檻的熱暴露資料，
           * 使用灰色顯示。
           */
          "circle-color": [
            "case",

            [
              "==",

              [
                "get",
                "climate_adaptation_rate_percent",
              ],

              null,
            ],

            "#64748b",

            [
              "interpolate",
              ["linear"],

              [
                "get",
                "climate_adaptation_rate_percent",
              ],

              0,
              "#ef4444",

              40,
              "#f59e0b",

              70,
              "#22d3ee",

              100,
              "#10b981",
            ],
          ],

          "circle-opacity": 0.85,
          "circle-stroke-color": "#ffffff",
          "circle-stroke-width": 1,
        },
      });

      map.on(
        "click",
        ADAPTATION_LAYER_ID,
        (event) => {
          const feature =
            event.features?.[0];

          if (
            !feature ||
            feature.geometry.type !== "Point"
          ) {
            return;
          }

          const properties =
            (
              feature.properties ?? {}
            ) as Record<string, unknown>;

          const coordinates = (
            feature.geometry as GeoJSON.Point
          ).coordinates.slice() as [
            number,
            number,
          ];

          /*
           * 當地圖跨越日期變更線時，確保 popup 出現在
           * 使用者點擊的世界副本，而不是另一側。
           */
          while (
            Math.abs(
              event.lngLat.lng -
                coordinates[0],
            ) > 180
          ) {
            coordinates[0] +=
              event.lngLat.lng >
              coordinates[0]
                ? 360
                : -360;
          }

          const adaptationRate =
            readNullableNumber(
              properties
                .climate_adaptation_rate_percent,
            );

          const exposureCoverage =
            readNullableNumber(
              properties
                .exposure_coverage_percent,
            );

          const averageSkinCooling =
            readNullableNumber(
              properties
                .annual_average_skin_improvement_c,
            );

          const maximumSkinCooling =
            readNullableNumber(
              properties
                .maximum_skin_improvement_c,
            );

          const effectiveCoolingHours =
            readNullableNumber(
              properties
                .effective_cooling_hours,
            );

          const sampledDayCount =
            readNullableNumber(
              properties.sampled_day_count,
            );

          const eligibleSampleCount =
            readNullableNumber(
              properties.eligible_sample_count,
            );

          const adaptationText =
            adaptationRate === null
              ? "No qualifying exposure"
              : `${adaptationRate.toFixed(1)}%`;

          const coverageText =
            exposureCoverage === null
              ? "—"
              : `${exposureCoverage.toFixed(1)}%`;

          const averageSkinText =
            averageSkinCooling === null
              ? "—"
              : `${averageSkinCooling.toFixed(
                  2,
                )} °C`;

          const maximumSkinText =
            maximumSkinCooling === null
              ? "—"
              : `${maximumSkinCooling.toFixed(
                  2,
                )} °C`;

          const effectiveCoolingHoursText =
            effectiveCoolingHours === null
              ? "—"
              : `${effectiveCoolingHours.toFixed(
                  1,
                )} hours`;

          const sampleCountText =
            sampledDayCount === null
              ? "—"
              : (
                  `${eligibleSampleCount ?? 0}` +
                  ` / ${sampledDayCount}`
                );

          const cityName = escapeHtml(
            readText(
              properties.city_name,
              "Unknown city",
            ),
          );

          const country = escapeHtml(
            readText(
              properties.country,
              "Unknown country",
            ),
          );

          new maplibregl.Popup({
            closeButton: true,
            closeOnClick: true,
            maxWidth: "320px",
          })
            .setLngLat(coordinates)
            .setHTML(`
              <div
                style="
                  color:#0f172a;
                  min-width:250px;
                  line-height:1.5;
                "
              >
                <strong
                  style="
                    display:block;
                    font-size:16px;
                    margin-bottom:2px;
                  "
                >
                  ${cityName}
                </strong>

                <div
                  style="
                    color:#475569;
                    font-size:13px;
                  "
                >
                  ${country}
                </div>

                <hr
                  style="
                    border:0;
                    border-top:1px solid #cbd5e1;
                    margin:10px 0;
                  "
                />

                <div>
                  <strong>
                    Exposure coverage:
                  </strong>
                  ${coverageText}
                </div>

                <div>
                  <strong>
                    Adaptation rate:
                  </strong>
                  ${adaptationText}
                </div>

                <div>
                  <strong>
                    Average skin cooling:
                  </strong>
                  ${averageSkinText}
                </div>

                <div>
                  <strong>
                    Maximum skin cooling:
                  </strong>
                  ${maximumSkinText}
                </div>

                <div>
                  <strong>
                    Effective cooling:
                  </strong>
                  ${effectiveCoolingHoursText}
                </div>

                <div>
                  <strong>
                    Eligible samples:
                  </strong>
                  ${sampleCountText}
                </div>
              </div>
            `)
            .addTo(map);
        },
      );

      map.on(
        "mouseenter",
        ADAPTATION_LAYER_ID,
        () => {
          map.getCanvas().style.cursor =
            "pointer";
        },
      );

      map.on(
        "mouseleave",
        ADAPTATION_LAYER_ID,
        () => {
          map.getCanvas().style.cursor = "";
        },
      );
    });

    return () => {
      map.remove();
      mapRef.current = null;
    };
  }, []);

  /*
   * React refs 不應在 render 階段讀寫。
   *
   * 在 effect 中同步最新的 data，並更新已存在的
   * MapLibre GeoJSON source。
   */
  useEffect(() => {
    dataRef.current = data;

    const map = mapRef.current;

    if (
      !map ||
      !map.isStyleLoaded()
    ) {
      return;
    }

    /*
     * getSource() 的回傳型別是通用 Source，
     * 因此必須明確縮窄為 GeoJSONSource，才能使用 setData()。
     */
    const source =
      map.getSource(
        ADAPTATION_SOURCE_ID,
      ) as
        | maplibregl.GeoJSONSource
        | undefined;

    if (!source) {
      return;
    }

    source.setData(
      data as GeoJSON.FeatureCollection,
    );
  }, [data]);

  return (
    <div className="relative">
      <div
        ref={containerRef}
        className="h-140 w-full overflow-hidden rounded-2xl"
        aria-label="Global climate adaptation map"
      />

      <MapLegend />
    </div>
  );
}


function MapLegend() {
  return (
    <div className="pointer-events-none absolute bottom-4 left-4 z-10 rounded-lg bg-white/95 px-4 py-3 text-xs text-slate-900 shadow-lg">
      <p className="mb-2 font-semibold">
        Climate Adaptation Rate
      </p>

      <div className="space-y-1.5">
        <LegendItem
          color="#64748b"
          label="No qualifying exposure"
        />

        <LegendItem
          color="#ef4444"
          label="0–39%"
        />

        <LegendItem
          color="#f59e0b"
          label="40–69%"
        />

        <LegendItem
          color="#22d3ee"
          label="70–99%"
        />

        <LegendItem
          color="#10b981"
          label="100%"
        />
      </div>
    </div>
  );
}


function LegendItem({
  color,
  label,
}: {
  color: string;
  label: string;
}) {
  return (
    <div className="flex items-center gap-2">
      <span
        className="h-3 w-3 rounded-full border border-white shadow-sm"
        style={{
          backgroundColor: color,
        }}
      />

      <span>{label}</span>
    </div>
  );
}


function readNullableNumber(
  value: unknown,
): number | null {
  if (
    value === null ||
    value === undefined ||
    value === ""
  ) {
    return null;
  }

  const numericValue = Number(value);

  if (!Number.isFinite(numericValue)) {
    return null;
  }

  return numericValue;
}


function readText(
  value: unknown,
  fallback: string,
): string {
  if (
    typeof value !== "string" ||
    value.trim() === ""
  ) {
    return fallback;
  }

  return value;
}


/*
 * MapLibre Popup 使用 setHTML，因此必須先 escape
 * 後端提供的城市名稱及國家名稱。
 */
function escapeHtml(
  value: string,
): string {
  return value.replace(
    /[&<>"']/g,
    (character) => {
      const replacements: Record<
        string,
        string
      > = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&#039;",
      };

      return replacements[character];
    },
  );
}