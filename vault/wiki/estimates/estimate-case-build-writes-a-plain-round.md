---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether a round of case-guppi gives the mechanism with a concrete example, a before and after for each option, case numbers only in the recommended answer, and an unknown term explained
method: "by hand, in a session after the render: one round of case-guppi read in the chat against the four parts of the Criterion"
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
**＋** Each question body says what each option changes, as a before and after.
**＋** Case numbers, the history of a slug and facts of the frame stand in the round only in the `➡️` line of a question, as the source of its recommendation.
**＋** A term the person has not met in the chat is explained in a few words where it first stands, or a common word replaces it.
**－** The `context` of a Case keeps its case numbers and frame facts: the sentence is about a round only.

## History

- 2026-09-28 created · [[decision-case-477.1]]
