---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether the recommend of each Case case-guppi builds holds one item per question of its rounds — the title, the recommendation and the answer in English as they stood when the person answered it, or a note that it was not answered — a sub-case with its own items and no problem
method: "by hand: the Case files of a later session after the render, each recommend read against the rounds of its Case in the chat"
checked: 2026-09-30
origin: raw/2026-09-30/1306/ledger.md#case-544.2
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi` answers with a Case, with `.claude/agents/case-guppi.md` rendered from `rule-case-build` and `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

Then:
The `recommend` of the Case is a list with one item per question of the rounds of `case-guppi` on the Case: the item's first line is the title of the question in bold as the round wrote it, with a sub-item `Recommended:` with what the agent recommended and a sub-item `Answer:` with the person's answer in English, both as they stood when the person answered that question.
**＋** A later question that replaced an earlier one is an item of its own, and the earlier item keeps its own recommendation and answer.
**＋** A question asked in more than one round is one item, with the recommendation and the answer of the last round in which the person answered it.
**＋** A question the person left unanswered is asked again in the next round under the same title; a question never answered has one item, whose `Answer:` sub-item says it was not answered and names the later question that replaced it, if one did.
**＋** A change the person asked for on a shown Case is an item whose first line is `**Change**`, with a line `Asked:` and a line `Taken:` that says how the Case took it.
**＋** A Case built with no round has one item: a line `Recommended:` and the line `Answer: ratified as built`.
**＋** An item whose answer changed only one sub-case stands in a `recommend` under that sub-case's heading, and the other items stand in the parent's `recommend`.
**＋** A Case with sub-cases carries `problem` on the parent only.
**－** No item quotes the person's words word for word.
**－** The promise of `estimate-case-check-requires-each-question-of-the-rounds` stands: each question title of the rounds has an item.

## Result

2026-09-30, by hand, the Case files of Cases 547 to 550 of session 1736 against their rounds in the chat: each recommend holds one item per question, the title in bold as the round wrote it, a Recommended line and an Answer line in English, no quotation of the person's words; but the item of Q2 of Case 549 gives the first recommendation (each text states the condition in its own words) while Q3 replaced it (the texts point to rule-case-protocol), against the latest recommendation and answer the Criterion asks for

## History

- 2026-09-30 created · [[decision-case-544.2]]
- 2026-09-30 status: pending → failed · raw/2026-09-30/1736/ledger.md#L21
- 2026-09-30 updated: the Criterion replaced whole — one item per question, its recommendation and answer as they stood when the person answered it, a question never answered noted (case 557.2) · [[decision-case-557.2]]
