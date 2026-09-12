---
type: estimate
kind: QA
status: pending
target: rule-settings
origin: raw/2026-09-12/ledger.md#case-85.2
sprint: migration
created: 2026-09-12
tags: [harness, render]
---

## Context

How to describe `settings.json` so that permissions have their own rule, the mode has
its own and the hooks have their own, while the file keeps one source.

## Criterion

### case 85.2

When:
`guppi render` runs, or someone reads `.claude/settings.json`.

Then:
`rule-settings` is a MOC, `enforcement: render`, `render_mode: full`,
`governs: .claude/settings.json`; its body is the whole file, with one `<!-- child -->`
line where a child owns the text.
**＋** Its `children` are `rule-default-mode`, `rule-permissions`, `rule-hook-registry`,
and that order is the order of the keys in the file.
**＋** Its Estimate reads the rendered file: it parses as JSON, `render --check` exits 0,
and the next session start writes its `session-start` line into the event log.
**－** The MOC holds no rule of its own about what a hook or a permission may be.

## Method

uv run guppi render, then json.load on .claude/settings.json and guppi render --check; the live half at the next session start — the session-start line in raw/<date>/event_log.md came from the rendered file

## History

- 2026-09-12 created · [[decision-case-85.2]]
