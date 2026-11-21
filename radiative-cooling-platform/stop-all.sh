#!/usr/bin/env bash

set -u

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_DIR="${PROJECT_ROOT}/.pids"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

case "$(uname -s)" in
    MINGW*|MSYS*|CYGWIN*) IS_WINDOWS=1 ;;
    *)                    IS_WINDOWS=0 ;;
esac

stop_service() {
    local service="$1"
    local pid_file="${PID_DIR}/${service}.pid"

    if [[ ! -f "${pid_file}" ]]; then
        echo -e "${YELLOW}${service}: no PID file found${NC}"
        return
    fi

    local pid
    pid="$(cat "${pid_file}" 2>/dev/null || true)"

    if [[ -z "${pid}" ]] || ! kill -0 "${pid}" 2>/dev/null; then
        echo -e "${YELLOW}${service}: process is not running${NC}"
        rm -f "${pid_file}"
        return
    fi

    echo "Stopping ${service}, PID: ${pid}"

    if (( IS_WINDOWS )); then
        # Must run while the parent is still alive, otherwise /T cannot find the children.
        local winpid=""
        [[ -r "/proc/${pid}/winpid" ]] && winpid="$(cat "/proc/${pid}/winpid")"

        if [[ -n "${winpid}" ]]; then
            taskkill //F //T //PID "${winpid}" >/dev/null 2>&1 || true
        fi

        kill "${pid}" 2>/dev/null || true
    else
        kill -- "-${pid}" 2>/dev/null || kill "${pid}" 2>/dev/null || true

        for ((i = 1; i <= 10; i++)); do
            kill -0 "${pid}" 2>/dev/null || break
            sleep 1
        done

        if kill -0 "${pid}" 2>/dev/null; then
            echo -e "${RED}Force-stopping ${service}${NC}"
            kill -9 "${pid}" 2>/dev/null || true
        fi
    fi

    echo -e "${GREEN}${service} stopped${NC}"
    rm -f "${pid_file}"
}

stop_glob() {
    local pattern="$1"
    local pid_file

    shopt -s nullglob
    for pid_file in "${PID_DIR}"/${pattern}.pid; do
        stop_service "$(basename "${pid_file}" .pid)"
    done
    shopt -u nullglob
}

echo "============================================================"
echo "Stopping the Radiative Cooling Platform"
echo "============================================================"

stop_service "frontend"
stop_service "celerybeat"
stop_glob   "celery-surrogate*"
stop_glob   "celery-main*"
[[ -f "${PID_DIR}/celery.pid" ]] && stop_service "celery"   # PID file from the old script
stop_service "backend"
stop_service "redis"

# Windows: warn if anything is still holding the ports
if (( IS_WINDOWS )); then
    for port in 8000 5173 3000 8080; do
        if netstat -ano 2>/dev/null | grep -qE "[:.]${port}[[:space:]].*LISTENING"; then
            echo -e "${YELLOW}Port ${port} is still in use. Find the PID with:${NC}"
            echo "  netstat -ano | grep :${port}"
            echo "  taskkill //F //T //PID <PID>"
        fi
    done
fi

echo
echo -e "${GREEN}All managed services have been stopped${NC}"