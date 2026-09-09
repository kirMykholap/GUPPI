---
title: "`log.md` rotates per session, and the previous one is copied into that day's archive"
type: proposal
status: current
authority: log-rotation-design
basis: human
sprint: S2
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "log.md"]
decided_by: [[the-deferrals-of-this-session-go-onto-the-sprint]]
tags: [vault, process, harness]
---

# Raised by the owner 2026-08-20, deliberately not built

**His reading is that `log.md` has grown too large.**

**The shape, as he gave it:** a new session starts a new `log.md`, and the previous one is copied
into that day's archive folder under a **`logs/` kind of its own** —
`archive/<date>/<session>/logs/`.

It sits beside the four kinds already decided
([[raw-gains-its-internal-structure-before-the-move]],
[[the-archive-gains-a-folder-per-session-inside-the-date]]), and it **would be the first archive
content that never lay in `raw/`** except the probe scaffolding
([[the-probe-scaffolding-is-archived-whole-into-specs]]).

# What it has to respect

**`log.md` is never rewritten** ([[archive-is-rewritten-by-a-path-move-and-log-md-never-is]]).
Rotation is a copy and a truncation of the live file, never an edit of what is copied — and the
copy's own paths stay as they were written, correct for the day they were written.

**It is outside the link set the gate reads** ([[log-md-is-outside-the-link-set-the-check-reads]]),
so nothing mechanical will notice if a rotation loses a day.

# What is open

- **Whether the rotation runs at `/ingest` or at session start.** At the ingest it is one more step
  in a ritual that already has ten; at session start it is a step nobody is watching.
- **Whether the live `log.md` keeps a pointer to the rotated one**, or whether the archive folder
  is the only index. The store's habit is a link in both directions.
- **Whether "session" here means the same thing `<session>` means in the archive path** — the
  journal's filename, which is written by `/handoff` **after** the log entries it would rotate.
  That ordering is the same one the probe archive hit.

# What not building it costs

**`log.md` keeps growing**, and it is the register least protected by anything: no gate rule reads
it, no rewrite touches it, and it is append-only by decision. **Its size is the only thing that
will ever signal a problem with it.**

Retired with `superseded_by:` the day it is built or refused
([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

# The trigger changed, and the design grew a second half — 2026-08-29

**The title above is now wrong about *when*.** The owner tied the rotation to the **sprint close**, not
to the session, selecting it against tying it to `/vault-lint` or to a sweep run — a sweep may fire
three times in a sprint or not at all, and a trigger that fires an unpredictable number of times cannot
be a rotation ([[log-md-is-filled-mechanically-and-rotates-when-the-sprint-closes]]).

**The title is left as it stands.** It is the design's address and the file is what every wikilink
resolves to; what the design *says* is corrected here, which is how this store repairs a page rather
than by moving it ([[a-title-names-what-is-counted-instead-of-counting-it]]).

**And the design gained a half it did not have: who writes the file.**

**owner:** «Библиотекарь в иделае вообще не должен трогать log.md. Лог должен заполнятсья механичсеки.»

**So the rotation and the writer are one item, not two.** A rotation whose file is still hand-written by
an agent moves the growth problem without touching the ownership problem, and the owner named both in
one turn.

**One piece of it is built.** `scripts/vault-archive.sh` appends its own line when its sweep runs, and
reports to whoever called it — the first line ever written into this register by something other than
the librarian ([[the-sweep-runs-for-real-over-every-criterion-and-records-what-it-moved]]).

**What is still open, and is why this page stays `current`:** what writes the `- miss:`, `- measure:`,
`- decision:` and `- ingest:` kinds once the librarian stops; where the rotated file lands, given that a
sprint spans several dated archive folders; and whether the brief's *From the librarian* section, which
is generated from this file, survives the change.

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*

# A live decision rules the other trigger, and neither page named the other — 2026-08-29

> [!NOTE] RAISED, NOT RESOLVED — different `authority:` slugs, so rule 3 of the gate cannot see it and
> no `CONTRADICTION` block is legal
> **[[log-md-is-filled-mechanically-and-rotates-when-the-sprint-closes]] is `current` and ties rotation
> to the sprint close**, rejecting `/vault-lint` and each-sweep triggers by name. **This proposal is per
> session** and lists its own trigger as open. **The owner's ruling stands unrevised**; he was asked
> again on 2026-08-29, the sizes were measured for him, and he did not answer.

**So this page's *what is open* section understates the state**: the trigger is not merely undecided
here, it is decided elsewhere and differently. **Building this proposal as written would break a live
ruling**, which is what a reader needs to know before picking it up.

**Found by [[the-decisions-agent]] on its first dispatch**, in the deferrals the journal carried rather
than in the decisions it was handed.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
