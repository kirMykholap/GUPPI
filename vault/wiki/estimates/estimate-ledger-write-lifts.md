---
type: estimate
kind: QA
status: pending
target: rule-ledger-write
origin: raw/2026-09-09/ledger.md#case-10
sprint: migration
created: 2026-09-09
tags: [session, hooks, harness, ledger]
---

## Context

This is the hook the whole migration waits on: item 5 of the definition of done says the
final session's ledger is written by it, not by hand. The unit cases pin the contract; the
live reading proves the registration.

## Criterion

Given a `Stop` payload whose reply carries a decision line and an estimate line inside a
`LEDGER` block, and a third decision line both bare and inside an untagged fence, with a
`hi` recorded for the session: the ledger gains exactly the two lines of the block, their
text verbatim and the time of writing in front, once, even when the hook runs twice on the
same payload; a line already present by hand, without a time, is not written again.
Without `hi` the hook exits 2 with a reason naming the count and the session, and
the ledger is untouched. With `stop_hook_active` true it exits 0 and writes nothing. With the `session-start` and the `hi` in yesterday's event log and only `tool` lines
in today's, the lines are written into today's ledger. A reply carrying a `LEDGER` block
that ends in `/pre-task` reaches the ledger once, at the next `Stop` of the session. In a
live session, the last lines of this slice reach `raw/2026-09-09/ledger.md` written by the
hook, not by hand.

### case 103.1

When:
The `Stop` hook (`uv run guppi ledger`) writes record lines.

Then:
The lines go to `raw/<hi date>/<hi HHMM>/ledger.md` — the session folder from `session_dir`, the same folder across midnight.
**＋** The dedupe reads every `ledger.md` under `raw/` at any depth.
**－** Without a `hi` the hook refuses as today; `event_log.md` stays per day as today.

### case 111.3

When:
The `Stop` hook has lines to write, or a script asks `session_dir` for the session's folder.

Then:
The session is a working one when a `hi` line of this session's stamp follows its first `session-start` in the logs walked; the folder is the first such `hi`.
**＋** A `session-start` of another session, before or after, changes nothing; a `resume` or `compact` of our own still does not close the window (case 14).
**－** A `hi` with `--------` or another stamp does not count.
**＋** `estimate-ledger-write-lifts` gets a `### case 111.3` block, `pending`; the test seeds our start, a foreign `resume` and a stamped `hi` and expects the window open, and a `--------` `hi` alone and expects it refused.

### case 111.6

When:
The `Stop` hook, `pretask`, `spec`, `gate` or `cleanup` asks whether the session has a `hi`, or where its folder is.

Then:
A `hi` of this session's stamp after its first `session-start` opens the window, as 111.3 says.
**＋** With no such line in the logs walked, a `--------` `hi` after a `session-start` of this session with no other session's start in between opens it — the rule before 111.3, kept for the sessions the old skill line opened.
**－** A `hi` of another session's stamp never counts.
**＋** `estimate-ledger-write-lifts` gets a `### case 111.6` block, `pending`; the test seeds an unstamped `hi` under our start and expects the window open, and the same with a foreign start between and expects it refused.

## Method

pytest in `tests/test_ledger.py` with piped payloads against a temp vault; the live
reading is taken once by hand and written into the estimate line.

## Result

unit: tests/test_ledger.py 32 green with the two cases of 103.1 — the lines land in raw/<hi date>/<hi HHMM>/ledger.md, across midnight under the hi date and nothing under today, a line already in a date-level ledger is not written twice; live 2026-09-13 session L: the first LEDGER block after the code change, the two readings at 22:36:57, landed in raw/2026-09-13/0652/ledger.md while raw/2026-09-13/ledger.md kept its last line of 22:18:17, and guppi tail printed both units, 2026-09-13 L1–L49 and 2026-09-13/0652 L1–L3

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-10
- 2026-09-09 updated: criterion follows the LEDGER block and the time prefix · raw/2026-09-09/ledger.md#case-15.1
- 2026-09-09 status: pending → passed · written by hand, no generator yet
- 2026-09-11 updated: the midnight window added to the criterion; pending until the reading · [[decision-case-55.1]]
- 2026-09-11 updated: the transcript read-back added to the criterion; pending until the live reading · [[decision-case-55.2]]
- 2026-09-11 status: pending → passed · raw/2026-09-11/ledger.md#L72
- 2026-09-13 criterion: case 103.1 added · [[decision-case-103.1]]
- 2026-09-13 status: pending → passed · raw/2026-09-13/0652/ledger.md#L4
- 2026-09-14 criterion: case 111.3 added · [[decision-case-111.3]]
- 2026-09-14 criterion: case 111.6 added · [[decision-case-111.6]]
