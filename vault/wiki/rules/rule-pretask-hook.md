---
type: rule
kind: Leaf
purpose: Prevents a Spec from being approved before its decisions were checked against each other and the vault
status: built
enforcement: hook
implementation_ref: [guppi/pretask.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-pretask-hook-gates]]"]
origin: raw/2026-09-09/ledger.md#case-24.1
sprint: migration
created: 2026-09-09
tags: [session, workflow, hooks, harness]
---

## Purpose

Prevents a Spec from being approved before its decisions were checked against each other
and the vault. `PreToolUse` on `ExitPlanMode`: in a working session with no `pretask`
line of this session's stamp after its `hi`, `uv run guppi pretask` exits 2 with the reason, which
blocks the approval once; the `/pre-task` call leaves the stamped line through `guppi gate` and the next exit passes. A `pretask` of another stamp or `--------` does not count, and a foreign `session-start` resets nothing (case 136.2). An
ordinary session, one without `/hi`, is not gated: no governance applies there. The
same module serves the skill: `uv run guppi pretask --check <plan>` compares the plan
with the session's ledger lines and frontier (cases 59.1–59.3, 59.6); `/pre-task` runs
it, the hook does not.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-24.1
- 2026-09-10 status: draft → built · cascade
- 2026-09-12 updated: guppi pretask --check lives here and serves /pre-task (case 66) · [[decision-case-66]]
- 2026-09-14 updated: the ExitPlanMode hook binds the pretask mark by the session's stamp, not by position (case 136.2) · [[decision-case-136.2]]
