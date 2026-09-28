---
type: estimate
kind: QA
status: pending
target: "[[rule-retro]]"
purpose: Whether Retro ends a failing test or a lint finding that the Baseline of work.md already holds as a note for the handoff, not debt, whatever Expected red names, and commits with make test green but for those tests
method: one reading by hand at the first /retro after the render in a session whose work.md Baseline holds a failing test or a lint finding line, recorded in the estimate line
origin: raw/2026-09-28/1318/ledger.md#case-479.4
sprint: migration
created: 2026-09-28
tags: [session, workflow, harness]
---

## Criterion

When:
The person invokes `/retro` in a session whose `raw/<date>/<hi HHMM>/work.md` holds a `## Baseline`, and a test fails in the `make test` of Retro, or a lint finding stood in Work Mode.

Then:
Retro counts each failing test and each lint finding line that `## Baseline` holds as red before the work, whatever `## Expected red` names, and writes it in the handoff as a note.
**＋** It is not debt: nothing is fixed or reverted into a patch for it, and it gets no `lesson[error]` line.
**＋** The commit of Retro needs `make style` clean and `make test` green, except for the failing tests that `## Baseline` holds.
**＋** A failing test that `## Baseline` does not hold is fixed or reverted into a patch, as before.
**－** Without `work.md` there is no baseline, and no red is excused as red before the work.
**－** `estimate-guppi-tests-green` still wants `make test` with no failed test on the branch: a red test of the baseline stays red there.

## History

- 2026-09-28 created · [[decision-case-479.4]]
