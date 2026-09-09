---
title: "The decision lifecycle is scoped by a date rather than back-filled, and the census stays owed"
type: decision
status: archived
authority: lifecycle-date-scope
binding: prohibition
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: action
target: date-scope-the-decision-fields
sources: ["archive/2026-08-30/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md", "wiki/decisions/_schema.yaml", "scripts/vault-check.sh"]
tags: [vault, record-schema, process]
---

# Context

**A prohibition of 2026-08-29 stands in the way of the whole lifecycle**: `wiki/decisions/` is
censused before its type system is changed
([[the-decisions-folder-is-censused-before-its-type-system-is-redesigned]]). **The census has never
run** — it is the decisions agent's second mode, and that mode is unexercised.

**299 decision pages sit in the folder.** Nothing about them was read as a set.

# The question

**Does the census run first, or is there a way to change the type system without touching the pages
the prohibition protects?**

# How it works after

**A dated cut.** `wiki/decisions/_schema.yaml` carries `lifecycle_from: 2026-08-30`; rule 16 judges
sections and the two lifecycle keys only on a page whose `created:` is on or after it. **The 299
older pages are untouched and are not back-filled**, so the prohibition is not crossed and the census
stays owed as work of its own.

**The two fields are declared `optional:` in the schema and made obligatory by rule 16's dated
verdict**, rather than declared `required:`. The frontmatter pass's `missing` verdict knows nothing
about dates, so `required:` would redden all 299 pages at once — and a red gate is what
`lock-the-librarian.ps1` reads as a refusal to dispatch the only writer permitted to clear it
([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]). **This is the order this file set has
already run three times**, on `basis`, `authority` and `binding`: legal first, then the fill, then the
promotion.

**What the shape costs is named rather than left to be found. It is a COHORT exemption and it does
not expire.** The older cohort never reddens again, even when a page in it is edited. Nothing in this
store had decided that case before: the nearest pages are about **per-page** declarations, which this
is not ([[a-declaration-that-silences-a-check-must-expire-or-be-re-derived]]).

**And a date was chosen over a counter for a measured reason.** An advisory carrying a debt count in
this repository does not get paid down — the region-coverage advisory read `9 of 15`, then `9 of 17`,
across weeks with nothing acted on
([[an-advisory-carrying-a-debt-count-does-not-get-paid-down]]).

# Recommendation

**Date-scope now and census later**, against running the census first. The session put both and
recommended this one; the census would have blocked the whole lifecycle behind work nobody had
scheduled.

# Ratification

**The owner selected it**, against running the census first: «Case 3: Принимаю твою рекомендацию».

**The `optional:`-not-`required:` half is the session's own reading of the tree**, resolved without
asking and written into the schema with its ground — one of five such forks that day, each now owed a
look in a `git diff` rather than a question.

**Built on 2026-08-30.**

# What the dated cut did not buy, and it is the class this store keeps paying for

**The design still shipped a verdict that could never be cleared, and `/pre-task` caught it**
([[a-verdict-that-cannot-be-cleared-survived-a-third-full-design-pass]]). A date scopes **which pages**
a rule ranges over; it says nothing about whether **every page in that range** has an action that turns
the verdict green. Those are different questions and only the second one has ever bitten here.

*(Compiled from `raw/handoffs/2026-08-30-a-decision-declares-its-target-and-the-reply-gets-a-form.md`.)*
