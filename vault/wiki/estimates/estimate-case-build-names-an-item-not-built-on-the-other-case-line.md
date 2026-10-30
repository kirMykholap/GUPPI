---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi names a Frontier item with no Case yet, by its id and the change it needs, on the Other Case line of its summary, and takes into the Case of an item the change its prompt carries from such a line
method: by hand, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec read against the Criterion, recorded in the estimate line
origin: raw/2026-10-29/2341/ledger.md#case-916.2
sprint: plugin
created: 2026-10-29
tags: [session, workflow, harness]
---

## Criterion

When:
In Plan Mode `case-guppi`, by `.claude/agents/case-guppi.md`, builds a Case that leaves a change to an item of `raw/<date>/<hi HHMM>/frontier.md` that no Case of the session has built, as a bound the person chose in a round.
**＋** Or the main agent dispatches `case-guppi` for an item with a prompt that holds a change an `**Other Case:**` line of another Case of the session asks of that item.

Then:
`case-guppi` writes into `context` the Frontier id of that item and what its Case must do, and its summary repeats both on a line `**Other Case:**` under the item of its own Case.
**＋** Dispatched with such a change, `case-guppi` takes it into the Case of the item, or answers with a round where it opens a fork, and the `context` names the Case that asked it.
**－** For a clash with another Case of the session, `case-guppi` keeps the form `.claude/agents/case-guppi.md` sets today.

## Result

2026-10-30, Retro of session 2341: the new Render of rule-case-build in the Spec (case 916.2), its old string standing once on the page, has case-guppi name in context the item by its Frontier id and the change it needs and repeat both on the Other Case line, and take into its Case a change its prompt carries or answer with a round, naming the Case that asked it; in this session Case 917.1 named C3 that way and Case 918 took the change in

## History

- 2026-10-30 created · [[decision-case-916.2]]
- 2026-10-30 status: pending → passed · raw/2026-10-29/2341/ledger.md#L34
