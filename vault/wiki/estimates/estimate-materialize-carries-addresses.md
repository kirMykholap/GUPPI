---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A decision line's {addresses:<lesson slug>} or a lesson line's {addressed_by:case N} lands on the lesson's entry as addressed_by, at the entry's level; a mark without its pair is incomplete
method: pytest tests/test_materialize.py on a temp ledger; the live reading the librarian's run on the first marked lesson
checked: 2026-09-23
origin: raw/2026-09-20/2106/ledger.md#case-284.3
sprint: migration
created: 2026-09-20
tags: [harness, workflow, ledger]
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

2026-09-23, uv run pytest tests/test_materialize.py -k "addresses_mark or marked_after_its_fix or lesson_mark": 4 passed — the decision's mark and the lesson's {addressed_by:case N} both land as addressed_by at the entry's level by one function, the page gets no field, a decision mark with no lesson is incomplete: [addresses], a lesson mark with no earlier decision line is incomplete: [addressed_by], neither fails the run

## History

- 2026-09-21 created · [[decision-case-284.3]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L6
- 2026-09-23 updated: the Criterion replaced whole — both marks land on the lesson entry by one function (case 377.3) · [[decision-case-377.3]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1355/ledger.md#L38
