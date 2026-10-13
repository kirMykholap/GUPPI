---
type: decision
case: "796"
status: current
children: ["[[decision-case-796.1]]", "[[decision-case-796.2]]"]
origin: raw/2026-10-13/1426/ledger.md#case-796
sprint: plugin
created: 2026-10-13
tags: [hooks, harness, workflow, render]
---

## Problem

An agent can rewrite a source file with a script typed inline and fed to an interpreter in a Bash or PowerShell call, and no check refuses it before it runs. The repair after the call fixes the line endings but not the choice, and the same choice has rewritten a source file in three sessions.

## Recommend

- **Where the fix lives**
  - Recommended: (a) the check before a Bash call also refuses a heredoc fed into an interpreter.
  - Answer: (a).
- **PowerShell calls**
  - Recommended: (a) Bash only, with the PowerShell gap named as not done.
  - Answer: (b) Bash and PowerShell.
- **Where the PowerShell check lives**
  - Recommended: (a) a new rule beside the Bash one, both checks importing one list of interpreters.
  - Answer: agreed, (a).
- **What the PowerShell check refuses**
  - Recommended: (a) a here-string piped into an interpreter.
  - Answer: agreed, (a).
- **A script passed by a flag**
  - Recommended: (a) leave it out, named as not done.
  - Answer: agreed, (a).
- **The section on how the Bash check works**
  - Recommended: (a) remove the section by hand, once.
  - Answer: agreed, (a).

## History

- 2026-10-13 created · raw/2026-10-13/1426/ledger.md#case-796
