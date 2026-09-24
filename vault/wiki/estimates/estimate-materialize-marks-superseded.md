---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A supersedes marks every entry of the earlier Case, in any unit
method: pytest in tests/test_materialize.py, the tests of the supersedes mark, plus one live reading of a librarian's run
checked: 2026-09-24
origin: raw/2026-09-16/1034/ledger.md#case-189
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger, librarian]
---

## Criterion

When:
`uv run guppi materialize` lifts a line with `{supersedes:case N}`, and the entries of Case N stand in this unit's `materialize.yaml` or in that of another unit under `raw/`.

Then:
Every entry with `case: N` gets `superseded_by`, whatever its kind, and the `decisions` record of Case N gets it too.
**＋** The `materialize.yaml` of another unit is written with that mark only.
**＋** An entry of Case N marked while no heading of Case N stands in the unit's `spec.md` carries no `incomplete: [then]`, and its `decisions` record no `case_text` and no `incomplete` for a section.
**－** An entry without `case` — an `estimate` or a `lesson` entry — gets no mark.

## Result

2026-09-24, `uv run pytest tests/test_materialize.py`: 75 passed

## History

- 2026-09-16 created · [[decision-case-189]]
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L1
- 2026-09-22 updated: the Criterion replaced whole — the entries of a superseded Case gone from the Spec carry no incomplete, the record no case_text; Given added, the shape of case 193 (case 299.3) · [[decision-case-299.3]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L26
- 2026-09-22 updated: the mark moves a folded reading (case 323) · [[decision-case-323]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L94
- 2026-09-25 updated: the Criterion replaced whole — the mark by the model of case 378; what generate skips and the readings of a marked create left to their own Estimates (case 397.5) · [[decision-case-397.5]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L31
