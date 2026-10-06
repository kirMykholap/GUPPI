---
type: estimate
kind: QA
status: passed
target: "[[rule-internal-context]]"
purpose: The text of sprint.md, backlog.md, brief.md, orchestration.md, where-to-stop.md, ratification.md and glossary.md is present in the first turn's context after /hi, without a read call, and case-schema.md is not
method: by hand, the text of .claude/skills/hi/SKILL.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-internal-context in the Spec, read against the Criterion, recorded in the estimate line
checked: 2026-10-06
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness]
---

## Criterion

When:
The person invokes `/hi`, with `.claude/skills/hi/SKILL.md` rendered from `rule-internal-context`.

Then:
The text of `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/brief.md`, `vault/wiki/orchestration.md`, `vault/wiki/where-to-stop.md`, `vault/wiki/ratification.md` and `vault/wiki/glossary.md` is in the context of the first turn, in that order, without a read call.
**＋** `vault/wiki/case-schema.md` is not in it.
**＋** The glossary and the backlog reach a session through this block alone. After a compaction, the paths of these files are in the list of `guppi recall`.
**－** A subagent, such as `librarian-guppi`, `ask-guppi` or one of Work Mode, carries none of these texts. Its prompt names what it needs.

## Result

2026-10-06, Retro, the Render of rule-internal-context in the Spec (case 689.1): its replace puts @vault/wiki/where-to-stop.md right after @vault/wiki/orchestration.md in the six @ lines of the page (lines 26-31), giving sprint, backlog, brief, orchestration, where-to-stop, ratification, glossary; case-schema.md is no @ line; guppi/recall.py reads the @ lines of the skill file, so the new path is in its list

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-20 updated: the recut to the shape of case 193 — purpose, method, the Criterion replaced whole; three texts expanded, case-schema.md the third (case 273.2) · [[decision-case-273.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L1
- 2026-09-21 updated: the Criterion replaced whole — four texts expanded, glossary.md the fourth (case 288.1) · [[decision-case-288.1]]
- 2026-09-21 updated: the purpose by the Criterion of 288.1 (case 290.3) · [[decision-case-290.3]]
- 2026-09-21 updated: the Criterion of 288.1 restored whole, replaced by the purpose update of 290.3 (case 291.2) · [[decision-case-291.2]]
- 2026-09-21 status: pending → passed · raw/2026-09-21/1315/ledger.md#L20
- 2026-09-27 updated: the Criterion replaced whole — backlog.md loaded by /hi (case 451.12) · [[decision-case-451.12]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L17
- 2026-10-02 updated: the Criterion replaced whole - orchestration.md and ratification.md in place of case-schema.md (case 595.4) · [[decision-case-595.4]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/2049/ledger.md#L3
- 2026-10-06 updated: the Criterion replaced whole — where-to-stop.md loaded after orchestration.md; purpose and method set anew (case 689.1) · [[decision-case-689.1]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L44
