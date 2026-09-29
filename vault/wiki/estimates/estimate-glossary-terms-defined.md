---
type: estimate
kind: QA
status: failed
target: "[[entity-glossary]]"
purpose: Every term names in where a live page that defines it, and no term stands twice
method: one reading of the table by hand after the librarian's run, plus make lint — no ref finding on entity-glossary
checked: 2026-09-29
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

2026-09-29, by hand at the /hi of session 1753, after the librarian's run d8c1f17 that applied case 515, the table of vault/wiki/glossary.md and make lint: 56 rows, 56 distinct terms, no C4 model, Delegate or retired term, every `where` a live page, no lint line on entity-glossary; but five rows name a `where` page that does not define the term: Vault (`rule-page-schemas` does not say what the vault is), `deferred_by` and `origin` (the body of `rule-page-generation` names neither), Entity / Rule (status) (`rule-page-generation` gives no `archived` status of an Entity or a Rule and no built once every Estimate passes), Hook (`rule-hook-registry` names neither the transcript nor the `hi` window across midnight)

## History

- 2026-09-22 created · [[decision-case-306.3]]
- 2026-09-22 updated: the rows on §N are gone with index.md (case 318) · [[decision-case-318]]
- 2026-09-22 updated: the Rule-class row is retired, not rewritten (case 321) · [[decision-case-321]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L84
- 2026-09-29 updated: the Criterion replaced whole — the one-time build of the table out, the purpose kept as When and Then (case 488.4) · [[decision-case-488.4]]
- 2026-09-29 status: pending → failed · raw/2026-09-29/1432/ledger.md#L5
- 2026-09-29 status: failed → failed · raw/2026-09-29/1753/ledger.md#L4
