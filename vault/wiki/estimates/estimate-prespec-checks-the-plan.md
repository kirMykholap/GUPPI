---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: prespec --check finds the session by its stamp, parses the plan and the ledger lines, and prints one line per finding, exit 1 on any
method: pytest .guppi/tests/test_prespec.py, the tests of --check
checked: 2026-09-24
origin: raw/2026-09-16/1955/ledger.md#case-203.1
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness, tests]
---

## Criterion

When:
`uv run --project .guppi guppi prespec --check <plan>` runs.

Then:
The stamp is `--session`, else `CLAUDE_SESSION_ID`; with neither, one line on stderr `prespec: no session id; pass --session <stamp> from the hi: line`, exit 2, nothing checked; with no file at `<plan>`, `prespec: no plan file at <plan>`, exit 2.
**＋** The session's window is found as the ledger hook finds it — by the stamped `hi`, over the event logs back to the date of its `session-start` — so the `hi` of yesterday's session is found after midnight; with no `hi` of the stamp, one line on stderr `prespec: no hi recorded for session <stamp>; nothing checked`, exit 0.
**＋** Each finding is one line on stdout; exit 1 on any finding, 0 on none.
**＋** A `then` block that does not parse is a finding of its Case, with the error.
**＋** Every record line of the window — the session's `ledger.md` whole, plus the date-level ledgers from the `hi` time on — goes through `parse_line`; one that does not parse is the finding `raw/<unit>/ledger.md:<n>: does not parse: <text>`.

## Result

2026-09-24, `uv run pytest tests/test_prespec.py`: 108 passed

## History

- 2026-09-16 created · [[decision-case-203.1]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L33
- 2026-09-17 updated: two lines in the Criterion — the stamp from --session or the environment, refused without one; the window found as the ledger hook finds it, across midnight (case 213.1) · [[decision-case-213.1]]
- 2026-09-17 updated: the Form line of the Criterion — a ref to a rule or entity the same plan creates is no finding (case 221) · [[decision-case-221]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L52
- 2026-09-20 ref `rule-pretask` → `rule-prespec` · [[decision-case-261]]
- 2026-09-20 ref `rule-pretask-hook` → `rule-prespec-hook` · [[decision-case-261]]
- 2026-09-20 renamed from `estimate-pretask-checks-the-plan` · [[decision-case-261]]
- 2026-09-20 updated: renamed with rule-prespec — the Criterion names guppi prespec, the mark prespec, the stderr prefix prespec and tests/test_prespec.py (case 261) · [[decision-case-261]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0740/ledger.md#L13
- 2026-09-20 status: passed → passed · raw/2026-09-20/0740/ledger.md#L16
- 2026-09-22 updated: one line of the Criterion — the lines of a Case superseded by a line of the window need no item, its heading in the plan is a finding (case 299.5) · [[decision-case-299.5]]
- 2026-09-22 status: pending → passed · raw/2026-09-21/1853/ledger.md#L28
- 2026-09-22 updated: the closer `· sprint` (case 310.6) · [[decision-case-310.6]]
- 2026-09-22 updated: the file route is a finding, not a route (case 320) · [[decision-case-320]]
- 2026-09-22 updated: any file item is a finding (case 323) · [[decision-case-323]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L87
- 2026-09-23 updated: the task line of a reading in the Criterion — matched as generate ticks it (case 327) · [[decision-case-327]]
- 2026-09-23 updated: the line on a create without method makes room for the finding of case 331 (case 338.2) · [[decision-case-338.2]]
- 2026-09-23 updated: the source segment of a Frontier line in the Criterion (case 335) · [[decision-case-335]]
- 2026-09-23 updated: the Criterion names an open Work line clean (case 356.1) · [[decision-case-356.1]]
- 2026-09-23 updated: the Criterion names the finding on a deferred sprint line (case 356.2) · [[decision-case-356.2]]
- 2026-09-23 status: pending → passed · raw/2026-09-23/1126/ledger.md#L40
- 2026-09-25 updated: the Criterion replaced whole — the run of prespec --check by the model of case 378; the lines, the frontier, the tasks and the form of an item moved to their own Estimates (case 399.1) · [[decision-case-399.1]]
- 2026-09-25 status: pending → passed · raw/2026-09-24/2214/ledger.md#L37
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
