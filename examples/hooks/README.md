# Hook examples

Homuncel uses Claude-compatible lifecycle hooks in `config.json` (`"hooks"`). There is no separate `hooks.json`.

Wire the script below with a project or user config snippet:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "shell|Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 examples/hooks/prefer_rg.py",
            "timeout": 15
          }
        ]
      }
    ]
  }
}
```

Copy `prefer_rg.py` next to your project (e.g. `.homuncel/hooks/prefer_rg.py`) and point `command` at that path.

Docs: [Memory, hooks & MCP](https://homuncel.netlify.app/docs/features/memory-hooks-mcp)
