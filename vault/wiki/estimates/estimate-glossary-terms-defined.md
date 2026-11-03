---
type: estimate
kind: QA
status: passed
target: "[[entity-glossary]]"
purpose: Every term names in where a live page that defines it, and no term stands twice
method: one reading of the table by hand after the librarian's run, plus uv run --project .guppi guppi check — no ref finding on entity-glossary
checked: 2026-09-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, harness]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi glossary` reads the `## Terms` table of `entity-glossary` at the librarian's run, and `guppi lint` and a reader read the same table.

Then:
Each row names in `where` a `[[slug]]` of a live page, and that page says what the term of the row is.
**＋** No claim of the meaning of a row contradicts its `where` page.
**＋** No term stands in two rows.
**－** A row does not fail because its `where` page leaves out a claim of its meaning.
**－** The terms that the Purpose of `entity-glossary` names as not rows, C4 model, Delegate and the retired terms, stand in no row.

## Result

2026-09-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
