---
type: decision
case: "521.2"
status: archived
create: ["[[estimate-materialize-marks-a-comment]]"]
update: ["[[rule-materialize]]"]
origin: raw/2026-09-29/1753/ledger.md#case-521.2
sprint: migration
created: 2026-09-29
tags: [harness, workflow, ledger]
---

## Problem

YAML cuts a value without quotes at ` #`, and no check sees the cut. So a short-form Case can reach the Spec, the Decision page and the backlog with a value the person never wrote, as the purpose of case 519 did. The backlog item of `rule-estimates-schema` also carries that cut text, and the sentence it was meant to correct is still wrong.

## History

- 2026-09-29 created · raw/2026-09-29/1753/ledger.md#case-521.2
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
