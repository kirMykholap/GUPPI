---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
purpose: generate applies every unit under raw/ that has a yaml, dates ascending, and a failing unit does not stop the walk
method: .guppi/tests/test_generate.py with two dated folders; live, the librarian's first run
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi generate` runs, with `--date` or without.

Then:
Without `--date` every unit under `vault/raw/` with a `materialize.yaml` is applied: the date-level yaml `vault/raw/<date>/materialize.yaml` first, then `vault/raw/<date>/<HHMM>/materialize.yaml` in folder order, dates ascending; `--date` walks the units of that date alone.
**＋** A unit with no unapplied entry changes no page; stdout carries one line per unit, `generate: <unit>: N page(s) written or changed`.
**＋** A failure on one unit is printed, the walk goes on, the exit code is 1 at the end.
**＋** A `--date` without a yaml is named on stderr, exit 1; no yaml anywhere — one line on stderr, exit 1.
**－** A unit `materialize` passed by (`carry.md`) has no yaml and is not walked.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
