---
type: estimate
kind: QA
status: passed
target: "[[rule-work-mode]]"
purpose: Whether /work, after the last task and in the same turn, takes in Frontier order each open W reading whose work is built and whose moment has come, closes its W line, leaves its line to the reply that ends Retro, and leaves open the readings this session changes, or the conserved Spec that /box gives it changes, or whose moment has not come
method: by hand, the text of the skill file rendered from rule-work-mode, or, at the Retro of the session that changes it, the new Render of rule-work-mode in the Spec, read against the Criterion, recorded in the estimate line
checked: 2026-10-05
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
The agent calls `/work` of `rule-work-mode` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the last task of `raw/<date>/<hi HHMM>/spec.md` is done.
**＋** Or `/box` called `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec, and the last task of that folder's `spec.md` is done.

Then:
Before `/retro`, the agent takes, in the order of `raw/<date>/<hi HHMM>/frontier.md`, each reading of an open `W` line whose work is built and whose moment, as its `method` names it, has come.
**＋** A moment of an earlier session, such as the librarian's run, has come.
**＋** Every reading taken is first marked done in `raw/<date>/<hi HHMM>/frontier.md`, and its `estimate[...]` line stands in the `LEDGER` block of the one reply that ends Retro.
**＋** The tasks, the readings and `/retro` run in one turn, and no reply ends before the reply that ends Retro, except at a stop of `vault/wiki/where-to-stop.md`.
**－** A reading of an Estimate this session creates or updates is not taken in this step: its `W` line stays open until `/retro` reads that Estimate or sets it `failed`, and closes the line.
**－** With a folder from `/box`, a reading of an Estimate that a decision line of that folder's `ledger.md` creates or updates is not taken in this step either, and Retro closes its `W` line the same way.
**－** A reading whose moment has not come is not taken, and its `W` line stays open.
**－** The step ticks no `read` box of `raw/<date>/<hi HHMM>/spec.md`.

## Result

2026-10-05, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
