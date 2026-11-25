---
type: estimate
kind: QA
status: pending
target: "[[rule-orchestration]]"
purpose: Whether each call that dispatches case-guppi passes the effort that its Frontier item and the person's words ask for, judged once at the dispatch, or the person's word up to high, holds it to the end of the Case, and passes no model
method: "by hand, at the Retro of the session that sets this Criterion, the new Render of rule-orchestration in the Spec read against the Criterion; by hand, after a session whose orchestration.md holds that Render: each Agent call of case-guppi in the transcript of that session under ~/.claude/projects/ read against the Criterion, with the Frontier item and the person's words its prompt holds, the transcript in the estimate line"
checked: 2026-11-25
origin: raw/2026-11-04/0807/ledger.md#case-1029.1
sprint: plugin
created: 2026-11-04
tags: [session, workflow, harness]
---

## Criterion

When:
The main agent, with `vault/wiki/orchestration.md` loaded, dispatches `case-guppi` by the Agent tool for a Case of Plan Mode or Work Mode.

Then:
The call passes the parameter `effort`, judged once at the dispatch by what the Frontier item and the person's words ask the Case to change.
**＋** The level is `low` for an item that asks to change only the text of pages and no code, and for the setup Case and the opening Case of a sprint.
**＋** The level is `high` for an item that asks to change a hook, a check or other code that judges a text.
**＋** The level is `medium` for every other item.
**＋** The person's word on a Case sets another level up to `high`, and the call passes that level.
**＋** The level holds to the end of the Case, through each `SendMessage`, also where the built Case changes more than its item asked.
**－** No new dispatch raises the level of a Case.
**－** No call passes `xhigh` or `max`.
**－** No call passes the parameter `model`.
**－** The dispatch of `.claude/agents/ask-guppi.md` does not change.

## Result

2026-11-25, /hi of session 0605, transcript ~/.claude/projects/c--PROJECTS-GUPPI/68550048-efc7-4790-9bd8-17ed548134c2.jsonl of session 1353 and the .meta.json of its subagents: five Agent calls of case-guppi, each passed effort — 1039 medium (L123), 1040 medium (L267), 1041 low (L380), 1042 medium (L462), 1043 low (L628) — and each subagent ran at that level; no call passed model, xhigh or max; no Case was dispatched twice, the answers and the findings of /pre-spec went by SendMessage; the dispatch of ask-guppi (L791) passed no effort, as before; not met: Case 1039, dispatched medium on the item C6 that named no code, changed .guppi/guppi/casecheck.py, the code of the hook of rule-case-check (1039.1), where the Criterion sets high for a Case that changes a hook

## History

- 2026-11-20 created · [[decision-case-1029.1]]
- 2026-11-25 status: pending → failed · raw/2026-11-25/0605/ledger.md#L1
- 2026-11-25 updated: the Criterion replaced whole — the level is judged once at the dispatch from the item and the person's words, and stands where the built Case changes more · [[decision-case-1054.1]]
