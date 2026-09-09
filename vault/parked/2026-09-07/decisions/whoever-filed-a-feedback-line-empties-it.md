---
title: "Whoever filed a feedback line is the ritual that empties it"
type: decision
status: current
authority: feedback-drain-ownership
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-22
created: 2026-08-22
sources: ["archive/2026-08-22/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict/handoffs/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict.md", ".superpowers/sdd/vault-feedback.md"]
tags: [process, vault, harness]
---

# The ruling, 2026-08-22

**Owner selected: the drain belongs to whichever ritual performed it.** `/ingest` files a line from
`.superpowers/sdd/vault-feedback.md` into `log.md`, so `/ingest` removes that line. `/handoff` drains
what it drains, so `/handoff` removes those.

**Rejected: `/ingest` not reading the file at all**, which is the other way to make one owner of the
deletion — and it loses the lines written *during* the ingest itself. **Four were written on this
date, three of them found by the librarian**, none of which could have reached the journal
`/handoff` had already closed ([[a-feedback-line-written-during-an-ingest-reaches-the-vault-one-session-late]]).

# The defect it repairs

**Today `/ingest` files each line and removes nothing; only `/handoff` empties the file.** A line
written in the window between the two is filed into `log.md` and survives in the file, so the next
`/handoff` drains it into a second journal and the next `/ingest` files it a second time.

**Five entries written between the handoff and the ingest of 2026-08-21 were in exactly that
state** — present in `log.md` and still standing in the file. **The header of the feedback file
describes the two-stage transfer correctly**, and neither stage owns the deletion for that window
([[vault-feedback-file]], [[the-drain-and-the-template-disagree-about-the-feedback-vocabulary]]).

**It is visible in one place only** — reading the file at the start of the next session — which is
why it survived several passes over the same two rituals
([[a-queue-only-one-party-can-drain-is-unbounded]]).

# The shape of the rule

**The obligation follows the act, not the file.** Neither ritual owns the file; each owns what it
took out of it, and the file is empty when both have run. That removes the window rather than
narrowing it, which is what a rule keyed on *who drains* would have done.

*(Compiled from `raw/handoffs/2026-08-22-the-strike-lands-and-a-quote-gets-a-verdict.md`.)*
