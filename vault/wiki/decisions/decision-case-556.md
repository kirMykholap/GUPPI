---
type: decision
case: "556"
status: current
update: ["[[estimate-estimates-schema-checked]]"]
origin: raw/2026-09-30/2042/ledger.md#case-556
sprint: migration
created: 2026-09-30
tags: [harness, render, schema]
---

## Problem

The method of `estimate-estimates-schema-checked` selects the tests by a name that the test of a page without `method` does not contain. So the reading behind the page's `passed` never ran the test of one of its promises. The question is how the method selects that test, and whether the page waits for a new reading.

## Recommend

- **How should the method select the test for a missing `method`?**
  - Recommended: (a) the singular filter `-k estimate`, as the method of `estimate-decisions-schema-checked` uses, with the method text naming a page without `method`; no code change.
  - Answer: (a). The person asked for a plain explanation first, and then agreed with the recommendation.
- **Should the page go back to waiting for a new reading?**
  - Recommended: (a) set the page `pending`, write its Criterion back word for word, and read it with the new command in a later session.
  - Answer: (a). The person agreed with the recommendation after the explanation.

## History

- 2026-09-30 created · raw/2026-09-30/2042/ledger.md#case-556
