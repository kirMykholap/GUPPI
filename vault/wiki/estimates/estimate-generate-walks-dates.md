---
type: estimate
kind: QA
status: passed
target: "[[rule-page-generation]]"
checked: 2026-09-16
origin: raw/2026-09-10/ledger.md#case-43
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

`materialize` and `generate` read one `raw/<date>/`, today by default. Nothing materializes the lines written after the librarian's commit unless the next session falls on the same date. The tail of session E was saved by a coincidence of dates only. (The Problem of case 43, in English.)

## Criterion

Given:
`guppi generate` applies the entries of a `materialize.yaml` in order; the `sections` of an `update` entry are whole replacements, `set` writes fields.
**＋** An `update` entry for an Estimate carries `sections.Criterion` and `set: {status: pending}`; a `create` entry carries `kind`, `purpose`, `method`, `tags` as fields (194.1).
**＋** An `estimate` entry carries `status` and `result`; the `result` opens with the date of the reading and the command (199).
**＋** The tests in `tests/test_generate.py` fix the behaviour; the live reading is the librarian's run of this session.
**－** `materialize`, `cleanup` and `lint` do not change here.

When:
`uv run guppi generate` runs, with `--date` or without.

Then:
Without `--date` every unit under `raw/` with a `materialize.yaml` is applied: the date-level yaml first, then `raw/<date>/<HHMM>/materialize.yaml` in folder order, dates ascending; `--date` walks the units of that date alone.
**＋** A unit with no unapplied entry changes no page; stdout carries one line per unit, `generate: <unit>: N page(s) written or changed`.
**＋** A failure on one unit is printed, the walk goes on, the exit code is 1 at the end.
**＋** A `--date` without a yaml is named on stderr, exit 1; no yaml anywhere — one line on stderr, exit 1.
**－** A unit `materialize` passed by (`carry.md`) has no yaml and is not walked.

## Method

tests/test_generate.py with two dated folders; live, the librarian's first run

## Result

2026-09-16, `pytest tests/test_generate.py`: 46 green — every unit with a yaml walked in date and folder order, a unit with nothing unapplied silent, a failure on one unit reported and the walk going on with exit 1, a missing yaml named on stderr

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-43
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L95
- 2026-09-11 fields to sections: criterion, method · [[decision-case-53.3]]
- 2026-09-13 criterion: case 103.3 added · [[decision-case-103.3]]
- 2026-09-14 updated: Context added from the Problem of case 43 (case 112.4) · [[decision-case-112.4]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L43
- 2026-09-16 updated: the Criterion replaced whole by case 201.5 — the head and block 103.3 recut into one (case 201.5) · [[decision-case-201.5]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L31
