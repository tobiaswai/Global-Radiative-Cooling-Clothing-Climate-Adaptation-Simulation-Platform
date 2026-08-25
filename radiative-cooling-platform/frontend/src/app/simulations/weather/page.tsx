"use client";

import {
  type FormEvent,
  useEffect,
  useState,
} from "react";
import { useRouter } from "next/navigation";

import {
  createSimulationJob,
  getCities,
} from "@/lib/api-client";
import type {
  City,
  WeatherSimulationRequest,
} from "@/types/simulation";


const initialRequest: WeatherSimulationRequest = {
  city_id: "dubai",
  start_time_local: "2025-07-15T10:00",
  duration_minutes: 120,
  output_interval_minutes: 1,

  person: {
    met: 2.6,
    body_surface_area_m2: 1.8,
    initial_core_temperature_c: 36.8,
    initial_skin_temperature_c: 33.7,
  },

  control_material: {
    name: "Ordinary clothing",
    clothing_insulation_clo: 0.5,
    solar_reflectance: 0.4,
    solar_transmittance: 0,
    infrared_emissivity: 0.8,
    projected_solar_area_factor: 0.25,
    absorbed_solar_to_body_fraction: 0.35,
  },

  rc_material: {
    name: "Radiative Cooling Clothing",
    clothing_insulation_clo: 0.4,
    solar_reflectance: 0.92,
    solar_transmittance: 0,
    infrared_emissivity: 0.95,
    projected_solar_area_factor: 0.25,
    absorbed_solar_to_body_fraction: 0.35,
  },
};


export default function WeatherSimulationPage() {
  const router = useRouter();

  const [cities, setCities] =
    useState<City[]>([]);

  const [request, setRequest] =
    useState<WeatherSimulationRequest>(
      initialRequest,
    );

  const [loadingCities, setLoadingCities] =
    useState(true);

  const [submitting, setSubmitting] =
    useState(false);

  const [error, setError] =
    useState("");


  useEffect(() => {
    let cancelled = false;

    async function loadCities() {
      setLoadingCities(true);
      setError("");

      try {
        const cityList = await getCities();

        if (!cancelled) {
          setCities(cityList);
        }
      } catch (caughtError) {
        if (!cancelled) {
          setError(
            caughtError instanceof Error
              ? caughtError.message
              : "Unable to load city list",
          );
        }
      } finally {
        if (!cancelled) {
          setLoadingCities(false);
        }
      }
    }

    void loadCities();

    return () => {
      cancelled = true;
    };
  }, []);


  async function handleSubmit(
    event: FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault();

    if (submitting) {
      return;
    }

    setSubmitting(true);
    setError("");

    try {
      const job =
        await createSimulationJob(request);

      router.push(
        `/simulations/${job.id}`,
      );
    } catch (caughtError) {
      setError(
        caughtError instanceof Error
          ? caughtError.message
          : "Unable to create simulation job",
      );

      setSubmitting(false);
    }
  }


  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <div className="mx-auto max-w-7xl px-6 py-10">
        <header>
          <p className="text-sm font-medium text-cyan-400">
            Historical Weather Simulation
          </p>

          <h1 className="mt-2 text-3xl font-bold">
            Historical Weather-Driven Simulation
          </h1>

          <p className="mt-3 max-w-3xl text-slate-400">
            Using ERA5 historical hourly weather data,
            create asynchronous dynamic simulation tasks for ordinary clothing and radiative cooling clothing.
          </p>
        </header>

        <form
          onSubmit={handleSubmit}
          className="mt-8 rounded-2xl border border-slate-800 bg-slate-900 p-6"
        >
          <div className="grid gap-5 md:grid-cols-2 lg:grid-cols-4">
            <label className="block">
              <span className="mb-2 block text-sm text-slate-300">
                City
              </span>

              <select
                value={request.city_id}
                disabled={
                  loadingCities
                  || submitting
                }
                onChange={(event) => {
                  setRequest((current) => ({
                    ...current,
                    city_id: event.target.value,
                  }));
                }}
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"
              >
                {loadingCities && (
                  <option value="">
                    Loading cities…
                  </option>
                )}

                {!loadingCities
                  && cities.length === 0 && (
                    <option value="">
                      No available cities
                    </option>
                  )}

                {cities.map((city) => (
                  <option
                    key={city.id}
                    value={city.id}
                  >
                    {city.name}－
                    {city.climate_type}
                  </option>
                ))}
              </select>
            </label>

            <label className="block">
              <span className="mb-2 block text-sm text-slate-300">
                Local Start Time
              </span>

              <input
                type="datetime-local"
                required
                value={
                  request.start_time_local
                }
                disabled={submitting}
                onChange={(event) => {
                  setRequest((current) => ({
                    ...current,
                    start_time_local:
                      event.target.value,
                  }));
                }}
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"
              />
            </label>

            <label className="block">
              <span className="mb-2 block text-sm text-slate-300">
                Simulation Duration (Minutes)
              </span>

              <input
                type="number"
                required
                min={1}
                max={1440}
                step={1}
                value={
                  request.duration_minutes
                }
                disabled={submitting}
                onChange={(event) => {
                  setRequest((current) => ({
                    ...current,
                    duration_minutes: Number(
                      event.target.value,
                    ),
                  }));
                }}
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"
              />
            </label>

            <label className="block">
              <span className="mb-2 block text-sm text-slate-300">
                Activity Intensity (MET)
              </span>

              <input
                type="number"
                required
                min={0.7}
                max={10}
                step={0.1}
                value={request.person.met}
                disabled={submitting}
                onChange={(event) => {
                  const met = Number(
                    event.target.value,
                  );

                  setRequest((current) => ({
                    ...current,
                    person: {
                      ...current.person,
                      met,
                    },
                  }));
                }}
                className="w-full rounded-lg border border-slate-700 bg-slate-950 px-3 py-2 outline-none focus:border-cyan-500 disabled:cursor-not-allowed disabled:opacity-50"
              />
            </label>
          </div>

          <section className="mt-8 rounded-xl border border-slate-800 bg-slate-950/50 p-5">
            <h2 className="text-lg font-semibold">
              Simulation Configuration Summary
            </h2>

            <dl className="mt-4 grid gap-4 text-sm sm:grid-cols-2 lg:grid-cols-4">
              <div>
                <dt className="text-slate-500">
                  Output Interval
                </dt>
                <dd className="mt-1 text-slate-200">
                  {
                    request
                      .output_interval_minutes
                  }{" "}
                  minutes
                </dd>
              </div>

              <div>
                <dt className="text-slate-500">
                  Control Clothing
                </dt>
                <dd className="mt-1 text-slate-200">
                  {
                    request.control_material
                      .clothing_insulation_clo
                  }{" "}
                  clo
                </dd>
              </div>

              <div>
                <dt className="text-slate-500">
                  Control Clothing Solar Reflectance
                </dt>
                <dd className="mt-1 text-slate-200">
                  {
                    request.control_material
                      .solar_reflectance
                  }
                </dd>
              </div>

              <div>
                <dt className="text-slate-500">
                  RC Clothing Solar Reflectance
                </dt>
                <dd className="mt-1 text-slate-200">
                  {
                    request.rc_material
                      .solar_reflectance
                  }
                </dd>
              </div>
            </dl>
          </section>

          <button
            type="submit"
            disabled={
              submitting
              || loadingCities
              || cities.length === 0
            }
            className="mt-6 rounded-xl bg-cyan-400 px-7 py-3 font-semibold text-slate-950 transition hover:bg-cyan-300 disabled:cursor-not-allowed disabled:opacity-50"
          >
            {submitting
              ? "Simulation task being set up..."
              : "Create Historical Weather Simulation Task"}
          </button>

          {error && (
            <div
              role="alert"
              className="mt-5 rounded-lg border border-red-900 bg-red-950 p-4 text-red-300"
            >
              {error}
            </div>
          )}
        </form>

        <section className="mt-8 rounded-xl border border-slate-800 bg-slate-900/50 p-5 text-sm text-slate-400">
          <h2 className="font-semibold text-slate-200">
            Asynchronous Task Flow
          </h2>

          <ol className="mt-3 list-inside list-decimal space-y-2">
            <li>
              The frontend submits the simulation configuration to FastAPI.
            </li>
            <li>
              The backend creates a task record in PostgreSQL.
            </li>
            <li>
              The Celery Worker downloads weather data and executes the numerical simulation.
            </li>
            <li>
              Upon successful creation, the page will automatically redirect to the task progress page.
            </li>
          </ol>
        </section>
      </div>
    </main>
  );
}