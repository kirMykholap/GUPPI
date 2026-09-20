---
type: decision
case: "193"
status: current
update: [estimates-schema-yaml, estimates-schema, index, glossary, rules-schema]
origin: raw/2026-09-16/1651/ledger.md#case-193
sprint: migration
created: 2026-09-16
tags: []
---

## Context

The Estimate model of case 182 is ratified by Cases 187–189 of session 1034: an Estimate is one promise, one way to check it and the last result; its Criterion is the `given`, `when` and `then` of one Case, replaced whole; `contract` on an `update`, `method`, `estimate_kind` and `estimate_slug` on a `create` go. The Rule-class files that describe the model are untouched. `index.md` in §2, §3, §5, §7 and §12 speaks of `### case N` blocks, of `method` on a Leaf `create` and of `contract: changed`. `estimates/schema.yaml` requires `## Context` and `## Method`; `estimates/schema.md` describes the Criterion as blocks. `glossary.md` repeats this in the rows Estimate and Case; `rules/schema.md` describes `## How it works` on a Leaf. Point 16 of the model named these files; no Case was written. This Case touches no Estimate: a Rule-class file has none.

## Problem

While the schemas and the map say the old model, Spec 1034 applies with contradictions: the ten new Estimates without `## Context` give ten lint findings, a reader of `index.md` gets a rule opposite to `case-schema.md`, and the table of `schema.md` stops agreeing with `schema.yaml`, which lint also checks. The question: the smallest set of changes to the Rule-class files that makes Spec 1034 applicable.

## Given

Cases 187, 188 and 189 are ratified and are applied by the same librarian run as this Case.
**＋** lint reads `estimates/schema.yaml` and checks the table of `estimates/schema.md` against it.
**＋** `guppi generate` writes every field of an entry's `fields` into the frontmatter, with no list of allowed fields.
**－** `rule-page-generation`, `rule-lint` and `rule-prespec` are deferred by case 191; this Case does not touch them, and point 10 of the model (Given and the Criterion list leave the Decision page) waits there too.

## History

- 2026-09-16 created · raw/2026-09-16/1651/ledger.md#case-193
