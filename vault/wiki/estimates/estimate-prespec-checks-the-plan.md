---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: prespec --check finds the session by its stamp, parses the plan and the ledger lines, and prints one line per finding, exit 1 on any
method: pytest .guppi/tests/test_prespec.py, the tests of --check
checked: 2026-09-24
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness, tests]
core: true
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

2026-09-24, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
