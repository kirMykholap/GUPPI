---
title: "The criterion that every governed file carries a region is reworded to admit a file that is generated whole"
type: decision
status: archived
authority: region-coverage-criterion-wording
binding: prohibition
basis: human
sprint: S2
decided: 2026-08-20
created: 2026-08-20
sources: ["archive/2026-08-19/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery/handoffs/2026-08-19-the-guard-is-built-and-the-ast-rule-moves-to-conditional-delivery.md", "sprint.md", "scripts/vault-check.sh"]
tags: [harness, vault, process]
---

# The ruling, 2026-08-20

The criterion read *every governed file carries a marked region*. It now reads:

> **every governed file carries a marked region **or is fully generated**.**

**The occasion is `.claude/rules/ast-boundaries.md`**, which the injector owns end to end and which
**can never acquire a region** — a region protects an insert into a file that has other content
around it, and a generated file has none
([[a-region-is-a-paired-comment-named-for-a-rule]],
[[a-claude-rules-file-is-generated-whole-and-deleted-by-its-own-marker]]). The criterion had
acquired a member for which it was unsatisfiable by construction, and the advisory would have named
that file on every run for good.

## The owner's wording beat the one the session offered, and the difference is the record

**The session proposed dropping marker-carrying files from the denominator.** The owner counts them
as **satisfied** instead.

**Dropping a file from a denominator hides it; counting it as satisfied says what is true.** The
file is governed, and it is handled — by the other mechanism. A denominator that quietly shrinks is
the same instrument failure this store has already priced elsewhere
([[a-denominator-is-walked-off-the-input-list]]), and it would have made the one file the criterion
could not describe the one file the criterion no longer saw.

**Rejected, therefore: the session's own fix.**

## What the check reads, and how the number is to be stated

**The marker is counted in the pass that already reads every governed file**, not by a grep per
file ([[a-fields-legal-values-live-beside-its-legal-keys]] is the same pass discipline applied to
the schema half).

**Stated the way the denominator ruling requires**
([[the-governed-denominator-may-grow-and-the-criterion-stays-a-file-count]]): the advisory reads
`a region or whole generation covers 2 of 15`, and **the numerator moved because a generated file
now counts as satisfied under the new wording, not because any file gained a region.** The thirteen
files that carried none that morning still carry none. Proved both ways in the real tree: the
marker stripped gives `1 of 15`, restored gives `2 of 15`
([[a-new-verdict-is-proved-in-the-real-tree-because-the-check-cannot-see-a-sandbox]]).

## What it obliges

**`sprint.md`'s criterion text is the librarian's to reword, and this is the wording.** The verdict
on the criterion is not: reading it is the owner's, and nothing here restates one
([[a-sprint-closes-on-its-goal]]).
