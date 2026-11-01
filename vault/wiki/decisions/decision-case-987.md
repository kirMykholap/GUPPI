---
type: decision
case: "987"
status: current
children: ["[[decision-case-987.1]]", "[[decision-case-987.2]]"]
origin: raw/2026-11-01/1721/ledger.md#case-987
sprint: plugin
created: 2026-11-01
tags: [session, workflow, harness, plugin, render, hooks, git]
---

## Problem

In the Claude Code CLI a Spec of a few Cases cannot be approved, so the session never reaches Work Mode, and GUPPI gives the person no other way to approve it.

## Recommend

- **What GUPPI does when the CLI withholds the approval**
  - Recommended: (c) approval by a typed command after leaving Plan Mode.
  - Answer: agreed, (c).
- **What the person types**
  - Recommended: (a) `/approve`.
  - Answer: the person's own name, `/approve-spec`.
- **What the command checks before it takes the Spec**
  - Recommended: (a) the same checks as the exit, through the same code, and the command refused while the session is still in Plan Mode.
  - Answer: agreed, (a).
- **How the person learns the way**
  - Recommended: (a) the agent names the way after an exit refused with no words of the person.
  - Answer: agreed, (a).
- **How the Case is checked**
  - Recommended: (a) a new Estimate, checked by a test of the hook and a by-hand trial in the CLI in this session's Work Mode.
  - Answer: agreed, (a).
- **What becomes of the insight and the README note**
  - Recommended: (a) the insight closed as fixed by this Case, the README left to its item of the sprint.
  - Answer: agreed, (a).
- **How the agent's words after a refused exit are checked**
  - Recommended: (a) a new Estimate, read in the record of the same CLI trial.
  - Answer: agreed, (a).
- **When the agent names the way**
  - Recommended: (a) in the reply that calls `ExitPlanMode`, one line before the call, worded as a condition, since the documentation shows that after Esc at the dialog Claude Code stops the turn and the agent gets no reply.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, the person agreed that the trials in the CLI do not run in this session's Work Mode, since the skill `/approve-spec`, its hook in `.claude/settings.json` and the new sentence of `orchestration.md` exist only after the librarian's render after this session.
  - Taken: the by-hand part of the method of each new Estimate waits for the librarian's run after this session; only the test of 987.1 is read in this session.

## History

- 2026-11-01 created · raw/2026-11-01/1721/ledger.md#case-987
