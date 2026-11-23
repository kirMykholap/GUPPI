---
type: decision
case: "1040"
status: current
create: ["[[estimate-plugin-install-asks-one-approval-in-plan-mode]]"]
update: ["[[rule-plugin-install]]"]
origin: raw/2026-11-20/1353/ledger.md#case-1040
sprint: plugin
created: 2026-11-20
tags: [plugin, harness, render]
---

## Problem

In a session that stands in Plan Mode, `/guppi:install` can write nothing until the person approves a plan, but the skill sets no such step, so the approval comes by chance and the person sees no list of the files of the project that will move.

## Recommend

- **What /guppi:install does when its session stands in Plan Mode**
  - Recommended: (a) a written plan step: the skill shows a plan of each file it copies and each file of the project it sets aside, asks the approval once, then runs the install.
  - Answer: agreed, (a).
- **Which approval option the plan names**
  - Recommended: (a) the plan names no option, and the person picks one.
  - Answer: agreed, (a).
- **What the plan step does when uv is missing**
  - Recommended: (a) on the person's yes, the installer of `uv` joins the plan as its first item and runs after the one approval.
  - Answer: agreed, (a).
- **When the new Estimate is read**
  - Recommended: (a) by hand, after the librarian's run of this session.
  - Answer: agreed, (a).

## History

- 2026-11-23 created · raw/2026-11-20/1353/ledger.md#case-1040
