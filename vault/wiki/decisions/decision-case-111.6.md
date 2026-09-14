---
type: decision
case: "111.6"
status: current
update: [rule-ledger-write]
origin: raw/2026-09-14/0747/ledger.md#case-111.6
sprint: migration
created: 2026-09-14
tags: [session, hooks, harness, ledger]
---

## Context

Today at 07:30:30 two sessions started in one second: this one, `fde37e7c`, and `19b07bbc`, session L, restored by `resume`. The `hi` of 07:30:39 carries `--------` — `CLAUDE_SESSION_ID` is empty in the `!` substitution of the skill — so the ledger hook tied it to the start nearest before it, the foreign one, and refused every line of this session. A second `/hi` did not help: `hi_recorded` sets `ours = False` on the foreign start and only a new `session-start` of our own sets it back; a `resume` of this session at 07:46:53 did. The lesson line of 07:44 ends "A second /hi at 07:44 fixed the window", which is false.

## Problem

The window of a session is inferred from the order of starts around an unstamped `hi`. One foreign start between our start and our `hi` — a restored tab is enough — takes the `hi` away, and the session cannot recover by any command of its own. `rule-event-log` names this as a known limit since Case 9. The lesson page will be born with a wrong root cause.

## Given

111.3 says a `hi` with `--------` does not count. The hook of 111.1 that writes a stamped `hi` reaches `settings.json` only after the librarian of this session renders it. Every `hi` of sessions A–M is `--------`, this session's included; the code of 111.3 in the working tree refused 13 lines at 09:5x, and `session_dir` — the folder `0747` of this session, its Spec, its ledger — resolves through that unstamped `hi` too. A fork of Work Mode, returned as a Case.
**＋** `hi_recorded` and `hi_moment` (`ledger.py`, as changed by 111.3) skip every line of another stamp. The tests of 111.3 stand; `test_an_unstamped_or_foreign_hi_does_not_count` splits: a foreign `hi` never counts; an unstamped `hi` counts by the old rule when no stamped one exists, and is refused after a foreign start.
**－** The fallback leaves with a later Case, once the readings of 111.1 pass and no writer of `--------` is left (111.4).

## Criterion

- [[estimate-ledger-write-lifts]] § case 111.6

## History

- 2026-09-14 created · raw/2026-09-14/0747/ledger.md#case-111.6
