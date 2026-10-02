---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook refuses a record line that parse_line cannot read, and says why only for the reply just finished
method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
checked: 2026-10-02
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
**＋** When the refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line: "ledger: line not written — the grammar of a ledger line does not read it: <line>. Write it again in the form of the table in ratification.md."
**＋** At every later `Stop`, a refused line from an earlier text of the transcript is skipped without a word.
**－** A refused line gets no other refusal of the hook and no other stderr line.
**－** A line already in the ledger of any session is not judged again.
**－** Without a `hi` the hook judges no line. With `stop_hook_active` set it judges the line the same, and its stderr line is told once a stretch, as `estimate-ledger-write-lifts` sets it.

## Result

2026-10-02, session 2049: `uv run pytest -q tests/test_ledger.py` 74 passed, test_flag_a_line_the_grammar_cannot_read_is_refused_aloud and test_a_refused_line_of_an_earlier_text_is_skipped_without_a_word among them

## History

- 2026-09-30 created · [[decision-case-552.2]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/2042/ledger.md#L33
- 2026-10-01 updated: the Criterion replaced whole — with stop_hook_active the line is judged the same, and its stderr line is told once a stretch (case 577.5) · [[decision-case-577.5]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1725/ledger.md#L10
- 2026-10-02 updated: the Criterion replaced whole - the refusal names the table in ratification.md (case 595.17) · [[decision-case-595.17]]
- 2026-10-02 status: pending → passed · raw/2026-10-02/2049/ledger.md#L23
