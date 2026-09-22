---
type: decision
case: "351"
status: current
create: ["[[estimate-prespec-simulates-the-pairs]]"]
update: ["[[rule-prespec]]", "[[estimate-prespec-reconciles]]", "[[insight-workflow-edit-pair-signed-from-a-grep-fragment]]"]
supersedes: ["[[decision-case-345]]"]
origin: raw/2026-09-22/2046/ledger.md#case-351
sprint: migration
created: 2026-09-22
tags: [harness, workflow, session, librarian]
---

## Context

Case 345 gives `pre-spec` a check of the anchors and leaves two defects. First: it changes the Render of `rule-prespec` and does not name `estimate-prespec-reconciles`, the live reading of that Render, `passed`, whose method is one reading by hand of the first `/pre-spec` after the render. That is the breach of case 187 which 341 and 342 exist to repair and which 347, 349 and 350 of this plan all observe. Second: it gives the Insight `addressed_by` as a list of two links, while the schema of an Insight requires one quoted wikilink — unlike `deferred_by`, which the same schema calls a list; all nine live Insights carry one.
`rule-prespec` stands `built`, a Leaf; the anchor of the pair stands once in it; the pair of case 335 of the conserved Spec touches another span. Two Estimate items in one `then` block each need a written `sections: Criterion`, or one wording is signed twice, so the Criterion of the created Estimate is written out. `estimate-prespec-checks-the-plan` is not named: a new check of `--check` has its own Estimate, as in cases 327 and 331.

## Problem

The Case changes a Render without naming its live reading, and writes `addressed_by` in a form the schema does not know.

## History

- 2026-09-23 created · raw/2026-09-22/2046/ledger.md#case-351
