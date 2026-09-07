---
title: "A restart interrupts a collection run rather than resuming it"
type: decision
status: current
authority: run-interruption-policy
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-05
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [collection, batches]
---

# A restart interrupts a run rather than resuming it

The owner's decision, taken during slice 2b.

**What it buys:** this is precisely what makes a daemon thread sufficient and a job queue
unnecessary. Resumption would require the run's position to be durable and re-entrant, which is a
queue by another name.

**What was rejected:** resuming an interrupted run. Not forbidden for ever — deferred, and listed
in [[collection-features-deferred]].

**What it obliges:** [[batch-lifecycle]] owns the rule that follows from it — a crashed run closes
as `interrupted` — and it obliges both cleanup paths, the sweep at container start and
[[stale-after-thirty-minutes]], because an interrupted run leaves a row nobody will close.

See [[collection-runs-in-a-thread]] for the mechanism this decision permits.
