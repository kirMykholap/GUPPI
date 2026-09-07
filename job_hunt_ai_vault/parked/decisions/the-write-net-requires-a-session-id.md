---
title: "The write net requires a `session_id`, and says nothing without one"
type: decision
status: current
authority: net-session-id-requirement
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact/handoffs/2026-08-20-the-pre-task-ritual-gets-a-moment-and-an-artefact.md", ".claude/hooks/ask-the-vault.ps1"]
tags: [harness, agents, process]
---

# The ruling, 2026-08-20

**Chosen:** the pre-task net in `.claude/hooks/ask-the-vault.ps1` speaks only on a payload carrying
a `session_id`. **Rejected:** speaking anyway, which is speaking on **every** edit.

**`once per session` is undefined without a session.** The advisory is spent by being said once, and
what spends it is a row in the ledger keyed on the session
([[the-pre-task-ledger]]). With no key there is nothing to spend, so the guard would fire on every
`Edit|Write` for the rest of the run — the exact noise it was built to avoid, attached to a ritual
the reader cannot satisfy ([[once-per-session-is-undefined-without-a-session]]).

**Ratified by the owner** after eight selftest cases asserting the guard's silence went red at once
and were right.

# The opposite choice is made on purpose next door

**The scoped-rule branch of the same hook speaks on every matching edit**, and that is not an
inconsistency: the consequence of repeating differs. An unrepeated rule delivery is a rule that is
not there after a compaction ([[a-guard-branch-in-the-edit-hook-delivers-a-path-scoped-rule]],
[[what-survives-a-compaction-is-whatever-has-something-that-runs-it-again]]); an unrepeated advisory
is a nag. **Annoying there, fatal here.**
