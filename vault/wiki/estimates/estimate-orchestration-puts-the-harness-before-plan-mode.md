---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether in a working session the main agent launches no Explore or Plan agent, asks by plain questions and no picker in Plan Mode, and exits Plan Mode only after pre-spec
method: by hand at the close of a later session, the Agent calls, the picker calls and the ExitPlanMode call of Plan Mode read in the transcript
checked: 2026-10-02
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow]
core: true
---

## Criterion

When:
A working session opened by `/hi` runs in Plan Mode, the Plan Mode instructions of Claude Code stand in the main agent's context, and `vault/wiki/orchestration.md` is rendered from `rule-orchestration`.

Then:
The main agent launches no Explore or Plan agent: `case-guppi` builds each Case, and `ask-guppi` asks the vault at `/pre-spec`.
**＋** It asks the person by a plain question in the chat and calls no picker tool while Plan Mode lasts.
**＋** It calls `ExitPlanMode` only after `/pre-spec` has run.
**－** The choice between `/work` and `/carry` after the Spec is written stays a picker, as `rule-spec-capture` sets it.

## Result

2026-10-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
