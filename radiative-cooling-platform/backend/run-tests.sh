#!/usr/bin/env bash

set -e

mkdir -p /c/nc
export NUMBA_CACHE_DIR="C:/nc"

PYTHON="./.venv/Scripts/python.exe"

if [ ! -f "$PYTHON" ]; then
  echo "Error: Not found $PYTHON"
  echo "Please create the .venv directory in the backend folder first"
  exit 1
fi

echo "Python:"
"$PYTHON" -c "import sys; print(sys.executable)"

echo "Numba cache:"
"$PYTHON" -c \
  "from numba.core import config; print(config.CACHE_DIR)"

echo "pythermalcomfort:"
"$PYTHON" -c \
  "import pythermalcomfort; print(pythermalcomfort.__file__)"

echo "Starting test execution..."
"$PYTHON" -m pytest -vv