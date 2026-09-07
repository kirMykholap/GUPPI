---
title: "Rules the vacancy list keeps: one PAGE_SIZE, one filter builder, an explicit tie-breaker, and empty strings that are not defaults"
type: concept
status: current
authority: vacancy-list-rules
basis: code
sprint: S0
created: 2026-08-13
sources: ["CLAUDE.md", "archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [filters, data]
---

# Rules the vacancy list keeps

**`PAGE_SIZE = 50` is defined once**, in `web/data/vacancies.py`. Never repeat the literal.

**Both `/vacancies` handlers build their filters through `_load_page`**; neither constructs
`VacancyFilters` itself. One builder means one place where a new filter has to be understood.

**String query parameters pass through `_or_none`.** A cleared form field arrives as `""`, which
filters like the default but does **not** compare equal to it — so a cleared field and an absent
one must be normalised to the same thing deliberately, not by accident.

**Ordering always carries an explicit tie-breaker.** PostgreSQL's `now()` is constant within a
transaction, so rows created together share a timestamp; without a tie-breaker their order is
whatever the planner felt like, and pagination silently repeats or drops rows.

**`applied_at` is never backdated.** If «звонок» is marked without «откликнулся», the field stays
empty — otherwise we invent an application event that never happened.

**The filters form names the sources of its trigger.** With a bare `hx-trigger="change"` on the
form, blurring the search field produced `htmx:trigger from FORM` and a **second** request for the
same state. Narrowing it to `change from:(#filters select, #filters input[type=checkbox])` makes
blur produce nothing. `test_filter_form_does_not_fire_on_a_bubbled_change` was verified by removal:
on the old markup it fails.

**A status change answers with the cell and nothing else** — `<select` is in the response, `<tr` and
`<html` are not. The two error paths differ deliberately, and the difference is visible on screen:

| Situation | Answer | What the cell shows |
|---|---|---|
| the pair no longer exists | 404 | a message, and **the `<select>` disappears** — there is no pair, so there is nothing to put in it |
| the status value is not allowed | 400 | a message, and **the `<select>` stays**, showing the truly stored status |

The vanishing select on the 404 path is a consequence, not a defect, and the message itself asks for
a reload.

See [[vacancy-query-tag-condition]] for where a new condition may and may not be added, and
[[tags-set-marker]] for why an orphan pair is hidden by default.

The status values themselves are identifiers rather than copy — see [[statuses-stay-english-identifiers]].

One thing the ordering does *not* read is the pair's own dates — see [[sorting-reads-objective-dates-only]].
