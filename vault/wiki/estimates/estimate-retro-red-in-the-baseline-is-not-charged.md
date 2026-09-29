---
type: estimate
kind: QA
status: pending
target: "[[rule-retro]]"
purpose: Whether Retro writes a failing test or a lint finding that the Baseline of work.md already holds as a line of Observations of handoff.md, not debt, whatever Expected red names, and commits with make test green but for those tests
method: one reading by hand at the first /retro after the render in a session whose work.md Baseline holds a failing test or a lint finding line, recorded in the estimate line
checked: 2026-09-29
origin: raw/2026-09-28/1318/ledger.md#case-479.4
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, in a session whose `raw/<date>/<hi HHMM>/work.md` holds a `## Baseline`, and a test fails in the `make test` of Retro, or a lint finding stood in Work Mode.

Then:
Retro counts each failing test and each lint finding line that `## Baseline` holds as red before the work, whatever `## Expected red` names, and writes it as a line of `## Observations` of `raw/<date>/<hi HHMM>/handoff.md`.
**＋** It is not debt: nothing is fixed or reverted into a patch for it, and it gets no `lesson[error]` line.
**＋** The commit of Retro needs `make style` clean and `make test` green, except for the failing tests that `## Baseline` holds.
**＋** A failing test that `## Baseline` does not hold is fixed, or reverted into a patch that `## Debt` of `raw/<date>/<hi HHMM>/handoff.md` names.
**－** Without `work.md` there is no baseline, and no red is excused as red before the work.
**－** `estimate-guppi-tests-green` still wants `make test` with no failed test on the branch: a red test of the baseline stays red there.

## Result

2026-09-29, by hand at the /retro of session 1753, whose work.md Baseline holds the make lint line "backlog: vault/wiki/backlog.md differs from its sources": the Retro counted it as red before the work and ended it as a note for the handoff, fixed and reverted nothing and wrote no lesson for it; make style clean and make test 923 passed, 2 skipped before the commit; no failing test, so the clause of a failing test outside the Baseline was not exercised

## History

- 2026-09-28 created · [[decision-case-479.4]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1753/ledger.md#L28
- 2026-09-30 updated: the Criterion replaced whole — the trigger covers the agent's call; a red of the Baseline is a line of Observations of handoff.md, and a patch of any other red test is named in Debt (case 531.4) · [[decision-case-531.4]]
