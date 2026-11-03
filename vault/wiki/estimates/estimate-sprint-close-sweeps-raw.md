---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint-close]]"
purpose: Whether the close of a sprint moves each finished session of raw/ to the archive whatever its date, and leaves the session of the run, an unfinished unit and a conserved Spec in raw/
method: uv run --project .guppi pytest .guppi/tests/test_sprint_close.py -k sweep
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [sprint, workflow, librarian]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi sprint-close --sprint <id>` of `.guppi/guppi/sprint_close.py` previews or closes a sprint, in the librarian's run or in `.guppi/tests/test_sprint_close.py` over a made-up vault.

Then:
After a close whose run of `guppi cleanup` exits 0, each unit of `vault/raw/` that `.guppi/guppi/archive.py` judges done moves to `vault/archive/` by the move of `guppi archive`, whatever its date.
**＋** Stdout holds one line per unit, moved or kept with its reason, in the form of `guppi archive`.
**＋** The preview without `--apply` names each unit the close would move, and moves none.
**－** The session of the run does not move.
**－** A unit with no yaml, an entry not applied or a ledger line outside the yaml stays in `vault/raw/`.
**－** A unit whose folder holds `carry.md`, judged by `is_carried_over` of `.guppi/guppi/materialize.py`, stays in `vault/raw/` with the reason `carried over`.
**－** A refused close moves no unit.

## Result

2026-10-09, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
