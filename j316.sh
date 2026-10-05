#!/bin/bash
set -e

SCRIPT="$(dirname "$(readlink -f "$0")")/run.py"

[[ -f "$SCRIPT" ]] || { echo "error: execution script not found in: $SCRIPT" >&2; exit 1; }

trap 'exit 0' INT TERM
exec python3 "$SCRIPT" "$@"
