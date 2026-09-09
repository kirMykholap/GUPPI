---
title: "An absent value never overwrites a known one, and a snippet never overwrites a full description"
type: concept
status: current
authority: field-overwrite-rules
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [data, collection]
---

# An absent value never overwrites a known one

Two applications of one principle: **we record what the site said, and silence is not a statement.**

## Descriptions

When `description_is_full = true` the incoming snippet is ignored entirely.

The reverse transition — pulling the full text in over a snippet — **does not count as a change of
description**: that is our own refinement, not an edit by the employer. Snippet replaced by a
different snippet does count.

Held by tests in `tests/integration/test_upsert.py`. The rule is correct today but describes a case
ordinary collection cannot produce: nothing in production code calls `fetch_description`, so
`description_is_full=true` has no producer. See [[description-is-full-has-no-producer]].

## Dates

`posted_at` is updated on every encounter — the site puts the card's *update* date there, not the
date of first publication — but `None` never overwrites a stored date. "We failed to parse a date
this time" is a gap in our data, not a statement by the site.

There is nothing to restore an overwritten date from: the schema keeps no raw date string, unlike
`location_raw`. That asymmetry has a cousin: see [[salary-cannot-be-reparsed]].

A related display quirk about dates, deliberate and cosmetic: [[the-collection-panel-shows-local-time-and-the-posted-at-column-does-not]].
