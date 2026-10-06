---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook writes the decision lines of a reply that follow an unmarked lesson of the session, then reminds the agent once a stretch of the addresses mark, and stops once a decision line carries it
method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
checked: 2026-10-07
origin: raw/2026-10-06/0104/ledger.md#case-685.1
sprint: migration
created: 2026-10-06
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` writes fresh decision lines of the reply just finished, and a `lesson[<slug>]` line stands before them, in the session's ledger or among the lines the same `Stop` writes, with no `{addressed_by:...}` and no decision line after it that carries `{addresses:<slug>}`.

Then:
The hook writes every line of the `Stop` as it would without the reminder, and holds back no line for the mark.
**＋** After the write, for each such lesson the hook exits 2 and prints: "ledger: lesson[<slug>] has no mark — did a Case of this session fix its cause? Then write the decision line of the Case or sub-case that fixed it again with {addresses:<slug>} added, alone in a LEDGER block; otherwise go on without it."
**＋** The stderr line names no Case, however many fresh decision lines follow the lesson.
**＋** The stderr line is printed only when it does not already stand in a refusal of the hook since the person's last message.
**＋** A decision line written again with `{addresses:<slug>}` lands beside the first line, the hook reminds of that lesson no more, and `guppi materialize` gives the lesson entry `addressed_by`.
**＋** The hook judges which lessons no mark links to a Case by one function of `guppi/materialize.py`, over the ledger lines in their order.
**－** A lesson that carries `{addressed_by:...}`, that a decision line after it marks, or that stands after every fresh decision line brings no reminder; nor does a fresh lesson line that the same `Stop` holds back or refuses.
**－** A `defer` line, and a decision line from an earlier text of the transcript, bring no reminder.
**－** A session with no `hi` gets no reminder. With `stop_hook_active` set and a transcript the hook cannot read, the lines land and the hook prints nothing.

## Result

2026-10-07, uv run pytest tests/test_ledger.py: 126 passed; the reminder after the write names no Case with fresh lines of cases 9 and 8.1, is told once a stretch so a later ratification of case 9 is silent, ends once a decision line carries the mark, and comes for no defer line

## History

- 2026-10-06 created · [[decision-case-685.1]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L33
- 2026-10-07 updated: the Criterion replaced whole — the reminder names no Case · [[decision-case-694.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-06/1448/ledger.md#L22
