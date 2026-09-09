---
title: "The HTTP cache empties dou's cookie jar, so collection degrades to the first page"
type: decision
status: current
authority: http-cache-side-effect
binding: prohibition
basis: code
sprint: S0
decided: 2026-08-06
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md"]
tags: [collection, data]
---

# The HTTP cache breaks dou's csrf token

With `HTTP_CACHE_ENABLED=true` the body is served from disk, **the cookie jar is never filled**,
and dou collection degrades to the first page with a warning.

dou paginates by POST to `/vacancies/xhr-load/` with a csrf token taken from a cookie
([[dou-ua]]) — and a cached body carries no `Set-Cookie`.

**Only while debugging.** Recorded because the symptom — one page of results and a warning — reads
like a parser fault rather than a cache setting.
