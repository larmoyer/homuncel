#!/usr/bin/env python3
"""PreToolUse hook: nudge shell commands toward ripgrep.

Exit codes (Homuncel / Claude-compatible):
  0 — allow (optionally rewrite tool input via stdout JSON)
  2 — block; stderr is shown to the agent

Stdin is a JSON event with tool_name / tool_input. HOMUNCEL_PROJECT_DIR
(and CLAUDE_PROJECT_DIR) are set to the session cwd.
"""

from __future__ import annotations

import json
import re
import sys

# (pattern, message) — first match wins
_RULES = [
    (
        r"^grep\b(?!.*\|)",
        "Prefer `rg` (ripgrep) over `grep` for faster, clearer search.",
    ),
    (
        r"^find\s+\S+\s+-name\b",
        "Prefer `rg --files -g PATTERN` (or `find` only when you need full find semantics).",
    ),
]


def _issues(command: str) -> list[str]:
    out: list[str] = []
    for pattern, message in _RULES:
        if re.search(pattern, command):
            out.append(message)
    return out


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0

    tool = (event.get("tool_name") or "").lower()
    if tool not in ("shell", "bash"):
        return 0

    command = (event.get("tool_input") or {}).get("command") or ""
    issues = _issues(command.strip())
    if not issues:
        return 0

    # Soft block: agent sees stderr and can retry with a better command.
    sys.stderr.write("Homuncel hook (prefer_rg):\n")
    for msg in issues:
        sys.stderr.write(f"  - {msg}\n")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
