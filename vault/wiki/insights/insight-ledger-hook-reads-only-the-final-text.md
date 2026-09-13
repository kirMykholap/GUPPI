---
type: insight
pattern: The ledger writer sees the last text of a turn, not the turn; a LEDGER block anywhere else in the turn is never written.
status: open
children: [lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call, lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn, lesson-transcript-omits-text-emitted-before-tool-calls]
severity: 3
origin: raw/2026-09-12/ledger.md#L101
sprint: migration
created: 2026-09-12
tags: [harness, hooks, ledger]
---

## Pattern

Two lessons on one writer.

`lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call` (session F): the replies that
acknowledged Cases 48 and 49 ended in a Skill call and in `ExitPlanMode`; no `Stop` fired
for those turns, and their LEDGER blocks never reached `ledger.md`.

`lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn` (session I): `Stop`
did fire, but the blocks of Cases 59.1, 59.2, 59.4, 60, 63, 64, 65 and 66 sat in a text
message followed by tool calls in the same turn and were lost; the blocks of 58, 59.3,
59.5-59.8, 61 and 62, each the last message of its turn, were written.

The condition that loses a block is the same in both: the block is not the last text of
the turn. No `Stop` event, and a `Stop` whose read-back does not collect an intermediate
message, are two halves of one gap.

## Proposal

A suggestion, not a decision. Read `guppi/ledger.py` - `transcript_texts` and the filter
that decides which messages are the main agent's - against the transcript of session I,
and settle one question: is an intermediate assistant text message in the transcript at
all, or is it collected and then dropped. If it is present, collect every assistant text
message of the `hi` window instead of the last one; if it is absent, the writer needs a
second event beside `Stop`. Either way the writer can count back: blocks seen against
lines written, shown at `/hi` with the unmaterialized tail.

## Children

- [[lesson-ledger-hook-misses-a-reply-ending-in-a-tool-call]]
- [[lesson-ledger-hook-drops-a-block-followed-by-tool-calls-in-the-turn]]
- [[lesson-transcript-omits-text-emitted-before-tool-calls]]

## History

- 2026-09-12 created · raw/2026-09-12/ledger.md#L101
- 2026-09-13 updated: synthesis: lesson-transcript-omits-text-emitted-before-tool-calls added, the text before a tool call is not in the transcript · raw/2026-09-13/ledger.md#L42
