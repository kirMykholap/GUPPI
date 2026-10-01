---
type: decision
case: "583"
status: current
update: ["[[estimate-estimates-schema-checked]]"]
supersedes: ["[[decision-case-576]]"]
origin: raw/2026-10-01/1725/ledger.md#case-583
sprint: migration
created: 2026-10-01
tags: [harness, render, schema]
---

## Problem

Lint enforces sections that a schema requires only under a condition, but no test checks it. The promise of `estimate-estimates-schema-checked` therefore rests on code that no test protects. The question is whether to write the test or to narrow the promise, and how far the test reaches.

## Recommend

- **Write a test, or narrow the promise?**
  - Recommended: (b) one test for every schema that has a section condition, written like the existing test for field conditions. It covers `## Result` on Estimate pages and `## Render` on Rule pages, and both Criteria stand.
  - Answer: (b), one test for every schema that has a section condition.

## History

- 2026-10-01 created · raw/2026-10-01/1725/ledger.md#case-583
