---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A supersedes marks every entry of the earlier Case, in any unit
method: pytest in tests/test_materialize.py, the tests of the supersedes mark, plus one live reading of a librarian's run
checked: 2026-09-16
origin: raw/2026-09-16/1034/ledger.md#case-189
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger, librarian]
---

## Criterion

When:
`guppi materialize` reads a line with `{supersedes:case N}`, and the entries of Case N
lie in this yaml or in the yaml of another session under `raw/`.

Then:
Every entry with `case: N` gets `superseded_by` — the lines of Case N and everything
derived from them; the `decisions` record of Case N as today.
**＋** `generate` applies none of them.
**＋** A foreign yaml is marked by the same rule.
**－** An entry without `case` — `estimate`, `lesson` — gets no mark.

## Result

2026-09-16, pytest tests/test_materialize.py -k supersed (5 passed) and the 1034 yaml after the librarian's run of 1955: the three defer entries of case 191 and its decisions record carry superseded_by 203.2, the estimate entry none, all three already applied so generate applied nothing new; a foreign yaml marked by the same rule

## History

- 2026-09-16 created · [[decision-case-189]]
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L1
