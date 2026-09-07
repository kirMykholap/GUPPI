---
title: "One shell, a vacancies page and a collection page, and exactly one poller on each"
type: concept
status: current
authority: shell-and-pages
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "docs/superpowers/specs/2026-08-06-shell-and-two-pages-design.md"]
tags: [web, htmx]
---

# The shell, the two pages, and who polls where

`base.html` is the shell: it holds the navigation, the profile selector and the collection
indicator. **The pages supply only `{% block content %}`** — «Вакансии» and «Сбор данных».

*(The title read "One shell, two pages, and exactly one poller on each" until 2026-08-18, and it now
names the pages instead of counting them — «Вакансии» at `/vacancies`, «Сбор данных» at `/collection`.
**They were never an inventory**: the pair is a design invariant of the product, and the section
"Two pages plus the shell is the whole planned set" below is this corpus answering, on 2026-08-14,
that nothing else was ever planned. That reasoning stood in a `quantity:` line until the field was rejected and the rule
was made unconditional in both halves
([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]],
[[a-title-names-what-is-counted-instead-of-counting-it]]). The **filename** still counts and waits
for its rename, which moves an address ([[the-title-rule-extends-to-filenames]],
[[a-page-rename-is-sed-and-verify]]).
**Closed 2026-08-19: the rename landed and the name counts nothing.** The sentence above was
written on 2026-08-18 and stood for one day; the wait is the record rather than an oversight,
because a filename is an address and the repair was scheduled as one sweep of sixteen names in a
single change, not taken by whichever session happened to open this page next.)*

Slice 3 turned the single `/vacancies` page into this, and rebuilt the tag model at the same time,
so that **«искать впредь» and «показывать сейчас» stop sharing one word**: whether a tag is
collected for is `ProfileTag.is_enabled`, whether its rows are on screen is a chip
([[tags-set-marker]]).

## The fragment addresses, renamed and added

| Route | What it is |
|---|---|
| `GET /collection/panel` | was `GET /vacancies/collection` |
| `POST /collection/start` | was `POST /vacancies/collect` |
| `GET /collection/indicator` | **new** — the compact «идёт сбор» line for the shell |
| `GET /vacancies/chips` | **new** — the chip row, which redraws itself when a run ends |

The two new ones are new rather than renamed, and the chip fragment is the first step of
[[table-refreshes-itself]].

## One poller per page, and the other one is present but inert

The indicator polls on every page **except** «Сбор данных», where the panel polls instead. Measured
on the slice 3 walk: on «Сбор данных», `/collection/panel` at 3048 and 6087 ms and **zero**
`/collection/indicator`; on «Вакансии» during a run, `/collection/indicator` at 3063 and 6108 ms and
**zero** `/collection/panel`.

**The indicator element still exists on «Сбор данных»** — a swap target must exist or htmx fails
silently ([[htmx-swap-target-invariant]]) — but it arrives without `hx-trigger` and without a line.
Presence and polling are two different things here, and the invariant only requires the first.

Polling of either kind lives exactly as long as the run does: [[polling-only-during-a-run]].

## What being two pages removed

**The tag toggle no longer carries the filter chips out of band.** The toggle lives on «Сбор
данных» and the chips on «Вакансии», so an out-of-band chip fragment could never find its target and
htmx would have written an error to the console on every toggle. Confirmed live: one
`POST /tags/<id>/enabled` per toggle, the tag caption and the collection panel changing in that one
exchange, exactly one `#collection` with none nested, and **an empty console**.

## Two pages plus the shell is the whole planned set

Asked on 2026-08-14 — *"what pages were planned in this project?"* — the corpus answers: **these
two, behind this shell, and nothing else was ever planned.** The resume editor and the AI interview
appear only as *examples of the island condition* on [[the-stack-stays-htmx]], not as a backlog;
[[collection-features-deferred]] holds four collection features deliberately not built, and a
forecast for slice 3 that did not come true.

**There is no roadmap page in this vault at all**, which is negative space worth stating rather
than a gap to fill: a page listing pages we might build would be a plan, and plans live in
`docs/superpowers/plans/`.

## Navigation is a full document load, and the profile rides on a cookie

Moving between the two pages reloads the document in both directions; `aria-current="page"` moves
with it, and `<h1>` and `<title>` follow. The profile selector's form submits to `page_path`, so its
`action` is `/vacancies` on one page and `/collection` on the other.

**The navigation links themselves are bare** — `/collection` with no parameters — so the selected
profile is carried by the cookie alone, with the consequences on [[profile-resolution]].

Where a run actually executes, and why one is enough: [[collection-runs-in-a-thread]].
