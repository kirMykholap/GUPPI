---
title: "Politeness to a job site is counted per process, so profiles collecting at once each knock at the full rate"
type: decision
status: current
authority: request-politeness
binding: prohibition
basis: code
sprint: S0
decided: 2026-08-05
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "docs/superpowers/specs/2026-08-05-collection-from-the-browser-design.md"]
tags: [collection, architecture]
---

# Politeness is counted per process

Collection from the browser and `jobhunt parse` from the host each have their own `HttpClient`,
their own pauses between requests, and their own caches of `robots.txt` and HTTP.

**Profiles are independent by construction** — spec §7 — so two collections of different profiles
can run at the same time and knock on work.ua twice as often as either believes it is doing.

*(The title read "Politeness to a job site is counted per process, so two profiles collecting at
once knock twice as often" until 2026-08-18, and the paragraph above is the scenario it was
describing. **Neither number counted anything that exists**: two profiles was the illustration and
"twice as often" was what followed from it — a third profile knocks three times as often by the
same arithmetic, so nothing arriving in the world could make the title stale. That argument stood
in a `quantity:` line until the field was rejected and the rule made unconditional over titles and
filenames alike ([[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]), which
withdrew the only way a page had to declare itself exempt. The title now states what per-process
counting does to any number of runs at once, instead of pricing one of them
([[a-title-names-what-is-counted-instead-of-counting-it]]). Not a supersession
([[a-title-corrected-in-place-is-not-a-supersession]]).)*

Slice 2b did not create this, but it made it noticeably easier to hit: before, you had to open two
terminals; now one press and one terminal suffice.

**It will show up only with a second profile, or when collecting from the browser and the terminal
at once.** Recorded rather than fixed, because a shared rate limiter needs a home that outlives
both processes, and today nothing has one.

See [[collection-runs-in-a-thread]] for why the browser run is a separate process context at all.
