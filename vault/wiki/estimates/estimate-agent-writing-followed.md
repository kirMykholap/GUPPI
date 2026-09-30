---
type: estimate
kind: QA
status: passed
target: "[[rule-agent-writing]]"
purpose: The agent's text holds to the section How the agent writes of CLAUDE.md, and the person's complaint is the test
method: by hand in a later session — the person's messages of one session read for a complaint about the agent's text, against the section in CLAUDE.md
checked: 2026-09-30
origin: raw/2026-09-20/1308/ledger.md#case-272.3
sprint: migration
created: 2026-09-20
tags: [harness, render, workflow]
---

## Criterion

When:
A session starts with `CLAUDE.md` loaded, and the agent writes a text — a reply, a page, a commit message, a document.

Then:
The person raised no complaint in the session that the agent's text broke the section `## How the agent writes` of `CLAUDE.md` — a claim with no real source or wider than the output it rests on, a sales pitch, a long or passive sentence, an answer not given first, a not-done left implied.
**－** A slip in the agent's text that the agent found and corrected itself, with no complaint of the person, is no fault.
**－** When the person says they did not follow and wants it said more simply, by `/wait-what` or in words, that is the normal use of `.claude/skills/wait-what/SKILL.md`, not a fault of this rule.
**－** The code the agent writes is not a text of this rule; `make style` judges the code.

## Result

2026-09-30, by hand, the person's messages of session 0248 read for a complaint about the agent's text: one complaint stands, that the two decisions of the pre-spec report lacked the question icons and shape; it is about the question shape of grill-me, not about a claim without a source or wider than its output, a sales pitch, a long or passive sentence, an answer not given first or a not-done left implied; the one request for a plainer text was a /wait-what on Q3 of the round on Case 534, the normal use of the skill

## History

- 2026-09-20 created · [[decision-case-272.3]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L4
- 2026-09-23 updated: the Criterion names the width of a claim (case 359) · [[decision-case-359]]
- 2026-09-26 status: pending → failed · raw/2026-09-26/1745/ledger.md#L36
- 2026-09-27 status: failed → failed · raw/2026-09-26/2300/ledger.md#L36
- 2026-09-27 updated: the Criterion replaced whole — the person's complaint is the test of the agent's text, a slip the agent corrected itself no fault (case 450) · [[decision-case-450]]
- 2026-09-28 status: pending → failed · raw/2026-09-28/0000/ledger.md#L32
- 2026-09-28 updated: the Criterion replaced whole — a request for a plain explanation, answered by the skill wait-what, is no complaint (case 477.4) · [[decision-case-477.4]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/0248/ledger.md#L34
