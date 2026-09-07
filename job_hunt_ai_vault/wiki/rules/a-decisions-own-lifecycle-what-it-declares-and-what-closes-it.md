---
title: "A decision's own lifecycle — what it declares, and what closes it"
type: rule
status: current
authority: repealed-status-mint
render: authority
basis: human
sprint: S3
created: 2026-08-31
sources: ["docs/vault-cleanup-families.md", "authority.md"]
decided_by: [[a-cancelled-page-takes-a-status-of-its-own]]
tags: [vault, process, record-schema]
---

# A decision's own lifecycle — what it declares, and what closes it

The mechanism minted on 2026-08-30 by which a decision names the one thing it produces, is discharged by that thing naming it back, and leaves the folder on that handshake rather than on any citation. Answers "what is this decision waiting for, and how would I know it was done". Distinct from *draining a folder into the archive*, which answers when a page may leave; this family answers what makes a decision **finished**.

**This rule is written into no file.** It is found by its `authority:` slug, by `.claude/hooks/serve-the-rule.ps1`, when a page carrying that slug is read. Each clause below is the claim of one decision, which keeps the reasoning and the rejected alternative it was taken against, and leaves for `archive/` when `scripts/vault-archive.sh` releases it.

# The rule text

- A cancelled page takes a status of its own, and the deprecated refusal stays unconditional ([[a-cancelled-page-takes-a-status-of-its-own]])
- A case that grows becomes a proposal, announced at the moment it happens ([[a-case-that-grows-becomes-a-proposal-and-is-announced-when-it-happens]])
- A decision declares its target, and the handshake between them is what closes it ([[a-decision-declares-its-target-and-the-handshake-closes-it]])
- A decision is discharged by being handed to its target, and the session never reports that the work is done ([[a-decision-is-discharged-by-being-handed-to-its-target]])
- A refused proposal takes every decision in its list, prohibitions included ([[a-refused-proposal-releases-every-decision-in-its-list]])
- Body sections are declared in every schema and filled only where they are written ([[the-body-sections-are-declared-in-every-schema-and-filled-where-they-are-written]])
- The checkbox records ratification and not completion, and the target is the archiver's criterion ([[the-checkbox-records-ratification-and-the-target-is-the-criterion]])
- The decision lifecycle is scoped by a date rather than back-filled, and the census stays owed ([[the-decision-lifecycle-fields-are-scoped-by-a-date-rather-than-back-filled]])
- The remaining `target_kind:` value is `none`, so no value of it collides with a value of `binding:` ([[the-fifth-target-kind-value-is-none-so-nothing-collides-with-binding]])
- The sprint close reviews the repeal decisions as a set ([[the-sprint-close-reviews-the-repeal-decisions-as-a-set]])
- The sweep reads the handshake before it releases a decision, and carriage stops being read off `decided_by:` ([[the-sweep-reads-the-handshake-before-it-releases-a-decision]])

# How this page was written

Drafted 2026-08-31 by `scripts/build-family-rules.py` from the family *a decision's own lifecycle — what it declares, and what closes it* of `authority.md`. The clause of each member is its title, because only two of the 295 prohibitions the cleanup surveyed carried a written rule text of their own.

**The slug is the script's pick and it is served by nothing yet.** `repealed-status-mint` is the `authority:` of [[a-cancelled-page-takes-a-status-of-its-own]], the earliest-decided member and the page named in `decided_by:`. It is a narrow name for a wide family, and it stands because no `concepts/` or `entities/` page carries any slug of this family — the mechanism was minted on 2026-08-30 and its only page outside `decisions/` is the proposal [[the-decision-lifecycle]]. The hook matches nothing here until that design produces a concept or an entity.
