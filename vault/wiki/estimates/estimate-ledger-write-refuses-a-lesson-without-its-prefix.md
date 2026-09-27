---
type: estimate
kind: QA
status: pending
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook refuses a lesson line whose slug does not open with lesson-, and says why only for the reply just finished
method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
origin: raw/2026-09-27/1819/ledger.md#case-460.5
sprint: migration
created: 2026-09-27
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run guppi ledger` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session. `category_of` of `guppi/materialize.py` does not put its slug under the lessons folder: the slug does not start with the lesson prefix.

Then:
The line is not written.
**＋** The other lines of the `Stop` are written as before.
**＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: lesson[<slug>] not written — a lesson slug starts with lesson-, then the area, then the cause: write the line again with the prefix."
**＋** At every later `Stop`, a refused line from an earlier text of the transcript is skipped without a word.
**－** A lesson line whose slug starts with the lesson prefix is written as before. A line already in the ledger of any session is not judged again.
**－** `estimate[...]` and `decision[...]` lines are not judged by their prefix.
**－** Without a `hi`, and with `stop_hook_active`, the hook acts as before and judges no line.

## History

- 2026-09-27 created · [[decision-case-460.5]]
