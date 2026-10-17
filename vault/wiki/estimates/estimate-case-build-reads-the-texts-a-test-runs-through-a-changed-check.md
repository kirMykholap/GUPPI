---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, for a Case that changes the code of a check, reads each live file of vault/ or .claude/ that a test runs through that check, directly or through a module that imports it, and puts each text the new check would refuse into the Case or says in context why it stands
method: by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; and, for each Case of that session that changes the code of a check, the tests of the full uv run --project .guppi guppi test run of Work Mode that fail on a live file of vault/ or .claude/ the Case does not name, counted in the estimate line
checked: 2026-10-17
origin: raw/2026-10-08/1547/ledger.md#case-736.1
sprint: migration
created: 2026-10-08
tags: [workflow, harness, tests]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, reads the frame of a Case that changes the code of a check.

Then:
It searches `.guppi/tests/` for the tests that read a live file of `vault/` or `.claude/`, not a copy under a temporary folder.
**＋** For each such test whose code reaches the changed code, directly or through a module that imports it, it reads that file against the new check.
**＋** Each text of that file that the new check would refuse enters the Case, or its `context` says why it stands.

## Result

2026-10-17, Retro of session 1805: .claude/agents/case-guppi.md as rendered holds the search for the tests that read a live file of vault/ or .claude/, the reading of that file against the new check for each test whose code reaches the changed code directly or through a module that imports it, and the text or the context for each refusal; Case 879 changes the hook of .guppi/guppi/ratified.py; the full uv run --project .guppi guppi test of Work Mode: 1756 passed, 6 skipped, 0 tests failing on a live file the Case does not name

## History

- 2026-10-08 created · [[decision-case-736.1]]
- 2026-10-08 status: pending → passed · raw/2026-10-08/1547/ledger.md#L10
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make test` → `uv run --project .guppi guppi test` · [[decision-case-820.7]]
- 2026-10-17 updated: the Criterion replaced whole — the line on an Insight of the repository of GUPPI dropped · [[decision-case-880.3]]
- 2026-10-17 status: pending → passed · raw/2026-10-17/1805/ledger.md#L60
