---
type: rule
kind: Leaf
purpose: Prevents an approved Spec from existing only in Claude Code's plan file, outside the repository
status: built
enforcement: hook
implementation_ref: [.guppi/guppi/spec.py, .claude/settings.json]
parent: "[[rule-plan-mode]]"
estimates: ["[[estimate-spec-capture-appends]]", "[[estimate-spec-capture-offers-the-fork]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, hooks, harness, workflow]
core: true
---

## Purpose

Prevents an approved Spec from existing only in Claude Code's plan file, outside the
repository. The ledger's decision lines are routing only; their content is the Spec, and
page `origin` fields point at both. A Spec copied by hand is copied late, partially, or
not at all.

The file has three writers: the hook `guppi spec` on `PostToolUse` of `ExitPlanMode`, which appends the approved plan to `raw/<hi date>/<hi HHMM>/spec.md` once, stamped, and, where the Claude Code CLI withholds that approval, on `UserPromptSubmit` when the person types `/approve-spec`, as `uv run --project .guppi guppi spec --typed`, which blocks the prompt while the session is in Plan Mode, before `/pre-spec` or while the check of the plan finds a finding — by the judgment of `gate` of `.guppi/guppi/prespec.py`, the same function the hook of `rule-prespec-hook` runs at `ExitPlanMode` — and with no plan file or no `/hi` of the session, and otherwise appends the plan file of the session in the same way and gives the agent the same line, the skill of `rule-skill-approve-spec` telling the agent to follow it; the `Stop` hook of `rule-spec-write`, which, once the file stands, writes each Case ratified after the approval — its sections replaced, or placed — removes a superseded Case, and writes a Case the reply shows in the short form under `## Deferred`; and Work Mode, which ticks the boxes of the `tasks` blocks. Having written the Spec, the hook prints the fork as `hookSpecificOutput.additionalContext`, the one shape in which the stdout of a `PostToolUse` hook reaches the agent,
into the context — `/work`, Work Mode on the Spec, or `/carry` to conserve it — naming the session folder and the Spec file; it blocks nothing: the agent asks the person by `AskUserQuestion` with the two options, the person picks, and the agent calls the skill picked. When the approved plan names the `spec.md` of a conserved Spec — a folder under `vault/raw/` that holds `carry.md` — the hook prints in place of the fork a line that names that folder and tells the agent to call `/box` with it and to ask the person nothing: the person took that Spec at the Frontier, as `rule-spec-box` sets it. The mechanism lives in the docstring of `.guppi/guppi/spec.py`.

## History

- 2026-11-03 shipped with GUPPI
