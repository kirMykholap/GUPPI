---
type: estimate
kind: QA
status: passed
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

`uv run guppi render` leaves `.claude/settings.json` byte-identical to the ratified Render
body (`git diff` empty after the two hook additions of cases 20 and 24.1 are applied by
hand once), the file parses as JSON, and the next session start still writes a
`session-start` line into `event_log.md`.

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
