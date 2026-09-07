---
title: "`ExitPlanMode` is an ordinary tool, and the owner performs the transition"
type: concept
status: current
authority: exit-plan-mode-events
basis: external
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/settings.json"]
tags: [harness, agents, process]
---

# It matches by name, on either event

**`PreToolUse` and `PostToolUse` both match `ExitPlanMode` by name**, like any other tool. That is
what makes the plan moment addressable at all:

- **`PreToolUse` fires before the plan is presented** — a finished plan exists and no source has
  been touched, which is the only moment a pre-task is worth what it costs
  ([[the-plan-check-hook]]);
- **`PostToolUse` fires after the tool succeeds** — that is, after the owner approves — and is
  therefore the machine-observable form of an approval.

# The agent does not perform the transition

**Asking Claude in chat to change the permission mode does not work.** The approve prompt is the
owner's, and it offers auto mode, manual edits, or keep planning.

**So the approved scope is recorded at `PostToolUse` and nowhere else**: there is no hook event for a
permission-mode change and no hook output that can cause one
([[no-hook-event-fires-when-the-permission-mode-changes]]).

**Whether a rejected plan also reaches `PostToolUse` is not measured.** If it does, a scope is
recorded that was never approved, and the effect is that the next plan is asked for a fresh
pre-task — failing towards asking more often, which is the direction a guard is allowed to be wrong
in ([[the-pre-task-state-machine-has-a-flag-for-the-plan-and-a-flag-for-the-write]]).
