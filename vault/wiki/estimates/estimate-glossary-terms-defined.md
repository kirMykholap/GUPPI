---
type: estimate
kind: QA
status: passed
target: "[[entity-glossary]]"
purpose: Every term names in where a live page that defines it, and no term stands twice
method: one reading of the table by hand after the librarian's run, plus uv run --project .guppi guppi check — no ref finding on entity-glossary
checked: 2026-09-30
origin: raw/2026-09-22/0014/ledger.md#case-306.3
sprint: migration
created: 2026-09-22
tags: [session, harness]
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

2026-09-30, the rows of vault/wiki/glossary.md after the librarian's run over 1306 (070d8e6) read against their where pages by a read-only subagent, its findings checked against the page text by hand, and make lint (exit 2, 62 lines, no ref finding on entity-glossary, only unread: failed on this Estimate): 56 rows by the subagent's count, every where slug a live rule page, no term in two rows, no excluded term in a row, the table equal to the Terms of entity-glossary; the row ref, slug, supersedes now agrees with rule-case-protocol (generate clears a defer only from the pages the superseding Case names); the row deferred_by says, as rule-rules-schema does, that a supersedes clears it, with no condition — no contradiction with its where page, the looser wording across rule-rules-schema, rule-entities-schema and rule-insights-schema stands as C5

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
- 2026-09-30 status: failed → passed · raw/2026-09-30/1736/ledger.md#L4
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make lint` → `uv run --project .guppi guppi check` · [[decision-case-820.7]]
