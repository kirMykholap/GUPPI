---
title: "The collection features deliberately not built are the banner, the schedule, resumption and cancellation"
type: decision
status: current
authority: collection-deferrals
binding: deferral
basis: human
sprint: S0
decided: 2026-08-05
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [collection, process]
---

# Four collection features deliberately not built

Deferred during slice 2b, each with a reason rather than an oversight.

| Not built | Why, and what it would take |
|---|---|
| the «условия изменились» banner | needs a snapshot of the tags and the frame taken at run time — there is nothing to compare against today |
| a schedule | the day a schedule is wanted is the day a job queue becomes worth its cost. See [[restart-interrupts-a-run]] |
| resuming an interrupted run | the same: durable, re-entrant position is a queue by another name |
| cancelling a run from the page | not attempted |

*(The title read "Four collection features deliberately not built: the banner, the schedule,
resumption and cancellation" until 2026-08-18, and the table above is the list it was counting.
**The count was of the page's own set** — the features were enumerated in the title itself, so
nothing outside the page could arrive and make the number wrong; a fifth deferral would make the
page incomplete rather than stale. That argument stood in a `quantity:` line until the field was
rejected and the rule made unconditional over titles and filenames alike
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]), which withdrew the only way a
page had to declare itself exempt. The title now names the features instead of counting them
([[a-title-names-what-is-counted-instead-of-counting-it]]). **The heading above still counts**, and
is left as it is: rule 10 reads the title and the filename, and the owner has not extended it to
body headings. Not a supersession ([[a-title-corrected-in-place-is-not-a-supersession]]).)*

## A forecast that turned out wrong, kept because the correction matters

The handoff paragraph that recorded these deferrals also forecast slice 3 as «adding and removing
tags from the browser, web forms for the profile and the collection frame».

**Slice 3 did none of that.** It built the shell, the two pages and the tag model — and it made
browser tag management *harder* to reach rather than nearer, because `tag remove` now refuses even
from the CLI. See [[no-soft-delete-for-tags]].

Web forms for the profile and the collection frame remain unbuilt and unplanned.
