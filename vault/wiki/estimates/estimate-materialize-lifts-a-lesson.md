---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
origin: raw/2026-09-16/1034/ledger.md#case-189
sprint: migration
created: 2026-09-16
tags: [harness, workflow, ledger]
ref: rule-materialize
purpose: A lesson line carries its source into the entry
method: pytest in tests/test_materialize.py, the tests of the lesson entry
---

## Criterion

When:
`guppi materialize` reads a `- lesson[...]` ledger line whose braces carry
`{source:...}`.

Then:
The entry carries `source` in its `fields`, and `generate` writes it into the page's
frontmatter.
**＋** A `knowledge` lesson whose line carries no `source` is still marked
`incomplete: [source]`; an `error` lesson never is.
**－** The applied entries of the earlier yamls are not rewritten: they record what
the parser did that day.

## Result

2026-09-16, `pytest tests/test_materialize.py`: 51 green; a lesson line with {source:...} carries source in its fields, a knowledge lesson without one is incomplete: [source], an error lesson never

## History

- 2026-09-16 created · [[decision-case-189]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1651/ledger.md#L30
