---
title: "The integration suite hangs rather than failing when the database is not up"
type: lesson
status: archived
authority: suite-hangs-without-a-database
basis: measurement
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "tests/conftest.py", "CLAUDE.md"]
tags: [testing, process, db-schema]
---

# Measured 2026-08-20

**Docker Desktop was not running, nothing listened on 5432, and `pytest` hung on a connection
attempt with no timeout for over 420 seconds** — against the `~75 s` for the whole suite that
`CLAUDE.md` records. It was killed rather than finishing.

**It does not fail. It waits.** There is no connect timeout on the path, so an unavailable database
is indistinguishable from a slow one until somebody decides how long is too long.

# What was salvaged, and how

**The 379 integration tests were not run and the reason is the environment rather than the code.**
Two things were established without a database:

- **`tests/conftest.py`'s changed module level is exercised by all 234 unit tests**, which passed.
- **`tests/integration/test_migrations.py` is exercised by collection**, which reported
  **379 tests collected** without connecting.

**The fixtures those 379 run through were not functionally changed.** That is the claim being made,
and it is narrower than *the suite passes* on purpose
([[the-test-database-is-built-and-truncated-by-its-fixtures]]).

# The practical rule

**Check that the database is up before starting the suite**, because the failure mode is a lost
seven minutes rather than an error. `docker compose up -d --build` is one command and the suite is
seventy-five seconds; the asymmetry is the whole argument.

**And say which tests did not run.** A handoff that reports *tests pass* over a suite that never
connected is the same class of claim as a guard reported as verified with half its surface uncovered
([[a-hole-was-shipped-in-work-already-reported-as-verified]]).

**Not the same lesson as [[test-suite-wall-clock]]**, which is about contention when the database
*is* up.

# It errored at setup this time instead of hanging, and the difference was not read — 2026-08-26

**`make test` was attempted with the database down and every test errored at setup**, rather than
waiting on a connection as the 2026-08-20 reading records. **The run was killed before `pytest`
printed its `ERRORS` block**, so *why* each test errored was never displayed.

**So the cause is inferred and not read.** It is consistent with this page — no database, fixtures
cannot build the schema — and it is *not the same observation*: an error at setup and a 420-second
wait are different behaviours, and nothing here explains which conditions produce which.

**What this costs is exactly what the page's own practical rule is about.** The suite did not run,
and *the suite did not run* is what the handoff says rather than anything about the product's state
([[a-hole-was-shipped-in-work-already-reported-as-verified]]).

**Re-running it with the database up is the first work of the next session**, and it is what turns
the inference above into a reading. Until then this section is testimony about one killed run and
nothing more ([[a-question-asked-is-not-a-question-answered]]).
