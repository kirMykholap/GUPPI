---
type: estimate
kind: QA
status: failed
target: "[[entity-glossary]]"
purpose: Every term names in where a live page that defines it, and no term stands twice
method: one reading of the table by hand after the librarian's run, plus make lint — no ref finding on entity-glossary
checked: 2026-09-30
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

2026-09-30, the 56 rows of vault/wiki/glossary.md read against their where pages by a read-only subagent, its findings checked against the page text by hand, and `make lint` (exit 2, 85 lines, no ref finding on entity-glossary, only `unread: failed` on this Estimate): every where slug is a live rule page, no term stands in two rows, no excluded term stands in a row; the rows Decision page, Main agent and Plan Mode no longer contradict their page; the row `ref`, `slug`, `supersedes` does — it says each `{supersedes:case N}` block clears the `deferred_by` of its Case, while rule-case-protocol says generate clears a defer only from the pages the superseding Case names (case 467.3, guppi/generate.py docstring)

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
- 2026-09-30 status: pending → failed · raw/2026-09-30/0248/ledger.md#L4
- 2026-09-30 status: failed → failed · raw/2026-09-30/1306/ledger.md#L3
