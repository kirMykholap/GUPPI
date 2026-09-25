---
type: estimate
kind: QA
status: passed
target: "[[rule-hook-registry]]"
method: the JSON case of tests/test_render.py; uv run guppi render --check after the render
checked: 2026-09-25
origin: raw/2026-09-09/ledger.md#case-18.2
sprint: migration
created: 2026-09-09
tags: [hooks, harness, render]
---

## Criterion

When:
`uv run guppi render` writes `.claude/settings.json`.

Then:
The `"hooks"` key of `.claude/settings.json` equals the Render of `rule-hook-registry` byte for byte, and every hook the harness runs is registered by one of its lines.
**＋** `uv run guppi render --check` exits 0 after the render.

## Result

2026-09-25, uv run pytest tests/test_render.py -k json: 4 passed; uv run guppi render --check: exit 0, no output

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-18.2
- 2026-09-10 status: pending → passed · written by hand, no generator yet
- 2026-09-12 criterion: case 85.3 added · [[decision-case-85.3]]
- 2026-09-12 updated: the criterion covers the hooks key; the whole-file clauses move to estimate-settings (case 99) · [[decision-case-99]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L46
- 2026-09-15 criterion: case 169.2 added · [[decision-case-169.2]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1809/ledger.md#L13
- 2026-09-24 updated: the Criterion replaced whole — the live reading of the Render, no count of commands (case 392.4) · [[decision-case-392.4]]
- 2026-09-25 status: pending → passed · raw/2026-09-25/1228/ledger.md#L41
