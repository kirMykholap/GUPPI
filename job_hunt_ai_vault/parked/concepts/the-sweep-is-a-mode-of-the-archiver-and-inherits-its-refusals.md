---
title: "The sweep is a mode of the archiver, so it inherits its refusals instead of acquiring an opinion"
type: concept
status: current
authority: sweep-mode-inheritance
basis: code
sprint: S3
created: 2026-08-29
sources: ["archive/2026-08-29/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md", "scripts/vault-archive.sh"]
tags: [vault, harness, process]
---

# What it is

**`--sweep` is a second entry point into `scripts/vault-archive.sh`, not a second mover.** It selects
the pages and then hands each one to the machinery the named-file mode already used, so it inherits
**eight existing refusals** rather than acquiring its own opinion about when a page may leave
([[vault-archive-sh]]).

**A second mover would have to answer the same eight questions again**, and two answers to one question
is the failure this store has already paid for in a schema, in a status list and in a case list
([[a-copied-list-drifts-and-a-sweep-cannot]]).

# The line between a refusal that is collected and one that ends the run

**The test is whether the answer could differ from one page to the next.**

| Collected, and the run continues | Fatal, exit 2 before the walk starts |
|---|---|
| a missing file | a malformed date |
| an occupied destination | an unknown kind |
| no live page holding the slug | no vault found |
| a `refused` proposal without its decision | |

**A per-page condition cannot end a run of hundreds**, because the pages after it are unaffected and
the operator would have to restart from the beginning to learn whether anything else was wrong. **A
run-wide condition must**, because every page will fail it identically and a collected list of 523
identical refusals is not a report ([[the-archive-sweep-reports-a-refusal-and-the-gate-stays-silent-about-placement]]).

**The refusals are printed *before* the gate runs**, so an operator reads what the sweep decided rather
than a gate verdict about the state it left ([[a-non-zero-exit-from-the-gate-no-longer-names-one-event]]).

# What the shape cost to build

**The preconditions were factored into a routine that returns a refusal instead of ending the
process** — the single largest change in the file. Before it, every precondition called the process's
own exit; a mode that continues past a failure cannot be built on a precondition that exits.

**`--dry-run` extends to it**, and the whole-run path-length check runs before anything moves: it
computes the longest destination path and refuses the run over 240 characters
([[an-archive-path-repeats-the-session-slug-and-reaches-the-windows-limit]]).

# `status: archived` is written before the move, and the order is what makes a verdict reachable

**The mark goes on while the page is still in `wiki/`, then the page moves.** Written the other way
round it would be equally correct on a run that finishes.

**The sweep does not always finish.** It continues past a refusal, so a run can end with a page still
in `wiki/` **wearing the mark of a move that did not complete** — and `scripts/vault-check.sh` carries
a verdict for exactly that state.

**Written after the move, that verdict is dead code**: no page could ever be in `wiki/` carrying
`archived`, and the check would pass forever while asserting it had checked something
([[the-archiver-sets-status-archived-and-the-value-enters-the-schema-first]],
[[the-gates-frontmatter-pass-reads-wiki-alone-and-archive-is-validated-by-no-schema]]).

**So the ordering is not a preference about tidiness; it is what makes the failure state
representable.** That is why `archived` had to be legal in every folder's schema before any sweep ran
— the mark can appear on a page the gate is still validating.

# The collecting path has never fired on this corpus

**The first real run refused nothing**, and that was predictable: every selected page already had a
live citer, by construction for the `decided_by:` criterion
([[the-sweep-runs-for-real-over-every-criterion-and-records-what-it-moved]]).

**So the continue-past-a-refusal behaviour decided on 2026-08-28 has one proof and it is a selftest
case.** A path a real corpus cannot reach is a path only a fixture can defend
([[a-rule-with-no-instrument-behind-it-is-a-rule-a-fixture-can-violate-for-a-week]]).

*(Compiled from `raw/handoffs/2026-08-29-the-sweep-runs-and-a-third-of-the-wiki-leaves.md`.)*
