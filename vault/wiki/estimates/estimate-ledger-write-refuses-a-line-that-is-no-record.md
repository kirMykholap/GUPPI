---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook refuses aloud a non-blank line of a LEDGER block that does not open with a record prefix, and says why only for the reply just finished
method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
origin: raw/2026-10-06/1448/ledger.md#case-695.1
sprint: migration
created: 2026-10-06
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py`, in a session with a `hi`, finds in a `LEDGER` block of a text of the main agent a non-blank line that does not open with `- decision[`, `- estimate[` or `- lesson[`.

Then:
The line is not written to the ledger.
**＋** The record lines of the same `Stop` are written and judged as before.
**＋** When the line stands in the reply just finished, the hook exits 2 with one stderr line per such line: "ledger: line not written — a LEDGER block holds only lines that open with - decision[, - estimate[ or - lesson[: <line>. Write it again with that opening, or leave it out."
**＋** A reply whose `LEDGER` block holds no record line gets the same stderr line for each such line.
**＋** Each stderr line is told once until the person's next message; a repeat of the same line stays silent.
**－** A line from an earlier text of the transcript is skipped at every later `Stop` without a word.
**－** A blank line, and a line in a block with another tag or with none, is not refused.
**－** Without a `hi` the hook judges no such line.

## Result

2026-10-07, uv run pytest tests/test_ledger.py: 126 passed; the stray tests refuse a near-miss line and a note of the reply just finished with the stderr line of case 695.1, refuse a block with no record line, land the record lines beside them, stay silent on a line of an earlier text, a blank line, an untagged block, a repeat already told and a session with no hi

## History

- 2026-10-07 created · [[decision-case-695.1]]
- 2026-10-07 status: pending → passed · raw/2026-10-06/1448/ledger.md#L18
