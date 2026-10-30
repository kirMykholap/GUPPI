---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook holds once an error lesson line with no addressed_by mark written after a decision line of the session, asks for the mark, writes the line written again unless another refusal of the hook keeps it out, and never holds a knowledge lesson line for its mark
method: uv run --project .guppi pytest .guppi/tests/test_ledger.py — piped payloads and a session ledger in a temp vault
checked: 2026-10-30
origin: raw/2026-10-05/2249/ledger.md#case-682.1
sprint: migration
created: 2026-10-05
tags: [session, hooks, harness, ledger]
---

## Criterion

When:
The `Stop` hook `uv run --project .guppi guppi ledger` of `.guppi/guppi/ledger.py` finds a fresh `lesson[<kind>][<slug>]` line in a `LEDGER` block of the session that carries no `{addressed_by:...}`, and a decision line of the session stands before it, in the session's ledger or earlier among the lines of the same `Stop`.

Then:
For a `lesson[error]` line, at the `Stop` of the reply that carries it, the hook holds the line back once, unless it already asked about it since the person's last message.
**＋** For each held line the hook exits 2 and prints: "ledger: lesson[<slug>] held — did a Case of this session fix its cause? Then add {addressed_by:case <N>}, the Case or sub-case that fixed it, and repeat the line; otherwise repeat it unchanged." The line names no Case, however many decision lines stand before the lesson line.
**＋** The held line lands as it stands once the hook's question about it stands in a refusal since the person's last message, or when it stands only in an earlier text of the transcript; neither way lands it while another refusal of the hook keeps it out, as `estimate-ledger-write-lifts` sets it.
**＋** A held line keeps back no other line: the rest of that `Stop` lands in the ledger.
**＋** A `lesson[knowledge]` line is never held for its mark: it lands at its first `Stop`, unless another refusal of the hook keeps it out.
**－** An unmarked line of either kind never lands beside a marked one: `{addressed_by:...}` on a `lesson[<slug>]` line in the session's ledger, or in that `Stop`, drops the unmarked line of the slug.
**－** The hook holds no lesson line that stands before every decision line of the session, no line it refuses for its prefix or cannot parse, no line that the ledger of some session already holds, and no line that `estimate-ledger-write-refuses-a-lesson-with-an-unlisted-tag` keeps out.
**－** A session with no `hi` gets no question; with `stop_hook_active` set and a transcript the hook cannot read, the line lands as it stands.

## Result

2026-10-30, Retro of session 2341: uv run --project .guppi pytest .guppi/tests/test_ledger.py 155 passed; the tests of the hold of an error lesson stand green, and the new ones show a lesson[knowledge] line after a decision line landing at its first Stop with (0, "") and a lesson[knowledge] line beside a marked line of its slug dropped

## History

- 2026-10-06 created · [[decision-case-682.1]]
- 2026-10-06 status: pending → passed · raw/2026-10-05/2249/ledger.md#L20
- 2026-10-06 updated: the Criterion replaced whole — a decision line after an unmarked lesson is written and left to the reminder (case 685.2) · [[decision-case-685.2]]
- 2026-10-06 status: pending → passed · raw/2026-10-06/0104/ledger.md#L49
- 2026-10-07 updated: the Criterion replaced whole — the question of the hold names no Case · [[decision-case-694.1]]
- 2026-10-07 status: pending → passed · raw/2026-10-06/1448/ledger.md#L21
- 2026-10-07 updated: the Criterion replaced whole — a line refused for a tag outside tags.md is not held for its mark and does not land (case 703.3) · [[decision-case-703.3]]
- 2026-10-07 status: pending → passed · raw/2026-10-07/0636/ledger.md#L31
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `uv run pytest` → `uv run --project .guppi pytest` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-30 updated: the Criterion replaced whole — only an error lesson is held for its mark · [[decision-case-915.3]]
- 2026-10-30 status: pending → passed · raw/2026-10-29/2341/ledger.md#L32
