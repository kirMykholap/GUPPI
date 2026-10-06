---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook holds once a lesson line with no addressed_by mark written after a decision line of the session, asks for the mark, and then writes the line written again
method: uv run pytest tests/test_ledger.py — piped payloads and a session ledger in a temp vault
checked: 2026-10-06
origin: raw/2026-10-05/2249/ledger.md#case-682.1
sprint: migration
created: 2026-10-05
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run guppi ledger` of `guppi/ledger.py` finds a fresh `lesson[<slug>]` line in a `LEDGER` block of the session that carries no `{addressed_by:...}`, and a decision line of the session stands before it, in the session's ledger or earlier among the lines of the same `Stop`.

Then:
At the `Stop` of the reply that carries it, the hook holds the line back once, unless it already asked about it since the person's last message.
**＋** For each held line the hook exits 2 and prints: "ledger: lesson[<slug>] held — did case <N> or case <M> fix its cause? Then add {addressed_by:case <N>}, the Case or sub-case that fixed it, and repeat the line; otherwise repeat it unchanged."
**＋** The Cases the stderr line names are those whose decision lines stand before the lesson line, in the order first seen.
**＋** The line lands as it stands once the hook's question about it stands in a refusal since the person's last message, or when it stands only in an earlier text of the transcript.
**＋** A held line keeps back no other line: the rest of that `Stop` lands in the ledger.
**－** An unmarked line never lands beside a marked one: `{addressed_by:...}` on a `lesson[<slug>]` line in the session's ledger, or in that `Stop`, drops the unmarked line of the slug.
**－** The hook holds no lesson line that precedes every decision line of the session, no line it refuses for its prefix or cannot parse, and no line that the ledger of some session already holds.
**－** The hook never holds a decision line for its `{addresses:...}`: it writes it, and the reminder after the write is `estimate-ledger-write-reminds-of-the-mark-on-a-decision-line`.
**－** A session with no `hi` gets no question. The flag `stop_hook_active` changes nothing here, but when it is set and the transcript is unreadable, the hook lets the line land as it stands.

## Result

2026-10-06, uv run pytest tests/test_ledger.py: 119 passed; the 682.1 tests hold an unmarked lesson after a decision line as before, and a lesson before every decision line is not held and gets only the reminder of case 685.1

## History

- 2026-10-06 created · [[decision-case-682.1]]
- 2026-10-06 status: pending → passed · raw/2026-10-05/2249/ledger.md#L20
- 2026-10-06 updated: the Criterion replaced whole — a decision line after an unmarked lesson is written and left to the reminder (case 685.2) · [[decision-case-685.2]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L49
