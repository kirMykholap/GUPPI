---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Pre-spec finds a Case of the plan that differs from its ratified copy in what the scripts apply, or whose prose is still Russian
method: uv run pytest tests/test_prespec.py -k ratified
checked: 2026-09-25
origin: raw/2026-09-23/1859/ledger.md#case-387.4
sprint: migration
created: 2026-09-23
tags: [session, workflow, harness]
---

## Criterion

When:
`guppi prespec --check <plan>` runs at `/pre-spec`, after the agent translated the names, `context` and `problem` of the plan, and reads the plan and its ratified copy `<plan>.ratified.md`.

Then:
A Case of the plan whose ids, `given`, `when`, `then`, `then` block or `tasks` differ from its section in the ratified copy: one finding naming the Case and the parts.
**＋** A Case of the plan with no section in the copy, and a section of the copy with no Case in the plan: one finding each.
**＋** A name, `context` or `problem` that still holds a Cyrillic letter: one finding.
**－** The section of a Case a `{supersedes:case N}` of the session's window names is no finding: that Case left the plan (case 299.1).
**－** The section of a parent with sub-cases in the copy, every one of them named by such a line, is no finding: the parent left the plan with them.
**－** A Case under `## Deferred` is not compared.

## Result

2026-09-25, uv run pytest tests/test_prespec.py -k ratified: 7 passed — a parent whose sub-cases in the copy are all superseded is no finding, a parent with one sub-case not superseded still is, the plan against its copy and the Cyrillic finding as before

## History

- 2026-09-24 created · [[decision-case-387.4]]
- 2026-09-24 status: pending → passed · raw/2026-09-23/1859/ledger.md#L27
- 2026-09-25 updated: the Criterion replaced whole — a parent whose every sub-case is superseded is no finding (case 417) · [[decision-case-417]]
- 2026-09-25 status: pending → passed · raw/2026-09-25/0051/ledger.md#L18
