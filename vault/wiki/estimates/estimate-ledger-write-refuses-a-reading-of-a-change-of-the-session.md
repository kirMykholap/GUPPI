---
type: estimate
kind: QA
status: pending
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook refuses a reading of an Estimate that a decision line of the same session creates or updates until the Retro of that session opens, writes it after, and says why only for the reply just finished
method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
checked: 2026-10-01
origin: raw/2026-09-25/1654/ledger.md#case-428.1
sprint: migration
created: 2026-09-25
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` finds a fresh `estimate[<slug>]` line in a `LEDGER` block of the session, and a decision line `create` or `update` of `<slug>` stands in the session's ledger or among the lines the hook writes on the same `Stop`.

Then:
While the event log of the session's window holds no mark `retro` of this session after its `hi`, the line is not written: the reading waits for Retro.
**＋** Once that mark stands, the line is written as any other reading of the `Stop`.
**＋** The mark is judged by `retro_marked` of `guppi/onward.py`, imported, the one judgment of the mark.
**＋** A line of a reply written before the mark stays refused, and the hook skips it at every later `Stop` without a word.
**＋** A reading of the old slug of a page that an `update` of this session renames falls under the same rule: the decision line names the old slug.
**＋** When a refused line stands in the reply just finished, the hook exits 2 with one stderr line per refused line, which names the Case and says that the reading is taken at the Retro of this session.
**＋** The other lines of the `Stop` are written as before.
**－** A reading of a slug that no decision line `create` or `update` of this session names is written as before; a `defer` line of the slug does not refuse it.
**－** Without a `hi` the hook judges no line. With `stop_hook_active` set it judges the line the same, and its stderr line is told once a stretch, as `estimate-ledger-write-lifts` sets it.

## Result

2026-10-01, uv run pytest tests/test_onward.py tests/test_ledger.py: 104 passed; tests/test_ledger.py test_a_reading_of_a_slug_the_session_changes_is_refused (create and update), test_a_decision_line_of_the_same_reply_refuses_it_too, test_a_refused_line_of_an_earlier_text_is_skipped_without_a_word, test_a_reading_with_a_defer_line_only_or_another_sessions_line_is_written and test_flag_a_reading_of_a_change_of_the_session_is_refused_aloud; no test names a rename, which the update line covers, since the decision line names the old slug

## History

- 2026-09-25 created · [[decision-case-428.1]]
- 2026-09-26 status: pending → passed · raw/2026-09-26/1745/ledger.md#L29
- 2026-10-01 updated: the Criterion replaced whole — with stop_hook_active the line is judged the same, and its stderr line is told once a stretch (case 577.6) · [[decision-case-577.6]]
- 2026-10-01 status: pending → passed · raw/2026-10-01/1725/ledger.md#L11
- 2026-10-05 updated: the Criterion replaced whole — the reading is refused only before the mark retro of the session (case 670.1) · [[decision-case-670.1]]
