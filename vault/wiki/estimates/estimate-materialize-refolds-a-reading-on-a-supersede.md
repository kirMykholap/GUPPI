---
type: estimate
kind: QA
status: pending
target: "[[rule-materialize]]"
purpose: A reading folded into a create that a later supersedes marks moves to the live create of the same slug in the unit, or becomes an estimate entry of its own; no reading folds into a superseded create
method: uv run pytest tests/test_materialize.py -k refold — create A, a reading, create B with supersedes A, the reading on B; create A, a reading, supersedes A without a new create, an estimate entry; a reading after the mark, not on A
origin: raw/2026-09-22/1121/ledger.md#case-309
sprint: migration
created: 2026-09-22
tags: [harness, librarian]
---

## Criterion

When:
`materialize` lifts a line with `{supersedes:case N}`, and a `create` entry of Case N in the unit's yaml holds `folded`: the readings of its slug folded into it, with their `status`, `result` and line numbers.

Then:
The readings of `folded` move to the live `create` of the same slug in this unit — `status`, `result`, the line numbers; the marked `create` loses `status`, `result` and `folded`.
**＋** With no live `create`, each reading becomes an `estimate` entry of its own from the ledger line of that number, after the mark.
**＋** A reading lifted after the mark is not folded into the marked `create`.
**－** A mark on a Case of another unit (`elsewhere`) moves nothing — no live `create` is there; the readings of that yaml stand as they are.

## Result

2026-09-22, uv run pytest tests/test_materialize.py -k "folded or after_the_mark": 3 passed, 70 deselected — the reading moves to the live create, becomes its own entry without one, and does not fold into a marked create

## History

- 2026-09-22 created · [[decision-case-309]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L90
- 2026-09-29 updated: the Criterion replaced whole — When and Then only, Given out, the fold of a reading moved into When (case 489.7) · [[decision-case-489.7]]
