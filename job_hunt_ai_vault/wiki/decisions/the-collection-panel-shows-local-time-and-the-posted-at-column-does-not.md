---
title: "The collection panel shows local time and the «Обновлена» column does not"
type: decision
status: current
authority: time-display
binding: prohibition
basis: code
sprint: S0
decided: 2026-08-06
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "src/jobhunt/web/templates/_collection.html"]
tags: [web, data]
---

# Two different clocks on one page

The collection panel converts to local time with `.astimezone()`; the «Обновлена» column prints
`posted_at` as it is.

It barely touches anything — `posted_at` arrives as a date without a time — but **around midnight
the column and the panel can name one moment as different days**.

Cosmetic, found by a final review, accepted. Recorded so the discrepancy is not chased as a
timezone bug in the parser.

## Where the `.astimezone()` came from: the panel printed UTC

The columns are `timestamptz` and arrive as **aware** UTC datetimes, and `strftime` on an aware
datetime prints **its own zone** rather than converting. The owner was shown «05.08 17:06» for a run
his own clock had at 20:06.

**This is the only place the interface shows a time of day** — the table prints dates only — so
nothing else was affected. Fixed with `TZ: Europe/Kyiv` on the app service in `docker-compose.yml`
plus `.astimezone()` before both `strftime` calls in `_collection.html`; verified afterwards, 20:16
on the wall clock rendering as «05.08 20:16».

**It changes no logic, and that is worth knowing before anyone removes it as suspicious:** every
clock read in the code is an explicit `datetime.now(UTC)` and `func.now()` is server-side, so `TZ`
reaches only `.astimezone()` and the container's log timestamps.
