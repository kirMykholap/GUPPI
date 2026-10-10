---
type: decision
case: "557.2"
status: archived
parent: "[[decision-case-557]]"
update: ["[[rule-case-build]]", "[[rule-case-protocol]]", "[[rule-decisions-schema]]", "[[estimate-case-build-records-the-rounds-in-recommend]]"]
origin: raw/2026-09-30/2042/ledger.md#case-557.2
sprint: migration
created: 2026-09-30
tags: [session, workflow, harness, ledger, render, schema]
---

## Recommend

- **How should an item of `recommend` read when a later question replaced its recommendation?**
  - Recommended: (b) each item keeps what was asked and answered at the time, with the title in bold and the sub-items `Recommended:` and `Answer:` as they stood when it was answered; a later question that replaced it is its own item; a question asked again is one item; a question the person left unanswered is asked again, and one never answered gets a short item that says so; `rule-case-protocol` and its render change too.
  - Answer: the person proposed to record every answered question with its recommendation and answer as sub-items, asked how costly it is for `case-guppi` to place each item under its sub-case, and asked for an example first; after the example and the explanation, (b); a later question added the short item for a question never answered.
- **What happens to a question that never got an answer, now that `recommend` holds only answered questions?**
  - Recommended: (a) an unanswered question still gets a short item: its `Answer:` sub-item says it was not answered and names the later question that replaced it, if one did; the check and its promise do not change.
  - Answer: agreed, (a).

## History

- 2026-09-30 created · raw/2026-09-30/2042/ledger.md#case-557.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
