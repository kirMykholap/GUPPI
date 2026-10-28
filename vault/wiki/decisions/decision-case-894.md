---
type: decision
case: "894"
status: current
children: ["[[decision-case-894.1]]", "[[decision-case-894.2]]", "[[decision-case-894.3]]"]
origin: raw/2026-10-28/1907/ledger.md#case-894
sprint: plugin
created: 2026-10-28
tags: [hooks, harness, workflow, session]
---

## Problem

In Plan Mode Claude Code asks the person before each write of `case-guppi` to its Case file, though the person ratifies each Case anyway. The setting the harness relied on, `permissionMode: auto`, is ignored in plan mode, and the allow list does not stop the prompt there.

## Recommend

- **How does the write of a Case file stop asking?**
  - Recommended: no option recommended, since the documentation does not settle whether an allow rule works in plan mode; (a), case files on the allow list, if the write of `frontier.md` did not ask.
  - Answer: the write of `frontier.md` asked for permission in this session; what to do then, and how to keep `case-guppi` from asking. Replaced by the question who writes the Case file.
- **What happens to the `permissionMode: auto` line of the helper?**
  - Recommended: (a) keep the line, and fix what the pages claim for it.
  - Answer: agreed, (a).
- **What does the check of `rule-permissions` promise for reads outside the project?**
  - Recommended: (a) drop that promise.
  - Answer: agreed, (a).
- **Who writes the Case file, so that no question comes?**
  - Recommended: (a) the guard hook writes the file and stops the call.
  - Answer: agreed, (a); let us try it this way.
- **How is the hook's write checked?**
  - Recommended: (a) rewrite the guard's check, and keep the "no question" promise in the check of `rule-permissions`, read after the first Case file written in plan mode of a later session.
  - Answer: agreed, (a).
- **What happens when the hook cannot make the write?**
  - Recommended: (a) an Edit that cannot apply is stopped with its reason; an error of the hook lets the call run.
  - Answer: agreed, (a).
- **One Case, or one part per page?**
  - Recommended: (a) three parts under one Case.
  - Answer: agreed, (a).

## History

- 2026-10-28 created · raw/2026-10-28/1907/ledger.md#case-894
