---
type: decision
case: "1002"
status: current
update: ["[[rule-orchestration]]", "[[estimate-orchestration-acknowledging-reply]]"]
origin: raw/2026-11-02/1337/ledger.md#case-1002
sprint: plugin
created: 2026-11-02
tags: [session, workflow, harness, ledger]
---

## Problem

The text tells the agent to translate each heading of the acknowledging reply, but it still names each one by an English literal. Twice the agent copied the English heading of the Frontier into a chat in another language.

## Recommend

- **What fixes the English heading**
  - Recommended: (b) rewrite `orchestration.md` so that it names the parts without English literals.
  - Answer: agreed, (b).
- **Which names the text drops**
  - Recommended: (a) every heading and label of the reply, and the Frontier heading in each reply that shows the Frontier.
  - Answer: agreed, (a).
- **How the fix is checked**
  - Recommended: (a) keep `estimate-orchestration-acknowledging-reply` and its Criterion, and make its reading wait for the render of the new text.
  - Answer: agreed, (a).

## History

- 2026-11-02 created · raw/2026-11-02/1337/ledger.md#case-1002
