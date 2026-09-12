---
type: estimate
kind: QA
status: pending
target: rule-hook-registry
origin: raw/2026-09-09/ledger.md#case-18.2
sprint: migration
created: 2026-09-09
tags: [hooks, harness, render]
---

## Context

The registry page is the only source of `.claude/settings.json` from Slice 2 on. The
first render must reproduce the hand-written file exactly, or the page was ratified with
a different registry than the one running; and a rendered file that no longer parses
would silently unregister every hook.

## Criterion

`uv run guppi render` writes the `"hooks"` key of `.claude/settings.json` from the Render
of `rule-hook-registry`, byte for byte, and every registration the harness runs is one of
its lines (case 85.3). That the assembled file parses and that the next session start
still writes its `session-start` line into `event_log.md` belong to `estimate-settings`,
which reads the whole file (case 99).

### case 85.3

When:
`guppi render` runs.

Then:
`rule-hook-registry` renders the four event keys only, as a `partial` child of
`rule-settings`.
**＋** Its Purpose keeps the hooks and drops `defaultMode`, which is now
`rule-default-mode`.
**－** The whole-file clauses — the file parses, the next start still logs — belong to
`estimate-settings` from now on; this page answers for the hook registrations.

## Method

The JSON case in `tests/test_render.py`; the live reading once by hand, written into the
estimate line.

## Result

Passing, 2026-09-10, session E. `tests/test_render.py` holds the JSON case; `render --check`
exited 0 at the close of D. Live: the start of session `c640ade7` wrote
`05:44:48 c640ade7 session-start clear` into `raw/2026-09-10/event_log.md` from the rendered
`.claude/settings.json`.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-18.2
- 2026-09-10 status: pending → passed · written by hand, no generator yet
- 2026-09-12 criterion: case 85.3 added · [[decision-case-85.3]]
- 2026-09-12 updated: the criterion covers the hooks key; the whole-file clauses move to estimate-settings (case 99) · [[decision-case-99]]
