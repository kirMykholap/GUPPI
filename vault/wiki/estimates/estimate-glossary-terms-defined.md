---
type: estimate
kind: QA
status: pending
target: "[[entity-glossary]]"
purpose: Every term names in where a live page that defines it, and no term stands twice
method: one reading of the table by hand after the librarian's run, plus make lint — no ref finding on entity-glossary
checked: 2026-09-22
origin: raw/2026-09-22/0014/ledger.md#case-306.3
sprint: migration
created: 2026-09-22
tags: [session, harness]
---

## Criterion

When:
`uv run guppi glossary` reads the `## Terms` table of `entity-glossary` at the librarian's run, and `guppi lint` and a reader read the same table.

Then:
Each row names in `where` a `[[slug]]` of a live page, and that page defines the term of the row.
**＋** No term stands in two rows.
**－** The terms that the Purpose of `entity-glossary` names as not rows, C4 model, Delegate and the retired terms, stand in no row.

## Result

2026-09-22, by hand: the ## Terms of entity-glossary holds 49 rows under one header; guppi lint — no ref finding on entity-glossary

## History

- 2026-09-22 created · [[decision-case-306.3]]
- 2026-09-22 updated: the rows on §N are gone with index.md (case 318) · [[decision-case-318]]
- 2026-09-22 updated: the Rule-class row is retired, not rewritten (case 321) · [[decision-case-321]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L84
- 2026-09-29 updated: the Criterion replaced whole — the one-time build of the table out, the purpose kept as When and Then (case 488.4) · [[decision-case-488.4]]
