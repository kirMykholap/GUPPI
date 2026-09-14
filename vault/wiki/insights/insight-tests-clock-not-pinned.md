---
type: insight
pattern: A test pins the date on one side of the call and lets the code read the real clock on the other; it passes on the day it is written and fails later.
status: actioned
children: ["[[lesson-tests-cli-date-pinned]]", "[[lesson-tests-generate-history-date-unpinned]]"]
severity: 0
addressed_by: "[[decision-case-145.3]]"
origin: raw/2026-09-11/ledger.md#L71
sprint: migration
created: 2026-09-11
tags: [harness, tests]
---

## Pattern

Two lessons, two months apart in the code, one cause.

`lesson-tests-cli-date-pinned`: the helpers wrote the event log under a pinned TODAY of 2026-09-09 while `cli.main` read the real clock; the three CLI dispatch tests went red on 2026-09-10.

`lesson-tests-generate-history-date-unpinned`: the run helper of `tests/test_generate.py` called `generate.run` without `now`, so History and log lines took the real clock while the assertions used the pinned DATE; five tests went red on 2026-09-11, on the committed tree, before any change of the session.

Both were fixed by making the two sides agree. Neither was caught when written, because on that day the clock and the pin were the same date.

## Proposal

A suggestion, not a decision. Every entry point that reads the clock takes `now` as a parameter, and every test helper passes the pinned date into it; a test that needs a date never reads the clock itself. A check that runs the suite under a shifted date would catch the rest of this class in one run.

## Children

- [[lesson-tests-cli-date-pinned]]
- [[lesson-tests-generate-history-date-unpinned]]

## Addressed by

- [[decision-case-145.3]]

## History

- 2026-09-11 created · raw/2026-09-11/ledger.md#L71
- 2026-09-14 updated: actioned: every run() takes now (the children's fixes); the clock of the tests pinned to 2001 by rule-tests-clock-pinned (145.1) (case 145.3) · [[decision-case-145.3]]
