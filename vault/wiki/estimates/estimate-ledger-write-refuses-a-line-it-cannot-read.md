---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook refuses a record line that parse_line cannot read, and says why only for the reply just finished
method: uv run --project .guppi pytest .guppi/tests/test_ledger.py — piped payloads and a session ledger in a temp vault
checked: 2026-10-02
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, hooks, harness, ledger]
core: true
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ledger` finds a fresh line `- decision[`, `- estimate[` or `- lesson[` in a `LEDGER` block of the session, and `parse_line` of `.guppi/guppi/materialize.py` returns None for it.

Then:
The line is not written.
**＋** The other lines of the `Stop` are written as before.
**＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: line not written — the grammar of a ledger line does not read it: <line>. Write it again in the form of the table in ratification.md."
**＋** At every later `Stop`, a refused line from an earlier text of the transcript is skipped without a word.
**－** A refused line gets no other refusal of the hook and no other stderr line.
**－** A line already in the ledger of any session is not judged again.
**－** Without a `hi` the hook judges no line. With `stop_hook_active` set it judges the line the same, and its stderr line is told once a stretch, as `estimate-ledger-write-lifts` sets it.

## Result

2026-10-02, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
