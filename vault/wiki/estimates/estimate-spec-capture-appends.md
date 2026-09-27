---
type: estimate
kind: QA
status: passed
target: "[[rule-spec-capture]]"
method: pytest in tests/test_spec.py with piped payloads against a temp vault; by hand, the next approval of a session after the change
checked: 2026-09-27
origin: raw/2026-09-09/ledger.md#case-20
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness, workflow]
---

## Criterion

When:
`ExitPlanMode` is approved, and `uv run guppi spec` runs on its `PostToolUse` with the plan in `tool_response.plan`.

Then:
In a session with a `hi`, the plan is appended to `raw/<hi date>/<hi HHMM>/spec.md` — a `---` separator when the file has content, the stamp `<!-- approved HH:MM:SS · session xxxxxxxx -->` and the plan text — once, even when the hook runs twice.
**＋** A second approval of the same session appends under `---` and its stamp.
**＋** The hook changes nothing that stands in the file: earlier documents, the sections the `Stop` hook of `rule-spec-write` wrote and a `## Deferred` section stay as they are, and `uv run guppi materialize` reads their Cases.
**－** Without a `hi` the hook exits 2 naming the session, and the file is untouched.
**－** The payload of another tool writes nothing: exit 0.

## Result

2026-09-27, uv run pytest tests/test_spec.py: 14 passed; by hand, the approval of session 1819: vault/raw/2026-09-27/1819/spec.md opens with <!-- approved 20:18:32 · session 938809b2 --> and the plan text, once

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-20
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L77
- 2026-09-11 updated: the Retro section survives a later approval; pending until the live reading · [[decision-case-57]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L34
- 2026-09-12 updated: the Deferred heading (cases 59.5, 66) · [[decision-case-66]]
- 2026-09-12 criterion: case 73.2 added · [[decision-case-73.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L37
- 2026-09-26 updated: the Criterion replaced whole — the Stop hook of rule-spec-write, not the agent, writes the sections the append leaves (case 441.10) · [[decision-case-441.10]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L35
