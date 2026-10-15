---
type: estimate
kind: QA
status: passed
target: "[[rule-case-build]]"
purpose: Whether case-guppi, for a Case that changes the code of a check, reads each live file of vault/ or .claude/ that a test runs through that check, directly or through a module that imports it, and puts each text the new check would refuse into the Case or says in context why it stands
method: by hand, the text of .claude/agents/case-guppi.md as rendered, or, at the Retro of the session that changes it, the new Render of rule-case-build in the Spec, read against the Criterion; and, for each Case of that session that changes the code of a check, the tests of the full uv run --project .guppi guppi test run of Work Mode that fail on a live file of vault/ or .claude/ the Case does not name, counted in the estimate line
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
**－** `insight-workflow-contract-change-leaves-its-derived-text-stale` stands `actioned` with `addressed_by: decision-case-736.1` and leaves the backlog.

## Result

2026-10-08, Retro, the new Render of rule-case-build in vault/raw/2026-10-08/1547/spec.md (Case 736.1) read against the Criterion of 736.1; the replace adds the step — Grep tests/ for the tests that read a live file of vault/ or .claude/, not a copy under a temporary folder; for each one whose code reaches the changed code, directly or through a module that imports it, read that file against the new check; each refused text enters the Case or context says why — and its old text stands once in vault/wiki/rules/rule-case-build.md; the update of insight-workflow-contract-change-leaves-its-derived-text-stale sets status actioned and addressed_by decision-case-736.1, and the page holds no deferred_by, so guppi backlog drops it at the librarian's run; no Case of this session changes the code of a check, so the full make test run counts 0 failures on an unnamed live file

## History

- 2026-10-08 created · [[decision-case-736.1]]
- 2026-10-08 status: pending → passed · raw/2026-10-08/1547/ledger.md#L10
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make test` → `uv run --project .guppi guppi test` · [[decision-case-820.7]]
