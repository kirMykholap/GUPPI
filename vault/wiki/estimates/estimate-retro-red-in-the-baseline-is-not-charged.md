---
type: estimate
kind: QA
status: passed
target: "[[rule-retro]]"
purpose: Whether Retro writes a failing test or a lint finding that the Baseline of work.md already holds as a line of Observations of handoff.md, not debt, whatever Expected red names, and commits with uv run --project .guppi guppi test green but for those tests
method: one reading by hand at a /retro in a session whose work.md Baseline holds a failing test or a lint finding line, recorded in the estimate line
checked: 2026-10-01
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose `raw/<date>/<hi HHMM>/work.md` holds a `## Baseline`, and a test fails in the `uv run --project .guppi guppi test` of Retro, or a lint finding stood in Work Mode.

Then:
Retro counts each failing test and each lint finding line that `## Baseline` holds as red before the work, whatever `## Expected red` names, and writes it as a line of `## Observations` of `raw/<date>/<hi HHMM>/handoff.md`.
**＋** It is not debt: nothing is fixed or reverted into a patch for it, and it gets no `lesson[error]` line.
**＋** The commit of Retro needs `uv run --project .guppi guppi style` clean and `uv run --project .guppi guppi test` green, except for the failing tests that `## Baseline` holds.
**＋** A failing test that `## Baseline` does not hold is fixed, or reverted into a patch that `## Debt` of `raw/<date>/<hi HHMM>/handoff.md` names.
**－** Without `work.md` there is no baseline, and no red is excused as red before the work.
**－** `estimate-guppi-tests-green` still wants `uv run --project .guppi guppi test` with no failed test on the branch: a red test of the baseline stays red there.

## Result

2026-10-01, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
