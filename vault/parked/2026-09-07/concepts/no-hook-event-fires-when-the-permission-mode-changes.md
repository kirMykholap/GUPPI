---
title: "No hook event fires when the permission mode changes, and no hook output can cause one"
type: concept
status: current
authority: permission-mode-visibility
basis: external
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/hooks/check-the-plan.ps1"]
tags: [harness, agents, process]
---

# `permission_mode` is input-only

**Every hook payload carries the mode the session is in, and nothing a hook prints can change it.**
There is no `PermissionModeChanged` event to register against, and no field in a hook's JSON output
that requests a transition.

**So a `Shift+Tab` out of plan mode is invisible.** A session can leave plan mode without any tool
call, and the harness learns about it only at the next event of some other kind.

# What follows for anything built on the mode

**A mode transition can be observed only where it coincides with a tool call.** `ExitPlanMode` is
that coincidence and it is the only one this harness has
([[exit-plan-mode-is-an-ordinary-tool-and-the-owner-performs-the-transition]]).

**That hole is why the write net exists.** A session that leaves plan mode by hand and starts
editing passes through no plan event at all, so the pre-task question has to be asked again at the
first write ([[the-guard-chain-appends-the-net-rather-than-branching-on-it]],
[[the-pre-task-state-machine-has-a-flag-for-the-plan-and-a-flag-for-the-write]]).

**And the mode is worth recording where it is seen**, because it is the only evidence of what the
session actually started in — which is not necessarily what the repository's settings say
([[the-vs-code-extension-reads-its-starting-mode-from-user-settings]]).
