---
type: estimate
kind: QA
status: passed
target: "[[rule-where-to-stop]]"
purpose: "Whether the run from /work to the librarian stops for the person on each condition of vault/wiki/where-to-stop.md and on no other, with the text loaded by /work and a stop after the call of /retro opening with STOP:"
method: by hand, the text of vault/wiki/where-to-stop.md as rendered and the lines of .claude/skills/work/SKILL.md and .claude/skills/box/SKILL.md that load it, or, at the Retro of the session that changes it, the new Render of rule-where-to-stop in the Spec and those lines, read against each line of the Criterion, recorded in the estimate line; a line of the Criterion that the text does not set is named
checked: 2026-10-13
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
**＋** In the merge tasks that the opening Case of a sprint holds by `.claude/skills/sprint-open/SKILL.md`, in the merge task that a review Case holds by `.claude/skills/pr-review/SKILL.md`, and in the tasks that a merge Case holds by `.claude/skills/merge-main/SKILL.md`, the agent stops, shows what stopped it and asks when a `git` or `gh` command refuses, or when the merge of a merge Case leaves in conflict a file that the merge Case does not settle.
**－** `git merge --no-ff --no-commit` of a merge Case of `.claude/skills/merge-main/SKILL.md` that exits non-zero only on files that the merge Case settles is no refusal, and the run goes on to the tasks that settle them.
**＋** When the full `make test` run of `/work` after its last task finds a failing test that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` does not hold, and its fix needs a choice that no ratified Case makes, the agent ends a reply with a question to the person that names the test and its failure.
**＋** When the auto mode classifier of Claude Code refuses a tool call that the run needs, the agent ends a reply with a question to the person that gives the shell command doing what the refused call would do, for the person to type after `!` in the prompt.
**＋** A reply that stops from the call of `/retro` until `raw/<date>/<hi HHMM>/handoff.md` stands opens with `STOP:`.
**＋** After the person's answer the run goes on from where it stopped.
**＋** After the person has run the command that a refusal of the auto mode classifier gave, the run goes on from where it stopped.
**＋** `vault/wiki/case-schema.md` names a task line that opens with `stop:` as a task that waits for the person's word.
**－** No other point stops the run: any other red test, at `/retro` too, a reading that only the person can take, an observation or a doubt ends as a lesson or a line of `raw/<date>/<hi HHMM>/handoff.md`.

## Result

2026-10-13, Retro by hand: the Render of rule-where-to-stop in spec.md (case 789.3) makes the sixth condition cover a refused git or gh command of the opening Case, a review Case and a merge Case, and a conflict a merge Case does not settle, with git merge --no-ff --no-commit on settled files no refusal; the other conditions stand as rendered

## History

- 2026-09-30 created · [[decision-case-531.7]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L6
- 2026-10-02 updated: the Criterion replaced whole — /box imports the file, and its stops (case 591.10) · [[decision-case-591.10]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/0004/ledger.md#L4
- 2026-10-08 updated: the Criterion replaced whole — a new red test of the full run of /work whose fix needs a new Case is a stop (case 736.3) · [[decision-case-736.3]]
- 2026-10-08 status: pending → passed · raw/2026-10-08/1547/ledger.md#L12
- 2026-10-08 updated: the Criterion replaced whole — a refusal of the auto mode classifier is a stop, and the person runs the command after ! (case 741) · [[decision-case-741]]
- 2026-10-08 status: pending → passed · raw/2026-10-08/2134/ledger.md#L13
- 2026-10-11 updated: the Criterion replaced whole — a refused merge or branch deletion in the merge tasks of the opening Case of a sprint is a stop · [[decision-case-775.3]]
- 2026-10-11 status: pending → passed · raw/2026-10-10/2350/ledger.md#L12
- 2026-10-13 updated: the Criterion replaced whole — a refused git or gh command in the merge tasks of the opening Case of a sprint, of a review Case or of a merge Case, and a conflict that a merge Case does not settle, is a stop · [[decision-case-789.3]]
- 2026-10-13 status: pending → passed · raw/2026-10-12/2349/ledger.md#L55
