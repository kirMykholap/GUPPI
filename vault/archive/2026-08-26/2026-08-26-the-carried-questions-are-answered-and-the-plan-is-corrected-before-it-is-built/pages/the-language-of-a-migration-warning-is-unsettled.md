---
title: "Whether a migration's warning is product output or developer output is unsettled, and the newest migration already answers it in practice"
type: decision
status: deprecated
authority: migration-warning-language
basis: measurement
binding: deferral
sprint: S2
decided: 2026-08-20
created: 2026-08-20
superseded_by: "[[a-migrations-warning-is-developer-output-and-stays-in-english]]"
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", "tests/integration/test_migrations.py"]
tags: [process, testing, db-schema]
---

# Deferred 2026-08-20, and the deferral is what is decided

**The question:** is what `alembic downgrade` prints to stderr **owner-facing product output**,
which stays Russian, or **developer output**, which the language rule reaches? Nothing has ruled it.

**Why it came up:** the seven Cyrillic substrings left in `tests/integration/test_migrations.py` were
read as product CLI output that stays Russian
([[the-migration-test-translation-stands-with-its-remaining-cyrillic]]). **The file itself refutes
that reading**: its newest tests are already English and assert `"1 parse_batches rows are dropped"`
— an English warning — against the same `captured.err`.

## The measurement that replaced the reading

Cyrillic characters per migration, measured across `migrations/versions/`:

| migration | Cyrillic characters |
|---|---|
| `0001`, `0002`, `0008` | none |
| `0003` | 371 |
| `0004` | 1984 |
| `0005` | 1694 |
| `0006` | 1190 |
| `0007` | 325 |

**So the substrings are Russian because the migrations they assert against are Russian**, and the
policy reading was an inference laid over a historical fact
([[a-fact-about-code-was-generalised-from-its-neighbour]]).

**Rejected: settling it now by translating the migrations.** That is `migrations/versions/`, outside
the sprint item's scope, and widening a scope asks
([[narrowing-a-scope-notifies-and-widening-it-asks]]).

## The consequence of not deciding it

- **The seven substrings in the translated test cannot go**, and any future reader who greps the
  file for Cyrillic finds them without finding the reason.
- **What an owner sees running `alembic downgrade` is two languages depending on the revision** —
  English on the newest, Russian on five of the others.
- **The unit of translation is the file, and this file's remainder is pinned by other files**
  ([[the-english-rule-is-forward-only-and-the-unit-is-the-file]]). That is a case the forward-only
  rule does not yet describe: a file can be as translated as it is allowed to be and still not be
  translated.
