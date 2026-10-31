---
type: estimate
kind: QA
status: passed
target: "[[rule-where-to-stop]]"
purpose: Whether a stop reply that asks the person to run commands by hand writes each command whole in each step, its variables included, with no reference to another step
method: "by hand, at Retro: the reply of a stop of Work Mode under the text of vault/wiki/where-to-stop.md that holds the sentence on each command written whole in each step, which asks the person to run commands by hand, read in the transcript of a session where such a stop came, under ~/.claude/projects/, against each line of the Criterion, the transcript named in the estimate line (the stop of the by-hand test of Case 953, in session 2026-10-31/0128)"
checked: 2026-10-31
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

## Result

2026-10-31, Retro of session 0431, the stop reply of the by-hand test of Case 953 in session 0128, transcript ~/.claude/projects/c--PROJECTS-GUPPI/850a2e1e-ab70-422f-8401-df00a3a64d5e.jsonl line 1186 (uuid 28f28933): two windows of 4 steps, 6 commands, each written whole with its folder and path; each step that opens a new window writes New-Item and Set-Location in its own command; no step names a part of its command by a reference to another step; 0 faults, read by a subagent of the Retro and checked against the Criterion

## History

- 2026-10-31 created · [[decision-case-945]]
- 2026-10-31 updated: the method reads the reply of any such stop in the transcript of its session, the Criterion written back unchanged · [[decision-case-960.2]]
- 2026-10-31 status: pending → passed · raw/2026-10-31/0431/ledger.md#L42
