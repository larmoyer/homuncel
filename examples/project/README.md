# Project overlay examples

Commit non-secret project defaults next to your code:

```text
your-repo/
  HOMUNCEL.md                 # always-on project instructions
  .homuncel/
    config.json               # sparse overlay (no API keys)
```

| File | Role |
|------|------|
| [`HOMUNCEL.md`](HOMUNCEL.md) | Injected every turn (also accepts `CLAUDE.md`) |
| [`project-config.json`](project-config.json) | Copy to `.homuncel/config.json` |

Docs: [Configuration](https://homuncel.netlify.app/docs/getting-started/configuration) · [Workflows](https://homuncel.netlify.app/docs/getting-started/workflows)
