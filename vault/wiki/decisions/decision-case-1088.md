---
type: decision
case: "1088"
status: current
update: ["[[rule-orchestration]]", "[[insight-orchestration-frontier-closer-leaves-the-box-open]]"]
origin: raw/2026-11-27/2214/ledger.md#case-1088
sprint: plugin
created: 2026-11-27
tags: [session, workflow, harness, orchestration]
---

## Problem

The main agent closes a Frontier line by an edit of its end alone and is refused by the guard each time, since the text it reads never says that the box and the closer change in one edit of the whole line.

## Recommend

- **What the Case does about the Insight**
  - Recommended: (b) one sentence in `orchestration.md` saying that a line closes by one `Edit` of the whole line, and the Insight set `actioned`.
  - Answer: agreed, (b).

## History

- 2026-11-28 created · raw/2026-11-27/2214/ledger.md#case-1088
