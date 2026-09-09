---
title: "Product work does not interleave into the vault sprint"
type: decision
status: current
authority: product-interleave
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", "sprint.md"]
tags: [process, vault]
---

# Decided 2026-08-17: the vault continues alone

**The vault continues alone until the owner decides to test it on the product.** No product slice
is interleaved into S2.

This answers the fourth of the four questions that blocked S2 from opening. **The stated default
held** — the answer is the one that was already being followed — and that is the point of having
asked it: the product has not moved since 2026-08-12, and after 2026-08-17 that is **a decision
rather than drift**.

**Rejected: interleaving a product slice to keep the application warm.** The argument against it is
the one this sprint is built on — the vault is being made usable rather than maintained, and a
sprint that is two goals is not one sprint ([[a-sprint-closes-on-its-goal]]).

## What it obliges

- **The tests and the browser walk stay unrun, correctly.** A session that changes no Python and no
  product code owes neither, and saying so explicitly is what stops the next session reading a
  missing `pytest` line as an omission.
- **The measurement the whole vault is for is still not taken.** Whether this store changes what a
  session does can only be answered against real work
  ([[the-measurement-is-whether-the-vault-changed-what-a-session-did]]), and every session spent on
  the vault alone postpones that answer.
- **The entity pages about the application still wait on the detector**, which is a different
  blocker and not this one ([[entities-describe-the-application-once-the-detector-exists]]).

## Applied again on 2026-08-18, and recorded as a decision rather than an omission

**`pytest`, `ruff check`, `ruff format --check` and the browser walk were not run**, deliberately.
Not one line of Python or template was touched in a session of four commits, all of them in
`scripts/` and the vault.

**It is written into the journal's own checks list in those words** so that the missing lines read
as this decision rather than as a lapse. That is the whole mechanism this page provides: the
default holds by being restated, and a default nobody restates becomes drift the first time
somebody asks why the suite was skipped.

**The check that was run is the one the work belonged to** — `bash scripts/vault-check.sh`, exit 0,
plus the selftest three times ([[vault-scripts]],
[[the-selftest-cost-scales-with-the-rule-pages-it-renders]]).

## Read as contradicting a vault task on 2026-08-20, and the page is not wrong

**S2's item 3 translated `tests/integration/test_migrations.py`, and the owner asked
«почему мы пошли править сам продукт? я думал мы говорим за вики».**

**The page bars product *work*, and item 3 is harness residue in a product file.** `269c877` is a
`feat(harness)` commit that changed that file by 11 insertions while building the test-database
guard ([[the-test-database-guard]]), so the file was made mixed-language **by the vault work**, and
translating it is that work's own residue rather than a product slice
([[the-english-rule-is-forward-only-and-the-unit-is-the-file]]).

**The librarian named this tension at `/pre-task`, before the work, and the reasoning stopped at
the agent boundary** — which is why the objection was re-derived one translation later
([[a-librarian-answer-that-stops-at-the-agent-boundary-is-not-an-answer-the-owner-has]]).

**Whether this page needs a clarifying line is open and is the owner's.** The evidence for one is
not that the page is wrong: it is that two readers landed in the same place, and the page's own text
does not say what to do when a vault change leaves residue inside `src/` or `tests/`.

# The clarifying line, given by the owner — 2026-08-26

*(the owner selected it.)*

**The rule forbids a product *slice*. It does not forbid a vault task that touches product files.**
A translation, a rename, a test that moves because a vault rule moved — those are vault work with
residue, and they are allowed.

**And it holds while *a* vault sprint is open, not specifically while S2 is open.** The page names S2
because S2 was the sprint of the day it was written; S2 closed on 2026-08-23 and the rule did not
close with it.

**Both halves were live misreadings rather than hypotheticals.** The page was read on 2026-08-26 as a
live `prohibition` naming a sprint that had been closed three days — one of two items on a carried
list that turned out to be rubbish
([[a-recommendation-given-without-checking-its-subject-is-delivered-like-one-that-was-checked]]).

**It is applied the same day**: the fourteen migration tests are named S4 rather than left waiting on
a Docker condition that cannot arrive inside a vault sprint
([[the-unrun-migration-tests-are-named-s4-work]]).

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*
