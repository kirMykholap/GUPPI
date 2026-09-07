---
title: "The English rule is forward-only and the unit of translation is the file"
type: decision
status: archived
authority: english-migration-method
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "CLAUDE.md", "tests/conftest.py"]
tags: [process, testing, architecture]
---

# Ruled 2026-08-20 by the owner

> «Мы переводим русский текст постепенно, когда наткнемся на него и увидим проблему, которую он
> создает.»

**So `CLAUDE.md`'s language rule does not reach back over existing code as an obligation.** It
applies when a file is touched and its Russian becomes a problem. **The unit is the file**, not the
line and not the repository.

**And the half that stops "gradually" from meaning "never": a file too large to translate in the
same change goes onto `sprint.md` rather than into silence.**

## What produced it

Adding the test-database guard to `tests/conftest.py` put English code beside three Russian
docstrings, **written to the rule rather than to its neighbours**, and left the file visibly saying
two things at once ([[the-test-database-guard]]). The question raised was whether the rule reaches
back or the existing docstrings are grandfathered; the ruling is neither, exactly.

**Rejected: leaving the file mixed and unrecorded**, and rejected: a sweep of the repository as a
task of its own.

## Executed and deferred on the day it was ruled

- **`tests/conftest.py`** — six Cyrillic lines to zero.
- **`tests/integration/test_migrations.py`** — 206 Cyrillic lines of 951, too large for the same
  change, so it went onto `sprint.md`. The file is mixed-language by that session's own hand, eight
  English lines above them.

## What it changes about the standing refusal

**It narrows [[migrating-the-repository-to-english]] from a standing refusal into a standing
method.** The proposal's answer was *not as a project*; the answer now is *as a by-product of
touching the file, with the remainder written down*.

## The deferred file was translated on 2026-08-20, and it did not go to zero

**`tests/integration/test_migrations.py` — 59 replacements, 191 insertions against 190 deletions.**
Comments, docstrings and assertion messages went to English. **Cyrillic remains, on the owner's
ruling and on the merits** ([[the-migration-test-translation-stands-with-its-remaining-cyrillic]]).

**Two things this ruling did not anticipate, both found in that one file:**

- **A file's remainder can be pinned by other files.** Seven surviving substrings are asserted
  against what five untranslated migrations print, so the unit is the file and the file cannot
  finish alone ([[the-language-of-a-migration-warning-is-unsettled]]).
- **A translation is exactly the change `--collect-only` cannot check.** An assertion message
  evaluates only on failure, so a broken f-string in one passes collection, `ruff check` and
  `ruff format --check` alike ([[collect-only-cannot-exercise-an-assertion-message]]).

**And the other half of the rule — a file too large goes onto `sprint.md` rather than into
silence — has its next candidate measured**: `tests/integration/test_cli.py` carries **298 Cyrillic
lines and 34 Russian test function names**, which the sprint does not name
([[migrating-the-repository-to-english]],
[[a-grep-that-prints-one-line-is-a-report-about-the-first-match-and-not-a-count]]).
