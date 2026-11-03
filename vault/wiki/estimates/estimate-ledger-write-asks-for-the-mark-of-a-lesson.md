---
type: estimate
kind: QA
status: passed
target: "[[rule-ledger-write]]"
purpose: Whether the ledger hook holds once an error lesson line with no addressed_by mark written after a decision line of the session, asks for the mark, writes the line written again unless another refusal of the hook keeps it out, and never holds a knowledge lesson line for its mark
method: uv run --project .guppi pytest .guppi/tests/test_ledger.py — piped payloads and a session ledger in a temp vault
checked: 2026-10-30
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, hooks, harness, ledger]
core: true
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

2026-10-30, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
