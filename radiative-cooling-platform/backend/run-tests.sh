#!/usr/bin/env bash

set -e

mkdir -p /c/nc
export NUMBA_CACHE_DIR="C:/nc"

PYTHON="./.venv/Scripts/python.exe"

if [ ! -f "$PYTHON" ]; then
  echo "錯誤：找不到 $PYTHON"
  echo "請先在 backend 目錄建立 .venv"
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

echo "開始執行測試..."
"$PYTHON" -m pytest -vv