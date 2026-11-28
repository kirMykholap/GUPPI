---
type: estimate
kind: QA
status: passed
target: "[[rule-work-mode]]"
purpose: Whether /work loads while guppi check or guppi test finds something, stops on the main branch but for the branch task of the opening Case of a sprint, which it runs first, writes the baseline of uv run --project .guppi guppi test and uv run --project .guppi guppi check into work.md before the first change — the exit code of each as the last line of its preamble line names it — and keeps it on a resume, runs the tasks of the Spec of the session or of the folder /box gives it in order with their ticks but leaves a guppi sprint-close line to the librarian, names that folder under Conserved Spec and deletes its carry.md, marks an expected red under Expected red, runs the check of the plan before the first task of a Case ratified in Work Mode, stops on its finding and ticks a task of that Case whose work already stands, and after the last task runs uv run --project .guppi guppi test in full and holds each failing test against the baseline, fixing a new one within ratified work
method: "by hand: uv run --project .guppi guppi render --check, and .claude/skills/work/SKILL.md, rendered from rule-work-mode, read against each line of the Criterion, recorded in the estimate line"
checked: 2026-11-23
origin: guppi
sprint: guppi
created: 2026-11-28
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run --project .guppi guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.
**＋** Or `/box` calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.
**＋** Or, while the run of `/work` goes on, the person ratifies a Case built in Work Mode.

Then:
`uv run --project .guppi guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
**＋** The skill loads while `uv run --project .guppi guppi check` or `uv run --project .guppi guppi test` finds something: its lines Tests and Lint run both commands with `--exit-zero`, and each line comes back with the output of its command and a last line that names the exit code of its run.
**＋** On the branch `main`, when `raw/<date>/<hi HHMM>/spec.md` holds the opening Case of a sprint, Case `<id>-1`, whose first task line runs `git switch -c <id>`, the agent runs that line before any other task and before it writes `work.md`, ticks its box, and runs the rest of the Spec on the branch `<id>`.
**＋** On the branch `main` with any other Spec, the skill stops and says so, and nothing is written or changed.
**＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `uv run --project .guppi guppi test` and of `uv run --project .guppi guppi check`, as the last line of Tests and of Lint names it, with each failing test and each lint finding line as printed, and an empty `## Expected red`.
**＋** When `work.md` already stands, its `## Baseline` stays as it is.
**＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task; a task line that opens with a code span holding `guppi sprint-close` it neither runs nor ticks, since the librarian runs it.
**＋** The reply that acknowledges a Case ratified in Work Mode ends the turn, since the hook of `rule-prespec-onward` sends nothing on once `raw/<date>/<hi HHMM>/spec.md` stands; at the person's next message the run goes on from where it stopped.
**＋** After the reply that acknowledges a Case ratified in Work Mode, and before the first task of that Case, the agent runs `uv run --project .guppi guppi prespec --check` on the plan file of the session, with the session id of its `hi:` line.
**＋** When that check prints a line that does not open with `note:`, the agent stops as the first condition of `vault/wiki/where-to-stop.md` sets it and sends the finding to the `case-guppi` of that Case; the run goes on after the person ratifies the fixed Case and the check prints no such line.
**＋** A task of that Case whose work already stands, done under the sub-case the Case replaces, is ticked in `raw/<date>/<hi HHMM>/spec.md` and not run again.
**＋** A task that changes `uv run --project .guppi guppi check`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
**＋** When the last task of `raw/<date>/<hi HHMM>/spec.md` is done, before the Work readings, the agent runs `uv run --project .guppi guppi test` in full and holds each failing test against `## Baseline` of `raw/<date>/<hi HHMM>/work.md`.
**＋** A failing test that `## Baseline` holds goes on, and a new one whose fix finishes ratified work is fixed.
**＋** With a folder from `/box`, `work.md` holds a third section, `## Conserved Spec`, naming the folder; the tasks run and ticked are those of that folder's `spec.md`; and the agent deletes that folder's `carry.md` when the last task is done, before the Work readings.
**－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.
**－** A new failing test whose fix needs a choice that no ratified Case makes is not fixed in that step: it is a stop of `vault/wiki/where-to-stop.md`.
**－** Any other new failing test goes on to `/retro`, which fixes it or reverts it into a patch.
**－** In a `/work` that `/box` calls no Case is ratified, so the check of the plan does not run there: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `raw/<date>/<hi HHMM>/handoff.md` as a line.

## Result

2026-11-23, passed in the repository of GUPPI.

## History

- 2026-11-28 shipped with GUPPI
