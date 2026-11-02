---
type: estimate
kind: QA
status: pending
target: "[[rule-work-mode]]"
purpose: Whether /work loads while guppi check or guppi test finds something, stops on main, writes the baseline of uv run --project .guppi guppi test and uv run --project .guppi guppi check into work.md before the first change — the exit code of each as the last line of its preamble line names it — and keeps it on a resume, runs the tasks of the Spec of the session or of the folder /box gives it in order with their ticks but leaves a guppi sprint-close line to the librarian, names that folder under Conserved Spec and deletes its carry.md, marks an expected red under Expected red, runs the check of the plan before the first task of a Case ratified in Work Mode, stops on its finding and ticks a task of that Case whose work already stands, and after the last task runs uv run --project .guppi guppi test in full and holds each failing test against the baseline, fixing a new one within ratified work
method: "by hand, after the librarian's render that writes .claude/skills/work/SKILL.md from the Render of rule-work-mode with --exit-zero on its lines Tests and Lint: uv run --project .guppi guppi render --check; .claude/skills/work/SKILL.md read against each line of the Criterion; the first /work that loads after that render while uv run --project .guppi guppi check exits 1, its preamble lines, its work.md and its run of the tasks read in the transcript of its session under ~/.claude/projects/ and in its spec.md and work.md against the Criterion; the lines on a Case ratified in Work Mode read in that transcript where that session ratifies one, otherwise against the text of the skill; recorded in the estimate line with the transcript named"
checked: 2026-10-31
origin: raw/2026-09-28/1318/ledger.md#case-479.2
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run --project .guppi guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.
**＋** Or `/box` calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.
**＋** Or, while the run of `/work` goes on, the person ratifies a Case built in Work Mode.

Then:
`uv run --project .guppi guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
**＋** The skill loads while `uv run --project .guppi guppi check` or `uv run --project .guppi guppi test` finds something: its lines Tests and Lint run both commands with `--exit-zero`, and each line comes back with the output of its command and a last line that names the exit code of its run.
**＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
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

2026-10-31, Retro of session 0431, uv run --project .guppi guppi render --check (exit 0), .claude/skills/work/SKILL.md against each line of the Criterion, main transcript 8727d5ce-2d69-40eb-8203-769b95b5cc28.jsonl lines 1434–1810, vault/raw/2026-10-31/0431/spec.md and work.md: on branch plugin the baseline was written once before the first change; Case 964, ratified in Work Mode, replaced 961.6; the reply that acknowledged it ended the turn, and at the person's next message guppi prespec --check ran on the plan before any task of the new Case, printing no finding; a finding of the Stop check of rule-case-check on the showing of Case 965 went to its case-guppi and the fixed Case was shown again; the stop: task and the three code tasks whose work stood were ticked with no new run; the full guppi test after the tasks had no new failure

## History

- 2026-09-28 created · [[decision-case-479.2]]
- 2026-10-02 updated: the Criterion replaced whole — /work runs the Spec of the folder /box gives it (case 591.7) · [[decision-case-591.7]]
- 2026-10-03 updated: method names the kind of its moment (case 613.3) · [[decision-case-613.3]]
- 2026-10-04 status: pending → passed · raw/2026-10-04/0004/ledger.md#L6
- 2026-10-04 updated: method names no /work the person types, a moment no one brings on (case 625) · [[decision-case-625]]
- 2026-10-04 updated: the Criterion replaced whole — a guppi sprint-close line is neither run nor ticked by Work Mode; purpose and method name it (case 628.4) · [[decision-case-628.4]]
- 2026-10-08 updated: the Criterion replaced whole — /work runs make test in full after its last task and holds each failing test against the baseline; purpose and method name it (case 736.2) · [[decision-case-736.2]]
- 2026-10-08 status: pending → passed · raw/2026-10-08/1547/ledger.md#L11
- 2026-10-14 updated: the Criterion replaced whole — the check of the plan before the tasks of a Case ratified in Work Mode, the stop on its finding, and the tick of a task whose work already stands (case 806.3) · [[decision-case-806.3]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make lint` → `uv run --project .guppi guppi check` · [[decision-case-820.7]]
- 2026-10-15 reworded: `make test` → `uv run --project .guppi guppi test` · [[decision-case-820.7]]
- 2026-10-31 updated: the method reads Case 964, ratified in the Work Mode of session 0431 and staged on purpose, the Criterion written back unchanged · [[decision-case-964]]
- 2026-10-31 status: pending → passed · raw/2026-10-31/0431/ledger.md#L48
- 2026-11-02 updated: the Criterion replaced whole — /work loads while guppi check is red, its preamble running guppi test and guppi check with --exit-zero; purpose and method name it · [[decision-case-1003.3]]
