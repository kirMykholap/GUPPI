---
title: "The probe scaffolding is archived whole into `specs/`, and dated by the day it left the working set"
type: decision
status: current
authority: probe-teardown-destination
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/handoffs/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock.md", "archive/2026-08-20/2026-08-20-the-suite-parallelises-and-the-librarian-gets-a-lock/specs/RUNBOOK.md"]
tags: [vault, process, harness]
---

# Decided 2026-08-20 by the owner

**All three files — `probe/RUNBOOK.md`, `.claude/rules/_probe-paths.md`,
`.claude/hooks/instructions-loaded.ps1` — go whole to `archive/<date>/<session>/specs/`.** Archived,
not deleted, on the vault's own definition of an artefact as an instruction that was executed
([[raw-holds-testimony-and-artefacts-are-frozen]], [[the-conditional-delivery-probe]]).

**Rejected: a fifth `<kind>` beside the four already decided.** More precise, and not worth a
change to a decided list ([[raw-gains-its-internal-structure-before-the-move]]).

## The date is today's, and that is the general rule

**owner: the date is the day the thing leaves the working set, not the day it was made.** The probe
spans 2026-08-18 and 2026-08-19 and several sessions each, so *the session that made it* has no
single answer while *what left the working set that day* does. That is the predicate
[[archive-is-dated-by-session-and-holds-what-left-the-working-set]] already carries, applied to
content whose making is spread over days.

## What it obliges

**The move runs after `/handoff`**, because `<session>` is the journal's own filename. That is a
sequencing constraint on the ritual, not a preference.

## It closes the block the teardown clause could not see

`probe/RUNBOOK.md` made its own deletion conditional on probe 4's answers reaching `wiki/`; the
reaching is what forbade the deletion, because the citations then existed
([[a-teardown-clause-cannot-see-that-it-has-become-what-it-guards]]). Archiving with a citation
rewrite is the exit, and `scripts/vault-archive.sh` is what performs it
([[vault-archive-sh]]).
