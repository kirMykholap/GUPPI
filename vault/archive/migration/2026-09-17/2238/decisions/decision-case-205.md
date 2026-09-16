---
type: decision
case: "205"
status: archived
defer: ["[[insight-ledger-hi-tied-to-its-session-by-position]]"]
superseded_by: ["[[decision-case-222]]"]
origin: raw/2026-09-16/1955/ledger.md#case-205
sprint: migration
created: 2026-09-16
tags: [harness, hooks, ledger]
---

## Context

`insight-ledger-hi-tied-to-its-session-by-position` is an Insight, `open`, severity 1, four children, `deferred_by: decision-case-192`, in its fourth brief. Its pattern: the event log binds a `hi` line to its session by the position of the `session-start` lines around it, not by an id; any start missing from the window or added to it sends the `hi` to the wrong session, and the ledger writer refuses. Case 111 already writes a stamped `hi` from the `UserPromptSubmit` hook and reads the window by that stamp, with the old rule as a fallback.

## Problem

Retiring the binding by position is code in two readers — `pretask.resolve_session` and the ledger hook's window — with its own Estimate and a live reading across midnight, which this session cannot take. This session ratified four Cases of code (201–204) with none built yet; a fifth waits for a session that can read it.

## Deferred

### [[insight-ledger-hi-tied-to-its-session-by-position]]

Retire the binding by position: `pretask.resolve_session` resolves the session from the
stamped `hi` and walks back to the date of that `hi`, instead of falling back to the
last `session-start` of today's event log; the ledger hook's window is checked against
it so the two readers do not disagree at midnight. Closes all four children of the
Insight. Needs its own Estimate and one live reading across midnight. Deferred by 192,
again by 205.

## History

- 2026-09-16 created · raw/2026-09-16/1955/ledger.md#case-205
- 2026-09-17 superseded by decision-case-222 · [[decision-case-222]]
- 2026-09-17 archived · superseded
- 2026-09-17 archived · cleanup
