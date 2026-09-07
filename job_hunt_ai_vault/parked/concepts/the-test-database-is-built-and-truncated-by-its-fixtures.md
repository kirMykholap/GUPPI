---
title: "The test database is created by a fixture and TRUNCATEd before every test, which is why its URL is never production's"
type: concept
status: current
authority: test-database
basis: code
sprint: S0
created: 2026-08-14
sources: ["tests/conftest.py", ".env.example", "archive/2026-08-14/2026-08-14-acceptance-and-the-shortened-claude-md/handoffs/2026-08-14-acceptance-and-the-shortened-claude-md.md"]
tags: [testing, db-schema]
---

# The suite owns its database, destructively

Written 2026-08-14 because **nothing in this vault described it** — `TEST_DATABASE_URL`,
`tests/conftest.py` and "never run the suite against the production database" lived only in the
repository's `CLAUDE.md`, and a grep over the whole wiki returned one unrelated hit. That gap is
the honest reason the rule stayed in `CLAUDE.md` when everything around it moved out
([[claude-md-is-a-map-and-four-rules]]).

## What the fixtures actually do

```
TEST_DATABASE_URL   default: postgresql+psycopg://jobhunt:jobhunt@localhost:5432/jobhunt_test
```

- **`engine`, session-scoped.** Connects to `…/postgres` with `AUTOCOMMIT`, asks `pg_database`
  whether the target exists and **creates it if it does not**, then builds every table with
  `Base.metadata.create_all`. So a fresh machine needs no setup step, and **the schema comes from
  the models, never from a migration** — the trap that costs a hand-written `ALTER TABLE` and is
  held by one test file alone: [[migrations-do-not-drift-from-the-models]];
- **`session`, per test.** Before yielding it runs `TRUNCATE TABLE "<name>" CASCADE` over **every**
  table in `Base.metadata.sorted_tables`, reversed, and commits;
- **`session_factory`** depends on `session` **not for the session but for that truncation** —
  without it, runs committed by code that commits for itself (`run_profile`) leak from one test
  into the next.

## The rule that follows, and why it cannot wait for a question

**Never run the suite against the production database.** The destructive act is not a dropped
database — the fixtures never drop one — it is `TRUNCATE … CASCADE` **of every table in whatever
database the URL names**, before every single test. Point `TEST_DATABASE_URL` at the working
database and the first test empties it, cascading through the links; there is no second chance and
no prompt.

`.env.example` names the variable with the default above, so the value is discoverable by reading
the file a newcomer copies. The suite also needs a **second** database and a second variable for
the migration checks, `MIGRATION_CHECK_DATABASE_URL` — that one *is* dropped and recreated around
each test, and it is described on [[migrations-do-not-drift-from-the-models]].

What a full run of this suite costs in wall-clock, and why a subagent runs only the tests covering
its own change: [[test-suite-wall-clock]].

## The fixture had no guard at all until 2026-08-20, and `CLAUDE.md` named the wrong mechanism

**Read at `tests/conftest.py`:** `Base.metadata.create_all` at line 31, and **no `drop_all` anywhere
in the file**. The irreversible act is `TRUNCATE TABLE "<t>" CASCADE` over every table at line 42,
before **every** test.

**The repository's `CLAUDE.md` says the fixture *"builds and drops schema"*.** The warning's force is
right and the mechanism it names is not — **and the mechanism is the half a reader checks a guard
against.** Reported as a miss; the file is the owner's and the session's to change.

**And there was no guard.** `TEST_DATABASE_URL` defaults safely to `jobhunt_test`, and until
2026-08-20 nothing asserted that the value it is *given* points anywhere but production. The guard
now exists, covers both destructive fixtures, and is enforced by a meta-test rather than by memory
([[the-test-database-guard]], [[a-guard-remembered-per-file-is-forgotten-in-the-next-file]]).

**The second destructive fixture is worse than this one** — `DROP DATABASE ... WITH (FORCE)`, under
`MIGRATION_CHECK_DATABASE_URL`, whose default name does not end in `_test`
([[migrations-do-not-drift-from-the-models]],
[[a-hole-was-shipped-in-work-already-reported-as-verified]]).

**The suite has also been shown to hang rather than fail when nothing listens on 5432**
([[the-integration-suite-hangs-rather-than-failing-when-docker-is-down]]).
