#!/usr/bin/env bash

set -u

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PID_DIR="${PROJECT_ROOT}/.pids"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

stop_service() {
    local service="$1"
    local pid_file="${PID_DIR}/${service}.pid"

    if [[ ! -f "${pid_file}" ]]; then
        echo -e "${YELLOW}${service}: no PID file found${NC}"
        return
    fi

    local pid
    pid="$(cat "${pid_file}" 2>/dev/null || true)"

    if [[ -n "${pid}" ]] && kill -0 "${pid}" 2>/dev/null; then
        echo "Stopping ${service}, PID: ${pid}"

        # Try to stop the process group first, then the individual process.
        kill -- "-${pid}" 2>/dev/null \
            || kill "${pid}" 2>/dev/null \
            || true

        for ((i = 1; i <= 10; i++)); do
            if ! kill -0 "${pid}" 2>/dev/null; then
                break
            fi

            sleep 1
        done

        if kill -0 "${pid}" 2>/dev/null; then
            echo -e "${RED}Force-stopping ${service}${NC}"
            kill -9 "${pid}" 2>/dev/null || true
        fi

        echo -e "${GREEN}${service} stopped${NC}"
    else
        echo -e "${YELLOW}${service}: process is not running${NC}"
    fi

    rm -f "${pid_file}"
}

echo "============================================================"
echo "Stopping the Radiative Cooling Platform"
echo "============================================================"

stop_service "frontend"
stop_service "celery"
stop_service "backend"
stop_service "redis"

echo
echo -e "${GREEN}All managed services have been stopped${NC}"