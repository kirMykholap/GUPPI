---
type: estimate
kind: QA
status: pending
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook refuses a lesson line whose addressed_by mark has no decision line of its Case before it in the session, judges it again until that line stands, and says why only for the reply just finished
method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
checked: 2026-09-29
origin: raw/2026-09-29/0137/ledger.md#case-497.1
sprint: migration
created: 2026-09-29
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run guppi ledger` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session, and the line carries `{addressed_by:case N}`.

Then:
When no decision line of Case N stands before the lesson line — in the session's ledger, or earlier among the lines of the same `Stop` — the line is not written.
**＋** The other lines of the `Stop` are written as before.
**＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — {addressed_by:case <N>} names no decision line before it in this session; its sub-cases have case <N.1>, case <N.2>: write the line again after the decision line of the Case that closed the cause, naming that Case." The part on the sub-cases stands only when a decision line of a sub-case of N stands in the session.
**＋** A refused line from an earlier text of the transcript is judged again at every `Stop` until it stands in the ledger. It is written at the first `Stop` where a decision line of Case N stands in the ledger before it. The hook says nothing about it.
**＋** The hook and `guppi materialize` judge the mark by one function of `guppi/materialize.py`, over the ledger lines in their order, and give the same answer for the same lines.
**－** A line that `estimate-ledger-write-refuses-a-lesson-without-its-prefix` refuses is not judged for its mark, and gets that refusal's stderr line alone.
**－** A lesson line whose mark has a decision line of Case N before it is written as before, and so is a lesson line with no mark. A line already in the ledger of any session is not judged again.
**－** Without a `hi` the hook judges no line. With `stop_hook_active` set it judges the line the same, and its stderr line is told once a stretch, as `estimate-ledger-write-lifts` sets it.

## Result

2026-09-29, uv run pytest tests/test_ledger.py: 56 passed; guppi/ledger.py imports marks_without_decision of guppi/materialize.py, no second judgment

## History

- 2026-09-29 created · [[decision-case-497.1]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1134/ledger.md#L25
- 2026-10-01 updated: the Criterion replaced whole — with stop_hook_active the line is judged the same, and its stderr line is told once a stretch (case 577.8) · [[decision-case-577.8]]
