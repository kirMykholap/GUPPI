---
title: "The startup sweep runs only under Docker; a bare uvicorn waits for the staleness window"
type: decision
status: current
authority: startup-sweep-coverage
binding: prohibition
basis: code
sprint: S0
decided: 2026-08-05
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [batches, collection]
---

# The startup sweep exists only under Docker

`jobhunt sweep-batches` is called by `docker-entrypoint.sh`. A developer who starts `uvicorn`
directly gets no sweep, and web batches that died with that process wait out
[[stale-after-thirty-minutes]] instead.

**Development only, and it has a one-line remedy:** run `jobhunt sweep-batches` by hand.

Recorded because the symptom — a run that looks alive for half an hour after the process is gone —
looks like a bug in the batch logic when it is in fact an absent entrypoint. See
[[batch-lifecycle]] for the two closers that exist for a process which can no longer speak for
itself.
