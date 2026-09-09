---
title: "The convergence pass that gives every family rule a live page carrying its slug"
type: proposal
status: current
authority: authority-convergence-pass
basis: human
sprint: S3
created: 2026-08-31
decided_by: [[the-slug-converges-by-hand-along-the-chain-of-types]]
sources: ["archive/2026-08-31/2026-08-31-the-families-become-rules/handoffs/2026-08-31-the-families-become-rules.md", "job_hunt_ai_vault/authority.md", "docs/vault-cleanup-verdicts.md"]
tags: [vault, retrieval, record-schema]
---

# Decisions

**One line per decision this proposal must close before it can be implemented.** A ticked box records
that the owner has **ratified** the answer, never that it is built.

- [x] [[the-slug-converges-by-hand-along-the-chain-of-types]] — by hand, next session, and rule 3's
  refusal is the point rather than an obstacle
- [x] [[the-hook-matches-the-exact-slug-and-resolves-nothing-through-the-register]] — the hook resolves
  nothing, so convergence is the only way a family rule reaches a member's reader
- [ ] What a merge candidate is, stated so a second person would pick the same pages — open
- [ ] What is done about a family holding no live concept or entity — open

# What would be built

**No code. A pass over the live pages of `wiki/concepts/`, `wiki/entities/` and `wiki/proposals/`,
repairing `authority:` by hand** so that each question is answered by one slug carried along the chain
of types the store already has: decision to proposal or rule to concept or entity.

**The denominator is roughly 245 pages** — the live non-decision folders as they stood after the sweep
of 2026-08-31: 147 concepts, 51 proposals, 47 entities. That is the reading of one day and it moves;
it is quoted here to size the work rather than as a criterion.

**The result is measurable in one number**: how many pages in `wiki/rules/` carry a slug that a live
page of another type also carries. It stood at fourteen of nineteen on the day the rules were written,
and it is the delivery's coverage — a rule always matches a read of itself, which is worth nothing.

# What it would take

- **Read the family, not the page.** `bash scripts/vault-authority.sh --near <slug>` returns the group,
  and the group is the unit of the judgement
  ([[the-authority-register-groups-the-corpus-and-the-family-is-the-unit-of-a-cleanup]]).
- **Move the slug onto the page that stays.** A concept or an entity outlives a decision, so the slug
  belongs on the one that will still be in `wiki/` afterwards.
- **Write the `authority.md` row in the same pass**, because a slug in the tree and not in the register
  reddens the gate and locks out the only party permitted to repair it
  ([[one-page-written-into-the-wiki-reaches-the-register-deadlock]]).
- **Never rename a file.** Moving a slug moves no address; renaming moves every inbound link and is a
  different piece of work ([[renaming-a-page]]).

# What is open

**What makes two slugs the same question.** The register groups by family and a family is wider than a
slug — `--near` returns up to fifteen members. Which of them may collapse into one is the judgement
this pass is, and nothing states the test.

**The four families with no live concept or entity.** `retro-ratification`, `page-naming`,
`missing-decision-compilation` and `repealed-status-mint` have no page to converge onto, so their
coverage waits on a concept or an entity being **written**. That is authorship, not convergence, and
this proposal does not cover it.

**Whether the pass is bounded by the nineteen rules or by the whole corpus.** Converging only what a
family rule needs is a day; converging every question in the store is the wider job the register was
built to make possible, and the owner has ruled on neither.

# What it obliges

**Nothing may be merged that would put two pages of one type under one slug.** Rule 3 of the gate
refuses it, and that refusal is the mechanism rather than an obstacle to it
([[authority-uniqueness-becomes-a-per-type-question]]).

**A page moved into `archive/` keeps its slug**, so a converged slug does not strand a register row
([[the-authority-register-step-is-repealed-and-an-archived-page-keeps-its-slug]]).

**Retired with `superseded_by:` the day it is built or refused**, after the librarian has checked that
nothing on it lives only here ([[a-built-proposal-retires-once-nothing-on-it-lives-only-there]]).

*(Compiled from `raw/handoffs/2026-08-31-the-families-become-rules.md`.)*
