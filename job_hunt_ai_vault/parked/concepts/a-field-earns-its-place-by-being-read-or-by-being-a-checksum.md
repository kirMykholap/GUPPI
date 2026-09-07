---
title: "A field earns its place by being read, or by being a checksum against a fact the tree already asserts"
type: concept
status: current
authority: field-admission-test
basis: human
sprint: S1
created: 2026-08-17
sources: ["archive/2026-08-16/2026-08-16-the-harness-becomes-a-build/handoffs/2026-08-16-the-harness-becomes-a-build.md", "docs/superpowers/specs/2026-08-16-harness-and-schemas-design.md"]
tags: [vault, testing]
---

# The test, and the half the data added to it

The test started as one clause — **a field is required only when something reads it and fails
without it** — which is this project's acceptance model applied to a schema: every criterion names
the command that decides it, and a required field nothing reads can be wrong forever
([[a-sprint-closes-on-its-goal]], [[the-owners-question-was-how-would-you-check-that]]).

**The data added a second clause.** A field also earns its place if **(b) it independently restates
a fact the tree already asserts, so a disagreement catches a writer's error.**

## Why (b) is a checksum rather than duplication

`type` and `status` agree with their folder on **every page of the corpus and always have**. Read
as duplication that is dead weight; read as a checksum it is a redundant encoding of one fact by
two independent writers — the folder chosen by a path, the field typed into frontmatter — and rule
2 of `vault-check.sh` compares them ([[vault-scripts]]).

**The checksum has never fired. That is not the same as being idle.** A check whose failure has not
happened yet is indistinguishable, by its output, from one that cannot fail — and the difference
matters exactly when the writer is unattended ([[the-librarian-writes-unattended]]). The distinction
the two clauses draw is the one this store keeps having to redraw: what a check *proves* against
what it *has caught* ([[a-check-that-passed-for-the-wrong-reason-becomes-a-rule]]).

## What the test is used for

It is the admission rule for the record schema, and it was applied field by field on 2026-08-16 —
including to fields that failed it and were kept anyway, with the failure written down rather than
hidden: [[the-frontmatter-core-is-fixed-and-updated-joins-it]]. A field kept as documentation is
labelled documentation in the schema, which is the honest third outcome the test allows.

## A field went around this test on the day it was being applied — 2026-08-18

**`quantity:` was introduced on 2026-08-17 without passing through here.** It was filed as an entity
that had appeared rather than as a decision taken, and on that same day this test was being applied
field by field to the frontmatter core, refusing one new field on exactly the ground that a field
nobody writes and nobody reads becomes a per-page invention
([[the-frontmatter-core-is-fixed-and-updated-joins-it]]).

**It would have failed the test, and not for the obvious reason.** Something did read it — rule 10
of `vault-check.sh` — so clause (a) was satisfied in the letter. What it lacked was the thing the
test is a proxy for: **a decision that the assertion may be made at all.** The field let a page
answer a question the owner had already closed twice.

**So the test is necessary and is not sufficient**, and the missing half is procedural rather than
logical: a field is admitted the way a decision is admitted
([[a-field-admitted-around-the-admission-procedure-outlives-the-rule-it-softens]],
[[the-quantity-field-is-rejected-and-the-rule-stays-unconditional]]).
