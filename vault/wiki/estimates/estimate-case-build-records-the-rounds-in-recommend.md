---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether the recommend of each Case case-guppi builds holds one item per question of its rounds — the title, the recommendation and the answer in English as they stood when the person answered it, or a note that it was not answered — each item on the parent or under the one sub-case its answer changed, and a sub-case with no problem
method: "by hand: the Case files of a later session after the render, each recommend read against the rounds of its Case in the chat"
checked: 2026-10-01
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
**＋** An item whose answer changed only one sub-case stands in the parent's `recommend` or in a `recommend` under that sub-case's heading; every other item stands in the parent's `recommend`.
**＋** A Case with sub-cases carries `problem` on the parent only.
**－** No item quotes the person's words word for word.
**－** The promise of `estimate-case-check-requires-each-question-of-the-rounds` stands: each question title of the rounds has an item.

## Result

2026-10-01, by hand, the Case files cases/case-577.md to case-581.md of session 1441, after the render of session 1237, each recommend read against the rounds in the chat: 577 holds one item per question Q1-Q5 with its title as the round wrote it, Recommended and an Answer in English, and one Change item with Asked and Taken for the finding of /pre-spec the person answered; 578 Q1-Q2, 579 Q1-Q5 with the answer to Q1 outside the options paraphrased in English, 581 Q1-Q4 of the rounds of 580; every item on the parent, problem on the parent only; no item quotes the person word for word; not exercised: a question replaced, a question left unanswered, a Case with no round

## History

- 2026-09-30 created · [[decision-case-544.2]]
- 2026-09-30 status: pending → failed · raw/2026-09-30/1736/ledger.md#L21
- 2026-09-30 updated: the Criterion replaced whole — one item per question, its recommendation and answer as they stood when the person answered it, a question never answered noted (case 557.2) · [[decision-case-557.2]]
- 2026-10-01 status: pending → failed · raw/2026-09-30/2356/ledger.md#L45
- 2026-10-01 updated: the Criterion replaced whole — an item whose answer changed only one sub-case may stand on the parent or under that sub-case (case 568) · [[decision-case-568]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1441/ledger.md#L34
