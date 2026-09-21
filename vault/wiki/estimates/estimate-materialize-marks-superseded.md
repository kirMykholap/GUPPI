---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A supersedes marks every entry of the earlier Case, in any unit
method: pytest in tests/test_materialize.py, the tests of the supersedes mark, plus one live reading of a librarian's run
checked: 2026-09-21
origin: raw/2026-09-16/1034/ledger.md#case-189
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger, librarian]
---

## Criterion

Given:
`{supersedes:case N}` on a decision line marks every entry of Case N `superseded_by` in the yaml of any unit (175, 177); `generate` applies none of them and ticks none of their lines (151, 286); Retro does not count them (282).
**＋** The Spec of a session is the plan approved at the end of Plan Mode, copied to `raw/<date>/<hi HHMM>/spec.md` (73.1); `## Case N — …` or `### Case N.M — …` is a heading, its section runs to the next such heading.
**＋** `materialize` takes the `then` and the texts of a Case from the Spec of the unit; what is missing it names in `incomplete`, never invents.
**＋** `tests/test_materialize.py` fixes the behaviour on a temp ledger.

When:
`guppi materialize` reads a line with `{supersedes:case N}`, and the entries of Case N lie in this yaml or in the yaml of another session under `raw/`.

Then:
Every entry with `case: N` gets `superseded_by` — the lines of Case N and everything derived from them; the `decisions` record of Case N as today.
**＋** `generate` applies none of them.
**＋** A foreign yaml is marked by the same rule.
**＋** An entry of Case N marked `superseded_by` while no heading N stands in the Spec of the unit carries no `incomplete: [then]`; its `decisions` record carries no `case_text` and no `incomplete` for `context`, `problem`, `given`, `when`; the mark alone is its completeness.
**－** Case N standing in the Spec — the entries are lifted as today; `--show` prints the same.
**－** An entry without `case` — `estimate`, `lesson` — gets no mark.

## Result

2026-09-21, uv run pytest tests/test_materialize.py 68 green, two new — the entries of a Case superseded and gone from the Spec carry superseded_by and no incomplete, its decisions record superseded_by and no case_text and no incomplete; the same Case with its heading in the Spec is lifted as before, incomplete then on the line without an item; the supersedes tests of 175 and 130.2 unchanged; live — the librarian's run of the first session where a Case is superseded in it and removed from the Spec, not this one

## History

- 2026-09-16 created · [[decision-case-189]]
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L1
- 2026-09-22 updated: the Criterion replaced whole — the entries of a superseded Case gone from the Spec carry no incomplete, the record no case_text; Given added, the shape of case 193 (case 299.3) · [[decision-case-299.3]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L26
