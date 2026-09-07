---
title: "The retro writes its own transit file, kept apart from the feedback draft"
type: decision
status: current
authority: retro-transit-file
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-ritual-gets-a-retro/handoffs/2026-08-17-the-ritual-gets-a-retro.md", ".claude/skills/retro/SKILL.md"]
tags: [process, harness]
---

# Decided 2026-08-17: `.superpowers/sdd/retro.md`, beside the feedback file and not inside it

**The retro writes `.superpowers/sdd/retro.md`**, its own git-ignored transit file. It is **not**
appended to [[vault-feedback-file]], and the property that separates them is the property that
makes each of them work:

| | `vault-feedback.md` | `retro.md` |
|---|---|---|
| written | in the turn the observation is made ([[feedback-is-recorded-in-the-turn-it-is-noticed]]) | at the end of the session, in one pass |
| holds | raw observations, unresolved | what has been resolved, with a verdict per line |
| read by | the retro, as evidence | `/handoff`, which routes it |

**The retro reads the feedback file and does not drain it.** Draining belongs to `/handoff`, which
is the step that files things; a retro that emptied the file would move raw observations into a
document whose whole contract is that its lines carry verdicts.

**Rejected: one file for both.** Mixing them loses the timestamp property — a line written in the
turn it was noticed carries the question that was asked and the grep that returned nothing, and a
line written at the end carries a mood about the session. That was the argument for the feedback
file existing at all, and it applies to keeping it single-purpose.

## What it obliges

Both files are git-ignored, both are session-local, and **neither is checked for having been
written to**. The failure mode named on [[vault-feedback-file]] — a session that never opens it
produces a section reading "none" and looks identical to one where nothing went wrong — now applies
to two channels instead of one.

# The same reasoning decided who drains the pre-task ledger — 2026-08-20

**The plan said `/retro` would drain `.superpowers/sdd/pre-task-ledger.tsv`. It is drained by
`/handoff`** ([[the-pre-task-ledger]]).

**This page rejects exactly that operation, and the reason applies unchanged**: the ledger's rows
are raw machine observations with no verdict on them, and the retro's output holds only resolved
lines. A retro that reads a raw file is doing the handoff's job in the step before it.

**So the ledger joins `.superpowers/sdd/vault-feedback.md` as a file `/handoff` drains and `/retro`
does not** ([[vault-feedback-file]]) — one direction for raw observations, one for the interrogation
that resolves them.

# The drain it assigns to `/handoff` is not built — reported 2026-08-20, fourth session

**This page rules who drains the pre-task ledger; it does not report that anyone does.** Verified by
grep: neither `.claude/skills/handoff/SKILL.md`, nor `/retro`, nor `.claude/templates/handoff.md`
mentions the ledger. **The ruling stands and the mechanism is missing**, and
[[the-pre-task-ledger]] carries the same assertion in the same words.

**The gap widened when the ledger began rotating.** A session that ends without the closing ritual
now has its rows filed into `.superpowers/sdd/ledger/` at the next `startup`, where a drain would
not look even once it is written
([[the-pre-task-ledger-holds-one-session-and-rotates-at-startup]], [[the-ledger-archive-directory]]).

**The work item names its file:** `.claude/skills/handoff/SKILL.md`. It was not built that night —
it is a change to a closing-ritual skill and was outside the approved scope.

# What the drain order costs, and it is paid every ingest

**A line written into `.superpowers/sdd/vault-feedback.md` *during* an ingest reaches the vault one
session late**, because `/handoff` has already emptied the file by then. It is a property of the
order this page and [[ingest-runs-after-handoff-at-the-end-of-a-session]] set between them, not a
leak ([[a-feedback-line-written-during-an-ingest-reaches-the-vault-one-session-late]]).

# The ledger is drained by nothing, and the sentence above naming it a file `/handoff` drains is cancelled — 2026-08-21

**The section *The same reasoning decided who drains the pre-task ledger* closes on *"the ledger
joins `.superpowers/sdd/vault-feedback.md` as a file `/handoff` drains"*. That half is withdrawn.**
The owner, at the retro of 2026-08-21: «Слив ledger не строим.»

**Corrected in place rather than retired, because only one of the two claims moved.** This page's
own subject — the retro writes `.superpowers/sdd/retro.md` and does not drain the feedback file — is
untouched, and so is the reasoning that kept the ledger away from `/retro`. What is gone is the
second half of the sentence: there is no drain, by anybody, and the work item naming
`.claude/skills/handoff/SKILL.md` is withdrawn rather than carried
([[the-pre-task-ledger]]).

**`vault-feedback.md` still is a file `/handoff` drains**, and the cost that order carries every
ingest is unchanged
([[a-feedback-line-written-during-an-ingest-reaches-the-vault-one-session-late]]).

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*
