---
type: decision
case: "876"
status: current
defer: ["[[rule-ledger-write]]", "[[rule-orchestration]]"]
supersedes: ["[[decision-case-836]]", "[[decision-case-863]]"]
origin: raw/2026-10-17/0027/ledger.md#case-876
sprint: plugin
created: 2026-10-17
tags: [session, hooks, harness, ledger, workflow]
---

## Context

Two live Decision pages hold defers from before Case 865: `decision-case-836` defers `lesson-ledger-window-stops-at-a-resume-on-the-next-day` and `lesson-case-build-agent-context-grows-on-every-resume`, and `decision-case-863` defers `decision-case-855`. Neither a Lesson nor a Decision page carries `deferred_by`, so `backlog.md` shows none of the three. The person chose: each lesson's cause moves to a defer of the rule page whose change would fix it, `rule-ledger-write` and `rule-orchestration`, and `decision-case-863` retires with nothing in its place, since in session 2104 the person chose no Case for the out-of-date sentence of `decision-case-855`. `estimate-backlog-renders` and `estimate-generate-cascades` already check the mechanism; the case file is `raw/2026-10-17/0027/cases/case-876.md`.

## Problem

Two live Decision pages put off two lessons and one Decision page, and since neither kind of page carries `deferred_by`, no line of `backlog.md` shows the three items.

## Deferred

### [[rule-ledger-write]]

session_event_logs of .guppi/guppi/ledger.py walks the event logs back from today and stops at the first date that holds a session-start of the stamp, so after a resume on the next day the ledger hook finds no /hi and refuses the decision lines (lesson-ledger-window-stops-at-a-resume-on-the-next-day); moved here from the defer of the lesson by Case 836

### [[rule-orchestration]]

Each round and each rebuild resumes the same case-guppi by SendMessage with its whole transcript, so its context only grows, and nothing caps it or hands a rebuild to a fresh agent with the case file and the reason alone (lesson-case-build-agent-context-grows-on-every-resume); moved here from the defer of the lesson by Case 836

## History

- 2026-10-17 created · raw/2026-10-17/0027/ledger.md#case-876
