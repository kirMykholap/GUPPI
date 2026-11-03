---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A supersedes marks every entry of the earlier Case, in any unit
method: pytest in .guppi/tests/test_materialize.py, the tests of the supersedes mark, a test where two decision lines retire one Case among them
checked: 2026-10-12
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger, librarian]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi materialize` lifts a decision line that carries one `{supersedes:case N}` block or several, and the entries of each Case N, or of its sub-cases, stand in this unit's `materialize.yaml` or in the `materialize.yaml` of another unit.
**＋** A later decision line lifted in the same run, or in a later run, carries a `{supersedes:case N}` block for the same Case N.

Then:
For each Case N that a block of the line names, every entry with `case: N` gets `superseded_by`, whatever its kind, and the `decisions` record of that Case gets it too.
**＋** The `superseded_by` of an entry is a list that holds each Case whose line retires the entry, in the order the lines are lifted, with no Case twice.
**＋** So does every entry and every `decisions` record of a sub-case of Case N at any depth. A block that names Case N.M marks N.M and its own sub-cases, and leaves its parent and its other sub-cases.
**＋** The entry of the line carries `supersedes` as a list with one Case per block, in the order of the blocks. The `decisions` record of its Case lists under `supersedes` every Case that its lines name.
**＋** The `materialize.yaml` of another unit is written with that mark only.
**＋** An entry marked while no heading of its own Case stands in the unit's `spec.md` carries no `incomplete: [then]`, and its `decisions` record no `case_text` and no `incomplete` for a section.
**＋** Whether a block covers a Case is judged by `in_family` of `.guppi/guppi/materialize.py`; `remove_case` of `.guppi/guppi/ratified.py`, `.guppi/guppi/prespec.py` and `.guppi/guppi/casecheck.py` import it.
**－** An entry without `case` — an `estimate` or a `lesson` entry — gets no mark.
**－** An entry of an existing `materialize.yaml` whose `supersedes` is one value, not a list, is read as a list of one.
**－** An entry of an existing `materialize.yaml` whose `superseded_by` is one value, not a list, is read as a list of one, and a new mark is appended to that list.

## Result

2026-10-12, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
