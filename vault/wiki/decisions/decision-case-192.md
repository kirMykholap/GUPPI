---
type: decision
case: "192"
status: current
defer: ["[[insight-ledger-hi-tied-to-its-session-by-position]]"]
origin: raw/2026-09-16/1034/ledger.md#case-192
sprint: migration
created: 2026-09-16
tags: [harness, hooks, ledger]
---

## Context

`insight-ledger-hi-tied-to-its-session-by-position` is an Insight, `open`, severity 1, with
four children. Its pattern: the event log binds a `hi` line to its session by the position
of the `session-start` lines around it, not by an id; any start missing from the window or
added to it sends the `hi` to the wrong session, and the ledger writer refuses. The fourth
child arrived yesterday: `pretask.resolve_session` falls back to the last `session-start`
of today's log when `--session` is absent and stops at midnight, unlike the hook's own
window, which crosses it.

## Problem

The proposal on the page was written before the Insight was actioned in case 136.4 and has
not been revisited since: the stamped `hi` of case 111 and a window read by stamp allow the
binding by position to be retired altogether. But that is a change to
`pretask.resolve_session`, and probably to the ledger hook's window — code, not text — and
deciding it at the close of a long session that is already carrying an unexecuted Spec
would be a fourth code decision where none of the first three has been built.

## Deferred

### [[insight-ledger-hi-tied-to-its-session-by-position]]

Retire the binding by position: `pretask.resolve_session` resolves the session from the
stamped `hi` and walks back to the date of that `hi`, instead of falling back to the
last `session-start` of today's event log; the ledger hook's window is checked against
it so the two readers do not disagree at midnight. Closes all four children of the
Insight. Needs its own Estimate and one live reading across midnight.

## History

- 2026-09-16 created · raw/2026-09-16/1034/ledger.md#case-192
