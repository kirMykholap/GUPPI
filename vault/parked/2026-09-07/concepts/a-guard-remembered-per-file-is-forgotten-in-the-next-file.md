---
title: "A guard remembered per file is a guard forgotten in the next file, so the guard is a test"
type: concept
status: current
authority: guard-enforcement-shape
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "tests/unit/test_db_guard.py", "tests/db_guard.py"]
tags: [testing, process, db-schema]
---

# The mechanism

`tests/unit/test_db_guard.py` **scans `tests/` and fails on any `*DATABASE_URL` read that does not
pass through `require_disposable_database`.** The requirement stops being remembered and becomes
mechanical ([[the-test-database-guard]]).

**A convention is enforced by whoever recalls it while writing the next file.** A test is enforced
by the suite, which is the only party present at every future edit.

# Where the shape came from

**Not from the session that built it.** [[test-suite-wall-clock]] already recorded this suite being
bitten by a guard that was opt-in where it should have been automatic, in the words *"a guard that
has to be remembered per test file is a guard that will be forgotten in the next file"* — which is
exactly what a per-call-site guard is. **That objection is what produced the meta-test**, and it
arrived from the corpus rather than from anybody's memory
([[a-hole-was-shipped-in-work-already-reported-as-verified]]).

# Each caller names its own suffix, and that is not an accident either

Rather than one shared list of permitted database names. So the migration check cannot reach the
truncating suite's database and vice versa — both directions proved. **A shared list is the shape
this store repairs by deleting rather than extending**
([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]]).

# The general form

**When a rule's cost of being forgotten is irreversible, the rule is a check and not a sentence.**
The same reasoning already put the vault's structural rules into `vault-check.sh` and the journal's
sections into a hook ([[the-journal-gate-hook]]), and it is the reason a sprint's acceptance
criteria each name a command ([[a-sprint-closes-on-its-goal]]).
