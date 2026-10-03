---
type: estimate
kind: QA
status: pending
target: "[[rule-work-mode]]"
purpose: Whether /work, after the last task and in the same turn, takes in Frontier order each open W reading whose work is built and whose moment has come, closes its W line, leaves its line to the reply that ends Retro, and leaves open the readings this session changes, or the conserved Spec that /box gives it changes, or whose moment has not come
method: "by hand at a /work and at a /work that /box calls: the replies after the last task, their LEDGER blocks and frontier.md read against the Criterion, recorded in the estimate line"
checked: 2026-09-30
origin: raw/2026-09-29/1134/ledger.md#case-508.3
sprint: migration
created: 2026-09-29
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the last task of `raw/<date>/<hi HHMM>/spec.md` is done.
**＋** Or `/box` called `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec, and the last task of that folder's `spec.md` is done.

Then:
Before `/retro`, the agent takes, in the order of `raw/<date>/<hi HHMM>/frontier.md`, each reading of an open `W` line whose work is built and whose moment, as its `method` names it, has come.
**＋** A moment of an earlier session, such as the librarian's run, has come.
**＋** Every reading taken is first marked done in `raw/<date>/<hi HHMM>/frontier.md`, and its `estimate[...]` line stands in the `LEDGER` block of the one reply that ends Retro.
**＋** The tasks, the readings and `/retro` run in one turn, and no reply ends before the reply that ends Retro, except at a stop of `vault/wiki/where-to-stop.md`.
**－** A reading of an Estimate this session creates or updates is not taken, and its `W` line stays open.
**－** With a folder from `/box`, a reading of an Estimate that a decision line of that folder's `ledger.md` creates or updates is not taken either, and its `W` line stays open.
**－** A reading whose moment has not come is not taken, and its `W` line stays open.
**－** The step ticks no `read` box of `raw/<date>/<hi HHMM>/spec.md`.

## Result

2026-09-30, by hand, the /work run of session 1736 that the agent called at the fork: after the last task, in the same turn and in the order of frontier.md, it took the readings whose moment had come — W4, W11, W13, W41 — closing each line [x] · work in frontier.md first; it wrote no LEDGER block in /work, and the lines stand in the reply that ends Retro; it left W15 (estimate-decisions-schema-checked, updated by case 548) and the readings whose moment had not come open; it ticked no read box of spec.md; no reply ended between /work and this reply

## History

- 2026-09-29 created · [[decision-case-508.3]]
- 2026-09-29 status: pending → failed · raw/2026-09-29/1753/ledger.md#L27
- 2026-09-30 updated: the Criterion replaced whole — the run is one turn; the reading lines stand in the reply that ends Retro; the stop of the step by the person is gone (case 531.8) · [[decision-case-531.8]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/1736/ledger.md#L42
- 2026-10-02 updated: the Criterion replaced whole — the Work readings of /box leave the Estimates the conserved Spec changes (case 591.12) · [[decision-case-591.12]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
