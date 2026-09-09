---
title: "The pre-task ledger holds one session and is rotated at `startup`, filing its rows away rather than deleting them"
type: decision
status: current
authority: ledger-retention
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-21
sources: ["archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md", ".claude/hooks/session-brief.ps1", ".claude/hooks/pre-task-state.ps1"]
tags: [harness, process, agents]
---

# Decided 2026-08-20, the owner's design, taken in conversation

**`.superpowers/sdd/pre-task-ledger.tsv` holds the rows of one session.** At `SessionStart` with
`source` = `startup` the whole file is moved to
`.superpowers/sdd/ledger/pre-task-ledger.<yyyy-MM-ddTHHmmss>.tsv`, and a fresh file opens with a
`#`-prefixed pointer row. **Records are filed away, never deleted**
([[the-ledger-archive-directory]]).

This answers the retention question [[the-pre-task-ledger]] named and deliberately refused to
invent: the file grew without bound and was read whole on every `Edit|Write`.

## What was rejected

- **The closing ritual as the trigger.** It can be skipped and has been, repeatedly, and on the day
  this was decided it did not touch this file at all ([[pre-task-was-skipped-again-and-the-record-is-a-recurrence-rather-than-an-incident]]).
- **A line-count threshold.** One more number to remember, for no gain once the file is per-session:
  a bound expressed as *one session* needs no figure and cannot drift
  ([[an-unsourced-number-is-dropped-not-chosen]]).

## What it obliges

**Rotation runs on `startup` alone.** A `resume`, a `compact` and a `clear` are the same live
session; filing its rows away mid-flight would drop the approved scope the plan path reads
([[the-pre-task-state-machine-has-a-flag-for-the-plan-and-a-flag-for-the-write]]).

**Rotation is a move of the whole file and never a read-modify-write**, which is what the ledger's
append-only design exists to protect
([[rotation-is-a-whole-file-move-and-never-a-read-modify-write]]).

**The growth did not end; it moved.** Out of the file a hook reads on every edit, and into a folder
nothing reads and nothing prunes, at roughly a kilobyte per session. Whether that folder needs a
bound of its own is open and is named on its own page rather than answered here.

# The trigger was moved from where the owner put it, and he has not ratified the move

**He proposed the process that empties the ledger, and named the closing ritual.** The session moved
it to `SessionStart` and went straight to writing the plan. He approved a plan containing it; he has
given no yes or no on the change itself, and the divergence that produced it is
[[a-question-shaped-like-a-proposal-was-executed-as-a-ratified-design]].

**The `startup`-only argument above is the session's reasoning and not his ruling.** It is written
here so that whoever brings him the question has the case in front of them.

# The archive is not pruned — the owner, 2026-08-21

**The paragraph above leaves one question open: *"Whether that folder needs a bound of its own is
open"*. It is answered, and the answer is no.** The owner ruled early in the session of 2026-08-21
that `.superpowers/sdd/ledger/` is not pruned. **The verdict existed only in chat for eight hours
before it was written down**, which is the shape [[chat-is-not-a-channel-that-survives-the-session]] already names.

**What was rejected is a retention rule of any kind** — a count of files, an age, a sweep at
rotation. The folder is git-ignored, nothing in the repository reads it, and it takes roughly a
kilobyte per session; the growth is the cheap kind ([[the-ledger-archive-directory]]).

**And it settles the drain question in the same direction.** Nothing drains the live ledger either
— «Слив ledger не строим» — so the rows a session appends end where rotation puts them
([[the-pre-task-ledger]], [[the-retro-writes-its-own-transit-file]]).

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*

# The `startup` trigger was ratified explicitly — 2026-08-26

*(the owner selected it.)* **The rotation trigger stays `startup`.**

**What changed is only the standing of the ruling.** It had been approved once, inside a plan he read
and accepted, and never by a direct yes — which is the shape this store has already been burned by,
where a design read inside a plan is later treated as an utterance
([[a-question-shaped-like-a-proposal-was-executed-as-a-ratified-design]],
[[the-retro-records-a-ruling-chosen-from-a-menu-and-ratifies-decisions-not-utterances]]).

**Nothing about the mechanism moves.** This is a ratification, and it is recorded so the next reader
does not re-open it looking for the direct answer.

*(Compiled from `raw/handoffs/2026-08-26-the-carried-questions-are-answered-and-the-plan-is-corrected-before-it-is-built.md`.)*
