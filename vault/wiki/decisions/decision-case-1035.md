---
type: decision
case: "1035"
status: current
children: ["[[decision-case-1035.1]]", "[[decision-case-1035.2]]", "[[decision-case-1035.3]]"]
origin: raw/2026-11-04/0807/ledger.md#case-1035
sprint: plugin
created: 2026-11-04
tags: [session, hooks, harness, ledger, workflow]
---

## Problem

Under Claude Code 2.1.317 the bracket of a refusal names no command, so no `Stop` hook of GUPPI finds its own refusal: the ledger hook holds a lesson again at each repeat, and each hook that tells a thing once a stretch tells it again.

## Recommend

- **How a hook recognises its own earlier refusal**
  - Recommended: (a) by the hook's name at the head of its own lines, the bracket ignored, the `--plan` run's lines opening with `onward --plan:`.
  - Answer: agreed, (a).
- **Which hooks the fix covers**
  - Recommended: (a) all four hooks, through the one shared reader.
  - Answer: agreed, (a).

## History

- 2026-11-20 created · raw/2026-11-04/0807/ledger.md#case-1035
