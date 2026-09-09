---
title: "The closing ritual produces knowledge the journal cannot hold, so the vault is off by a session on it"
type: lesson
status: archived
authority: closing-ritual-offset
basis: human
sprint: S2
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", ".superpowers/sdd", "log.md"]
tags: [process, vault]
---

# Written by the session that produced `aebb308`, and inherited undrained

**The journal is written before the ritual finishes**, so anything the ritual itself produces has no
place in it. Two findings of that session are the evidence: the ingest review found four titles
carrying a count, and the start-clean check found the `SessionStart` hook's sort defect. **Neither
existed when `/handoff` ran.**

`raw/` is immutable, so the journal cannot be amended
([[raw-holds-testimony-and-artefacts-are-frozen]]). The carry is `vault-feedback.md`, which means
**the vault is off by one session on anything the closing ritual produces** — and a reader of the
next journal sees those findings attributed to the wrong session unless they are marked as
inherited, which the journal of 2026-08-17 did explicitly.

# The half that was avoidable

**One of the two was knowable earlier.** The date-prefix collision that broke the hook's sort is
created by `/handoff` itself, at the moment it picks the filename — so that check belongs **inside
the skill that creates the collision**, not in a later review.

The general form: a defect a step introduces should be checked by that step. Anything else pays for
the round trip and risks the finding landing in the wrong session's record.

# What it costs today

- **Provenance is off by one** for the ritual's own findings, and only a hand-written mark says so.
- **The feedback file is the only carry**, and nothing checks that it was drained — the failure mode
  already named on [[vault-feedback-file]]. Six lines sat in it undrained until 2026-08-17, from a
  session that wrote no journal at all.
- **The retro does not solve it.** It runs before the handoff too
  ([[the-retro-step]], [[the-end-of-a-session-is-a-retrospective]]).

# Where the findings pile up instead

They reach the brief's `Alarms` section, which only the owner can drain and which nothing bounds —
[[a-queue-only-one-party-can-drain-is-unbounded]]. The two failures compound: the ritual produces
findings the journal cannot hold, and the place they are held instead is a list that grows.

# A second journal is the repair available inside the ritual as it stands — 2026-08-26

**A session wrote its journal and the conversation carried on.** What followed the write was four
owner rulings, a one-day-old defect in the gate, and a direct instruction to clean `raw/` — none of
which the journal could hold, because `raw/` is immutable.

**The session wrote a second journal for the same day** and stated the compilation order in its own
header, because two uncompiled sources carrying one date leave the ingest's *oldest first* tie-break
with nothing to break the tie with ([[the-sidecar-is-the-single-definition-of-compiled]]).

**The ingest already provides for more than one uncompiled source**, so nothing had to change: they
are compiled one at a time, in the stated order, inside one dispatch.

**What that costs by default, and what the second journal avoids**: everything decided after the
first journal was written would otherwise have travelled in the *next* session's handoff, one
session late — the same cadence a feedback line written during an ingest already has
([[a-feedback-line-written-during-an-ingest-reaches-the-vault-one-session-late]]).

**Whether something better should exist is not decided.** This records the workaround and its cost,
not a design.

*(Compiled from `raw/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md`.)*
