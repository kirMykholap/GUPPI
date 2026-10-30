---
type: estimate
kind: QA
status: pending
target: "[[rule-where-to-stop]]"
purpose: Whether a stop reply that asks the person to run commands by hand writes each command whole in each step, its variables included, with no reference to another step
method: "by hand, after the first stop of Work Mode under the new text of vault/wiki/where-to-stop.md whose reply asks the person to run commands by hand: that reply read against each line of the Criterion, recorded in the estimate line"
origin: raw/2026-10-30/2345/ledger.md#case-945
sprint: plugin
created: 2026-10-30
tags: [session, workflow, harness]
---

## Criterion

When:
Work Mode stops on a condition of `vault/wiki/where-to-stop.md`, and the reply asks the person to run commands by hand.

Then:
Each step of the reply writes out whole each command it asks the person to run, as the person types it, with each variable, folder and flag the command needs.
**＋** A step that starts a program in a new window or terminal writes the variables that the start needs in its own command.
**－** No step names a part of its command by a reference to another step.

## History

- 2026-10-31 created · [[decision-case-945]]
