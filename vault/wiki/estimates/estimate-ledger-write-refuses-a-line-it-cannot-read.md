---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook refuses a record line that parse_line cannot read, and says why only for the reply just finished
method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
checked: 2026-09-30
origin: raw/2026-09-30/1736/ledger.md#case-552.2
sprint: migration
created: 2026-09-30
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run guppi ledger` finds a fresh line `- decision[`, `- estimate[` or `- lesson[` in a `LEDGER` block of the session, and `parse_line` of `guppi/materialize.py` returns None for it.

Then:
The line is not written.
**＋** The other lines of the `Stop` are written as before.
**＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: line not written — the grammar of a ledger line does not read it: <line>. Write it again in the form of the table in case-schema.md."
**＋** At every later `Stop`, a refused line from an earlier text of the transcript is skipped without a word.
**－** A refused line gets no other refusal of the hook and no other stderr line.
**－** A line already in the ledger of any session is not judged again.
**－** Without a `hi`, and with `stop_hook_active`, the hook acts as before and judges no line.

## Result

2026-09-30, uv run pytest tests/test_ledger.py: 63 passed

## History

- 2026-09-30 created · [[decision-case-552.2]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/2042/ledger.md#L33
