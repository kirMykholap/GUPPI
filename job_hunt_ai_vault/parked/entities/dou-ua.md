---
title: "dou.ua — HTML listings, POST pagination, a csrf token from a cookie"
type: entity
status: current
authority: dou-source
basis: code
sprint: S0
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [collection, data]
---

# dou.ua

One of the two sources. What is worth knowing about it:

**It moved from RSS to the HTML listing, and the reason is a parsing failure that could not be
fixed in the feed.** The feed's title had the shape `Роль в Компанія, Зарплата, Місто` with a
**variable number of parts**, so splitting on the last comma turned the company into
«Антенор, $1000–3000, Київ» on any query that carried a salary. In the HTML the company is its own
tag. There is no way to make a variable-arity string parse reliably; the fix was to stop parsing it.

**Pagination is POST to `/vacancies/xhr-load/`, with a csrf token taken from a cookie.** Hence
[[http-cache-breaks-dou-csrf]]: a cached body carries no `Set-Cookie`, the jar stays empty, and
pagination dies after page one.

**Up to 41 requests in one source+tag pair** — `max_batches=40` — each bounded by a 30 s timeout.
That number is the input to [[stale-after-thirty-minutes]]; changing it invalidates the window.

**It lists several cities, comma-separated**, and does not say which is primary — see
[[collection-frame-city-check]].

**The currency sign precedes the number** (`від $1600`), which once broke a word-boundary search
and yielded `(1600, 1600)` instead of `(1600, None)`. See [[salary-cannot-be-reparsed]] for why
that cost a full re-parse.
