---
type: estimate
kind: QA
status: pending
target: "[[rule-work-mode]]"
purpose: Whether /work, after the last task and before /retro, takes in Frontier order each open W reading whose work is built and whose moment has come, closes its W line and writes its line, and leaves open the readings this session changes or whose moment has not come
method: "by hand at the first /work after the render: the replies after the last task, their LEDGER blocks and frontier.md read against the Criterion, recorded in the estimate line"
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
**＋** Every reading taken is first marked done in `raw/<date>/<hi HHMM>/frontier.md`, and a later reply, ending in text, carries its `estimate[...]` line inside a `LEDGER` block.
**＋** The person can stop the step in the chat, and the lines not reached stay open.
**－** A reading of an Estimate this session creates or updates is not taken, and its `W` line stays open.
**－** A reading whose moment has not come is not taken, and its `W` line stays open.
**－** The step ticks no `read` box of `raw/<date>/<hi HHMM>/spec.md`.

## History

- 2026-09-29 created · [[decision-case-508.3]]
