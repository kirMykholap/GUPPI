---
type: estimate
kind: QA
status: passed
target: "[[rule-where-to-stop]]"
purpose: Whether a stop reply that asks the person to run commands by hand writes each command whole in each step, its variables included, with no reference to another step
method: "by hand, at Retro: the reply of a stop of Work Mode under the text of vault/wiki/where-to-stop.md that holds the sentence on each command written whole in each step, which asks the person to run commands by hand, read in the transcript of a session where such a stop came, under ~/.claude/projects/, against each line of the Criterion, the transcript named in the estimate line"
checked: 2026-10-31
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
Work Mode stops on a condition of `vault/wiki/where-to-stop.md`, and the reply asks the person to run commands by hand.

Then:
Each step of the reply writes out whole each command it asks the person to run, as the person types it, with each variable, folder and flag the command needs.
**＋** A step that starts a program in a new window or terminal writes the variables that the start needs in its own command.
**－** No step names a part of its command by a reference to another step.

## Result

2026-10-31, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
