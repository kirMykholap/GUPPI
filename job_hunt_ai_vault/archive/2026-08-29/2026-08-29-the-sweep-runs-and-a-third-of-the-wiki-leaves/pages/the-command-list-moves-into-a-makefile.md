---
title: "The command list moves into a `Makefile`, not into a shell dispatcher"
type: decision
status: archived
authority: command-list-home
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-17
created: 2026-08-17
sources: ["archive/2026-08-17/2026-08-17-the-rules-leave-the-prose/handoffs/2026-08-17-the-rules-leave-the-prose.md", "CLAUDE.md"]
tags: [harness, process, testing]
---

# Decided by the owner on 2026-08-17, overruling the session. Not built.

**The session recommended `scripts/do.sh`** on the ground that `make` is not installed in this
environment — Git Bash ships none — and a shell dispatcher needs no install. **He overruled it, and
the session agrees the argument was weak**: five minutes of setup against a convention every agent
already knows without being told.

**Rejected: `scripts/do.sh`.** Rejected for a reason worth writing down — *no installation required*
is a one-time cost weighed against a recurring one, and the recurring side was the whole point.

## The evidence for moving it at all, measured the same day

`## Commands` in the repository's `CLAUDE.md` says `bash scripts/vault-check.sh` takes **`~2 s`**. It
takes **`4.9 s`**, measured 2026-08-17. **The list drifted from reality inside the same session that
changed the thing it describes** — which is the drifting-list failure with no intervening days to
excuse it ([[a-drifting-list-is-repaired-by-deleting-it-not-extending-it]],
[[the-repository-claude-md-after-the-rules-left-it]]).

## What it obliges

- **Pipelines belong there too, not only single commands.** `make check` rather than four commands
  remembered in the right order — that is the value, and a list of four commands in prose cannot
  express it.
- **`## Commands` then points at the `Makefile` instead of restating it**, which is the same move as
  deleting `## Where things are` ([[where-things-are-is-deleted-now-and-generated-later]]).
- **`make help` is the third consumer of one unbuilt generator**, with the map and a generated
  `Where things are` ([[a-generator-fills-a-marked-region-from-the-tree]]).

The design, and what a `Makefile` would hold, is [[a-makefile-holds-the-projects-pipelines]].

# Revived 2026-08-26, with the checks as the occasion

**The owner reopened `make` when he ordered a single entry point for the check system**, which gives
this decision a second consumer beyond `## Commands`
([[the-checks-get-a-single-entry-point-and-make-is-the-revived-candidate]]).

**`make` is on this machine** — GNU Make 4.4.1, via chocolatey — and the no-new-dependencies rule
does not reach it, which removes the one objection that had never been checked.

*(Compiled from `raw/handoffs/2026-08-26-the-gate-hangs-on-a-store-stub-and-the-checks-get-their-names.md`.)*
