---
type: estimate
kind: QA
status: passed
target: "[[rule-case-protocol]]"
purpose: Whether in a working session the main agent launches no Explore or Plan agent, asks by plain questions and no picker in Plan Mode, and exits Plan Mode only after pre-spec
method: by hand at the close of a later session, the Agent calls, the picker calls and the ExitPlanMode call of Plan Mode read in the transcript
checked: 2026-10-01
origin: raw/2026-09-30/2356/ledger.md#case-561.14
sprint: migration
created: 2026-09-30
tags: [session, workflow]
---

## Criterion

When:
A working session opened by `/hi` runs in Plan Mode, and the Plan Mode instructions of Claude Code stand in the main agent's context.

Then:
The main agent launches no Explore or Plan agent: `case-guppi` builds each Case, and `ask-guppi` asks the vault at `/pre-spec`.
**＋** It asks the person by a plain question in the chat and calls no picker tool while Plan Mode lasts.
**＋** It calls `ExitPlanMode` only after `/pre-spec` has run.
**－** The choice between `/work` and `/carry` after the Spec is written stays a picker, as `rule-spec-capture` sets it.

## Result

2026-10-01, by hand, session 1237 from /hi at 12:37:19 to ExitPlanMode at 14:20:02: the Agent calls were case-guppi three times and ask-guppi once at /pre-spec, no Explore or Plan agent; no picker tool was called while Plan Mode lasted, every question was a plain question in the chat; ExitPlanMode came after the prespec mark of 14:08:41; the choice between /work and /carry was the one picker, after ExitPlanMode

## History

- 2026-10-01 created · [[decision-case-561.14]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L33
