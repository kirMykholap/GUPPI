---
type: estimate
kind: QA
status: pending
target: "[[rule-page-generation]]"
purpose: generate applies every unit under raw/ that has a yaml, dates ascending, and a failing unit does not stop the walk
method: tests/test_generate.py with two dated folders; live, the librarian's first run
checked: 2026-09-17
origin: raw/2026-09-10/ledger.md#case-43
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Criterion

When:
`uv run guppi generate` runs, with `--date` or without.

Then:
Without `--date` every unit under `vault/raw/` with a `materialize.yaml` is applied: the date-level yaml `vault/raw/<date>/materialize.yaml` first, then `vault/raw/<date>/<HHMM>/materialize.yaml` in folder order, dates ascending; `--date` walks the units of that date alone.
**＋** A unit with no unapplied entry changes no page; stdout carries one line per unit, `generate: <unit>: N page(s) written or changed`.
**＋** A failure on one unit is printed, the walk goes on, the exit code is 1 at the end.
**＋** A `--date` without a yaml is named on stderr, exit 1; no yaml anywhere — one line on stderr, exit 1.
**－** A unit `materialize` passed by (`carry.md`) has no yaml and is not walked.

## Result

2026-09-17, `uv run pytest -q tests/test_generate.py` 48 passed, and the pages after the librarian's run of 2238 (commit be891c1): `estimate-generate-writes`, `-generate-walks-dates`, `-lint-catches`, `-pretask-reconciles`, `-materialize-assembles` each carry a `method` field and no `## Context` or `## Method` section; `uv run guppi lint` reads `unmigrated: 34 pages in the shape before case 193`; the walk of that run took four units — 1034, 1651, 1955, 2238 — dates ascending, per the brief

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-43
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L95
- 2026-09-11 fields to sections: criterion, method · [[decision-case-53.3]]
- 2026-09-13 criterion: case 103.3 added · [[decision-case-103.3]]
- 2026-09-14 updated: Context added from the Problem of case 43 (case 112.4) · [[decision-case-112.4]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L43
- 2026-09-16 updated: the Criterion replaced whole by case 201.5 — the head and block 103.3 recut into one (case 201.5) · [[decision-case-201.5]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L31
- 2026-09-17 updated: method as a field, the old sections dropped — the recut completed (case 211.3) · [[decision-case-211.3]]
- 2026-09-18 status: pending → passed · raw/2026-09-17/1119/ledger.md#L24
- 2026-09-20 ref `estimate-pretask-hook-gates` → `estimate-prespec-hook-gates` · [[decision-case-261]]
- 2026-09-20 updated: the word moved: the module pretask → prespec and the slug -pretask-reconciles → -prespec-reconciles in the Criterion; the promise and the reading unchanged, passed kept (case 265) · [[decision-case-265]]
- 2026-09-29 updated: the Criterion restored whole — the text of case 201.5, which case 211.3 overwrote; purpose set (case 489.2) · [[decision-case-489.2]]
