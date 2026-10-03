# Config examples

Drop (or merge) into `~/.homuncel/config.json` or `<repo>/.homuncel/config.json`.

Models and credentials are placeholders — create them with the CLI instead of hand-editing secrets:

```bash
homuncel credential create --name openai --type bearer --token sk-…
homuncel model create --name gpt --endpoint https://api.openai.com/v1 --model gpt-4.1 --credential openai --tier strong
homuncel model create --name fast --endpoint https://api.openai.com/v1 --model gpt-4.1-mini --credential openai --tier light
homuncel model use auto
```

| File | Intent |
|------|--------|
| [`config-ask.json`](config-ask.json) | Prompt before risky tools (default-friendly) |
| [`config-auto.json`](config-auto.json) | Smart Auto-review; Auto model pool |
| [`config-sandbox.json`](config-sandbox.json) | Shell in sandbox without asking; network off |

Docs: [Configuration](https://homuncel.netlify.app/docs/getting-started/configuration) · [Sandbox](https://homuncel.netlify.app/docs/tui/sandbox)
