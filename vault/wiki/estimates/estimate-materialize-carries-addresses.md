---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A decision line's {addresses:<lesson slug>} or a lesson line's {addressed_by:case N} lands on the lesson's entry as addressed_by, at the entry's level; a mark without its pair is incomplete
method: pytest .guppi/tests/test_materialize.py on a temp ledger; the live reading the librarian's run on the first marked lesson
checked: 2026-09-23
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger]
core: true
---

## Criterion

When:
`guppi materialize` assembles a unit whose ledger holds a lesson line and a decision line of Case N, the one written second carrying the mark: `{addresses:<lesson slug>}` on the decision line, or `{addressed_by:case N}` on the lesson line.

Then:
The lesson entry carries `addressed_by: decision-case-N` at the entry's level, set by one function for both marks.
**＋** A decision entry with the mark carries `addresses: [<slug>, …]`.
**－** The lesson page gets no `addressed_by` field.
**－** A decision mark naming no lesson of the unit is `incomplete: [addresses]` on the decision entry, and the run does not fail.
**－** A lesson mark with no decision line of Case N earlier in the unit is `incomplete: [addressed_by]` on the lesson entry, and the run does not fail.

## Result

2026-09-23, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
