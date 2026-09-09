---
title: "A boundary described more strongly than it is implemented is worse than no boundary"
type: lesson
status: archived
authority: boundary-overclaiming
basis: measurement
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [testing, architecture]
---

# A boundary overclaimed is worse than one absent

The wave-2 AST boundaries let through `Vacancy as V`, `models.Vacancy(...)`, `setattr`,
`update(Vacancy)` and `from urllib import request` — while the handoff stated that "no file writes
its objective fields".

**The next session would have trusted the boundary more than it was worth**, which is precisely
the damage: an absent boundary makes you careful, an overclaimed one makes you careless.

The remedy is now permanent: every boundary is documented **together with what it does not catch**.
See [[architectural-boundaries]] for the current list, including the exclusions given as a path
from the package root rather than by filename — so a new `web/upsert.py` does not slip past.

## The same shape in documentation

Documentation overclaims too, and it did so three times in this project's own records:

- an orphan pair was said to "hang in the general list" when it is in fact **hidden**;
- a saved link was said to carry `profile=` and be portable, unconditionally, when it does so only
  if the profile came from the address;
- table libraries were said to be rejected because they cannot filter server-side — **no document
  ever said that**, and several of them can, and it does not help.

Each was believed until someone compared the claim with the thing. See
[[ingest-is-units-and-verdicts]] for the check that now makes such comparisons cheap, and
[[docstrings-drift-inside-their-own-commit]] for the smallest version of the same failure.
