---
type: decision
case: "997"
status: current
update: ["[[rule-orchestration]]", "[[estimate-orchestration-acknowledging-reply]]"]
origin: raw/2026-11-02/0039/ledger.md#case-997
sprint: plugin
created: 2026-11-02
tags: [session, workflow, harness, ledger]
---

## Problem

The text of the acknowledging reply names its labels by English words and gives their language only at the end, so the agent copied the English words into a chat in another language, and the check of that reply failed.

## Recommend

- **How the fix works**
  - Recommended: (a) rewrite the text of `orchestration.md` so it says first that each heading and label is translated into the language of the chat, the words in code spans being only the English names of the parts.
  - Answer: agreed, (a).
- **Which replies the fix covers**
  - Recommended: (a) every reply in `orchestration.md` that shows the Frontier.
  - Answer: agreed, (a).
- **How done is checked**
  - Recommended: (a) replace the Criterion of `estimate-orchestration-acknowledging-reply`, naming each label, and make its reading wait for the librarian's render.
  - Answer: agreed, (a).

## History

- 2026-11-02 created · raw/2026-11-02/0039/ledger.md#case-997
