---
type: estimate
kind: QA
status: pending
target: "[[rule-materialize]]"
origin: raw/2026-09-16/1034/ledger.md#case-189
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger, librarian]
ref: rule-materialize
purpose: A supersedes marks every entry of the earlier Case, in any unit
method: pytest in tests/test_materialize.py, the tests of the supersedes mark, plus one live reading of a librarian's run
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

## History

- 2026-09-16 created · [[decision-case-189]]
