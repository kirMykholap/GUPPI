---
type: decision
case: "934"
status: archived
defer: ["[[rule-spec-capture]]"]
supersedes: ["[[decision-case-909]]"]
superseded_by: ["[[decision-case-953]]"]
origin: raw/2026-10-30/1713/ledger.md#case-934
sprint: plugin
created: 2026-10-30
tags: [session, hooks, harness, workflow]
---

## Problem

The item of `rule-spec-capture` asks how GUPPI approves a Spec too long for the CLI, but the cause of the refusal is not known, and the person wants the approval kept as it is until a test shows whether Claude Code or the terminal is at fault.

## Recommend

- **How the person approves a long Spec in the CLI**
  - Recommended: (a) the person approves in the chat, and the hook before `ExitPlanMode` answers it with allow, so no dialog opens.
  - Answer: none of the options; keep the approval as it is, with the dialog of `ExitPlanMode` and the plan file unchanged; the cause is likely the terminal, since the test ran in a standalone PowerShell window and not in the terminal of the editor; rewrite the item as a bug with a test that finds the cause.
- **What the test compares**
  - Recommended: (a) one plan of the size that failed, approved in a standalone PowerShell window and in the terminal of VS Code, the size of each window and whether the dialog opened noted, the result recorded by a lesson line.
  - Answer: agreed, (a).
- **How this Case is checked**
  - Recommended: (a) by `estimate-backlog-renders`, with no new Estimate.
  - Answer: agreed, (a).

## Deferred

### [[rule-spec-capture]]

Bug: approval of a long plan is withheld in the Claude Code CLI, and the cause is not known: the Claude Code CLI or the terminal it runs in, since the refusal was seen in a standalone PowerShell window, with a plan of 15347 bytes, and the approval of a long plan stays as it is until the cause is known. Test: approve by ExitPlanMode one plan of that size in a standalone PowerShell window and in the terminal of VS Code, note the size of each window and whether the approval dialog opened, and record the result by a lesson line, so that the Case that fixes the bug knows where the fault lies (lesson-plugin-cli-withholds-approval-of-a-long-plan; moved here from the defer of case 909)

## History

- 2026-10-30 created · raw/2026-10-30/1713/ledger.md#case-934
- 2026-10-31 superseded by decision-case-953 · [[decision-case-953]]
- 2026-10-31 archived · superseded
- 2026-10-31 archived · cleanup
