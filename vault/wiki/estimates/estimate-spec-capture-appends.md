---
type: estimate
kind: QA
status: pending
target: "[[rule-spec-capture]]"
method: pytest in tests/test_spec.py with piped payloads against a temp vault; by hand, the next approval of a session after the change
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

block 73.2 at the approval of 11:40:48: the plan copied whole to raw/2026-09-14/1029/spec.md under `<!-- approved 11:40:48 · session 19037d1c -->`, 64696 bytes for a 64648-byte plan

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-20
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L77
- 2026-09-11 updated: the Retro section survives a later approval; pending until the live reading · [[decision-case-57]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L34
- 2026-09-12 updated: the Deferred heading (cases 59.5, 66) · [[decision-case-66]]
- 2026-09-12 criterion: case 73.2 added · [[decision-case-73.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L37
- 2026-09-26 updated: the Criterion replaced whole — the Stop hook of rule-spec-write, not the agent, writes the sections the append leaves (case 441.10) · [[decision-case-441.10]]
