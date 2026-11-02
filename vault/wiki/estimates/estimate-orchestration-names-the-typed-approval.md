---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the reply in which the main agent calls ExitPlanMode holds, before the call, one line worded as a condition that names Esc, Shift+Tab and /approve-spec for a CLI that offers no approval, and claims nothing of the client
method: "by hand, after the librarian's run that applies the update of rule-orchestration naming /approve-spec and renders vault/wiki/orchestration.md: in the trial in the Claude Code CLI that reads estimate-skill-approve-spec-takes-the-spec, the reply that calls ExitPlanMode read in the transcript of that session under ~/.claude/projects/ against the Criterion"
checked: 2026-11-02
origin: raw/2026-11-01/1721/ledger.md#case-987.2
sprint: plugin
created: 2026-11-01
tags: [session, workflow, harness, plugin]
---

## Criterion

When:
In a working session the main agent writes the reply that calls `ExitPlanMode`.

Then:
Before the call, the reply holds one line worded as a condition: if the Claude Code CLI offers no approval for this plan, press Esc, leave Plan Mode with Shift+Tab and type `/approve-spec`.
**＋** The line claims nothing of the client: it does not say that the CLI withholds the approval.
**－** The line adds no step and no question: the agent calls `ExitPlanMode` in the same reply, only after `/pre-spec`, as before.

## Result

2026-11-02, the transcript cf6603da of session 1412 of the clone C:\PROJECTS\GUPPI-trial: the reply that calls ExitPlanMode holds before the call one line worded as a condition, "Если Claude Code CLI не предложит подтвердить этот план, нажмите Esc, выйдите из Plan Mode через Shift+Tab и наберите /approve-spec", which claims nothing of the client and adds no question

## History

- 2026-11-01 created · [[decision-case-987.2]]
- 2026-11-02 status: pending → passed · raw/2026-11-02/1337/ledger.md#L5
