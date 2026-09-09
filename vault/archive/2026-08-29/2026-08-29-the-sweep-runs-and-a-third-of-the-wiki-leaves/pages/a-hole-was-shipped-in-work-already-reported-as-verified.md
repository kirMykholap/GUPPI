---
title: "A hole was shipped in work already reported as verified, and read-only scouts found it"
type: lesson
status: archived
authority: verified-coverage-claim
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "tests/db_guard.py", "tests/conftest.py"]
tags: [testing, agents, db-schema]
---

# What the hole was

The test-database guard covered `TEST_DATABASE_URL` and **not** `MIGRATION_CHECK_DATABASE_URL`,
whose fixture runs `DROP DATABASE ... WITH (FORCE)` — **worse than the `TRUNCATE` the guard was
written for**, under a variable whose default name `jobhunt_migration_check` does not end in
`_test`, so the suffix rule did not even fit ([[the-test-database-guard]]).

**Verified rather than assumed, and the split matters:** the unguarded state pre-dates the session.
**The incomplete guard and the claim of verification are the session's.**

# Who found it

**Two of six read-only scouts, independently**, dispatched one per `wiki/` folder
([[read-only-scouts-one-per-folder-ahead-of-the-librarian]]). The `concepts/` scout named
[[migrations-do-not-drift-from-the-models]] as the page that already recorded the second variable —
**the fact was in the store the whole time**.

**A third scout then refuted the shape of the fix.** The `lessons/` scout cited
[[test-suite-wall-clock]] — *"a guard that has to be remembered per test file is a guard that will
be forgotten in the next file"* — which is exactly what a per-call-site guard is. **That objection
is what produced the meta-test** ([[a-guard-remembered-per-file-is-forgotten-in-the-next-file]]).

# The lesson, and it is not "use scouts"

**"Verified" is a claim about coverage, and coverage is the thing a working session is worst placed
to judge.** The session had run the tests it wrote, and they passed. What it had not done is ask
what else was of the same kind — and *what else is of this kind* is exactly the question a store
answers and a working memory does not.

**The scouts earned their cost on correctness before they earned anything on wall clock**, and the
correctness half is the one that does not depend on the timing measurement holding
([[read-only-scouts-one-per-folder-ahead-of-the-librarian]]).

# It is the strongest evidence for the breadth reading

**A targeted read of the pages a brief named could not find a page nobody pointed at.** That is the
half of the owner's theory of the day's errors that holds
([[breadth-was-what-was-missing-and-pre-task-is-one-way-to-buy-it]],
[[pre-task-was-not-run-before-the-first-items-of-this-session]]).
