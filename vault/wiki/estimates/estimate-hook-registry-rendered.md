---
type: estimate
kind: QA
status: passed
target: "[[rule-hook-registry]]"
method: the JSON case of .guppi/tests/test_render.py; uv run --project .guppi guppi render --check after the render
checked: 2026-09-25
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, render]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi render` writes `.claude/settings.json`.

Then:
The `"hooks"` key of `.claude/settings.json` equals the Render of `rule-hook-registry` byte for byte, and every hook the harness runs is registered by one of its lines.
**＋** `uv run --project .guppi guppi render --check` exits 0 after the render.

## Result

2026-09-25, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
