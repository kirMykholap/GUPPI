---
type: estimate
kind: QA
status: pending
target: "[[rule-orchestration]]"
purpose: Whether each call that dispatches case-guppi passes the effort of the kind of its Case, or the person's word up to high, holds it to the end of the Case, and passes no model
method: "by hand, at the Retro of the session that creates this Estimate, the new Render of rule-orchestration in the Spec read against the Criterion; by hand, after a session whose orchestration.md holds this text: each Agent call of case-guppi in the transcript of that session under ~/.claude/projects/ read against the Criterion, the transcript in the estimate line"
origin: raw/2026-11-04/0807/ledger.md#case-1029.1
sprint: plugin
created: 2026-11-04
tags: [session, workflow, harness]
---

## Criterion

When:
The main agent, with `vault/wiki/orchestration.md` loaded, dispatches `case-guppi` by the Agent tool for a Case of Plan Mode or Work Mode.

Then:
The call passes the parameter `effort`, by what the Frontier item and the person's words ask the Case to change.
**＋** The level is `low` for a Case that changes only the text of pages and no code, and for the setup Case and the opening Case of a sprint.
**＋** The level is `high` for a Case that changes a hook, a check or other code that judges a text.
**＋** The level is `medium` for every other Case.
**＋** The person's word on a Case sets another level up to `high`, and the call passes that level.
**＋** The level holds to the end of the Case, through each `SendMessage`.
**－** No new dispatch raises the level of a Case.
**－** No call passes `xhigh` or `max`.
**－** No call passes the parameter `model`.
**－** The dispatch of `.claude/agents/ask-guppi.md` does not change.

## History

- 2026-11-20 created · [[decision-case-1029.1]]
