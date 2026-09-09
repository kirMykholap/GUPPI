---
title: "The ledger archive directory"
type: entity
status: current
authority: ledger-archive
basis: code
sprint: S2
created: 2026-08-21
sources: ["archive/2026-08-20/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness/handoffs/2026-08-20-the-ingest-picks-by-sidecar-and-the-owner-cannot-see-the-harness.md", ".claude/hooks/pre-task-state.ps1"]
tags: [harness, process, agents]
---

# What it is

**`.superpowers/sdd/ledger/`** — one file per rotated session,
`pre-task-ledger.<yyyy-MM-ddTHHmmss>.tsv`, git-ignored like everything under `.superpowers/`.
It appeared on 2026-08-20 in `abd2a53`, with
[[the-pre-task-ledger-holds-one-session-and-rotates-at-startup]].

**A rotated file is a whole file moved**, not a filtered copy
([[rotation-is-a-whole-file-move-and-never-a-read-modify-write]]), and the fresh ledger that
replaces it opens with a `#`-prefixed pointer row.

# Nothing prunes it and nothing reads it

**Both halves are true today and neither is an oversight.** The rows are read out of the *live*
ledger by `Read-LedgerState`; once a file is here, no code in this repository opens it. What it is
for is a human at a retro asking what a past session did
([[one-ledger-is-the-record-the-heartbeat-and-the-permission-mode]]).

**The growth did not end, it moved.** Out of the file a hook reads on every `Edit|Write`, and into a
folder nobody reads, at roughly a kilobyte per session — measured from a live ledger holding
**7 rows and 404 bytes across two sessions**. Whether it needs a bound of its own is open, and it is
named here rather than answered: inventing a retention rule is a decision about the project
([[a-queue-only-one-party-can-drain-is-unbounded]]).

**The unbounded half is now the cheap half**, which is the part worth carrying forward: a file that
is read on every edit and a file that is read by nobody have very different costs for the same
number of bytes.

# The open question above is answered: it is not pruned — the owner, 2026-08-21

**"Whether it needs a bound of its own is open" is no longer open.** The owner ruled that
`.superpowers/sdd/ledger/` is not pruned, and the ruling is written where the retention decision
lives ([[the-pre-task-ledger-holds-one-session-and-rotates-at-startup]]). **Nothing prunes it and
nothing reads it stays true, and both halves are now deliberate rather than merely observed.**

*(Compiled from `raw/handoffs/2026-08-21-a-claim-is-looked-up-before-a-page-is-written.md`.)*

# An empty result from here reads exactly like an absent row in the live ledger — 2026-08-29

**A session reported that its `make smoke` had not been recorded, and it had.** Three `smoke:0` rows
stood in `.superpowers/sdd/pre-task-ledger.tsv`. **The session read `.superpowers/sdd/ledger/`, which is
this directory, and took an empty result for an absent row.**

**Cost: one unnecessary `make smoke` run, about four minutes**, in a session whose own complaint was
that it had spent its length arguing.

**Nothing in the vault says which of the two paths is the live ledger.** That is the gap: this page says
the archive is written by rotation and read by nothing, and [[the-pre-task-ledger]] describes the live
file, but no page puts the two paths side by side and says *look here, not there*. **This section is
that sentence.**

**And the rows it would have found were partly false anyway** — the recorder writes a green smoke row
for any command whose output merely contains the marker
([[an-instrument-that-hunts-a-literal-excludes-the-corpus-that-documents-it]]).

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
