---
title: "The `required` half of a paired `authority:` waits on the taxonomy, because it would redden the unpaired concepts on its first run"
type: decision
status: current
authority: paired-authority-requirement
binding: deferral
basis: human
sprint: S3
decided: 2026-08-30
created: 2026-08-30
target_kind: none
target: none
sources: ["archive/2026-08-30/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md", "job_hunt_ai_vault/authority.md"]
tags: [vault, record-schema, retrieval]
---

# Context

**The owner's ruling has two halves**: a concept and an entity answering the same question **may**
share an `authority:` slug, and in that pair they **must**
([[concepts-are-non-functional-requirements-and-entities-are-functional]]).

**Only the permission landed on 2026-08-30.** Rule 3 of the gate narrowed to comparing slugs within a
type, which makes the sharing legal ([[authority-uniqueness-becomes-a-per-type-question]]); nothing
requires the pair.

**The measurement that decides the order:** of the 51 families holding `concepts/` and `entities/`
pages, **24 hold both, 22 hold concepts with no entity — 54 pages — and five hold entities with no
concept, seven pages.**

# The question

**Does the pair requirement switch on with the permission, or wait?**

# How it works after

**It waits.** Requiring the pair now reddens 54 pages on the first run, and a red gate is what
`lock-the-librarian.ps1` reads as a refusal to dispatch — locking out the only writer permitted to
clear it ([[a-lock-on-a-red-tree-hides-the-health-of-what-it-guards]]).

**This is the fill order this file set has run four times**: legal first, then the corpus is filled,
then the field is promoted. It ran that way for `basis`, for `authority`, for `binding` and for the
two lifecycle fields.

**What it waits on is not a back-fill but a judgement.** Fifty-four concepts with no entity are not
fifty-four missing entities: under the new taxonomy some of them are entities in the wrong folder,
some are concepts with nothing functional behind them, and telling those apart is the sweep's work.
**So the requirement switches on after the taxonomy has been applied, not before.**

**No sprint is named**, which puts this in the same bucket as the day's other deferrals
([[everything-on-the-frontier-but-the-cleanup-is-deferred-and-none-of-it-names-a-sprint]]).

# Recommendation

**Defer it, on the order this store has already used four times.** The alternative is a gate that goes
red on the day a permission is granted, for pages nobody has looked at yet.

**Rejected: requiring the pair in the same change as permitting it.**

# Ratification

**The session understood it from the tree, and the owner ratified the pairing rule that contains
both halves.** He did not rule on the order; the arithmetic did, and the fill order is the store's own
precedent rather than a new judgement.

*(Compiled from `raw/handoffs/2026-08-30-a-rule-is-served-by-lookup-and-the-gate-fails-quietly.md`.)*
