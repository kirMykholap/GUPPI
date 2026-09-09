---
title: "The archive is a directory of the vault and gains a folder per session inside the date"
type: decision
status: archived
authority: archive-session-folder-shape
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-19
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "job_hunt_ai_vault/CLAUDE.md"]
tags: [vault, process, harness]
---

# The ruling, 2026-08-19

**The archive is `job_hunt_ai_vault/archive/`, and its shape is `archive/<date>/<session>/`.**

This **refines** [[archive-is-dated-by-session-and-holds-what-left-the-working-set]], which settled
`archive/<session date>/` and left the day flat. Three answers, all the owner's:

| The question | The answer |
|---|---|
| a folder per what, inside the date | **per session** — a day holds several, and 2026-08-19 already held three |
| how the files lie inside a session folder | **as they lie in `raw/`**, so the `handoffs/` and `notes/` substructure is preserved rather than flattened |
| what names a session folder | **the journal's own filename** — date plus slug |

**Rejected: naming a session folder from the harness's session id.** It is a UUID, and it would name
the folder something no human can read. The journal's filename already carries the date and a slug
unique to the session, so **no system data is needed** and nothing has to be plumbed through to get
it.

## Rejected: the commit as the archive

The teardown of `probe/RUNBOOK.md` had been drafted against *"the commit `f552abd` is the archive"*.
**That reading cannot work**: `sources:` names paths and cannot cite a commit, so the twelve
citations pointing at the probe scaffolding would have had nowhere to point
([[the-conditional-delivery-probe]], [[a-destination-that-is-also-a-citation-loses-to-whichever-loop-runs-first]]
for the other half of a path that is both). Git holds the bytes; it does not hold an address a page
can carry.

## What it obliges

- **The move is a move, not a delete.** Nothing is removed under this design — the file travels from
  `raw/` to `archive/` — so the immutability rule over both directories is untouched, and the word
  *cleanup* is the misleading half of how it was first described
  ([[raw-holds-testimony-and-artefacts-are-frozen]]).
- **The citations are the open half, not the move.** Measured at `b6fc6d8`: 150 of 165 pages name
  `raw/handoffs`, **23 of those in prose**, where no detector exists
  ([[moving-raw-into-a-dated-archive]], [[a-rewriter-must-be-paired-with-a-detector]]).
- **The condition for a move already exists as a command**: `vault-coverage.sh` printing
  `INGEST COMPLETE` ([[handoff-retires-only-when-every-unit-has-a-verdict]]).
- **How it is executed is a separate ruling**:
  [[raw-is-emptied-by-a-script-and-the-move-lives-inside-the-ingest]].

# Breached a second time, by 239 pages, and repaired before the commit — 2026-08-29

**The first archiving sweep put 239 pages into `archive/2026-08-29/2026-08-29-the-first-sweep/`, a
folder naming no session.** The correct folder — `2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves`,
named by the journal's own filename, as this page requires — existed beside it, holding that session's
journal and its two ingest retirements.

**`scripts/vault-archive.sh` takes the session as an argument and never derives it**, so the name came
off the command line and nothing checked it ([[vault-archive-sh]]).

**Predicted verbatim on 2026-08-22** by
[[the-session-slug-is-written-to-a-file-and-the-handoff-reads-it]], **and caught by nothing until
`/pre-task` read the plan of 2026-08-29.** Not by the gate, not by the sweep's own refusals, not by the
ingest that ran inside the wrong folder.

**Repaired before the commit, and the cost of the two timings is the useful measurement**: 239 pages
moved with `git mv`, **one `sources:` citation rewritten**, three prose mentions left standing in
`log.md`, `brief.md` and [[the-vault-directory]] — one command and one edit **while the move was
uncommitted**. The same repair after a commit is 239 committed paths and nobody has done it. The gate
after the move read exit 0 in 19.4 s with the advisory unchanged.

**What the second breach argues for is derivation rather than an argument.** The prohibition is
four sessions old, has now been broken twice, and both breaches were a name typed by hand into a script
that could have read it from the journal.

*(Compiled from `raw/handoffs/2026-08-29-the-librarian-gets-its-readers-and-the-plan-is-cut-to-what-builds.md`.)*
