---
title: "The `pre_task` column gains a state for asserting nothing, rather than defaulting to `no`"
type: decision
status: current
authority: pre-task-column-states
binding: prohibition
basis: code
sprint: S2
decided: 2026-08-20
created: 2026-08-21
sources: ["archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md", ".claude/hooks/pre-task-state.ps1"]
tags: [harness, process, testing]
---

# Decided 2026-08-20, before the row that needed it was written

**A `session-start:<source>` row carries `-` in `pre_task`.** The column had two values, and the new
row fits neither: nothing had been asked of the ritual at the moment a session starts.

**Rejected: writing `no`.** `no` on that row asserts to a human reading the ledger at a retro that a
ritual had been skipped, when nothing had been owed. That is the failure
[[a-column-a-human-reads-is-not-the-column-a-branch-reads]] already records from the other
direction — the same column, the same reader, and a value chosen for a branch's convenience.

**It was found by the `/pre-task` run that preceded the plan**, not by review: the constraint was
one of the three that dispatch returned before approval
([[a-pre-task-paid-for-itself-in-findings-nobody-would-have-made]]).

## What it obliges

**`Add-LedgerLine` takes `[object]` rather than `[bool]`**, so omitting the argument yields `-` and
every existing caller is untouched. A `[bool]` parameter cannot express *no assertion*: it coerces
absence to `$false`, which is exactly the sentence this decision refuses to write.

**The state machine is unaffected.** It asks whether a `pre-task` row exists and how it compares to
the last approved scope; a row that asserts nothing about the ritual answers neither question and is
read for the other jobs it does
([[the-session-start-row-is-the-instrument-the-reset-and-the-rotation-signal]]).
