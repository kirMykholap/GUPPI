---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: Every unit under raw/ is walked, so a line written after the librarian's commit is lifted by the next run
method: uv run --project .guppi pytest .guppi/tests/test_materialize.py; live, the librarian's next run over more than one unit
checked: 2026-09-24
origin: raw/2026-09-10/ledger.md#case-43
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
---

## Criterion

When:
`uv run --project .guppi guppi materialize` runs, with `--date` or without.

Then:
The unit of the walk is a session folder `raw/<date>/<HHMM>/` holding a `ledger.md`: its yaml `raw/<date>/<HHMM>/materialize.yaml`, its Spec `raw/<date>/<HHMM>/spec.md` alone, the `origin` of its entries `raw/<date>/<HHMM>/ledger.md#case-N` and `#L<n>`.
**＋** A date-level `raw/<date>/ledger.md` is a unit of the old shape: every Spec of the date in folder order and `raw/<date>/spec.md` when it exists, the yaml `raw/<date>/materialize.yaml`, `origin` in the date form; on a date with both shapes the date-level unit goes first; the yaml's `spec` field names the file each Case was found in.
**＋** Without `--date` the walk covers every unit under `raw/`, dates ascending; `--date` walks the units of that date; stdout carries one line per yaml; a line written after the librarian's commit of its unit is lifted by the next run.

## Result

2026-09-24, `uv run pytest tests/test_materialize.py`: 75 passed

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
- 2026-09-25 updated: the Criterion replaced whole — the walk by the model of case 378, the error of a line and of a unit left to estimate-materialize-fails-alone; purpose and method as fields (case 397.4) · [[decision-case-397.4]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L30
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
