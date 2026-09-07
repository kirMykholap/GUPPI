---
title: "The suite runs far slower under contention than idle, which is why a subagent runs only its own tests"
type: lesson
status: archived
authority: suite-timing
basis: measurement
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "CLAUDE.md"]
tags: [testing, process, agents]
---

# 75 seconds idle, 250–360 under contention

The full suite takes about **75 s on an idle machine** and **250–360 s while other agents are
working**, because they contend for the same CPU and the same Docker bind mount.

During one slice several implementers ran it more than once each. **That alone accounted for a
large share of that slice.**

> *Corrected 2026-08-14, by the owner's decision.* This sentence read «a large share of **the six
> hours** that slice took». The figure is in **neither of this page's sources** — `grep` over
> `raw/handoffs/2026-08-12-handoff-before-the-vault.md` and `CLAUDE.md` finds no "six hours" at all
> — while [[how-a-slice-is-executed]], [[agent-round-trip-cost]] and the primary journal all say
> **eight to ten hours**. The owner does not know which slice it referred to and considers the
> number unimportant, so **the quantity is dropped and the claim kept**, rather than one candidate
> being chosen over the other: [[an-unsourced-number-is-dropped-not-chosen]]. Surfaced by the Q2
> acceptance answer of 2026-08-14, which reported it as a provenance blur and correctly declined to
> resolve it ([[the-acceptance-questions]]). If the slice is ever identified, the figure returns
> named. A `basis: measurement` page must not carry a number its sources do not.

Hence the rule: **a subagent runs only the tests covering its own change** — named for it in the
dispatch — and the full suite is the controller's job, once per task, in the main session. A
targeted file runs in seconds and answers the same question about the code just written.

This is the same species of reasoning as [[agent-round-trip-cost]]: the expensive thing was never
the checking, it was the number of times the checking was paid for in wall-clock.

One more timing fact worth keeping beside it: **the test database is built from the models by
`Base.metadata.create_all` and therefore never follows a migration.** That already cost a
hand-written `ALTER TABLE` during slice 2b and will recur on the next migration. What that costs
and what catches it is a subject of its own, and it is not a footnote on suite timing:
[[migrations-do-not-drift-from-the-models]] — including the second database
(`MIGRATION_CHECK_DATABASE_URL`) those tests need and that nothing else names.

And one safety fact of the same family: **the web tests could start a real collection against the
developer's own database**, because the guard that prevents it was opt-in where the CLI tests make
it `autouse`. A guard that has to be remembered per test file is a guard that will be forgotten in
the next file. Closed by the 2b final review.

Two environment facts that bite before any test runs: [[docker-desktop]] and [[app-restart-required]].

## Its guard lesson was cited back at us, by a scout, on 2026-08-20

**The sentence on this page — *"a guard that has to be remembered per test file is a guard that will
be forgotten in the next file"* — refuted the shape of a fix while it was being built.** A read-only
scout over `lessons/` produced it against a proposed per-call-site test-database guard, and
**that objection is what produced the meta-test** ([[the-test-database-guard]],
[[a-guard-remembered-per-file-is-forgotten-in-the-next-file]],
[[read-only-scouts-one-per-folder-ahead-of-the-librarian]]).

**Worth recording because it is what a store is for**: the lesson was three days old, nobody
remembered it, and it changed a design.

**A separate wall-clock finding of the same day is not this page's**: with nothing listening on
5432 the suite hangs rather than failing, for over 420 seconds against the ~75 s recorded here
([[the-integration-suite-hangs-rather-than-failing-when-docker-is-down]]).
