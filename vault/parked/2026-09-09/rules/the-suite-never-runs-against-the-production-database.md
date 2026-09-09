---
title: "The test database comes from `TEST_DATABASE_URL`, and the suite never runs against production"
type: rule
status: current
governs: CLAUDE.md
render: region
basis: human
sprint: S2
created: 2026-08-17
sources: ["CLAUDE.md", "tests/conftest.py", "[[the-test-database-is-built-and-truncated-by-its-fixtures]]", "[[claude-md-is-a-map-and-four-rules]]"]
decided_by: [[claude-md-is-a-map-and-four-rules]]
tags: [harness, testing, db-schema]
---

# What travels

<!-- text -->
**The test database comes from** `TEST_DATABASE_URL` (see `tests/conftest.py`) and is created
by the fixture. **Never run the suite against the production database** — the fixture builds
and drops schema, and there is no second chance.
<!-- /text -->

**That is rule 1 of the repository's `CLAUDE.md`, to the word.** The migration changed its form and
nothing else: it was the first item of a numbered list and is now three unindented lines, because a
marker stands alone at column zero and an ordinal shipped inside a rule page would drift as the
rules around it move ([[the-owner-decides-how-a-slice-is-executed]]).

**The slice was diffed against the file, not read against it.** The three lines were cut out of
`CLAUDE.md` by line number, the ordinal and the list indent were stripped mechanically, and the
result was compared byte for byte with what the marks above enclose. **Rewording a rule while moving
it would be a change nobody decided**, and it would be invisible in the diff of a migration that is
supposed to be a move.

Everything below this line stays on this page — that is the whole mechanism
([[what-travels-from-a-rule-page-is-a-marked-slice]]).

# Why it cannot wait for a question

**The window is one test, not one suite.** The per-test `session` fixture runs
`TRUNCATE TABLE "<name>" CASCADE` over every table in `Base.metadata.sorted_tables` *before* it
yields, so a `TEST_DATABASE_URL` pointing at the working database is emptied by the first test that
asks for a session, cascading through the links, with no prompt and nothing to undo
([[the-test-database-is-built-and-truncated-by-its-fixtures]]).

The admission test for the four rules that stayed in that file is a single sentence — **obeying them
late is the same as not obeying them at all** ([[claude-md-is-a-map-and-four-rules]]). For this one,
*late* is measured in seconds.

## Where the corpus is more precise than the rule's own wording

**The text says the fixture "builds and drops schema"; the fixtures build and truncate.** `engine`
creates the database if it is absent and calls `Base.metadata.create_all`; `session` truncates. A
database *is* dropped and recreated around each test, but by the migration check and under a second
variable, `MIGRATION_CHECK_DATABASE_URL` ([[migrations-do-not-drift-from-the-models]]).

**The wording is not corrected here, and must not be.** What travels is what the file says today;
this migration is a move. The imperative is unaffected either way — a truncation of every table is
as unrecoverable as a drop — and the exact mechanism is one link away.

# What the admission test says about it

`tests/conftest.py` holds **how** the test database is built, and holds it well enough that the
concept page was written from the code. **Nothing holds the imperative half.** *Never point it at
production* is an instruction about a value that arrives from outside the tree — an environment
variable, or `.env` — and a fixture reading `TEST_DATABASE_URL` cannot ask whether the URL it was
handed is the one somebody's data is in. It would do exactly as it was told and report green.

So the rule is half-mechanised: the fixture is the *how*, and the *never* has no holder but a
reader. That is precisely the folder's admission test — imperative, and not enforced by a test
([[rules-becomes-a-type-of-its-own]]).

**One reason this rule stayed in `CLAUDE.md` has since expired, and it is worth saying so.** At the
cut of 2026-08-14 it was there partly because *nothing in the vault described it at all*; the
concept page closed that gap the same day ([[claude-md-is-a-map-and-four-rules]]). What keeps the
text in front of a reader now is the lateness criterion alone, which is exactly what the injector
delivers on.

# Where it renders

`governs: CLAUDE.md` — the repository's own file, written as a path from the repository root and
resolved against nothing else ([[governs-is-a-path-from-the-repository-root]]). The text lands in a
paired comment named for this page's slug ([[a-region-is-a-paired-comment-named-for-a-rule]]), in a
file on its way to being a dispatch table ([[the-repository-claude-md-becomes-a-dispatch-table]]).

**The page and its region belong in one change, and this page arrived first.** The librarian writes
`wiki/`; the region and the injector run are the session's, in the same commit. Until then rule 12
reports this rule as governing a file that carries no region for it, which is the expected state of
a half-finished migration rather than a defect in the page. If the rule is ever replaced, the
successor renders and this page does not ([[a-deprecated-rule-does-not-render]]).

> [!CAUTION] CONTRADICTION
> **The gate is red on a second line, and that one is not about the missing region.** This page is
> one of several current rules governing `CLAUDE.md`, and `governs:` is required to be unique across
> current rules, so `vault-check.sh` prints *two current rules govern the same destination:
> `CLAUDE.md`*. The injector renders them all into that file without complaint — measured.
> Unresolved, and not the librarian's to choose:
> [[a-deprecated-rule-does-not-render]] carries the measurement, [[rules-becomes-a-type-of-its-own]]
> carries the migration it collides with.

> [!NOTE] RESOLVED BY THE OWNER, 2026-08-17
> **The uniqueness went out of the check, and the migration stands.** At `e478c19` the owner removed
> `governs:` uniqueness from `scripts/vault-check.sh`, on the first day it met a real tree: it was
> stricter than the schema it guarded, which says a rule names the one destination *its own* text
> goes to and says nothing about a destination taking one rule. What it appeared to protect is held
> by verdicts that read the tree instead — one slug marking two regions in one file, and a region
> sitting in a file its rule does not govern — and its selftest case **flipped rather than
> disappearing**: two rules on one file with two regions is now asserted green. The gate no longer
> prints that line. The block above is left standing as the record of the alarm that produced the
> decision, which is the point of marking rather than choosing
> ([[ask-before-weakening-or-working-around-a-rule]]).

# The mechanism and the prohibition are different pages

[[the-test-database-is-built-and-truncated-by-its-fixtures]] answers `authority: test-database` —
what the fixtures do, which variable names what, and what the second database is for. This page
carries only the instruction, and carries `governs:` instead of an `authority:`, so the pair does
not read as two answers to one question ([[rules-becomes-a-type-of-its-own]]).
