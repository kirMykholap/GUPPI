---
title: "The pre-task state machine has a flag for the plan and a flag for the write, and no special cases"
type: concept
status: current
authority: pre-task-state-machine
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", "archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md", ".claude/hooks/pre-task-state.ps1"]
tags: [harness, agents, process]
---

# What the ledger is asked

**`pre-task` and `scope-approved` are rows**, and every question the harness asks is a comparison
between them ([[the-pre-task-ledger]]).

- **The plan path asks whether a pre-task exists that is newer than the last approved scope.** A
  pre-task belongs to the plan it checked; once that plan is approved the scope closes and the next
  plan inherits nothing ([[one-pre-task-per-approved-scope-and-the-answer-comes-back-per-item]]).
- **The write path asks only whether the session ever passed through either gate.** It is a net, not
  the ritual: a session with an approved scope has already been through the plan path, and nagging
  it at its first write would fire on every session that did the right thing.

# Why the comparison is lexical, and which way a tie falls

**The timestamp format is fixed-width, so lexical order is chronological order** and no date parsing
happens in a hook.

**The comparison is `-le` rather than `-lt`**, so a pre-task and an approval landing inside the same
second resolve towards **asking again**. That is the direction a guard is allowed to be wrong in,
and it is the same reasoning applied to a rejected plan reaching `PostToolUse`: an approval recorded
that never happened costs the next plan a fresh pre-task
([[the-plan-check-hook]]).

# What has no special case

**A `/compact` and a `/clear` are not branches** — the bit's survival falls out of keying on
`session_id` ([[the-approved-scope-survives-a-compact-and-not-a-clear]]).

**Nothing detects a `/pre-task`**; it records itself, and the state machine reads only what was
recorded ([[the-ritual-records-itself-rather-than-being-detected]]).

# A `/clear` is a branch now, and the sentence above is dated — 2026-08-20, fourth session

**"A `/compact` and a `/clear` are not branches" was true until `abd2a53`.** `Read-LedgerState` now
drops everything a session accumulated before a `session-start:clear` row, so the reset is written
rather than falling out of keying on `session_id`
([[the-session-start-row-is-the-instrument-the-reset-and-the-rotation-signal]],
[[the-approved-scope-survives-a-compact-and-not-a-clear]]).

**A `/compact` is still not a branch**, and the halves are worth keeping apart: the machine now has
one special case and it is the one whose absence was the recorded risk. The sentence above stands as
what was true when it was written, because a claim about the tree is dated where it stands
([[the-region-coverage-figure-is-dated-where-it-stands]]).

**The reset is asserted in both directions in the selftest** — a `compact` row leaves a pre-task
standing and a `clear` row drops it — so a branch that fired always, or never, fails one of the
pair ([[a-case-that-passes-before-the-change-tests-nothing]]).
