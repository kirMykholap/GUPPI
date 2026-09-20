---
type: estimate
kind: QA
status: passed
target: "[[rule-internal-context]]"
purpose: The text of sprint.md, brief.md and case-schema.md is present in the first turn's context after /hi, without a read call
method: one reading at the /hi of a session, by hand
checked: 2026-09-20
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness]
---

## Criterion

Given:
The `/hi` SKILL is the Render of `rule-skill-hi` with its children in markers; `rule-internal-context` is the block of `@` lines Claude Code expands when the skill is invoked.
**＋** `tests/test_render.py` fixes the text of the block.

When:
The person invokes `/hi`.

Then:
The text of `sprint.md`, `brief.md` and `case-schema.md` is present in the first turn's context, in that order, without a read call.
**－** The glossary is not in the list — it arrives through `CLAUDE.md`.

## Result

2026-09-20, the /hi of session 1749 read by hand: sprint.md, brief.md and case-schema.md present in the first turn in that order, expanded by the @ lines of the SKILL, no read call; the glossary through CLAUDE.md

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-20 updated: the recut to the shape of case 193 — purpose, method, the Criterion replaced whole; three texts expanded, case-schema.md the third (case 273.2) · [[decision-case-273.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L1
