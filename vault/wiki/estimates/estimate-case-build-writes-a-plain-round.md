---
type: estimate
kind: QA
status: failed
target: "[[rule-case-build]]"
purpose: Whether a round of case-guppi gives the mechanism with a concrete example, a before and after for each option, case numbers only in the recommended answer, and an unknown term explained
method: "by hand, in a session after the render: one round of case-guppi read in the chat against the four parts of the Criterion"
checked: 2026-09-29
origin: raw/2026-09-28/1318/ledger.md#case-477.1
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi` answers with a round of questions, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`.

Then:
The `**Context:**` of a first round gives the mechanism in plain words, with one concrete example of where it goes wrong.
**＋** The instructions of `case-guppi` point each question to the question shape of `.claude/skills/grill-me/SKILL.md` and word no shape of their own.
**＋** Case numbers, the history of a slug and facts of the frame stand in the round only in the `➡️` line of a question, as the source of its recommendation.
**＋** A term the person has not met in the chat is explained in a few words where it first stands, or a common word replaces it.
**－** The shape of a question is read by `estimate-skill-grill-me-asks-in-rounds`, not here.
**－** The `context` of a Case keeps its case numbers and frame facts: the sentence is about a round only.

## Result

2026-09-29, by hand, the rounds of case-guppi in session 1134: Context of each first round gave the mechanism with one example, questions in the grill-me shape, terms explained; but the first round on C1 names "case 193" in its Context, and the round on C4 names "Cases 506 and 507" in the Now line of Q3, outside the ➡️ lines

## History

- 2026-09-28 created · [[decision-case-477.1]]
- 2026-09-28 status: pending → failed · raw/2026-09-28/2000/ledger.md#L25
- 2026-09-29 updated: the Criterion replaced whole — the instructions point to the question shape of the grill-me template, read by estimate-skill-grill-me-asks-in-rounds; this promise keeps the Context, the case numbers and the terms (case 501.2) · [[decision-case-501.2]]
- 2026-09-29 status: pending → failed · raw/2026-09-29/1134/ledger.md#L39
