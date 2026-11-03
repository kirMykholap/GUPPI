---
type: estimate
kind: QA
status: passed
target: "[[rule-where-to-stop]]"
purpose: "Whether the run from /work to the librarian stops for the person on each condition of vault/wiki/where-to-stop.md and on no other, with the text loaded by /work and a stop after the call of /retro opening with STOP:"
method: by hand, the text of vault/wiki/where-to-stop.md as rendered and the lines of .claude/skills/work/SKILL.md and .claude/skills/box/SKILL.md that load it, or, at the Retro of the session that changes it, the new Render of rule-where-to-stop in the Spec and those lines, read against each line of the Criterion, recorded in the estimate line; a line of the Criterion that the text does not set is named
checked: 2026-10-17
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the run goes from the tasks of `raw/<date>/<hi HHMM>/spec.md` to the librarian's report.
**＋** Or the agent calls `/box` on `PreToolUse Skill`, and the run goes from its first step to the librarian's report.

Then:
The context of `/work` holds the text of `vault/wiki/where-to-stop.md`, rendered from `rule-where-to-stop`.
**＋** The context of `/box`, from `.claude/skills/box/SKILL.md`, holds the same text.
**＋** The agent ends a reply with a question to the person on a fork that changes a contract, on a hook refusal whose text gives no step it can follow or says that it is a stop, and before an action that git in the repository cannot undo.
**＋** A fork that changes a contract is a choice that no ratified Case makes, or a ratified Case that turns out wrong: by a text the agent finds wrong or too narrow, or by a finding of `uv run --project .guppi guppi prespec --check` on the plan after a Case ratified in Work Mode.
**＋** Before a task of `raw/<date>/<hi HHMM>/spec.md` whose text opens with `stop:`, the agent stops and asks; the task runs after the person's word.
**＋** On the branch `main` the agent stops and says so: Work Mode does not start there.
**＋** In a run of `/box`, the agent stops and asks when `uv run --project .guppi guppi box --check` prints a line, or when a `git merge --ff-only` of `/box` refuses.
**＋** In the merge tasks that the opening Case of a sprint holds by `.claude/skills/sprint-open/SKILL.md`, the agent stops, shows what stopped it and asks when a `git` or `gh` command refuses.
**＋** When the full `uv run --project .guppi guppi test` run of `/work` after its last task finds a failing test that `## Baseline` of `raw/<date>/<hi HHMM>/work.md` does not hold, and its fix needs a choice that no ratified Case makes, the agent ends a reply with a question to the person that names the test and its failure.
**＋** When the auto mode classifier of Claude Code refuses a tool call that the run needs, the agent ends a reply with a question to the person that gives the shell command doing what the refused call would do, for the person to type after `!` in the prompt.
**＋** A reply that stops from the call of `/retro` until `raw/<date>/<hi HHMM>/handoff.md` stands opens with `STOP:`.
**＋** After the person's answer the run goes on from where it stopped.
**＋** After the person has run the command that a refusal of the auto mode classifier gave, the run goes on from where it stopped.
**＋** `vault/wiki/case-schema.md` names a task line that opens with `stop:` as a task that waits for the person's word.
**－** No other point stops the run, but a stop that a skill the project holds sets in the tasks of its own Case: any other red test, at `/retro` too, a reading that only the person can take, an observation or a doubt ends as a lesson or a line of `raw/<date>/<hi HHMM>/handoff.md`.

## Result

2026-10-17, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
