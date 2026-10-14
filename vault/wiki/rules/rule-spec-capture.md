---
type: rule
kind: Leaf
purpose: Prevents an approved Spec from existing only in Claude Code's plan file, outside the repository
status: built
enforcement: hook
implementation_ref: [guppi/spec.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, hooks, harness, workflow]
core: true
---

## Purpose

Prevents an approved Spec from existing only in Claude Code's plan file, outside the
repository. The ledger's decision lines are routing only; their content is the Spec, and
page `origin` fields point at both. A Spec copied by hand is copied late, partially, or
not at all.

The file has three writers: the hook `guppi spec` on `PostToolUse` of `ExitPlanMode`, which appends the approved plan to `raw/<hi date>/<hi HHMM>/spec.md` once, stamped; the `Stop` hook of `rule-spec-write`, which, once the file stands, writes each Case ratified after the approval — its sections replaced, or placed — removes a superseded Case, and writes a defer-only Case under `## Deferred`; and Work Mode, which ticks the boxes of the `tasks` blocks. Having written the Spec, the hook prints the fork as `hookSpecificOutput.additionalContext`, the one shape in which the stdout of a `PostToolUse` hook reaches the agent,
into the context — `/work`, Work Mode on the Spec, or `/carry` to conserve it — naming the session folder and the Spec file; it blocks nothing: the agent asks the person by `AskUserQuestion` with the two options, the person picks, and the agent calls the skill picked. When the approved plan names the `spec.md` of a conserved Spec — a folder under `vault/raw/` that holds `carry.md` — the hook prints in place of the fork a line that names that folder and tells the agent to call `/box` with it and to ask the person nothing: the person took that Spec at the Frontier, as `rule-spec-box` sets it. The mechanism lives in the docstring of `guppi/spec.py`.

## History

- 2026-10-14 shipped with GUPPI
