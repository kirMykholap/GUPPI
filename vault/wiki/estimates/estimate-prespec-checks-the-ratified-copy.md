---
type: estimate
kind: QA
status: passed
target: "[[rule-prespec]]"
purpose: Pre-spec finds a Case of the plan that differs from its ratified copy in what the scripts apply, or whose prose is still Russian
method: uv run pytest tests/test_prespec.py -k ratified
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
**－** A Case under `## Deferred` is not compared.

## Result

2026-09-24, uv run pytest tests/test_prespec.py -k ratified: 5 passed — a copy equal but the name passes, a difference in the then block, a missing section either way, a superseded Case no finding, Russian prose a finding with or without a copy

## History

- 2026-09-24 created · [[decision-case-387.4]]
- 2026-09-24 status: pending → passed · raw/2026-09-23/1859/ledger.md#L27
