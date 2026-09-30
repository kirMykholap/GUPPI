---
type: estimate
kind: QA
status: pending
target: "[[rule-case-build]]"
purpose: Whether the recommend of each Case case-guppi builds holds one item per question of its rounds — the title, the latest recommendation, the latest answer in English — a sub-case with its own items and no problem
method: "by hand: the Case files of a later session after the render, each recommend read against the rounds of its Case in the chat"
origin: raw/2026-09-30/1306/ledger.md#case-544.2
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness]
---

## Criterion

When:
`case-guppi` answers with a Case, with `.claude/agents/case-guppi.md` rendered from `rule-case-build` and `vault/wiki/case-schema.md` rendered from `rule-case-protocol`.

Then:
The `recommend` of the Case is a list with one item per question of the rounds of `case-guppi` on the Case: the item's first line is the title of the question in bold as the round wrote it, followed by a line `Recommended:` with what the agent recommended and a line `Answer:` with the person's answer in English.
**＋** Where a later question changed the recommendation or the answer of an earlier one, the earlier item gives the latest recommendation and the latest answer.
**＋** A change the person asked for on a shown Case is an item whose first line is `**Change**`, with a line `Asked:` and a line `Taken:` that says how the Case took it.
**＋** A Case built with no round has one item: a line `Recommended:` and the line `Answer: ratified as built`.
**＋** An item whose answer changed only one sub-case stands in a `recommend` under that sub-case's heading, and the other items stand in the parent's `recommend`.
**＋** A Case with sub-cases carries `problem` on the parent only.
**－** No item quotes the person's words word for word.

## History

- 2026-09-30 created · [[decision-case-544.2]]
