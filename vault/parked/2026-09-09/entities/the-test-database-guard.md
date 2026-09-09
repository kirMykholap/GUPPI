---
title: "The test-database guard, and the meta-test that makes it unforgettable"
type: entity
status: current
authority: test-database-guard
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "tests/db_guard.py", "tests/unit/test_db_guard.py", "tests/conftest.py"]
tags: [testing, db-schema, process]
---

# What it is

`tests/db_guard.py` — one guard for both destructive fixtures — and `tests/unit/test_db_guard.py`,
the meta-test that enforces its use. Built 2026-08-20.

**Every read of a `*DATABASE_URL` inside `tests/` goes through `require_disposable_database`.**
The rule that a fixture must never point at production has been in the repository's `CLAUDE.md`
since the beginning ([[the-test-database-is-built-and-truncated-by-its-fixtures]]) and until this
day nothing asserted it.

## Two destructive fixtures, not one

`TEST_DATABASE_URL` drives a fixture that `TRUNCATE`s every table before **every** test.
`MIGRATION_CHECK_DATABASE_URL` drives a fixture that runs `DROP DATABASE ... WITH (FORCE)` — a
strictly worse act, under a variable whose default name `jobhunt_migration_check` does not even end
in `_test` ([[migrations-do-not-drift-from-the-models]]).

**The first version of the guard covered only the first of them**, and that hole shipped inside
work already reported as verified ([[a-hole-was-shipped-in-work-already-reported-as-verified]]).

## Each caller names its own suffix

Rather than sharing one list of permitted names. So the migration check cannot reach the
truncating suite's database and vice versa — proved in both directions. A shared list is the shape
this store already records as a defect that drifts
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

## Why the meta-test and not a convention

**A guard remembered per file is a guard forgotten in the next file**
([[a-guard-remembered-per-file-is-forgotten-in-the-next-file]]). That objection came from the
corpus rather than from the session: [[test-suite-wall-clock]] already records this suite being
bitten by a guard that was opt-in where it should have been automatic.

## What was not run

The 379 integration tests, on the day the guard was written — Docker was not up
([[the-integration-suite-hangs-rather-than-failing-when-docker-is-down]]). The changed lines are
exercised by the 234 unit tests and by collection; the fixtures the 379 run through were not
functionally changed.
