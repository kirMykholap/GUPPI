---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: Every unit under raw/ is walked, so a line written after the librarian's commit is lifted by the next run
method: uv run --project .guppi pytest .guppi/tests/test_materialize.py; live, the librarian's next run over more than one unit
checked: 2026-09-24
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi materialize` runs, with `--date` or without.

Then:
The unit of the walk is a session folder `raw/<date>/<HHMM>/` holding a `ledger.md`: its yaml `raw/<date>/<HHMM>/materialize.yaml`, its Spec `raw/<date>/<HHMM>/spec.md` alone, the `origin` of its entries `raw/<date>/<HHMM>/ledger.md#case-N` and `#L<n>`.
**＋** A date-level `raw/<date>/ledger.md` is a unit of the old shape: every Spec of the date in folder order and `raw/<date>/spec.md` when it exists, the yaml `raw/<date>/materialize.yaml`, `origin` in the date form; on a date with both shapes the date-level unit goes first; the yaml's `spec` field names the file each Case was found in.
**＋** Without `--date` the walk covers every unit under `raw/`, dates ascending; `--date` walks the units of that date; stdout carries one line per yaml; a line written after the librarian's commit of its unit is lifted by the next run.

## Result

2026-09-24, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
