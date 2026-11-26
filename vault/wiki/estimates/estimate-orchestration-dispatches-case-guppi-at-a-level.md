---
type: estimate
kind: QA
status: passed
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

2026-11-26, /hi of session 2333, transcript ~/.claude/projects/c--PROJECTS-GUPPI/86f6e9ab-3ce6-47ac-b6b5-c5e6f1340992.jsonl of session 1515 and the .meta.json of its subagents: three Agent calls of case-guppi, each passed effort high and each subagent ran at high — 1069 on C2, frontierguard judging a shell command (L96), 1070 on C3, config.py judging the value of main_branch and the render refusing it (L301), 1071 on C4, prespec reporting a method that reads a transcript (L302) — each item a change to a hook or a check that judges a text; the answers of the rounds, the second passes, the findings of /pre-spec and the rebuild of 1070 after prespec --check went by SendMessage, no Case was dispatched twice; no call passed model, xhigh or max; the dispatch of ask-guppi (L815) passed no effort

## History

- 2026-11-20 created · [[decision-case-1029.1]]
- 2026-11-25 status: pending → failed · raw/2026-11-25/0605/ledger.md#L1
- 2026-11-25 updated: the Criterion replaced whole — the level is judged once at the dispatch from the item and the person's words, and stands where the built Case changes more · [[decision-case-1054.1]]
- 2026-11-26 status: pending → failed · raw/2026-11-26/1336/ledger.md#L1
- 2026-11-26 updated: the Criterion replaced whole — the level follows the widest change the item, a fix it offers or an answer to its question could make · [[decision-case-1064]]
- 2026-11-27 status: pending → passed · raw/2026-11-26/2333/ledger.md#L2
