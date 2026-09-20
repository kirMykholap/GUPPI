---
type: estimate
kind: QA
status: pending
target: "[[rule-internal-context]]"
purpose: The text of sprint.md, brief.md and case-schema.md is present in the first turn's context after /hi, without a read call
method: one reading at the /hi of a session, by hand
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

Passing. Both texts were present in the first turn, expanded by the `@`-imports inside
the skill body (2026-09-09 16:11, session B).

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-20 updated: the recut to the shape of case 193 — purpose, method, the Criterion replaced whole; three texts expanded, case-schema.md the third (case 273.2) · [[decision-case-273.2]]
