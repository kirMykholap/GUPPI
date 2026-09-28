---
type: estimate
kind: QA
status: pending
target: "[[rule-work-mode]]"
purpose: Whether /work stops on main, writes the baseline of make test and make lint into work.md before the first change — running a command itself when its substitution is empty — and keeps it on a resume, runs the tasks of the Spec in order with their ticks, and marks an expected red under Expected red
method: "uv run guppi render --check; by hand, in a session after the render, the first /work the agent calls at the fork and the first /work the person types: the branch, work.md, the ticks of spec.md and each Expected red line read against the Criterion, and, where a substitution came back empty, the agent's own run of its command, recorded in the estimate line"
origin: raw/2026-09-28/1318/ledger.md#case-479.2
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.

Then:
`uv run guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
**＋** When a `!` substitution of `.claude/skills/work/SKILL.md` comes back empty, the agent runs its command itself — `git branch --show-current` before the check of the branch, `make test` and `make lint` before the first change — and uses that result.
**＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
**＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `make test` and of `make lint` with each failing test and each lint finding line as printed, and an empty `## Expected red`.
**＋** When `work.md` already stands, its `## Baseline` stays as it is.
**＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task.
**＋** A task that changes `make lint`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
**－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.

## History

- 2026-09-28 created · [[decision-case-479.2]]
