---
title: "`pytest --collect-only` cannot exercise an assertion message, and neither can `ruff`"
type: concept
status: current
authority: collect-only-blindspot
basis: code
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer/handoffs/2026-08-20-the-lock-fires-and-deadlocks-the-vaults-only-writer.md", "tests/integration/test_migrations.py"]
tags: [testing, process]
---

# The mechanism

**An assertion message evaluates only when its assertion fails.** So a malformed f-string inside one
is invisible to:

- `pytest --collect-only`, which imports the module and never runs the body;
- `ruff check`, which does not evaluate;
- `ruff format --check`, likewise.

**All three pass.** The defect surfaces first on the day a test fails for a real reason — the worst
possible moment for a second defect, because the message that was supposed to explain the failure is
the thing that breaks ([[a-test-that-fails-for-its-own-reasons-proves-nothing]]).

# Where it bites hardest, which is exactly where it was met

**A comment-and-message translation.** Collect-only is the accepted salvage on a Docker-less tree
([[the-integration-suite-hangs-rather-than-failing-when-docker-is-down]]), and a translation that
touches no executable statement looks like precisely the change collect-only is sufficient for.
**It is not**, because the strings a translation rewrites are the strings collect-only cannot reach
([[the-migration-test-translation-stands-with-its-remaining-cyrillic]]).

# The instrument that closes it

**An `ast` pass, run before and after**: every `FormattedValue` expression with its conversion and
format spec, plus every plain string carrying a literal brace, compared as a set with line numbers
stripped because they move. **28 interpolations, byte-identical as a set.**

**It was named by the librarian at `/pre-task`, not by the session**, and the answer to it is a
mechanism rather than care ([[a-gap-named-by-a-reviewer-is-closed-by-a-mechanism-rather-than-by-care]]).
