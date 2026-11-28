---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether each call that dispatches case-guppi passes the effort set by the widest change that its Frontier item, a fix the item offers, an answer to its question or the person's words could make, judged once at the dispatch, or the person's word up to high, holds it to the end of the Case, and passes no model
method: "by hand, at the Retro of the session that sets this Criterion, the new Render of rule-orchestration in the Spec read against the Criterion; by hand, after a session whose orchestration.md holds that Render: each Agent call of case-guppi in the transcript of that session under ~/.claude/projects/ read against the Criterion, with the Frontier item and the person's words its prompt holds, the transcript in the estimate line"
checked: 2026-11-26
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
The main agent, with `vault/wiki/orchestration.md` loaded, dispatches `case-guppi` by the Agent tool for a Case of Plan Mode or Work Mode.

Then:
The call passes the parameter `effort`, judged once at the dispatch by the widest change that the Frontier item, each fix its words offer, each answer its question could lead to and the person's words would make.
**＋** The level is `low` when each such change touches only the text of pages and no code, and for the setup Case and the opening Case of a sprint.
**＋** The level is `high` when one such change touches a hook, a check or other code that judges a text.
**＋** The level is `medium` for every other item, an item where one such change touches other code included.
**＋** The person's word on a Case sets another level up to `high`, and the call passes that level.
**＋** The level holds to the end of the Case, through each `SendMessage`, also where the built Case changes more than its item asked.
**－** No new dispatch raises the level of a Case.
**－** No call passes `xhigh` or `max`, and no call passes the parameter `model`.
**－** The dispatch of `.claude/agents/ask-guppi.md` does not change.

## Result

2026-11-26, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
