---
type: decision
case: "1039"
status: current
children: ["[[decision-case-1039.1]]", "[[decision-case-1039.2]]"]
origin: raw/2026-11-20/1353/ledger.md#case-1039
sprint: plugin
created: 2026-11-20
tags: [session, workflow, harness, case-build, hooks]
---

## Problem

A Case built later in a session can make lines of a Case already built false, and nothing finds them before `/pre-spec`, so the stale Case is built and ratified again late.

## Recommend

- **Which step should find the lines of other Cases of the session that a new Case makes stale?**
  - Recommended: (a) the check of a built Case also searches the session's Case files.
  - Answer: agreed, (a).
- **Which Case files of the session should the check search?**
  - Recommended: (a) every Case file of the session but the Case's own.
  - Answer: agreed, (a).
- **What should the agent do with a line of another Case that its change makes false?**
  - Recommended: (a) the stale line goes on an `**Other Case:**` line.
  - Answer: agreed, (a).
- **Should this Case close the Insight that the lesson joined?**
  - Recommended: (a) yes, set the Insight to actioned.
  - Answer: agreed, (a).

## History

- 2026-11-23 created · raw/2026-11-20/1353/ledger.md#case-1039
