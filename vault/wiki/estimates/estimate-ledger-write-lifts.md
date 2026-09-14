---
type: estimate
kind: QA
status: passed
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

### case 122

When:
The agent calls a skill through the `Skill` tool and `guppi gate` runs.

Then:
The gate reads the `then` items of every Case in the session's `spec.md` and in the plan file the session's event log names last under `.claude/plans/`, and the decision lines of the session's window as `guppi pretask --check` reads them.
**＋** When an item has no decision line of its Case, the gate exits 2 and writes nothing: `gate: /<skill> refused — N item(s) of the Spec have no ledger line (case A, case B). The text before a tool call is never kept: end this reply in text with the LEDGER block, then call /<skill> in the next reply.`
**＋** Every item with its line, or no source found: exit 0, silent; the `/handoff` check of the dirty tree runs as before.
**＋** `rule-ledger-write` gains `guppi/gate.py` and `tests/test_gate.py` in `implementation_ref`; its "How it works" says the gate, not the agent's memory, holds the reply back.
**＋** `rule-case-protocol` says, after the paragraph on the `Stop` hook: "A reply that carries a `LEDGER` block ends in that text. No tool call follows it in the same reply: the text before a tool call is never kept, and the hook reads nothing." — rendered into `CLAUDE.md`, `contract: same`.
**＋** `estimate-ledger-write-lifts` gets a `### case 122` block, `pending`; the test seeds a plan with one item and an empty ledger and expects exit 2 with the case named, then the item's line and expects 0, then no plan path and no `spec.md` and expects 0; the live half is read at the first `/pre-task` of this session after its lines are written: the call passes.
**－** `{supersedes:case 117}`: `decision-case-117` is superseded, `rule-ledger-write` loses `deferred_by`.

## Method

pytest in `tests/test_ledger.py` with piped payloads against a temp vault; the live
reading is taken once by hand and written into the estimate line.

## Result

block 122 against tests/test_gate.py (an item without its line → exit 2 naming the case; the line in raw/<date>/<HHMM>/ledger.md → 0; no plan path and no spec.md → 0; a defer item of spec.md → 2; the Spec check before the tree check) and live: guppi gate on this session's payload with every item lined → exit 0

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
- 2026-09-14 criterion: case 122 added · [[decision-case-122]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L7
- 2026-09-14 status: passed → passed · raw/2026-09-14/1029/ledger.md#L32
