---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the main agent names the Cases it sends to case-guppi at the same time as built at the same time, and, once all have answered, sends back each Case whose summary carries a Sibling line, one at a time and once, before the Cases are shown together
method: "by hand, after the first send of two or more Cases to case-guppi at the same time under the new Render of rule-orchestration: the prompts and messages of the main agent from that send to the showing of its Cases read against the Criterion, recorded in the estimate line"
checked: 2026-10-28
origin: raw/2026-10-16/2104/ledger.md#case-872.2
sprint: plugin
created: 2026-10-16
tags: [session, workflow]
---

## Criterion

When:
The main agent sends two or more Cases of the session to their `case-guppi` at the same time — the dispatch of a batch, the answers of a batch sent back, or the loop after the findings of `/pre-spec` — with `vault/wiki/orchestration.md` rendered from `rule-orchestration` and `.claude/skills/pre-spec/SKILL.md` rendered from `rule-prespec`.

Then:
The prompt or message to each `case-guppi` names each other Case of that send as built at the same time.
**＋** Once every `case-guppi` of the send has answered with its Case, the main agent sends back each Case whose item in the summary carries a line `**Sibling:**`, one at a time, each after the one before has answered, with a message that the build of each Case that line names has ended.
**＋** The second pass runs once, and the Cases of the send are shown after it, together, for one ratification.
**＋** In the loop after the findings of `/pre-spec`, the second pass comes before the `ask-guppi` runs confirm their findings.
**－** A Case whose summary carries no line `**Sibling:**` does not go back in the second pass.
**－** The main agent reads no case file to find the Cases of the second pass.

## Result

2026-10-28, Work readings, the main agent's messages of session 1907 from the /pre-spec send to the showing: each SendMessage to the case-guppi of 892, 893 and 894 named the other two as built at the same time; once all three had answered, only Case 893, whose summary carried a Sibling line, went back, once, with the message that the build of 894 had ended; 892 and 894 did not go back; the second pass came before the ask-guppi run confirmed its findings; no case file was read to find the Cases of the second pass; the three Cases were shown together for one ratification

## History

- 2026-10-17 created · [[decision-case-872.2]]
- 2026-10-28 status: pending → passed · raw/2026-10-28/1907/ledger.md#L14
