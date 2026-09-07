---
title: "The end of a collection resets the chip row, and showing what was collected beats preserving the manual choice"
type: decision
status: current
authority: chip-state-after-collection
binding: prohibition
basis: human
sprint: S0
decided: 2026-08-06
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [filters, tag-model]
---

# The end of a collection resets the chip row

When a run finishes, «Вакансии» first redraws the chip row — `GET /vacancies/chips`, a fresh
`list_filter_tags` and a default `VacancyFilters()` — and only then re-requests the rows. Every
chip returns to the state inherited from `ProfileTag.is_enabled`, exactly as on an ordinary page
open.

**A chip cleared by hand does not survive a run, and this is visible on screen.**

## Why, rather than "leave the chips as they are"

The server cannot tell "the user cleared this chip" from "this chip did not exist when the page was
drawn" — a form submits only its checked boxes. See [[tags-set-marker]].

So a tag that found its first vacancy **during** the run had no chip, was not sent in the refresh
request, and its new rows would be filtered out of the very table that had just refreshed in order
to show them.

**The owner's decision: showing what was collected matters more than preserving the manual chip
selection.** Raised by slice 3's final review, `dd1b446`.

## What was rejected

A richer marker carrying the whole rendered set. That is a change to the filter model, not a fix to
a defect, and it was not worth it for this.

See [[table-refreshes-itself]] for the chain that produces this behaviour.
