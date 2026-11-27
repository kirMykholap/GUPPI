---
type: decision
case: "1078"
status: current
children: ["[[decision-case-1078.1]]", "[[decision-case-1078.2]]", "[[decision-case-1078.3]]", "[[decision-case-1078.4]]"]
origin: raw/2026-11-27/0947/ledger.md#case-1078
sprint: plugin
created: 2026-11-27
tags: [hooks, harness, workflow, session]
---

## Problem

The plan file that Claude Code shows at the exit of Plan Mode holds every Case whole, so the person cannot see at a glance what the Spec will do, where it stops and what it checks.

## Recommend

- **Where the whole Cases stand before the approval**
  - Recommended: (a) a second file beside the plan file, which `spec.md` takes at the approval.
  - Answer: none of the options: the file that holds the whole Cases should be `spec.md` itself, the copying and the rest staying as they are, so that the plan the person is shown is a separate short file. Replaced by **How far the whole Cases move out of the plan file**.
- **What each Case shows in the map**
  - Recommended: (a) the name and the task list, cut from the Case by the hook.
  - Answer: (a), widened: not just the name but a short description of what each item, task or stop is.
- **Which visual elements the map uses**
  - Recommended: (b) plain Markdown and signs, with a summary table at the top.
  - Answer: the person likes the signs and wants them on the Frontier at least, with signs for `W`, `A` and the rest; for the plan file, try the Mermaid diagram (c), and if it does not work, fall back on the signs.
- **When you first see the map**
  - Recommended: (b) a preview in this Work Mode, and the reading at the next exit of Plan Mode.
  - Answer: (b).
- **How the approval is marked once spec.md holds the Cases from the start**
  - Recommended: (a) the stamp line marks the approval.
  - Answer: (a), with a question: can the hook also write the short entry into the plan file, or does that need the agent's judgment? The hook builds it from the Case, with no judgment of an agent. The move itself went to a later session by **How far the whole Cases move out of the plan file**.
- **Where the signs stand in the Frontier**
  - Recommended: (b) in the Frontier the replies show, and in the map.
  - Answer: (b).
- **Which sign each kind of line takes**
  - Recommended: (a) one sign for each kind and state, the letter beside it.
  - Answer: (a), but a blue question mark in place of 🙋 for a question to the person, if such a sign exists.
- **Which sign a question to you takes**
  - Recommended: (a) ❔, the white question mark.
  - Answer: (b) ❓, the red question mark.
- **How far the whole Cases move out of the plan file**
  - Recommended: (c) the map at the head of the plan file now, and the move into `spec.md` as a new item for a later session.
  - Answer: (c).

## History

- 2026-11-27 created · raw/2026-11-27/0947/ledger.md#case-1078
