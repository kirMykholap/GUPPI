---
type: estimate
kind: QA
status: pending
target: "[[rule-spec-write]]"
purpose: The Stop hook writes a deferred Case into the Spec as the reply showed it
method: uv run pytest tests/test_ratified.py -k defer, then by hand the first defer the person asks for after the change
origin: raw/2026-09-25/1228/ledger.md#case-421.1
sprint: migration
created: 2026-09-25
tags: [hooks, harness, workflow]
---

## Criterion

When:
The `Stop` hook `uv run guppi ratified` runs after a reply whose `LEDGER` block holds lines of a Case N that are all `defer` — beside the lines of other Cases or alone — and the same reply shows `## Case N —` in the short form: `context`, `problem` and a fence tagged `then` with its `defer` items.

Then:
The hook writes that Case under `## Deferred` of the plan file while Plan Mode lasts, and of `raw/<date>/<hi HHMM>/spec.md` once that file stands, at Retro: the heading, `context`, `problem` and the `then` block as the reply shows them.
**＋** The section of Case N is replaced when it stands there, appended at the end of `## Deferred` otherwise; the heading `## Deferred` is added when the file has none.
**＋** A reply with no showing of Case N, or a `then` block without a `defer` item carrying `slug`, `type` and `purpose` for each `defer` line of the reply: exit 2 with the reason on stderr; on the re-fire (`stop_hook_active`) exit 0.
**－** The ratified copy `<plan>.ratified.md` gets no defer, and the check after the write does not run on it.

## History

- 2026-09-25 created · [[decision-case-421.1]]
