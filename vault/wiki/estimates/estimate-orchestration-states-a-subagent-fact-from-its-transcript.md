---
type: estimate
kind: QA
status: passed
target: "[[rule-orchestration]]"
purpose: Whether the main agent states as its own what a subagent of the session did only after it reads the fact in the transcript of that subagent, and passes on a subagent's report of its own calls marked as that report
method: "by hand at the Retro of the session that changes it: the new Render of rule-orchestration in the Spec read against the Criterion; after the first reply of the main agent under that Render that states what a subagent did: that reply and the tool calls of the main agent before it read against the Criterion, recorded in the estimate line"
checked: 2026-10-30
origin: raw/2026-10-30/0304/ledger.md#case-923
sprint: plugin
created: 2026-10-30
tags: [session, workflow, orchestration]
---

## Criterion

When:
The main agent, with `vault/wiki/orchestration.md` rendered from `rule-orchestration`, states in a reply what a subagent of the session did: a tool call it made, a tool error it met, or a hook that refused its call.

Then:
Before a reply that states such a fact as its own, the main agent has read that fact in the transcript of that subagent.
**＋** The reply states no such fact as its own from the summary of the subagent alone.
**－** What a subagent reports of its own calls, such as the rules a search of `ask-guppi` broke, the main agent may pass on with no transcript, marked as the report of that subagent.
**－** A ledger line of a showing is still copied from the summary of `case-guppi`, as `vault/wiki/orchestration.md` sets it.

## Result

2026-10-30, Work readings of session 2005, transcript 5c343872 of session 1713, the first session under the Render: no reply of the main agent states a tool call, a tool error or a hook refusal of a subagent as its own; the first reply that states what a subagent did, at 17:58:59, passes on the librarian's report of its own calls (git diff -U0 on decision-case-897, "No hook refused a call") marked "Ниже его отчёт без изменений"; only the − line of the Criterion was exercised

## History

- 2026-10-30 created · [[decision-case-923]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/2005/ledger.md#L53
