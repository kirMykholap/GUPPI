---
title: "A correction note is dated the day the text became false, not the day the session ran"
type: decision
status: archived
authority: correction-note-date
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-19
sources: ["archive/2026-08-19/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys/handoffs/2026-08-19-the-corpus-stops-counting-and-the-gate-learns-its-keys.md", "job_hunt_ai_vault/index.md"]
tags: [record-schema, vault, process]
---

# Decided by the owner on 2026-08-19

> **owner: the correction note's date is the date the text became false**, not the date of the
> session.

This corpus corrects in place rather than by supersession wherever the claim has not changed
([[a-title-corrected-in-place-is-not-a-supersession]]), and every such correction carries a date —
*"This line read X until 2026-08-18"*, *"Two clauses of the paragraph above went false on
2026-08-18"*. The question the ruling answers is **which** date that is, and nothing had said.

# What produced it: one session, spanning midnight

The session of 2026-08-19 opened at **23:31 on 2026-08-18** and ran across midnight. Its corpus
retitles falsified their pages before midnight and its rename sweep falsified addresses after, so
**one session's notes legitimately carry two different dates** — the retitle notes read 2026-08-18
and everything from the sweep onward reads 2026-08-19.

Under the rejected reading, every note of that session would have carried one date and the reader
would be told that a page went false hours after it actually did.

# The ground

**A dated note is evidence about the world, not a record of who was at the keyboard.** Its whole use
is to let a later reader ask *what was true when this was written* — which is the same question
`decided:` answers for a decision, and `decided:` already takes the day the ruling was given rather
than the day it was compiled ([[the-frontmatter-core-is-fixed-and-updated-joins-it]]). Git records
who wrote what and when, and records it better.

**Rejected: the session's date, one per session.** It is cheaper to apply and it is wrong exactly
when a session is long — which is when a corpus-wide sweep happens, which is when the notes are
written.

# What it obliges

**A note names the day its subject became false.** Where that day is not knowable, the note says so
rather than guessing; a wrong date on a correction is worse than no date, because it is checkable and
nobody checks it.

**It does not change `created:` or `sprint:`.** Those are properties of the page, taken when the page
is written. This rule is about the dated clause inside a body, and about nothing else.
