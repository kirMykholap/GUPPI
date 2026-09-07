---
title: "Collection runs in a daemon thread, and its whole state lives in the database"
type: concept
status: current
authority: collection-execution
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [collection, batches, web, db-schema]
---

# Collection runs in a thread, and its state lives in the database

A press on the page starts a daemon thread inside the app process, which calls the same
`run_profile` the CLI calls. The container talks to the internet.

**The state of a run lives in the database, never in process memory.** One row per run in
`parse_batches`; a partial unique index permits one `running` batch per profile.

That single choice is what makes the rest work:

- **a second press is refused by the index**, not by a check in code — the database is the guard;
- **a run started from the terminal disables the buttons on the page**, because `jobhunt parse`
  opens a batch of its own and the index does not care who pressed;
- progress is read from rows the runner already commits — no separate progress channel exists.

Who is allowed to close such a batch is a separate question, owned by [[batch-lifecycle]].

**A restart interrupts a run rather than resuming it**, and that is what makes a thread sufficient
and a job queue unnecessary. See [[restart-interrupts-a-run]].

The cost of committing progress early is dangling rows after a crash, closed by
[[stale-after-thirty-minutes]] and by `jobhunt sweep-batches` at container start. See
[[batch-lifecycle]] for who is allowed to close a batch.
