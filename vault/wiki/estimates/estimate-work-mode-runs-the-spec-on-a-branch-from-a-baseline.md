---
type: estimate
kind: QA
status: pending
target: "[[rule-work-mode]]"
purpose: Whether /work stops on main, writes the baseline of uv run --project .guppi guppi test and uv run --project .guppi guppi check into work.md before the first change — running a command itself when its substitution is empty — and keeps it on a resume, runs the tasks of the Spec of the session or of the folder /box gives it in order with their ticks but leaves a guppi sprint-close line to the librarian, names that folder under Conserved Spec and deletes its carry.md, marks an expected red under Expected red, runs the check of the plan before the first task of a Case ratified in Work Mode, stops on its finding and ticks a task of that Case whose work already stands, and after the last task runs uv run --project .guppi guppi test in full and holds each failing test against the baseline, fixing a new one within ratified work
method: "by hand, at Retro: the new Render of rule-work-mode in the Spec read against each line of the Criterion, recorded in the estimate line; uv run --project .guppi guppi render --check; by hand, after the first /work that runs on the rendered .claude/skills/work/SKILL.md and in which a Case is ratified in Work Mode: the end of the turn after its acknowledging reply, the check of the plan before its first task, what followed a finding and the ticks of its tasks read against the Criterion, recorded in the estimate line"
checked: 2026-10-08
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
**＋** When a `!` substitution of `.claude/skills/work/SKILL.md` comes back empty, the agent runs its command itself — `git branch --show-current` before the check of the branch, `uv run --project .guppi guppi test` and `uv run --project .guppi guppi check` before the first change — and uses that result.
**＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
**＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `uv run --project .guppi guppi test` and of `uv run --project .guppi guppi check` with each failing test and each lint finding line as printed, and an empty `## Expected red`.
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

2026-10-08, Retro, the new Render of rule-work-mode in vault/raw/2026-10-08/1547/spec.md (Case 736.2) read against each line of the Criterion of 736.2: the empty-substitution, main, baseline, resume, task order and ticks, sprint-close, Expected red and /box lines stand in the current Render; the new replace adds the full make test run after the last task, held against ## Baseline of work.md — a Baseline failure goes on, a new one within ratified work is fixed, one needing a choice no ratified Case makes is the stop of where-to-stop.md, any other goes on to /retro; both replace targets stand once in the page; the /work of this session at the fork ran on migration and wrote work.md before any change (make test exit 0, make lint exit 2, 14 lines); render --check waits for the librarian's render; a /work that /box calls and the /work of a session that closes a sprint were not observed

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
