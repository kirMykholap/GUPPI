---
type: estimate
kind: QA
status: passed
target: "[[rule-work-mode]]"
purpose: Whether /work, after the last task and in the same turn, takes in Frontier order each open W reading whose work is built and whose moment has come, closes its W line, leaves its line to the reply that ends Retro, and leaves open the readings this session changes, or the conserved Spec that /box gives it changes, or whose moment has not come
method: "by hand at a /work and at a /work that /box calls: the replies after the last task, their LEDGER blocks and frontier.md read against the Criterion, recorded in the estimate line"
checked: 2026-10-04
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

2026-10-04, at the /hi of session 0004, by hand: the /work of session 0317 that the agent called at the fork (transcript 5b311f89): after the last task, make test and make style at 05:03:08, it took in the order of frontier.md W6 `estimate-case-build-writes-the-case` and W19 `estimate-end-of-work-order`, closed both `[x] … · work` at 05:04:20 and called /retro at 05:04:23; their lines stand only in the LEDGER block of the reply that ends Retro at 05:05:59, ledger lines 52–53; of the open W lines it left, 27 name an Estimate a decision line of 0317 updates, and the other 7 were read later from moments of sessions 1341 and 1416 or still wait; the /work that /box called in session 1416 (transcript 682b0e2f): after work.md and the deletion of carry.md at 14:38:26, it took W17 `estimate-hi-takes-a-conserved-spec` and W29 `estimate-spec-capture-offers-the-fork` in that order, closed both at 14:39:36, called /retro at 14:39:41, and their lines stand in the reply that ends Retro at 14:40:43; no decision line of raw/2026-10-03/1341/ledger.md names a W Estimate; in neither run did a reply end before the reply that ends Retro, the first Stop coming at 05:06:02 and 14:40:45; the step ticked no `read` box: the read boxes of 0317/spec.md stood open at 05:04:50, and bda8f3f4 does not touch 1341/spec.md

## History

- 2026-09-29 created · [[decision-case-508.3]]
- 2026-09-29 status: pending → failed · raw/2026-09-29/1753/ledger.md#L27
- 2026-09-30 updated: the Criterion replaced whole — the run is one turn; the reading lines stand in the reply that ends Retro; the stop of the step by the person is gone (case 531.8) · [[decision-case-531.8]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/1736/ledger.md#L42
- 2026-10-02 updated: the Criterion replaced whole — the Work readings of /box leave the Estimates the conserved Spec changes (case 591.12) · [[decision-case-591.12]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/0004/ledger.md#L5
