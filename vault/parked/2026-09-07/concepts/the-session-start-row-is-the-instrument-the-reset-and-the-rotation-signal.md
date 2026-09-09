---
title: "The `session-start` row is the instrument, the reset and the rotation signal, and it is correct under either answer to the question it measures"
type: concept
status: current
authority: session-start-row
basis: code
sprint: S2
created: 2026-08-21
sources: ["archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md", ".claude/hooks/session-brief.ps1", ".claude/hooks/pre-task-state.ps1"]
tags: [harness, process, agents]
---

# One row, appended by `SessionStart`, doing three jobs

**`session-start:<source>` carries the reason the session started** — `startup`, `resume`,
`compact` or `clear` — in the `event` column of the pre-task ledger, and `-` in `pre_task`
([[the-pre-task-column-gains-a-state-for-asserting-nothing]]).

**It is the instrument for a question nobody had measured**: whether a `/clear` keeps the session
identifier. Two append-only rows can be compared; the `.session` stamp is overwritten in place and
leaves no *before* ([[the-pre-task-ledger]]).

**It is the reset.** `Read-LedgerState` drops everything the session accumulated before a
`session-start:clear` row, which discharges the repair
[[the-approved-scope-survives-a-compact-and-not-a-clear]] designed and deferred.

**It is what tells the rotation this is a new session** rather than the same one resumed, compacted
or cleared ([[the-pre-task-ledger-holds-one-session-and-rotates-at-startup]]).

# It is correct under either answer to the question it asks

**If `session_id` does not survive a `/clear`**, the reset lands on a state that is already empty and
costs nothing. **If it does survive**, the reset is the branch that was owed. A guard whose
correctness does not depend on the measurement it enables is the shape to reach for when the
measurement is expensive to arrange — and this one was then withdrawn by the owner and never taken.

**Reaching the same behaviour from either branch is not the same as not needing the measurement.**
What is lost by not measuring is the *explanation*: the page carrying the behaviour stays
`basis: inference`, and a later reader looking for the branch that implements the survival rule will
still not find one.

# One row rather than three artefacts

**The columns are the design and the consumers are not.** Three jobs on one row is the same
arrangement the ledger already uses for the record, the heartbeat and the permission mode
([[one-ledger-is-the-record-the-heartbeat-and-the-permission-mode]]).
