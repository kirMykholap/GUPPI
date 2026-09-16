---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
origin: raw/2026-09-10/ledger.md#case-43
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Context

`materialize` and `generate` read one `raw/<date>/`, today by default. Nothing materializes the lines written after the librarian's commit unless the next session falls on the same date. The tail of session E was saved by a coincidence of dates only. (The Problem of case 43, in English.)

## Criterion

Given:
A unit `raw/<date>/<HHMM>/` holds `ledger.md` and `spec.md`; a Case in the Spec has a heading, the sections `given`, `when`, `then` and a `then` block.
**＋** `guppi generate` applies the `sections` of an `update` entry as whole replacements and writes every field of a `create` entry's `fields` into the frontmatter.
**＋** Cases 189 and 190.3 are ratified; their entries for these same pages apply before the entries of this Case, in ledger order.
**－** The tests in `tests/test_materialize.py` fix the behaviour; the live reading is the librarian's run of this session.

When:
`uv run guppi materialize` runs, with `--date` or without.

Then:
The unit of the walk is a session folder `raw/<date>/<HHMM>/` holding a `ledger.md`: its yaml `raw/<date>/<HHMM>/materialize.yaml`, its Spec `raw/<date>/<HHMM>/spec.md` alone, the `origin` of its entries `raw/<date>/<HHMM>/ledger.md#case-N` and `#L<n>`.
**＋** A date-level `raw/<date>/ledger.md` (the shape before case 103) is a unit of the old shape: every Spec of the date in folder order and `raw/<date>/spec.md` when it exists, the yaml `raw/<date>/materialize.yaml`, `origin` in the date form; on a date with both shapes the date-level unit goes first; the yaml's `spec` field names the file each Case was found in.
**＋** Without `--date` the walk covers every unit under `raw/`, dates ascending; `--date` walks the date-level ledger and every session of the date; stdout carries one line per yaml; a line written after the librarian's commit of its date is lifted by the next run.
**＋** An error of a unit — no `ledger.md`, a Case heading in two files — stops the walk with exit 1; a line whose lift failed marks its entry, the unit exits 1 and the walk goes on.
**－** A unit whose folder holds `carry.md` is skipped — that is `estimate-materialize-skips-a-carried-over-unit`, not this one.

## Method

tests/test_materialize.py with two dated folders; live, the librarian's first run over 2026-09-09 and 2026-09-10

## Result

2026-09-16, `pytest tests/test_materialize.py`: 51 green, the walk tests unchanged — the session folder as the unit with its own yaml, Spec and origin, the date-level ledger of the old shape first, --date on one date, one stdout line per yaml, a unit error stopping the walk with exit 1 and a failed line letting it go on; live, `materialize --show` without --date walked 2026-09-15/2225, 2026-09-16/1034 and 2026-09-16/1651 in that order

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-43
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L94
- 2026-09-11 fields to sections: criterion, method · [[decision-case-53.3]]
- 2026-09-13 criterion: case 103.2 added · [[decision-case-103.2]]
- 2026-09-14 updated: Context added from the Problem of case 43 (case 112.4) · [[decision-case-112.4]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/0747/ledger.md#L42
- 2026-09-14 criterion: case 142.4 added · [[decision-case-142.4]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1633/ledger.md#L56
- 2026-09-16 updated: block 73.5 merged into the Criterion — the yaml's spec field names the file each Case was found in; the rest of 73.5 already stood there in blocks 103.2 and 142.4 (case 189) · [[decision-case-189]]
- 2026-09-16 updated: the Criterion replaced whole by case 194.2 — the head, 103.2, 142.4 and the spec field of 73.5 recut into one (case 194.2) · [[decision-case-194.2]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1651/ledger.md#L35
