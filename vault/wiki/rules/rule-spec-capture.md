---
type: rule
kind: Leaf
purpose: Prevents an approved Spec from existing only in Claude Code's plan file, outside the repository
status: built
enforcement: hook
implementation_ref: [guppi/spec.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-spec-capture-appends]]", "[[estimate-spec-capture-offers-the-fork]]"]
origin: raw/2026-09-09/ledger.md#case-20
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness, workflow]
---

## Purpose

Prevents an approved Spec from existing only in Claude Code's plan file, outside the
repository. The ledger's decision lines are routing only; their content is the Spec, and
page `origin` fields point at both. A Spec copied by hand is copied late, partially, or
not at all.

The file has three writers: the hook `guppi spec` on `PostToolUse` of `ExitPlanMode`, which appends the approved plan to `raw/<hi date>/<hi HHMM>/spec.md` once, stamped; the `Stop` hook of `rule-spec-write`, which, once the file stands, writes each Case ratified after the approval — its sections replaced, or placed — removes a superseded Case, and writes a defer-only Case at Retro under `## Deferred` (cases 421.1, 441); and Work Mode, which ticks the boxes of the `tasks` blocks. Having written the Spec, the hook prints the fork as `hookSpecificOutput.additionalContext`, the one shape in which the stdout of a `PostToolUse` hook reaches the agent (case 255),
into the context — `/work`, Work Mode on the Spec, or `/carry` to conserve it — naming the session folder and the Spec file; it blocks nothing: the agent asks the person by `AskUserQuestion` with the two options, the person picks, and the agent calls the skill picked (cases 190.5, 479.1). The mechanism lives in the docstring of `guppi/spec.py` (case 200.4).

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-20
- 2026-09-10 status: draft → built · cascade
- 2026-09-11 updated: spec.md has two writers: the hook at ExitPlanMode and the agent at Retro under ## Retro · [[decision-case-57]]
- 2026-09-11 status: built → draft · cascade
- 2026-09-12 updated: Work Mode is the third writer of spec.md, ticking boxes only (case 59.3) · [[decision-case-59.3]]
- 2026-09-12 updated: the Deferred heading, written at the close of Plan Mode and at Retro (case 59.5) · [[decision-case-59.5]]
- 2026-09-12 status: draft → built · cascade
- 2026-09-12 updated: the Spec lands in the session's folder raw/<hi date>/<hi HHMM>/ (case 73.2) · [[decision-case-73.2]]
- 2026-09-12 status: built → draft · cascade
- 2026-09-14 status: draft → built · cascade
- 2026-09-16 updated: after writing the Spec the hook prints the fork — Work Mode or /carry — naming the session folder and the Spec file (case 190.5) · [[decision-case-190.5]]
- 2026-09-16 estimate estimate-spec-capture-offers-the-fork added · [[decision-case-190.5]]
- 2026-09-16 status: built → draft · cascade
- 2026-09-16 updated: How it works dropped, its facts and the fork of 190.5 in Purpose; supersedes 196.4 (case 200.4) · [[decision-case-200.4]]
- 2026-09-16 status: draft → built · cascade
- 2026-09-20 updated: the fork line goes to the agent as additionalContext, not as plain stdout (case 255) · [[decision-case-255]]
- 2026-09-20 status: built → draft · cascade
- 2026-09-20 status: draft → built · cascade
- 2026-09-26 updated: the writers of spec.md: the Stop hook of rule-spec-write writes a Case ratified after the approval, removes a superseded one and writes a defer at Retro (case 441.6) · [[decision-case-441.6]]
- 2026-09-26 status: built → draft · cascade
- 2026-09-27 status: draft → built · cascade
- 2026-09-28 updated: the fork is asked by AskUserQuestion with the two options /work and /carry, and the agent calls the skill picked (case 479.1) · [[decision-case-479.1]]
- 2026-09-28 status: built → draft · cascade
- 2026-09-28 status: draft → built · cascade
