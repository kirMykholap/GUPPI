---
type: estimate
kind: QA
status: passed
target: "[[rule-hook-registry]]"
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

### case 169.2

When:
`guppi render` writes `.claude/settings.json`; then the person submits a prompt.

Then:
`UserPromptSubmit` carries two commands in order: `uv run guppi event prompt`, then `uv run guppi gate`, both with timeout 30.
**－** The other events and matchers as today.

## Method

The JSON case in `tests/test_render.py`; the live reading once by hand, written into the
estimate line.

## Result

block 169.2, live 2026-09-15 session S: .claude/settings.json carries uv run guppi event prompt and uv run guppi gate on UserPromptSubmit, guppi render --check exit 0; the day's event log has hi at 18:09:02 from the first and the marks pretask 20:01:16 (the agent's call) and retro 20:31:22 (typed) from the second

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-18.2
- 2026-09-10 status: pending → passed · written by hand, no generator yet
- 2026-09-12 criterion: case 85.3 added · [[decision-case-85.3]]
- 2026-09-12 updated: the criterion covers the hooks key; the whole-file clauses move to estimate-settings (case 99) · [[decision-case-99]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/ledger.md#L46
- 2026-09-15 criterion: case 169.2 added · [[decision-case-169.2]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1809/ledger.md#L13
