---
type: estimate
kind: QA
status: pending
target: "[[rule-where-to-stop]]"
purpose: "Whether the run from /work to the librarian stops for the person on each condition of vault/wiki/where-to-stop.md and on no other, with the text loaded by /work and a stop after the call of /retro opening with STOP:"
method: "by hand at the first run from /work to the librarian after the render: the context of /work, the replies of the turn and the Spec read against the Criterion, recorded in the estimate line; a condition that does not arise is named as not exercised"
origin: raw/2026-09-29/2024/ledger.md#case-531.7
sprint: migration
created: 2026-09-29
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the run goes from the tasks of `raw/<date>/<hi HHMM>/spec.md` to the librarian's report.

Then:
The context of `/work` holds the text of `vault/wiki/where-to-stop.md`, rendered from `rule-where-to-stop`.
**＋** The agent ends a reply with a question to the person on a fork that changes a contract, on a hook refusal whose text gives no step it can follow or says that it is a stop, and before an action that git in the repository cannot undo.
**＋** Before a task of `raw/<date>/<hi HHMM>/spec.md` whose text opens with `stop:`, the agent stops and asks; the task runs after the person's word.
**＋** On the branch `main` the agent stops and says so: Work Mode does not start there.
**＋** A reply that stops from the call of `/retro` until `raw/<date>/<hi HHMM>/handoff.md` stands opens with `STOP:`.
**＋** After the person's answer the run goes on from where it stopped.
**＋** `vault/wiki/case-schema.md` names a task line that opens with `stop:` as a task that waits for the person's word.
**－** No other point stops the run: a red test, a reading that only the person can take, an observation or a doubt ends as a lesson or a line of `raw/<date>/<hi HHMM>/handoff.md`.

## History

- 2026-09-30 created · [[decision-case-531.7]]
