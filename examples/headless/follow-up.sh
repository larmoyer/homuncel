#!/usr/bin/env bash
# Push a follow-up while a `homuncel run` for the same --cwd is in flight.
set -euo pipefail

TEXT="${1:-Also check whether tests pass.}"

homuncel follow-up \
  --cwd "${HOMUNCEL_CWD:-$PWD}" \
  --text "$TEXT"
