#!/usr/bin/env bash

set -Eeuo pipefail

# ============================================================
# Radiative Cooling Platform Startup Script
#
# Startup order:
#   1. Activate the Python virtual environment
#   2. Start Redis
#   3. Start FastAPI
#   4. Start the Celery worker
#   5. Start the frontend
#
# The browser will not be opened automatically.
# ============================================================

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

BACKEND_DIR="${PROJECT_ROOT}/backend"
FRONTEND_DIR="${PROJECT_ROOT}/frontend"
LOG_DIR="${PROJECT_ROOT}/logs"
PID_DIR="${PROJECT_ROOT}/.pids"

# FastAPI settings
BACKEND_APP="${BACKEND_APP:-app.main:app}"
BACKEND_HOST="${BACKEND_HOST:-127.0.0.1}"
BACKEND_PORT="${BACKEND_PORT:-8000}"

# Celery settings
CELERY_APP="${CELERY_APP:-app.worker.celery_app:celery_app}"
CELERY_CONCURRENCY="${CELERY_CONCURRENCY:-4}"

# Redis settings
REDIS_HOST="${REDIS_HOST:-127.0.0.1}"
REDIS_PORT="${REDIS_PORT:-6379}"
REDIS_CONTAINER_NAME="${REDIS_CONTAINER_NAME:-radiative-cooling-redis}"

# Common frontend development-server ports
FRONTEND_PORTS=(5173 3000 8080)

mkdir -p "${LOG_DIR}" "${PID_DIR}"

# ============================================================
# Output colors
# ============================================================

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

info() {
    echo -e "${CYAN}[INFO]${NC} $*"
}

success() {
    echo -e "${GREEN}[OK]${NC} $*"
}

warning() {
    echo -e "${YELLOW}[WARNING]${NC} $*"
}

error() {
    echo -e "${RED}[ERROR]${NC} $*" >&2
}

section() {
    echo
    echo "============================================================"
    echo "$*"
    echo "============================================================"
}

# ============================================================
# Detect the operating system
# ============================================================

UNAME="$(uname -s)"

case "${UNAME}" in
    Linux*)
        PLATFORM="linux"
        ;;
    Darwin*)
        PLATFORM="macos"
        ;;
    MINGW*|MSYS*|CYGWIN*)
        PLATFORM="windows-bash"
        ;;
    *)
        PLATFORM="unknown"
        ;;
esac

info "Detected platform: ${PLATFORM}"

# ============================================================
# Port utilities
# ============================================================

port_is_open() {
    local host="$1"
    local port="$2"

    python - "${host}" "${port}" <<'PY'
import socket
import sys

host = sys.argv[1]
port = int(sys.argv[2])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(0.5)

try:
    sock.connect((host, port))
except OSError:
    sys.exit(1)
else:
    sys.exit(0)
finally:
    sock.close()
PY
}

wait_for_port() {
    local service_name="$1"
    local host="$2"
    local port="$3"
    local timeout="${4:-30}"

    info "Waiting for ${service_name} at ${host}:${port}"

    for ((i = 1; i <= timeout; i++)); do
        if port_is_open "${host}" "${port}"; then
            success "${service_name} is ready"
            return 0
        fi

        sleep 1
    done

    error "${service_name} did not open port ${port} within ${timeout} seconds"
    return 1
}

# ============================================================
# PID utilities
# ============================================================

save_pid() {
    local service="$1"
    local pid="$2"

    echo "${pid}" > "${PID_DIR}/${service}.pid"
}

process_is_running() {
    local pid="$1"

    [[ -n "${pid}" ]] && kill -0 "${pid}" 2>/dev/null
}

# ============================================================
# Validate the project structure
# ============================================================

section "Checking the project environment"

if [[ ! -d "${BACKEND_DIR}" ]]; then
    error "Backend directory not found: ${BACKEND_DIR}"
    exit 1
fi

if [[ ! -d "${FRONTEND_DIR}" ]]; then
    error "Frontend directory not found: ${FRONTEND_DIR}"
    exit 1
fi

if [[ ! -f "${FRONTEND_DIR}/package.json" ]]; then
    error "Frontend package.json not found: ${FRONTEND_DIR}/package.json"
    exit 1
fi

# ============================================================
# Activate the Python virtual environment
# ============================================================

section "Activating the Python virtual environment"

VENV_DIR="${BACKEND_DIR}/.venv"

if [[ -f "${VENV_DIR}/bin/activate" ]]; then
    # Linux, WSL2, and macOS
    VENV_ACTIVATE="${VENV_DIR}/bin/activate"
elif [[ -f "${VENV_DIR}/Scripts/activate" ]]; then
    # Windows Git Bash
    VENV_ACTIVATE="${VENV_DIR}/Scripts/activate"
else
    error "Python virtual environment not found: ${VENV_DIR}"

    echo
    echo "Create the virtual environment first:"
    echo
    echo "  cd \"${BACKEND_DIR}\""
    echo "  python -m venv .venv"
    echo
    echo "Linux, WSL2, or macOS:"
    echo "  source .venv/bin/activate"
    echo
    echo "Windows Git Bash:"
    echo "  source .venv/Scripts/activate"
    echo
    echo "Install the Python dependencies:"
    echo "  pip install -r requirements.txt"

    exit 1
fi

# shellcheck disable=SC1090
source "${VENV_ACTIVATE}"

success "Virtual environment activated: ${VIRTUAL_ENV:-${VENV_DIR}}"

if ! command -v python >/dev/null 2>&1; then
    error "Python was not found in the virtual environment"
    exit 1
fi

info "Python executable: $(command -v python)"
info "Python version: $(python --version 2>&1)"

# ============================================================
# Check required dependencies
# ============================================================

section "Checking dependencies"

if ! python -c "import uvicorn" >/dev/null 2>&1; then
    error "uvicorn is not installed in the virtual environment"
    echo
    echo "Install the backend dependencies with:"
    echo "  source \"${VENV_ACTIVATE}\""
    echo "  python -m pip install -r \"${BACKEND_DIR}/requirements.txt\""
    exit 1
fi

if ! python -c "import celery" >/dev/null 2>&1; then
    error "Celery is not installed in the virtual environment"
    echo
    echo "Install the backend dependencies with:"
    echo "  source \"${VENV_ACTIVATE}\""
    echo "  python -m pip install -r \"${BACKEND_DIR}/requirements.txt\""
    exit 1
fi

if ! command -v npm >/dev/null 2>&1; then
    error "npm was not found. Install Node.js before starting the system."
    exit 1
fi

success "Required dependencies are available"

# ============================================================
# 1. Start Redis
# ============================================================

section "1/4 Starting Redis"

if port_is_open "${REDIS_HOST}" "${REDIS_PORT}"; then
    success "Redis is already running at ${REDIS_HOST}:${REDIS_PORT}"
else
    if command -v redis-server >/dev/null 2>&1; then
        info "Starting Redis with the local redis-server command"

        redis-server \
            --bind "${REDIS_HOST}" \
            --port "${REDIS_PORT}" \
            > "${LOG_DIR}/redis.log" 2>&1 &

        REDIS_PID=$!
        save_pid "redis" "${REDIS_PID}"

    elif command -v docker >/dev/null 2>&1; then
        info "Local redis-server was not found; starting Redis with Docker"

        EXISTING_CONTAINER="$(
            docker ps -a \
                --filter "name=^/${REDIS_CONTAINER_NAME}$" \
                --format '{{.Names}}' 2>/dev/null || true
        )"

        if [[ "${EXISTING_CONTAINER}" == "${REDIS_CONTAINER_NAME}" ]]; then
            docker start "${REDIS_CONTAINER_NAME}" >/dev/null
        else
            docker run \
                --name "${REDIS_CONTAINER_NAME}" \
                --detach \
                --publish "${REDIS_PORT}:6379" \
                redis:7-alpine >/dev/null
        fi
    else
        error "Neither redis-server nor Docker was found"
        echo
        echo "Install Redis or Docker before starting the system."
        echo "Expected Redis address: redis://${REDIS_HOST}:${REDIS_PORT}/0"
        exit 1
    fi

    if ! wait_for_port "Redis" "${REDIS_HOST}" "${REDIS_PORT}" 30; then
        if [[ -f "${LOG_DIR}/redis.log" ]]; then
            echo
            error "Recent Redis log output:"
            tail -n 50 "${LOG_DIR}/redis.log" || true
        fi

        exit 1
    fi
fi

# ============================================================
# 2. Start FastAPI
# ============================================================

section "2/4 Starting the FastAPI backend"

if port_is_open "${BACKEND_HOST}" "${BACKEND_PORT}"; then
    success "FastAPI is already running at http://${BACKEND_HOST}:${BACKEND_PORT}"
else
    info "Starting FastAPI application: ${BACKEND_APP}"

    (
        cd "${BACKEND_DIR}"

        exec python -m uvicorn "${BACKEND_APP}" \
            --reload \
            --host "${BACKEND_HOST}" \
            --port "${BACKEND_PORT}"
    ) > "${LOG_DIR}/backend.log" 2>&1 &

    BACKEND_PID=$!
    save_pid "backend" "${BACKEND_PID}"

    if ! wait_for_port \
        "FastAPI backend" \
        "${BACKEND_HOST}" \
        "${BACKEND_PORT}" \
        45; then

        echo
        error "FastAPI failed to start. Recent log output:"
        tail -n 50 "${LOG_DIR}/backend.log" || true
        exit 1
    fi
fi

# ============================================================
# 3. Start the Celery worker
# ============================================================

section "3/4 Starting the Celery worker"

if [[ -f "${PID_DIR}/celery.pid" ]]; then
    OLD_CELERY_PID="$(cat "${PID_DIR}/celery.pid" 2>/dev/null || true)"

    if process_is_running "${OLD_CELERY_PID}"; then
        warning "Celery appears to be running with PID ${OLD_CELERY_PID}"
        warning "Run ./stop-all.sh before restarting it"
    else
        rm -f "${PID_DIR}/celery.pid"
    fi
fi

if [[ ! -f "${PID_DIR}/celery.pid" ]]; then
    if [[ "${PLATFORM}" == "windows-bash" ]]; then
        # The solo pool avoids common multiprocessing issues on Windows.
        CELERY_POOL="solo"
        CELERY_CONCURRENCY="1"

        warning "Windows Git Bash detected"
        warning "Celery will use the solo pool to avoid Windows multiprocessing errors"
    else
        CELERY_POOL="${CELERY_POOL:-prefork}"
    fi

    info "Celery application: ${CELERY_APP}"
    info "Celery pool: ${CELERY_POOL}"
    info "Celery concurrency: ${CELERY_CONCURRENCY}"

    (
        cd "${BACKEND_DIR}"

        exec python -m celery \
            -A "${CELERY_APP}" \
            worker \
            --loglevel=info \
            --pool="${CELERY_POOL}" \
            --concurrency="${CELERY_CONCURRENCY}"
    ) > "${LOG_DIR}/celery.log" 2>&1 &

    CELERY_PID=$!
    save_pid "celery" "${CELERY_PID}"

    sleep 5

    if process_is_running "${CELERY_PID}"; then
        success "Celery worker started with PID ${CELERY_PID}"
    else
        error "Celery worker failed to start"
        tail -n 50 "${LOG_DIR}/celery.log" || true
        rm -f "${PID_DIR}/celery.pid"
        exit 1
    fi
fi

# ============================================================
# 4. Install frontend dependencies and start the frontend
# ============================================================

section "4/4 Starting the frontend"

cd "${FRONTEND_DIR}"

if [[ ! -d "node_modules" ]]; then
    info "node_modules was not found; installing frontend dependencies"

    if [[ -f "pnpm-lock.yaml" ]] && command -v pnpm >/dev/null 2>&1; then
        pnpm install
    elif [[ -f "yarn.lock" ]] && command -v yarn >/dev/null 2>&1; then
        yarn install
    else
        npm install
    fi
fi

if [[ -f "pnpm-lock.yaml" ]] && command -v pnpm >/dev/null 2>&1; then
    FRONTEND_COMMAND=(pnpm dev)
elif [[ -f "yarn.lock" ]] && command -v yarn >/dev/null 2>&1; then
    FRONTEND_COMMAND=(yarn dev)
else
    FRONTEND_COMMAND=(npm run dev)
fi

info "Frontend command: ${FRONTEND_COMMAND[*]}"

"${FRONTEND_COMMAND[@]}" > "${LOG_DIR}/frontend.log" 2>&1 &

FRONTEND_PID=$!
save_pid "frontend" "${FRONTEND_PID}"

cd "${PROJECT_ROOT}"

# ============================================================
# Wait for the frontend
# ============================================================

section "Waiting for the frontend"

FRONTEND_URL=""

for ((i = 1; i <= 60; i++)); do
    for port in "${FRONTEND_PORTS[@]}"; do
        if port_is_open "127.0.0.1" "${port}"; then
            FRONTEND_URL="http://localhost:${port}"
            break 2
        fi
    done

    if ! process_is_running "${FRONTEND_PID}"; then
        error "The frontend process stopped unexpectedly"
        tail -n 50 "${LOG_DIR}/frontend.log" || true
        rm -f "${PID_DIR}/frontend.pid"
        exit 1
    fi

    sleep 1
done

# ============================================================
# Display startup information
# ============================================================

echo
echo -e "${GREEN}============================================================${NC}"
echo -e "${GREEN}System startup completed${NC}"
echo -e "${GREEN}============================================================${NC}"
echo
echo "Backend API:  http://localhost:${BACKEND_PORT}"
echo "API docs:     http://localhost:${BACKEND_PORT}/docs"

if [[ -n "${FRONTEND_URL}" ]]; then
    echo "Frontend:     ${FRONTEND_URL}"
else
    warning "The frontend port could not be detected automatically"
    echo "Check the frontend log: ${LOG_DIR}/frontend.log"
fi

echo
echo "Log directory: ${LOG_DIR}"
echo
echo "View the backend log:"
echo "  tail -f logs/backend.log"
echo
echo "View the Celery log:"
echo "  tail -f logs/celery.log"
echo
echo "View the frontend log:"
echo "  tail -f logs/frontend.log"
echo
echo "Stop all services:"
echo "  ./stop-all.sh"
echo