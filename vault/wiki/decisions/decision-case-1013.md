---
type: decision
case: "1013"
status: current
update: ["[[rule-orchestration]]", "[[estimate-orchestration-acknowledging-reply]]", "[[insight-orchestration-acknowledging-reply-keeps-headings-in-english]]"]
origin: raw/2026-11-02/2155/ledger.md#case-1013
sprint: plugin
created: 2026-11-02
tags: [session, workflow, harness, ledger, orchestration]
---

## Problem

The text asks for every heading of the acknowledging reply in the language of the chat, while the language rule keeps a term of the harness in English, so the agent keeps the heading of the Frontier in English and the rule calls that a failure that the person does not see as one.

## Recommend

- **How the Case keeps the headings of a reply in the language of the chat**
  - Recommended: (a) a check of the headings when the reply ends.
  - Answer: none of the options; the person asked to soften the rule: the text is written in the right language, a heading sometimes stays in English because it holds terms, and that is normal; it is no problem now, an Estimate failed for this reason should be set passed, and the current behaviour suits the person.
- **Which replies the Case covers**
  - Recommended: (b) those replies and the first reply after `/hi`.
  - Answer: not answered; the answer to "How the Case keeps the headings of a reply in the language of the chat" keeps the current behaviour, so no reply changes its form.

## History

- 2026-11-03 created · raw/2026-11-02/2155/ledger.md#case-1013
