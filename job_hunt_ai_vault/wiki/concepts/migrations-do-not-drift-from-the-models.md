---
title: "Migrations are not allowed to drift from the models, and only one test file can tell"
type: concept
status: current
authority: migration-drift
basis: code
sprint: S0
created: 2026-08-13
sources: ["tests/integration/test_migrations.py", "migrations/env.py", "alembic.ini", ".env.example", "archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md"]
tags: [db-schema, testing, architecture]
---

# The schema has two descriptions, and they must agree

The database is described twice: by the ORM models in `src/jobhunt/db/models.py`, and by the
Alembic revisions in `migrations/versions/` (`0001` … `0008` on 2026-08-13). Production is built
from the second — `docker-entrypoint.sh` runs `alembic upgrade head` before the app starts.

**Nothing else in the suite compares them.** `tests/conftest.py` builds the test database with
`Base.metadata.create_all`, so the models are asked about themselves: change a model without
writing a migration and all ~600 tests still pass, while the container that applies migrations
gets a schema without the column. The test for `parse_batches` says it plainly of its own
subject — the partial unique index is checked on a migrated database rather than through the
model, because "совпадение модели с собой ничего не говорит про то, что накатится на боевую".

## What holds it: `tests/integration/test_migrations.py`

Fourteen tests, of three shapes:

- **`alembic upgrade head` on an empty database, then `alembic check`.** The comparison is
  configured in `migrations/env.py` with **`compare_type=True` and `compare_server_default=True`**,
  in both the online and the offline path — without the second, a changed default is drift the
  check does not see.
- **A round trip per revision, from 0004 onwards**: `upgrade head` → `downgrade <previous>` →
  `upgrade head` → `alembic check`. It exists because `downgrade()` used to be called by nothing,
  so a downgrade that half-worked — one that creates the same index twice on the second upgrade —
  was invisible. Revisions 0001–0003 predate the rule.
- **Downgrade fidelity and data preservation.** The shape of the schema at 0003, 0004 and 0005 is
  written out as explicit table and column sets, **derived from the migration files rather than
  from the models**, because `alembic check` can only compare against head. These tests also assert
  that a migration **announces on stderr what it destroys or folds together** — the pair a
  downgrade drops, the disabled tag it hands back, the number of links a cascade would take, the
  duplicate roles an upgrade collapses into one, stray data in a column about to be dropped —
  captured with `capsys`.

## The second database, and the variable nothing names

Every one of these tests runs against a scratch database of its own:

```
MIGRATION_CHECK_DATABASE_URL
  default: postgresql+psycopg://jobhunt:jobhunt@localhost:5432/jobhunt_migration_check
```

The `migration_check_db` fixture drops it (`DROP DATABASE … WITH (FORCE)`) and creates it again
around **each** test, so a previous run cannot make the next one pass. The URL reaches Alembic
through `cfg.attributes["sqlalchemy.url"]`, which `migrations/env.py` prefers over
`settings.database_url` — that indirection is what keeps a migration check off the production
database.

**Nothing in the arrival path named that variable.** It was not in `.env`, not in `.env.example`,
not in `docker-compose.yml`; it existed only as this file's own default. A machine whose Postgres
is not at those credentials fails this file and no other, and the failure reads as a broken test
rather than as a missing environment. Setting it is part of running the suite, not part of running
the app.

**Half fixed on 2026-08-13: `.env.example` now names it**, with the default above, so the variable
is discoverable by reading the file a newcomer copies. `docker-compose.yml` still does not, and
does not need to — these tests never run in the container.

## Where this sits among the other boundaries

[[architectural-boundaries]] lists the seven rules an AST test can hold. This one is not of that
kind — it is a rule about two artefacts agreeing at runtime, and the only way to check it is to
build the schema both ways and diff them. That is why it costs a database and 14 tests instead of
a `grep` over imports.

The cost of not having it has been paid once already: a hand-written `ALTER TABLE` during slice 2b
([[test-suite-wall-clock]], which carries the timing this file adds to). And 0008's round trip has
a second role its neighbours do not — it is the only place the partial unique index that permits
[[collection-runs-in-a-thread]] one `running` batch per profile is checked as the migration
actually creates it, rather than as the model declares it.

## Its database is now guarded, and this page is what found that it was not — 2026-08-20

**`MIGRATION_CHECK_DATABASE_URL` runs `DROP DATABASE ... WITH (FORCE)`.** When a test-database guard
was built for `TEST_DATABASE_URL`, this variable was left out — and **this page is what a read-only
scout named as the record of the second variable's existence**
([[a-hole-was-shipped-in-work-already-reported-as-verified]],
[[read-only-scouts-one-per-folder-ahead-of-the-librarian]]).

Both destructive fixtures now read their URL through `require_disposable_database`, and **each names
its own suffix** rather than sharing a list, so the migration check cannot reach the truncating
suite's database and vice versa ([[the-test-database-guard]]).

**`jobhunt_migration_check` does not end in `_test`**, which is why a suffix rule written for one
fixture did not fit the other and why the guard takes the suffix from its caller.
