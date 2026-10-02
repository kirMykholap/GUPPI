---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether in a working session the main agent launches no Explore or Plan agent, asks by plain questions and no picker in Plan Mode, and exits Plan Mode only after pre-spec
method: by hand at the close of a later session, the Agent calls, the picker calls and the ExitPlanMode call of Plan Mode read in the transcript
checked: 2026-10-02
origin: raw/2026-09-30/2356/ledger.md#case-561.14
sprint: migration
created: 2026-09-30
tags: [session, workflow]
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

2026-10-02, the close of session 2049, by hand from the transcript: the Agent calls of Plan Mode were five dispatches of case-guppi and one of ask-guppi at /pre-spec, no Explore or Plan agent; no picker call while Plan Mode lasted, every question a plain question in the chat; ExitPlanMode called once, after /pre-spec and its second check; the only picker, the choice between /work and /carry, came after ExitPlanMode

## History

- 2026-10-01 created · [[decision-case-561.14]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L33
- 2026-10-02 renamed from `estimate-case-protocol-puts-the-harness-before-plan-mode` · [[decision-case-595.14]]
- 2026-10-02 updated: moved to rule-orchestration; the Criterion replaced whole - the order as orchestration.md sets it (case 595.14) · [[decision-case-595.14]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/2049/ledger.md#L28
