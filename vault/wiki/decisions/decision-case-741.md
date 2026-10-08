---
type: decision
case: "741"
status: current
update: ["[[rule-where-to-stop]]", "[[estimate-where-to-stop-stops-only-on-its-conditions]]", "[[insight-permissions-classifier-weighs-the-rules-not-the-persons-word]]"]
origin: raw/2026-10-08/2134/ledger.md#case-741
sprint: migration
created: 2026-10-08
tags: [session, workflow, harness, render]
---

## Problem

When the auto mode classifier refuses an action that a ratified task needs, the run goes on without it. The task stays undone, even when the person asked for it, and only the person can run it.

## Recommend

- **What to do with this Insight**
  - Recommended: (a) a new stop condition in `where-to-stop.md`: the run stops on a refusal of the classifier, gives the person the command to type after `!`, and goes on after the person has run it; the Insight is set `actioned`, and the Criterion of `estimate-where-to-stop-stops-only-on-its-conditions` is replaced.
  - Answer: agreed, (a).

## History

- 2026-10-08 created · raw/2026-10-08/2134/ledger.md#case-741
