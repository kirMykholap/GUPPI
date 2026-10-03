---
type: estimate
kind: QA
status: passed
target: "[[rule-where-to-stop]]"
purpose: "Whether the run from /work to the librarian stops for the person on each condition of vault/wiki/where-to-stop.md and on no other, with the text loaded by /work and a stop after the call of /retro opening with STOP:"
method: "by hand at a run from /work to the librarian, and at a run of /box: the context of /work and of /box, the replies of the turn and the Spec read against the Criterion, recorded in the estimate line; a condition that does not arise is named as not exercised"
checked: 2026-10-04
origin: raw/2026-09-29/2024/ledger.md#case-531.7
sprint: migration
created: 2026-09-29
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the run goes from the tasks of `raw/<date>/<hi HHMM>/spec.md` to the librarian's report.
**＋** Or the agent calls `/box` on `PreToolUse Skill`, and the run goes from its first step to the librarian's report.

Then:
The context of `/work` holds the text of `vault/wiki/where-to-stop.md`, rendered from `rule-where-to-stop`.
**＋** The context of `/box`, from `.claude/skills/box/SKILL.md`, holds the same text.
**＋** The agent ends a reply with a question to the person on a fork that changes a contract, on a hook refusal whose text gives no step it can follow or says that it is a stop, and before an action that git in the repository cannot undo.
**＋** Before a task of `raw/<date>/<hi HHMM>/spec.md` whose text opens with `stop:`, the agent stops and asks; the task runs after the person's word.
**＋** On the branch `main` the agent stops and says so: Work Mode does not start there.
**＋** In a run of `/box`, the agent stops and asks when `uv run guppi box --check` prints a line, or when a `git merge --ff-only` of `/box` refuses.
**＋** A reply that stops from the call of `/retro` until `raw/<date>/<hi HHMM>/handoff.md` stands opens with `STOP:`.
**＋** After the person's answer the run goes on from where it stopped.
**＋** `vault/wiki/case-schema.md` names a task line that opens with `stop:` as a task that waits for the person's word.
**－** No other point stops the run: a red test, a reading that only the person can take, an observation or a doubt ends as a lesson or a line of `raw/<date>/<hi HHMM>/handoff.md`.

## Result

2026-10-04, at the /hi of session 0004, by hand: the run of session 0317 (transcript 5b311f89) from the /work the agent called at the fork at 04:57:36 to the librarian's report at 05:13:39, and the run of /box of session 1416 (transcript 682b0e2f) from 14:37:13 to the report at 14:47:46: the /work call of 0317 carried vault/wiki/where-to-stop.md as a file attachment; in 1416 the /box call carried it as a file attachment and the /work call 13 seconds later as an already-read attachment of the same file; neither run stopped for the person and no condition of the file arose: no fork of a contract, no task opening with `stop:` in raw/2026-10-03/0317/spec.md or raw/2026-10-03/1341/spec.md, `guppi box --check` printing nothing and both merges of /box fast-forwards, and the one `git checkout -- tests/test_casecheck.py` of 0317, at 05:05:33, came after the commit 783d24e5 held that file and discarded nothing; the refusals of bashguard at 05:00:15 and of `guppi onward` at 05:06:02 and 14:40:45 each gave a step the agent followed; case-schema.md names a task opening with `stop:` as one that waits for the person's word; not exercised: a stop, a reply opening with STOP:, the branch main, a refused check or merge of /box, a run going on after the person's answer

## History

- 2026-09-30 created · [[decision-case-531.7]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L6
- 2026-10-02 updated: the Criterion replaced whole — /box imports the file, and its stops (case 591.10) · [[decision-case-591.10]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/0004/ledger.md#L4
