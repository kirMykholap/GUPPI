---
type: estimate
kind: QA
status: pending
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook refuses a reading of an Estimate that a decision line of the same session creates or updates, and says why only for the reply just finished
method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
checked: 2026-09-26
origin: raw/2026-09-25/1654/ledger.md#case-428.1
sprint: migration
created: 2026-09-25
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run guppi ledger` finds a fresh `estimate[<slug>]` line in a `LEDGER` block of the session, and a decision line `create` or `update` of `<slug>` stands in the session's ledger or among the lines the hook writes on the same `Stop`.

Then:
The line is not written: what a session changes, it does not measure, and the reading of `<slug>` waits for a later session.
**＋** A reading of the old slug of a page that an `update` of this session renames is refused by the same rule: the decision line names the old slug.
**＋** The other lines of the `Stop` are written as before.
**＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: estimate[<slug>] not written — case N creates or updates <slug> in this session; what a session changes it does not measure: take the reading in a later session and name it in the handoff."
**＋** A refused line of an earlier text of the transcript is skipped at every later `Stop` without a word.
**－** A reading of a slug that no decision line `create` or `update` of this session names is written as before; a `defer` line of the slug does not refuse it.
**－** Without a `hi` the hook judges no line. With `stop_hook_active` set it judges the line the same, and its stderr line is told once a stretch, as `estimate-ledger-write-lifts` sets it.

## Result

2026-09-26, `uv run pytest -q tests/test_ledger.py`; 42 passed, a reading of a slug a create or update of the session names is refused with exit 2 and the stderr line, an earlier text skipped silently, a defer or another session's line lets it through

## History

- 2026-09-25 created · [[decision-case-428.1]]
- 2026-09-26 status: pending → passed · raw/2026-09-26/1745/ledger.md#L29
- 2026-10-01 updated: the Criterion replaced whole — with stop_hook_active the line is judged the same, and its stderr line is told once a stretch (case 577.6) · [[decision-case-577.6]]
