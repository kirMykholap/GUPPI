---
title: "STALE_AFTER is thirty minutes because liveness is marked once per source+tag pair, not once per request"
type: decision
status: current
authority: staleness-window
binding: prohibition
basis: code
sprint: S0
decided: 2026-08-05
created: 2026-08-13
sources: ["archive/2026-08-12/2026-08-12-handoff-before-the-vault/handoffs/2026-08-12-handoff-before-the-vault.md", "archive/2026-08-13/2026-08-13-second-brain-phase-2/handoffs/2026-08-13-second-brain-phase-2.md", "src/jobhunt/ingest/batches.py", "docker-entrypoint.sh"]
tags: [batches, collection]
---

# Thirty minutes, and the arithmetic behind it

`run_profile` calls `touch()` after each source+tag pair. Inside one pair `fetch_listings` may make
up to 41 requests — dou.ua, `max_batches=40` — each under a 30-second timeout.

**Hence `STALE_AFTER = 30 minutes`: the window must cover the longest possible pair.** If it does
not, a live run is declared dead, the next press evicts it, two threads work on one profile, and
`upsert_vacancies` — read-then-insert with no `ON CONFLICT` — drops the loser.

## How the number was wrong before, and why that matters

The window used to be **15 minutes**, justified in a comment by «25 pages against 2 s pacing —
under two minutes». **Both halves of that were wrong**: the stamp is written once per pair rather
than per page, and each request is bounded by the 30 s timeout rather than by the pacing. The real
figure is **≈ 21 minutes**, which the 15-minute window sat under.

The consequence is not cosmetic. The next run supersedes a stale batch and starts collecting, so
declaring a live runner dead puts **two threads on one profile**.

**The fix the reviewer prescribed would not have worked.** It proposed a stamp per request inside
`run_source` — but `run_source` is called once per pair, `fetch_listings` paginates inside it, and
`touch()` does not commit. Reviewing a number is not the same as reviewing the arithmetic under it.

**The old number outlived the code in a second file.** `docker-entrypoint.sh` still described
`STALE_AFTER` as 15 minutes until 2026-08-13, months after `src/jobhunt/ingest/batches.py` was
changed to 30 — found by a reviewer reading the two together, not by any test. A constant quoted in
prose is a copy, and copies drift ([[docstrings-drift-inside-their-own-commit]]).

## Why not the right form

The right form is a mark per **request**. It needs the stamp to reach the database from inside
`fetch_listings`, and today neither party can do that: `touch()` does not commit, and parsers must
not know about the database ([[normalisation-layer]]). It would take a progress signal added to the
`BaseParser` contract — a deliberate deferral, not something half-built.

## What this obliges

**If you raise `max_batches`, `max_pages` or the timeout, recompute this arithmetic.** The number
is not a round half-hour chosen for taste; it is a bound on the longest pair, and changing any of
its three inputs invalidates it.

Not a problem today: only a source answering at the edge of its timeout for dozens of consecutive
requests reaches the ceiling.

See [[batch-lifecycle]] for the other closer this rule cooperates with, and
[[sweep-runs-only-under-docker]] for the gap in the other cleanup path.
