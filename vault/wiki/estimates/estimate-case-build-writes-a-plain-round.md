---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether a round of case-guppi gives the mechanism with a concrete example, a list one item per line, a number only beside a quotation of what it points to, and an unknown term explained
method: "by hand, in a session after the render: one first round and one later round of case-guppi read in the chat against the Criterion"
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
**＋** A list in the `**Context:**` stands one item per line under the sentence that introduces it, as `.claude/skills/grill-me/SKILL.md` sets a list.
**＋** The instructions of `case-guppi` point each question, and each list of the Context, to `.claude/skills/grill-me/SKILL.md` and word no shape of their own.
**＋** The round says what it rests on in plain words and uses no number where plain words are enough.
**＋** A case or decision number, a session id, a ledger line number, a commit hash or a date in the history of a page stands in any line of the round, the `➡️` line included, only beside a short quotation of the words it points to, as the source of that quotation.
**＋** A term the person has not met in the chat is explained in a few words where it first stands, or a common word replaces it.
**－** A page name in a code span is no such reference: it stays where the question is about that page.
**－** The shape of a question, and what counts as a list, are read by `estimate-skill-grill-me-asks-in-rounds`, not here.
**－** The `context`, `problem` and `recommend` of a Case keep their numbers as `rule-case-protocol` allows: this promise is about a round only.

## Result

2026-09-29, by hand, the rounds of case-guppi in session 1134: Context of each first round gave the mechanism with one example, questions in the grill-me shape, terms explained; but the first round on C1 names "case 193" in its Context, and the round on C4 names "Cases 506 and 507" in the Now line of Q3, outside the ➡️ lines

## History

- 2026-09-28 created · [[decision-case-477.1]]
- 2026-09-28 status: pending → failed · raw/2026-09-28/2000/ledger.md#L25
- 2026-09-29 updated: the Criterion replaced whole — the instructions point to the question shape of the grill-me template, read by estimate-skill-grill-me-asks-in-rounds; this promise keeps the Context, the case numbers and the terms (case 501.2) · [[decision-case-501.2]]
- 2026-09-29 status: pending → failed · raw/2026-09-29/1134/ledger.md#L39
- 2026-09-29 updated: the Criterion replaced whole — a list in the Context one item per line; a number in any line of a round only beside a quotation of what it points to (case 512, supersedes 511.2) · [[decision-case-512]]
