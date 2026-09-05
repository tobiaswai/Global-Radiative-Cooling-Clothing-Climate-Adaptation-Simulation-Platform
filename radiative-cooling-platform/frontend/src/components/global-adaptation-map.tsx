"use client";

import {
  useEffect,
  useRef,
} from "react";
import * as maplibregl from "maplibre-gl";
import type * as GeoJSON from "geojson";

import type {
  GeoJsonFeatureCollection,
} from "@/types/global-batch";


type Props = {
  data: GeoJsonFeatureCollection;
};


export default function GlobalAdaptationMap({
  data,
}: Props) {
  const containerRef =
    useRef<HTMLDivElement | null>(null);

  const mapRef =
    useRef<maplibregl.Map | null>(null);

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
    });

    mapRef.current = map;

    map.on("load", () => {
      map.addSource("adaptation", {
        type: "geojson",
        data: data as GeoJSON.FeatureCollection,
      });

      map.addLayer({
        id: "adaptation-circles",
        type: "circle",
        source: "adaptation",
        paint: {
          "circle-radius": [
            "interpolate",
            ["linear"],
            [
              "get",
              "climate_adaptation_rate_percent",
            ],
            0,
            7,
            100,
            18,
          ],
          "circle-color": [
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
          "circle-opacity": 0.85,
          "circle-stroke-color": "#ffffff",
          "circle-stroke-width": 1,
        },
      });

      map.on(
        "click",
        "adaptation-circles",
        (event) => {
            const feature =
                event.features?.[0];

          if (!feature) {
            return;
          }

          const properties =
            feature.properties;

          const coordinates = (
            feature.geometry as GeoJSON.Point
          ).coordinates.slice() as [
            number,
            number,
          ];

          new maplibregl.Popup()
            .setLngLat(coordinates)
            .setHTML(`
              <div style="color:#0f172a;min-width:210px">
                <strong>${properties?.city_name}</strong>
                <div>${properties?.country}</div>
                <hr style="margin:8px 0" />
                <div>
                  Adaptation rate:
                  ${Number(
                    properties?.climate_adaptation_rate_percent,
                  ).toFixed(1)}%
                </div>
                <div>
                  Average skin cooling:
                  ${Number(
                    properties?.annual_average_skin_improvement_c,
                  ).toFixed(2)} °C
                </div>
                <div>
                  Maximum skin cooling:
                  ${Number(
                    properties?.maximum_skin_improvement_c,
                  ).toFixed(2)} °C
                </div>
              </div>
            `)
            .addTo(map);
        },
      );

      map.on(
        "mouseenter",
        "adaptation-circles",
        () => {
          map.getCanvas().style.cursor =
            "pointer";
        },
      );

      map.on(
        "mouseleave",
        "adaptation-circles",
        () => {
          map.getCanvas().style.cursor = "";
        },
      );
    });

    return () => {
      map.remove();
      mapRef.current = null;
    };
  }, [data]);

  return (
    <div
      ref={containerRef}
      className="h-140 w-full overflow-hidden rounded-2xl"
    />
  );
}