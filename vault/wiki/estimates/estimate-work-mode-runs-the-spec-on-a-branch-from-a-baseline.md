---
type: estimate
kind: QA
status: passed
target: "[[rule-work-mode]]"
purpose: Whether /work stops on main, writes the baseline of make test and make lint into work.md before the first change — running a command itself when its substitution is empty — and keeps it on a resume, runs the tasks of the Spec of the session or of the folder /box gives it in order with their ticks but leaves a guppi sprint-close line to the librarian, names that folder under Conserved Spec and deletes its carry.md, marks an expected red under Expected red, and after the last task runs make test in full and holds each failing test against the baseline, fixing a new one within ratified work
method: "uv run guppi render --check; by hand, a /work the agent calls at the fork, a /work that /box calls and the /work of a session that closes a sprint: the branch, work.md, the ticks of the Spec, the guppi sprint-close line neither run nor ticked, the carry.md of the folder, each Expected red line, and the full make test run after the last task with what followed each failing test, read against the Criterion, and, where a substitution came back empty, the agent's own run of its command, recorded in the estimate line"
checked: 2026-10-08
origin: raw/2026-09-28/1318/ledger.md#case-479.2
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.
**＋** Or `/box` calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.

Then:
`uv run guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
**＋** When a `!` substitution of `.claude/skills/work/SKILL.md` comes back empty, the agent runs its command itself — `git branch --show-current` before the check of the branch, `make test` and `make lint` before the first change — and uses that result.
**＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
**＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `make test` and of `make lint` with each failing test and each lint finding line as printed, and an empty `## Expected red`.
**＋** When `work.md` already stands, its `## Baseline` stays as it is.
**＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task; a task line that opens with a code span holding `guppi sprint-close` it neither runs nor ticks, since the librarian runs it.
**＋** A task that changes `make lint`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
**＋** When the last task of `raw/<date>/<hi HHMM>/spec.md` is done, before the Work readings, the agent runs `make test` in full and holds each failing test against `## Baseline` of `raw/<date>/<hi HHMM>/work.md`.
**＋** A failing test that `## Baseline` holds goes on, and a new one whose fix finishes ratified work is fixed.
**＋** With a folder from `/box`, `work.md` holds a third section, `## Conserved Spec`, naming the folder; the tasks run and ticked are those of that folder's `spec.md`; and the agent deletes that folder's `carry.md` when the last task is done, before the Work readings.
**－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.
**－** A new failing test whose fix needs a choice that no ratified Case makes is not fixed in that step: it is a stop of `vault/wiki/where-to-stop.md`.
**－** Any other new failing test goes on to `/retro`, which fixes it or reverts it into a patch.

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
