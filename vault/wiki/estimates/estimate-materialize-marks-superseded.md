---
type: estimate
kind: QA
status: pending
target: "[[rule-materialize]]"
purpose: A supersedes marks every entry of the earlier Case, in any unit
method: pytest in tests/test_materialize.py, the tests of the supersedes mark, plus one live reading of a librarian's run
checked: 2026-09-26
origin: raw/2026-09-16/1034/ledger.md#case-189
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger, librarian]
---

## Criterion

When:
`uv run guppi materialize` lifts a decision line that carries one `{supersedes:case N}` block or several, and the entries of each Case N, or of its sub-cases, stand in this unit's `materialize.yaml` or in the `materialize.yaml` of another unit.

Then:
For each Case N that a block of the line names, every entry with `case: N` gets `superseded_by`, whatever its kind, and the `decisions` record of that Case gets it too.
**＋** So does every entry and every `decisions` record of a sub-case of Case N at any depth. A block that names Case N.M marks N.M and its own sub-cases, and leaves its parent and its other sub-cases.
**＋** The entry of the line carries `supersedes` as a list with one Case per block, in the order of the blocks. The `decisions` record of its Case lists under `supersedes` every Case that its lines name.
**＋** The `materialize.yaml` of another unit is written with that mark only.
**＋** An entry marked while no heading of its own Case stands in the unit's `spec.md` carries no `incomplete: [then]`, and its `decisions` record no `case_text` and no `incomplete` for a section.
**＋** Whether a block covers a Case is judged by `in_family` of `guppi/materialize.py`; `remove_case` of `guppi/ratified.py`, `guppi/prespec.py` and `guppi/casecheck.py` import it.
**－** An entry without `case` — an `estimate` or a `lesson` entry — gets no mark.
**－** An entry of an existing `materialize.yaml` whose `supersedes` is one value, not a list, is read as a list of one.

## Result

2026-09-26, `uv run pytest -q tests/test_materialize.py` and the librarian's run af86af6; 80 passed, and live case 430's four blocks landed as a list in block order with only the superseded_by mark written into the yamls of units 0051 and 1228

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
- 2026-09-25 updated: the Criterion replaced whole — a decision line may carry several {supersedes:case N} blocks, and each named Case is marked (case 429) · [[decision-case-429]]
- 2026-09-26 status: pending → passed · raw/2026-09-26/1745/ledger.md#L32
- 2026-10-05 updated: the Criterion replaced whole — a tag marks the Case and its sub-cases, by in_family (case 660.2) · [[decision-case-660.2]]
