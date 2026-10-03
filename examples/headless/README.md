# Headless / automation examples

`homuncel run` executes **one** agent turn with no TUI. Use JSON (one final object) or NDJSON events.

| Script | Mode |
|--------|------|
| [`run-json.sh`](run-json.sh) | `--json` — sync final answer |
| [`run-events.sh`](run-events.sh) | `--events jsonl` — live tool stream |
| [`follow-up.sh`](follow-up.sh) | Push a mid-run follow-up to the inbox |

Prereqs: Homuncel installed, models/credentials configured (see [Quickstart](https://homuncel.netlify.app/docs/getting-started/quickstart)).

Docs: [Headless run](https://homuncel.netlify.app/docs/reference/headless) · [CI/CD](https://homuncel.netlify.app/docs/enterprise/ci-cd)
