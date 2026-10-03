#!/usr/bin/env bash
# Stream NDJSON events (status / tool / assistant_delta / final).
set -euo pipefail

TEXT="${1:-List Go packages under ./internal and say which look like CLI entrypoints.}"

homuncel run \
  --cwd "${HOMUNCEL_CWD:-$PWD}" \
  --approval "${HOMUNCEL_APPROVAL:-yolo}" \
  --model "${HOMUNCEL_MODEL:-auto}" \
  --events jsonl \
  --text "$TEXT" \
  | jq -rc '
      if .type == "tool" then
        [.phase, .name, (.args.command // .args.path // "")] | @tsv
      elif .type == "final" then
        "FINAL\t" + (.assistant_text // "" | .[0:120])
      elif .type == "status" then
        "STATUS\t" + (.status // "")
      else empty end
    '
