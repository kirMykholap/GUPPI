---
title: "Every htmx swap target must exist in the rendered page, and the check strips script blocks on the declaration side and the presence side"
type: concept
status: current
authority: swap-target-invariant
basis: code
sprint: S0
created: 2026-08-13
sources: ["CLAUDE.md", "archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [htmx, testing]
---

# Every swap target declared must exist in the page

**A missing target makes htmx skip the request silently** — nothing on screen, nothing in the
network panel. The invariant lives in `tests/integration/test_web_vacancies.py`.

## The defect that produced it

On an empty list the filters were dead, silently. `<tbody id="rows">` sat inside `{% if rows %}`
while the form, the chips and the search all targeted `#rows`. No rows, no target, and htmx raised
`htmx:targetError` without sending anything. For a profile with every tag disabled, the
"вакансии выключенных тегов" checkbox — the remedy that state exists for — did nothing.

The other half of the same bug: narrowing a filter to zero left the table header with no
explanation, because all four empty-state messages lived in `vacancies.html` while htmx swaps
`_rows.html`.

## Checked per page

The web layer has two pages ([[one-shell-the-vacancies-and-collection-pages-and-one-poller-on-each]]), so the invariant is checked **per page**. `OOB_TARGETS_BY_PAGE` says
which out-of-band targets each page owns, and a second assertion requires the union of those sets
to equal the out-of-band targets found across all templates — so a new `hx-swap-oob` cannot be
added without a page claiming it. A third test parametrises over the map's keys, so a key cannot
be declared without being exercised against a real request.

## The strip is load-bearing, not tidy

The invariant strips `<script>` blocks on **both** the declaration side and the presence side.
`base.html` discusses `<div id="collection">` in prose inside a script comment, and for a slice
and a half the id search found that prose and counted the target as satisfied on every page.
**The invariant that exists because htmx fails silently was itself failing silently.** Do not
delete either strip — assertions pinned to them go red if you do.

*(The title read "Every htmx swap target must exist in the rendered page, and the check strips
script blocks on both sides" until 2026-08-18, and the paragraph above names the two sides it was
counting. **They were never a count of the world**: a comparison has a declaration side and a
presence side because that is what a comparison is, and a third side would make this page wrong
rather than stale. That reasoning stood in a `quantity:` line until the field was rejected and the
rule was made unconditional in both halves
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]); the title now names the two
sides instead of counting them ([[a-title-names-what-is-counted-instead-of-counting-it]]).)*

That trap is general, not htmx-specific: see
[[an-example-inside-a-code-block-satisfies-a-search]].

The same silence in the other direction — a swap that destroys the element which would have made the next request — is [[error-swap-gated-on-content-type]].
