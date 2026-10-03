#!/usr/bin/env bash
# One-shot headless turn; stdout is a single final JSON object.
set -euo pipefail

TEXT="${1:-Summarize the top-level README in three bullets.}"

homuncel run \
  --cwd "${HOMUNCEL_CWD:-$PWD}" \
  --approval "${HOMUNCEL_APPROVAL:-yolo}" \
  --model "${HOMUNCEL_MODEL:-auto}" \
  --json \
  --text "$TEXT"
