---
type: estimate
kind: QA
status: passed
target: "[[rule-materialize]]"
purpose: A lesson line carries its source into the entry
method: pytest in .guppi/tests/test_materialize.py, the tests of the lesson entry
checked: 2026-10-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, ledger]
core: true
---

## Criterion

When:
`guppi materialize` reads a `- lesson[...]` ledger line whose braces carry `{source:...}`.

Then:
The entry carries `source` in its `fields`, and `generate` writes it into the page's frontmatter.
**＋** A `knowledge` lesson whose line carries no `source` is still marked `incomplete: [source]`; an `error` lesson never is.
**－** The applied entries of the yamls of earlier sessions are not rewritten: each records what the parser did in its own session.

## Result

2026-10-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
