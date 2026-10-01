---
type: estimate
kind: QA
status: passed
target: "[[rule-retro]]"
purpose: Whether Retro writes a failing test or a lint finding that the Baseline of work.md already holds as a line of Observations of handoff.md, not debt, whatever Expected red names, and commits with make test green but for those tests
method: one reading by hand at the first /retro after the render in a session whose work.md Baseline holds a failing test or a lint finding line, recorded in the estimate line
checked: 2026-10-01
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

2026-10-01, by hand, the /retro of session 2356, the Baseline of its work.md (make lint exit 2 at guppi backlog --check; guppi lint: 3 findings on rule-spec-box, the fence of decision-case-13, 5 deferred, 42 unread) against its handoff.md: one line of Observations names that red as red before the work and says nothing was fixed for it; no Debt line, no patch and no lesson[error] for it; make style clean and make test 1034 passed, 2 skipped before the commit f7581b07; no failing test, so the clause of a failing test outside the Baseline was not exercised

## History

- 2026-09-28 created · [[decision-case-479.4]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1753/ledger.md#L28
- 2026-09-30 updated: the Criterion replaced whole — the trigger covers the agent's call; a red of the Baseline is a line of Observations of handoff.md, and a patch of any other red test is named in Debt (case 531.4) · [[decision-case-531.4]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1237/ledger.md#L4
