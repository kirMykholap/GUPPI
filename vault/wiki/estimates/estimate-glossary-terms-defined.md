---
type: estimate
kind: QA
status: pending
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
Each row names in `where` a `[[slug]]` of a live page, and that page says what the term of the row is.
**＋** No claim of the meaning of a row contradicts its `where` page.
**＋** No term stands in two rows.
**－** A row does not fail because its `where` page leaves out a claim of its meaning.
**－** The terms that the Purpose of `entity-glossary` names as not rows, C4 model, Delegate and the retired terms, stand in no row.

## Result

2026-09-29, by hand at the /hi of session 2024 after the librarian's run 1c196e8, the table of vault/wiki/glossary.md against each where page and make lint: 57 rows, 57 distinct terms, no C4 model, Delegate or retired term, every where a live page, no lint line on entity-glossary but the unread one; the rows rewritten by case 520 (Vault, deferred_by, origin, Entity (status), Rule (status)) now match their pages; but Hook: rule-hook-registry does not say what a hook is; Retro: the row puts the short defer under ## Retro in the Spec, rule-retro line 46 puts it under ## Deferred; Harness: rule-harness does not say the harness is hooks, agents and skills rendered from rules/

## History

- 2026-09-22 created · [[decision-case-306.3]]
- 2026-09-22 updated: the rows on §N are gone with index.md (case 318) · [[decision-case-318]]
- 2026-09-22 updated: the Rule-class row is retired, not rewritten (case 321) · [[decision-case-321]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L84
- 2026-09-29 updated: the Criterion replaced whole — the one-time build of the table out, the purpose kept as When and Then (case 488.4) · [[decision-case-488.4]]
- 2026-09-29 status: pending → failed · raw/2026-09-29/1432/ledger.md#L5
- 2026-09-29 status: failed → failed · raw/2026-09-29/1753/ledger.md#L4
- 2026-09-30 status: failed → failed · raw/2026-09-29/2024/ledger.md#L5
- 2026-09-30 updated: the Criterion replaced whole — the where page says what the term is and contradicts no claim of the row; a claim it leaves out does not fail the row (case 527.2) · [[decision-case-527.2]]
