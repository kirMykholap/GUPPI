---
type: decision
case: "752"
status: archived
create: ["[[estimate-case-build-finds-an-existing-judgment]]"]
update: ["[[rule-case-build]]", "[[insight-workflow-case-written-without-reading-the-pages-it-changes]]"]
origin: raw/2026-10-09/2049/ledger.md#case-752
sprint: migration
created: 2026-10-09
tags: [session, workflow, harness]
---

## Problem

A task of a Case can add a second copy of a judgment the code already holds, and nothing catches it before `/pre-spec`, after the person has ratified the Case.

## Recommend

- **Where does the step that catches a second copy stand?**
  - Recommended: (a) a step in the instructions of `case-guppi`: before a task adds code that judges a text, it searches the code for an existing implementation, and the task imports it or moves it into one module.
  - Answer: agreed, (a).
- **How wide is the search for an existing copy?**
  - Recommended: (a) the code under `guppi/`, judged by what it does, with a test over both sides where they cannot share the code.
  - Answer: agreed, (a).
- **How is the new step checked?**
  - Recommended: (a) a new Estimate of its own, read by hand at the Retro of this session against the new Render in the Spec.
  - Answer: agreed, (a).
- **What happens to the lesson cluster this lesson belongs to?**
  - Recommended: (a) the Case sets the group to `actioned`, with this Case as the fix.
  - Answer: agreed, (a).

## History

- 2026-10-09 created · raw/2026-10-09/2049/ledger.md#case-752
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
