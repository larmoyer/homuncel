# Homuncel examples

Starter snippets for common setups. Homuncel’s **source is not in this repository** — copy these into your machine’s `~/.homuncel/` or a project’s `.homuncel/` and adjust.

| Folder | What’s inside |
|--------|----------------|
| [`config/`](config/) | `config.json` profiles (ask / auto / sandbox) |
| [`hooks/`](hooks/) | Claude-compatible PreToolUse hook (prefer `rg`) |
| [`headless/`](headless/) | `homuncel run` / `follow-up` scripts for CI and hosts |
| [`project/`](project/) | Project instructions (`HOMUNCEL.md`) + sparse project config |

Full reference: [Configuration](https://homuncel.netlify.app/docs/getting-started/configuration) · [Hooks & MCP](https://homuncel.netlify.app/docs/features/memory-hooks-mcp) · [Headless run](https://homuncel.netlify.app/docs/reference/headless)

> These examples are starting points. Validate locally before sharing a project config — never commit real API keys.
