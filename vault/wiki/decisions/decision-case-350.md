---
type: decision
case: "350"
status: current
update: ["[[rule-estimates-schema]]", "[[estimate-estimates-schema-checked]]"]
supersedes: ["[[decision-case-343]]"]
origin: raw/2026-09-22/2046/ledger.md#case-350
sprint: migration
created: 2026-09-22
tags: [harness, render, schema]
---

## Context

Case 343 set out to repair the promise that a `method` naming one of the four forms earns no finding, and repaired half of it. It made the exception for the Estimate of a MOC and none for the Estimate of a Leaf: `check_method` earns a finding on a `tests/…` path that is not on disk, and on a `make <target>` the Makefile does not hold. A reader of the schema signs `pytest tests/test_x.py` for a file that does not exist and believes it clean. Its second error: the text says a page of the old shape is one with no `method` field, while `is_old_shape` counts a page as old-shaped on any of four triggers — no `method` field, a `## Context` section, a `## Method` section, or a `### case N` block in the Criterion; three of the four hold for pages that do carry the field.
`rule-estimates-schema` renders `vault/wiki/estimates/schema.yaml`; the live reading is `estimate-estimates-schema-checked`, `passed`, whose Criterion covers the prose as data and does not itself change. The words "the one spelling of a reading" hold once the code task of case 330.1 of the conserved Spec lands: `READING` still stands in `guppi/lint.py`.

## Problem

The text that is to bring the schema into agreement with lint disagrees with it in two more places: what the Estimate of a Leaf may name, and what makes a page old-shaped.

## History

- 2026-09-23 created · raw/2026-09-22/2046/ledger.md#case-350
