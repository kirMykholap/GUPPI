---
title: "A docstring drifts from its code inside the same commit, so checking it is part of the edit"
type: lesson
status: archived
authority: comment-drift
basis: measurement
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [process, testing]
---

# A comment drifts from its code inside its own commit

A re-review found **five such places in a single wave**:

- a column was renamed and the comment beside it was not;
- a number's source changed from an estimate to an exact counter, and the docstring still described
  the estimate;
- a second page limit appeared and the class documenting the limits did not know about it.

**Checking the docstrings of the functions you touched is part of the edit, not separate tidying.**
Nobody schedules a pass for it, so it never happens as a pass.

Two neighbours of the same failure, both larger:

- a **plan's code sample is a starting point, not the truth.** Over one iteration implementers
  found around twenty discrepancies in briefs: unused imports that broke the linter (five times),
  lists of files to change with no real consumer of the changed signature, incomplete `downgrade`
  steps that lost data silently, a forgotten index rename that `alembic check` catches. **If a
  sample disagrees with a test from the same brief, the test is right.**
- a **warning that always fires stops being read**, which is why the convention is `logger.info`
  with numbers for the normal outcome and `warning` only for what should not have happened — in
  particular when a condition filtered out the **whole** set. The template-level version of the
  same rule is [[name-only-non-zero-counters]].

And the smallest, most expensive form: **literals of invisible characters must be checked byte by
byte.** `_THIN_SPACES = (" ", " ", " ")` in the normalisation layer contained three ordinary ASCII
spaces under a comment claiming they were given by code point. The replacement was a no-op, and
«80 000 – 120 000 грн» parsed as `(80, 0)`. **It survived three reviews**, because the characters
are visually identical and the test case commented "narrow and non-breaking spaces" contained
ordinary ones too.
