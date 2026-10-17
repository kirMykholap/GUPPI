---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, for a Case that changes a live file of vault/ or .claude/, reads the code of each test that reads that file live — the test functions, the functions of the test file they call, its helpers included, and the functions of .guppi/guppi/ they call — against the new text, and puts each place where the new text would fail the test into the Case as a task, or says in context why it stands
method: by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; and, for each Case of that session that changes a live file of vault/ or .claude/, its context and tasks read for the tests that read that file live, each one named or said to stand
checked: 2026-10-17
origin: raw/2026-10-10/1508/ledger.md#case-754
sprint: migration
created: 2026-10-10
tags: [workflow, harness, tests]
---

## Criterion

When:
`case-guppi`, with `.claude/agents/case-guppi.md` rendered from `rule-case-build`, reads the frame of a Case that changes a live file of `vault/` or `.claude/`, by a page `update` or by the render of its rule.

Then:
It searches `.guppi/tests/` for the tests that read that file live, not a copy under a temporary folder.
**＋** For each such test, it reads the new text against the test functions that read the file, each function of the test file they call, its helpers included, and the functions of `.guppi/guppi/` they call.
**＋** Each place where the new text would fail the test enters the Case as a task that changes the test or the text, or its `context` says why it stands.

## Result

2026-10-17, Retro of session 1805: .claude/agents/case-guppi.md as rendered holds the search of .guppi/tests/ for the tests that read that file live, not a copy under a temporary folder, the reading of the test functions, their helpers and the functions of .guppi/guppi/ they call, and the task or the context for each place that would fail; Case 879 changes rule-spec-write and rule-spec-capture and its context names the Grep over .guppi/tests/ (test_spec.py, its docstring alone); Case 880 changes live Estimates and its context names callers and live_pages of test_guppi_package.py and the live build of test_ship.py

## History

- 2026-10-10 created · [[decision-case-754]]
- 2026-10-10 status: pending → passed · raw/2026-10-10/1508/ledger.md#L5
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-17 updated: the Criterion replaced whole — the line on an Insight of the repository of GUPPI dropped · [[decision-case-880.2]]
- 2026-10-17 status: pending → passed · raw/2026-10-17/1805/ledger.md#L59
