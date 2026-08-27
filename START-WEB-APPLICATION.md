# Web Application Startup Guide

This document explains how to run the **Global Radiative Cooling Clothing Climate Adaptation Simulation Platform** locally.

The system includes the following services:

- PostgreSQL database
- Redis
- FastAPI backend
- Celery Worker
- Next.js frontend

---

## 1. Project Structure

Run the commands in this document from the repository root unless otherwise specified.

```text
Global-Radiative-Cooling-Clothing-Climate-Adaptation-Simulation-Platform/
├── .github/
├── docs/
├── scripts/
├── README.md
└── radiative-cooling-platform/
    ├── backend/
    ├── frontend/
    └── compose.yaml
```

Confirm the current repository root:

```bash
git rev-parse --show-toplevel
```

---

## 2. Install Required Software

Before starting the application, install the following software:

- Git
- Python 3.12
- Node.js 22
- npm
- Docker Desktop
- Visual Studio Code

Verify the installed versions:

```bash
git --version
python --version
node --version
npm --version
docker --version
docker compose version
```

Before starting PostgreSQL and Redis, make sure Docker Desktop is running.

---

## 3. Configure Environment Variables

### 3.1 Backend Environment Variables

Create the following file:

```text
radiative-cooling-platform/backend/.env
```

Add the following content:

```env
APP_NAME=Radiative Cooling Simulation API
APP_ENV=development

DATABASE_URL=postgresql+psycopg://rc_user:rc_password@localhost:5432/radiative_cooling

CELERY_BROKER_URL=redis://localhost:6379/0
CELERY_RESULT_BACKEND=redis://localhost:6379/1

FRONTEND_ORIGIN=http://localhost:3000
```

> The `.env` file is for local development only. Do not commit it to Git.

### 3.2 Frontend Environment Variables

Create the following file:

```text
radiative-cooling-platform/frontend/.env.local
```

Add the following content:

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

After modifying `.env.local`, restart Next.js.

---

## 4. Start PostgreSQL and Redis

Open the first terminal and navigate to the platform directory:

```bash
cd radiative-cooling-platform
```

Start the Docker services:

```bash
docker compose up -d
```

Check the container status:

```bash
docker compose ps
```

PostgreSQL and Redis should both be running.

### Check PostgreSQL

```bash
docker compose exec postgres pg_isready -U rc_user -d radiative_cooling
```

Expected output:

```text
accepting connections
```

### Check Redis

```bash
docker compose exec redis redis-cli ping
```

Expected output:

```text
PONG
```

### View Docker Logs

```bash
docker compose logs -f
```

Press `Ctrl+C` to exit the log view. This does not stop the containers.

---

## 5. Install Backend Dependencies

Open a second terminal:

```bash
cd radiative-cooling-platform/backend
```

### Windows PowerShell

Create a Python virtual environment:

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### Git Bash

```bash
source .venv/Scripts/activate
```

### macOS or Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Install Python Packages

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Verify that the FastAPI application can be imported:

```bash
python -c "from app.main import app; print(app.title)"
```

---

## 6. Run Database Migrations

Remain in the following directory:

```text
radiative-cooling-platform/backend
```

Run all Alembic migrations:

```bash
python -m alembic upgrade head
```

View the current migration version:

```bash
python -m alembic current
```

Check whether the models and migrations are synchronized:

```bash
python -m alembic check
```

Expected output:

```text
No new upgrade operations detected.
```

If you receive an error indicating that a database table does not exist, make sure PostgreSQL is running and execute the migration command again:

```bash
python -m alembic upgrade head
```

---

## 7. Start the FastAPI Backend

Remain in the backend directory:

```text
radiative-cooling-platform/backend
```

Run:

```bash
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Expected output:

```text
Uvicorn running on http://127.0.0.1:8000
Application startup complete.
```

Test the backend health endpoint:

```text
http://127.0.0.1:8000/api/v1/health
```

Open the Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

Open ReDoc:

```text
http://127.0.0.1:8000/redoc
```

Keep this terminal running.

---

## 8. Start the Celery Worker

Open a third terminal:

```bash
cd radiative-cooling-platform/backend
```

### Windows PowerShell

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Start the Celery Worker:

```powershell
celery -A app.worker.celery_app:celery_app worker --loglevel=info --pool=solo
```

For local development on Windows, using `--pool=solo` is recommended.

### macOS, Linux, or WSL2

```bash
source .venv/bin/activate
celery -A app.worker.celery_app:celery_app worker --loglevel=info --concurrency=2
```

After the Worker starts, it should list the available simulation tasks, for example:

```text
[tasks]
  . simulation.run_weather
```

Check whether the Worker responds:

```bash
celery -A app.worker.celery_app:celery_app inspect ping
```

Expected output:

```text
pong
```

Keep this terminal running.

---

## 9. Install Frontend Dependencies

Open a fourth terminal:

```bash
cd radiative-cooling-platform/frontend
```

For the first installation or a clean installation, run:

```bash
npm ci
```

If `package.json` and `package-lock.json` are not synchronized, run:

```bash
npm install
```

If `package-lock.json` changes, commit the updated file to Git.

### Windows EPERM Error

If Windows displays an error similar to the following:

```text
EPERM: operation not permitted, unlink
lightningcss.win32-x64-msvc.node
```

Stop all Node.js processes:

```powershell
taskkill /F /IM node.exe /T
```

Delete `node_modules`:

```powershell
cmd /c "rd /s /q node_modules"
```

Reinstall the dependencies:

```powershell
npm cache verify
npm ci
```

---

## 10. Start the Next.js Frontend

Remain in the frontend directory:

```text
radiative-cooling-platform/frontend
```

Run:

```bash
npm run dev
```

Expected output:

```text
Local: http://localhost:3000
```

Open the web application:

```text
http://localhost:3000
```

Common pages:

```text
http://localhost:3000/materials
http://localhost:3000/materials/new
http://localhost:3000/simulations
http://localhost:3000/simulations/new
http://localhost:3000/simulations/weather
```

Keep this frontend terminal running.

---

## 11. Terminal Configuration

A complete local development environment normally requires four terminals.

### Terminal 1: PostgreSQL and Redis

```bash
cd radiative-cooling-platform
docker compose up -d
```

### Terminal 2: FastAPI

Windows:

```powershell
cd radiative-cooling-platform/backend
.\.venv\Scripts\Activate.ps1
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

macOS or Linux:

```bash
cd radiative-cooling-platform/backend
source .venv/bin/activate
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### Terminal 3: Celery Worker

Windows:

```powershell
cd radiative-cooling-platform/backend
.\.venv\Scripts\Activate.ps1
celery -A app.worker.celery_app:celery_app worker --loglevel=info --pool=solo
```

macOS, Linux, or WSL2:

```bash
cd radiative-cooling-platform/backend
source .venv/bin/activate
celery -A app.worker.celery_app:celery_app worker --loglevel=info --concurrency=2
```

### Terminal 4: Next.js

```bash
cd radiative-cooling-platform/frontend
npm run dev
```

---

## 12. Recommended Startup Order

Start the services in the following order:

```text
1. Docker Desktop
2. PostgreSQL and Redis
3. Alembic migrations
4. FastAPI backend
5. Celery Worker
6. Next.js frontend
```

System request flow:

```text
Browser
  ↓
Next.js
  ↓
FastAPI
  ├── PostgreSQL
  └── Celery → Redis → Worker
                     ↓
              Simulation Result
```

---

## 13. Verify the System

### 13.1 Verify Docker Services

```bash
cd radiative-cooling-platform
docker compose ps
```

Confirm that PostgreSQL and Redis are running normally.

### 13.2 Verify the Backend

Open:

```text
http://127.0.0.1:8000/api/v1/health
```

Expected response:

```json
{
  "status": "healthy",
  "service": "radiative-cooling-api"
}
```

### 13.3 Verify the API Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

Confirm that the API groups are displayed correctly, for example:

- Benchmarks
- Materials
- Simulations
- Weather

### 13.4 Verify the Frontend

Open:

```text
http://localhost:3000
```

Confirm that the Materials and Simulations pages work correctly.

### 13.5 Verify an Asynchronous Simulation

1. Open the historical weather simulation page.
2. Select a city and date.
3. Submit the simulation.
4. Confirm that the page redirects to the Simulation Job page.
5. Confirm that the status changes from `queued` to `running`.
6. Wait for the status to change to `completed`.
7. Confirm that the charts and summary data are displayed correctly.
8. Test the CSV or JSON export feature.

---

## 14. Run Tests

### Backend Tests

Navigate to the backend directory:

```bash
cd radiative-cooling-platform/backend
```

Run all tests:

```bash
python -m pytest
```

Run tests and generate a coverage report:

```bash
python -m pytest --cov=app --cov-report=term-missing --cov-report=html
```

Run only unit tests:

```bash
python -m pytest -m unit
```

Run only integration tests:

```bash
python -m pytest -m integration
```

Run benchmark tests:

```bash
python -m pytest -m benchmark
```

### Frontend Checks

Navigate to the frontend directory:

```bash
cd radiative-cooling-platform/frontend
```

Run:

```bash
npm run lint
npm run build
```

---

## 15. Stop the System

### Stop FastAPI

In the FastAPI terminal, press:

```text
Ctrl+C
```

### Stop Celery

In the Celery terminal, press:

```text
Ctrl+C
```

On Windows, you may need to press it multiple times.

### Stop Next.js

In the frontend terminal, press:

```text
Ctrl+C
```

### Stop PostgreSQL and Redis

Navigate to:

```bash
cd radiative-cooling-platform
```

Stop the containers:

```bash
docker compose down
```

This command preserves the PostgreSQL and Redis volume data.

To delete the data as well:

```bash
docker compose down -v
```

> Warning: `docker compose down -v` permanently deletes the local PostgreSQL database and Redis data.

---

## 16. Quick Start

### Windows PowerShell

#### Start the Infrastructure Services

```powershell
cd radiative-cooling-platform
docker compose up -d
```

#### Start the Backend

```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python -m alembic upgrade head
python -m uvicorn app.main:app --reload --port 8000
```

#### Start Celery

Open a new PowerShell terminal:

```powershell
cd radiative-cooling-platform\backend
.\.venv\Scripts\Activate.ps1
celery -A app.worker.celery_app:celery_app worker --loglevel=info --pool=solo
```

#### Start the Frontend

Open a new PowerShell terminal:

```powershell
cd radiative-cooling-platform\frontend
npm run dev
```

### macOS, Linux, or WSL2

#### Start the Infrastructure Services and Backend

```bash
cd radiative-cooling-platform
docker compose up -d

cd backend
source .venv/bin/activate
python -m alembic upgrade head
python -m uvicorn app.main:app --reload --port 8000
```

#### Start Celery

Open a new terminal:

```bash
cd radiative-cooling-platform/backend
source .venv/bin/activate
celery -A app.worker.celery_app:celery_app worker --loglevel=info --concurrency=2
```

#### Start the Frontend

Open a new terminal:

```bash
cd radiative-cooling-platform/frontend
npm run dev
```

---

## 17. Local Service URLs

| Service | URL |
|---|---|
| Next.js frontend | `http://localhost:3000` |
| FastAPI backend | `http://localhost:8000` |
| Health API | `http://localhost:8000/api/v1/health` |
| Swagger UI | `http://localhost:8000/docs` |
| ReDoc | `http://localhost:8000/redoc` |
| PostgreSQL | `localhost:5432` |
| Redis | `localhost:6379` |

---

