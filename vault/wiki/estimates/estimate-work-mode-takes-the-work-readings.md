---
type: estimate
kind: QA
status: pending
target: "[[rule-work-mode]]"
purpose: Whether /work, after the last task and in the same turn, takes in Frontier order each open W reading whose work is built and whose moment has come, closes its W line, leaves its line to the reply that ends Retro, and leaves open the readings this session changes or whose moment has not come
method: "by hand at the first /work after the render: the replies after the last task, their LEDGER blocks and frontier.md read against the Criterion, recorded in the estimate line"
checked: 2026-09-29
origin: raw/2026-09-29/1134/ledger.md#case-508.3
sprint: migration
created: 2026-09-29
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the last task of `raw/<date>/<hi HHMM>/spec.md` is done.

Then:
Before `/retro`, the agent takes, in the order of `raw/<date>/<hi HHMM>/frontier.md`, each reading of an open `W` line whose work is built and whose moment, as its `method` names it, has come.
**＋** A moment of an earlier session, such as the librarian's run, has come.
**＋** Every reading taken is first marked done in `raw/<date>/<hi HHMM>/frontier.md`, and its `estimate[...]` line stands in the `LEDGER` block of the one reply that ends Retro.
**＋** The tasks, the readings and `/retro` run in one turn, and no reply ends before the reply that ends Retro, except at a stop of `vault/wiki/where-to-stop.md`.
**－** A reading of an Estimate this session creates or updates is not taken, and its `W` line stays open.
**－** A reading whose moment has not come is not taken, and its `W` line stays open.
**－** The step ticks no `read` box of `raw/<date>/<hi HHMM>/spec.md`.

## Result

2026-09-29, by hand at the /retro of session 1753, the replies after the last task of /work, their LEDGER block and frontier.md: the step took W12 and W15, closed each [x] · work in frontier.md first and wrote their lines in a LEDGER block of a reply that ended in text, left the readings of Estimates this session updates, and ticked no read box; but it skipped W1 (estimate-agent-writing-followed) and W6 (estimate-case-build-writes-the-case), whose by-hand moment, a later session, had come, and the person did not stop the step

## History

- 2026-09-29 created · [[decision-case-508.3]]
- 2026-09-29 status: pending → failed · raw/2026-09-29/1753/ledger.md#L27
- 2026-09-30 updated: the Criterion replaced whole — the run is one turn; the reading lines stand in the reply that ends Retro; the stop of the step by the person is gone (case 531.8) · [[decision-case-531.8]]
