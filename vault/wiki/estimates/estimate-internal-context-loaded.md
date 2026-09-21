---
type: estimate
kind: QA
status: passed
target: "[[rule-internal-context]]"
purpose: The text of sprint.md, brief.md, case-schema.md and glossary.md is present in the first turn's context after /hi, without a read call
method: one reading at the /hi of a session, by hand
checked: 2026-09-21
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness]
---

## Criterion

Given:
The `/hi` skill is the Render of `rule-skill-hi` with its children in markers; `rule-internal-context` is the block of `@` lines Claude Code expands when the skill is invoked.
**＋** A subagent receives the `CLAUDE.md` hierarchy and not the content of an invoked skill (Claude Code docs, sub-agents).
**＋** `guppi recall` prints the `@` lines of the skill file after a compaction (287).
**＋** `guppi render --check` keeps the skill file equal to the page.

When:
The person invokes `/hi`.

Then:
The text of `sprint.md`, `brief.md`, `case-schema.md` and `glossary.md` is present in the first turn's context, in that order, without a read call.
**＋** The glossary reaches a session through this block alone; after a compaction its path is in the list of `guppi recall`.
**－** A subagent — `librarian-guppi`, `ask-guppi`, one of Work Mode — carries no glossary; its prompt names what it needs.

## Result

2026-09-21, the /hi of session 1315 read by hand against the Criterion of 288.1 restored by 291.2: sprint.md, brief.md, case-schema.md and glossary.md present in the first turn in that order, expanded by the four @ lines of the SKILL, no read call; no compaction in the session so far, guppi recall not exercised

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-20 updated: the recut to the shape of case 193 — purpose, method, the Criterion replaced whole; three texts expanded, case-schema.md the third (case 273.2) · [[decision-case-273.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L1
- 2026-09-21 updated: the Criterion replaced whole — four texts expanded, glossary.md the fourth (case 288.1) · [[decision-case-288.1]]
- 2026-09-21 updated: the purpose by the Criterion of 288.1 (case 290.3) · [[decision-case-290.3]]
- 2026-09-21 updated: the Criterion of 288.1 restored whole, replaced by the purpose update of 290.3 (case 291.2) · [[decision-case-291.2]]
- 2026-09-21 status: pending → passed · raw/2026-09-21/1315/ledger.md#L20
