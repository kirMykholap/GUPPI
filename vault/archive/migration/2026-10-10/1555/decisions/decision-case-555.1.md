---
type: decision
case: "555.1"
status: archived
parent: "[[decision-case-555]]"
create: ["[[estimate-case-check-exits-2-on-an-error]]"]
update: ["[[rule-case-check]]"]
origin: raw/2026-09-30/2042/ledger.md#case-555.1
sprint: migration
created: 2026-09-30
tags: [hooks, harness, workflow, session]
---

## Recommend

- **The Case check at the end of a reply**
  Recommended: (a) block on its own error, as the ledger hook does.
  Answer: (a), agreed.
- **The Case check when `case-guppi` answers**
  Recommended: (a) keep it quiet on its own error, since a send-back would loop and the later refusal keeps a faulty Case from the person.
  Answer: (a). The person asked why, the main agent explained it, and the person agreed with the recommendation.

## History

- 2026-09-30 created · raw/2026-09-30/2042/ledger.md#case-555.1
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
