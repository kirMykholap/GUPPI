---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook writes the decision lines of a reply that follow an unmarked lesson of the session with no reminder of the addresses mark, and lands a decision line that carries it
method: uv run --project .guppi pytest .guppi/tests/test_ledger.py — piped payloads and a session ledger in a temp vault; by hand, at the Retro of the session that changes it, the new Render of rule-orchestration in the Spec read against the Criterion
checked: 2026-10-30
origin: raw/2026-10-06/0104/ledger.md#case-685.1
sprint: migration
created: 2026-10-06
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py` writes fresh decision lines of the reply just finished, and a `lesson[<slug>]` line of the session stands before them, in the session's ledger or among the lines of the same `Stop`, with no `{addressed_by:...}` and no decision line after it that carries `{addresses:<slug>}`.

Then:
The hook writes every line of the `Stop` and prints no line about the lesson.
**＋** When no other refusal of the hook stands at that `Stop`, it exits 0.
**＋** A decision line that carries `{addresses:<slug>}` lands in the session's ledger as any decision line of its Case does.
**＋** `.guppi/guppi/ledger.py` holds no question about a lesson before a Case, and the new Render of `rule-orchestration` in the Spec names no reply that answers one.
**－** The hook holds back no decision line because it lacks `{addresses:...}`.

## Result

2026-10-30, Retro of session 2341: uv run --project .guppi pytest .guppi/tests/test_ledger.py 155 passed, among them a lesson before fresh decision lines of one Case and of several Cases giving (0, ""), a decision line with {addresses:lesson-x} landing, no decision line held for the mark, and ledger holding no reminder_message or unaddressed; the new Render of rule-orchestration in the Spec replaces the one reply that answered the reminder with the mark the summary of case-guppi holds, and a Grep of reminder over rule-orchestration finds no other such reply, only the booking example

## History

- 2026-10-06 created · [[decision-case-685.1]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L33
- 2026-10-07 updated: the Criterion replaced whole — the reminder names no Case · [[decision-case-694.2]]
- 2026-10-07 status: pending → passed · raw/2026-10-06/1448/ledger.md#L22
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-30 updated: the Criterion replaced whole — no reminder of a lesson with no mark · [[decision-case-915.1]]
- 2026-10-30 status: pending → passed · raw/2026-10-29/2341/ledger.md#L30
