---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A reading folded into a create that a later supersedes marks moves to the live create of the same slug in the unit, or becomes an estimate entry of its own; no reading folds into a superseded create
method: uv run --project .guppi pytest .guppi/tests/test_materialize.py -k refold — create A, a reading, create B with supersedes A, the reading on B; create A, a reading, supersedes A without a new create, an estimate entry; a reading after the mark, not on A
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, librarian]
core: true
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

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
