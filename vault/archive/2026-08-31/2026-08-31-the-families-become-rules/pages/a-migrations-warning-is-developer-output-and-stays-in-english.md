---
title: "A migration's warning is developer output and is written in English, and the migrations already applied are not translated"
type: decision
status: archived
authority: migration-warning-language
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-26
created: 2026-08-26
supersedes: "[[the-language-of-a-migration-warning-is-unsettled]]"
sources: ["archive/2026-08-26/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md", "migrations/versions", "tests/integration/test_migrations.py"]
tags: [process, db-schema, testing]
---

# The ruling, 2026-08-26

*(the owner selected it, against translating the old migrations and against the reading that a
migration's warning is product output.)*

**What `alembic downgrade` prints to stderr is developer output.** The language rule reaches it, so
it is written in English ([[english-in-the-repository-russian-with-the-owner]]).

**Migrations `0003` through `0007` are not translated.** The rule is forward-only and the unit is the
file ([[the-english-rule-is-forward-only-and-the-unit-is-the-file]]); a migration already applied is
history.

# What this settles

**The question this replaces was open from 2026-08-20** — is the warning owner-facing product output,
which stays Russian, or developer output ([[the-language-of-a-migration-warning-is-unsettled]]). The
measurement that page carries stands: the Cyrillic in `tests/integration/test_migrations.py` is there
because the migrations it asserts against are Russian, and `0004` alone carries 1,984 Cyrillic
characters.

**The newest migrations were already answering it in practice.** `0001`, `0002` and `0008` carry no
Cyrillic at all, and the newest tests assert against an English warning. **The practice was right and
had no ruling behind it**; this is the ruling.

# What it does not do

**The seven Cyrillic substrings in the translated test still cannot go**, because they assert against
migrations that are not being translated. That is the case the forward-only rule still does not
describe: a file can be as translated as it is allowed to be and still not be translated
([[the-migration-test-translation-stands-with-its-remaining-cyrillic]]).

**And an owner running `alembic downgrade` still sees two languages depending on the revision.** That
is accepted rather than repaired.

# Rejected

**Rejected: translating `0003`–`0007`.** It is a rewrite of applied history for no reader — the
warnings have already been printed to whoever was going to read them.

**Rejected: reading the warning as product output.** The product's Russian surface is the web page
and the CLI the owner runs; a migration's stderr is read by whoever is changing the schema.
