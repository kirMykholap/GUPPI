---
type: estimate
kind: QA
status: pending
target: "[[rule-orchestration]]"
purpose: Whether each call that dispatches case-guppi passes the effort set by the widest change that its Frontier item, a fix the item offers, an answer to its question or the person's words could make, judged once at the dispatch, or the person's word up to high, holds it to the end of the Case, and passes no model
method: "by hand, at the Retro of the session that sets this Criterion, the new Render of rule-orchestration in the Spec read against the Criterion; by hand, after a session whose orchestration.md holds that Render: each Agent call of case-guppi in the transcript of that session under ~/.claude/projects/ read against the Criterion, with the Frontier item and the person's words its prompt holds, the transcript in the estimate line"
checked: 2026-11-26
origin: raw/2026-11-04/0807/ledger.md#case-1029.1
sprint: plugin
created: 2026-11-04
tags: [session, workflow, harness]
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

2026-11-26, /hi of session 1336, transcript ~/.claude/projects/c--PROJECTS-GUPPI/64d3e510-98a4-4064-b510-3e5e3bf57c6a.jsonl of session 2003 and the .meta.json of its subagents: four Agent calls of case-guppi, each passed effort — 1058 low (L132), 1059 medium (L263), 1060 medium (L424), 1061 low (L609) — and each subagent ran at that level; the answers, the findings of /pre-spec and the rebuild of 1060 as 1063 went by SendMessage, no Case was dispatched twice; no call passed model, xhigh or max; the dispatch of ask-guppi (L773) passed no effort; not met: 1060 was dispatched medium on the item C4, which asked only how case-schema.md sets a passed one-off Estimate, text of pages and no code, where the Criterion sets low; 1061 was dispatched low on the item C2, whose first option was that the copy is written only after guppi style is clean, a change to the code of guppi ship, where the Criterion sets medium

## History

- 2026-11-20 created · [[decision-case-1029.1]]
- 2026-11-25 status: pending → failed · raw/2026-11-25/0605/ledger.md#L1
- 2026-11-25 updated: the Criterion replaced whole — the level is judged once at the dispatch from the item and the person's words, and stands where the built Case changes more · [[decision-case-1054.1]]
- 2026-11-26 status: pending → failed · raw/2026-11-26/1336/ledger.md#L1
- 2026-11-26 updated: the Criterion replaced whole — the level follows the widest change the item, a fix it offers or an answer to its question could make · [[decision-case-1064]]
