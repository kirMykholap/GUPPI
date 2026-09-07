---
title: "A deferred check must actually be run when its condition arrives — the Criticals of a final review came from one that was not"
type: lesson
status: archived
authority: deferred-check-discipline
basis: measurement
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [testing, process]
---

# A deferred check has to be run when its condition arrives

A snapshot test — `tests/unit/test_normalize_fixtures_snapshot.py` — runs **every** card of
**every** fixture through normalisation and pins the parsed values.

**Both Criticals of a final review were found by that one command**, and both had passed every
per-task review, because those reviews looked at a diff while the defect was only visible when
fixture met behaviour:

- `'Київ, Варшава (Польща)'` yielded the city `'Київ, Варшава'`, so a profile framed on «Київ»
  **silently discarded a Kyiv vacancy** — it never reached the database. See
  [[collection-frame-city-check]].
- `'від $1600'` yielded `(1600, 1600)` instead of `(1600, None)`: dou.ua puts the currency symbol
  before the number and it broke a word-boundary search. See [[dou-ua]] and
  [[salary-cannot-be-reparsed]].

*(The title read "A deferred check must actually be run when its condition arrives — two Criticals
came from one that was not" until 2026-08-18, and the two bullets above are where the count now
lives, as evidence rather than as a headline. **Two was a reading of one past day**, not of the
world: that review is over and its Criticals cannot become three. That reasoning stood in a
`quantity:` line until the field was rejected and the rule made unconditional over titles and
filenames alike ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]) — a number
that cannot drift still leaves the title, because the mechanism that let a page say so has been
withdrawn. The title now names the review the Criticals came from instead of counting them
([[a-title-names-what-is-counted-instead-of-counting-it]]), and that is a correction in place and
not a supersession ([[a-title-corrected-in-place-is-not-a-supersession]]).)*

## The lesson is about the ledger, not the parser

**The first of those Criticals sat in the ledger as a deferred item reading "re-check when the
parsers are connected."** The parsers were connected. The fixtures were captured. **The re-check
was never done.**

A deferred item is a debt with no due date unless its condition is written as a trigger someone
will meet. "Re-check when X" belongs next to X, not in a list nobody re-reads.

See [[a-test-green-under-any-implementation]] for the neighbouring failure — a check that runs but
proves nothing.

## Another one owed against a condition — 2026-08-20

**The 14 tests of `tests/integration/test_migrations.py` were not run.** Docker is down and the suite
hangs rather than failing ([[the-integration-suite-hangs-rather-than-failing-when-docker-is-down]]).

**The honest claim, in the words it was written in:** `ruff check` and `ruff format --check` clean
over `src tests` (88 files); `pytest --collect-only` reports **14 tests in 0.06 s**; the interpolation
set is byte-identical before and after
([[collect-only-cannot-exercise-an-assertion-message]]). **No executable statement changed — only
comments, docstrings and message strings.**

**Re-check when Docker is next up.** The trigger is a condition, not a date, and it belongs beside
the condition rather than in a brief ([[the-deferrals-of-this-session-go-onto-the-sprint]]).

**Why it matters that the claim stays narrow:** a narrow claim read as a broad one is how a hole
ships inside work already reported as verified
([[a-hole-was-shipped-in-work-already-reported-as-verified]]).
