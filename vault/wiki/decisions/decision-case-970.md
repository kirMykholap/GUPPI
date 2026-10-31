---
type: decision
case: "970"
status: current
children: ["[[decision-case-970.1]]", "[[decision-case-970.2]]", "[[decision-case-970.3]]"]
origin: raw/2026-10-31/1831/ledger.md#case-970
sprint: plugin
created: 2026-10-31
tags: [session, workflow, harness, case-build]
---

## Problem

The builder runs word searches of the vault before the rules Grep of the vault query and may skip the lesson and insight searches, so the query does not check the vault in the order and the scope that the recipe means.

## Recommend

- **When the builder runs the vault query**
  - Recommended: (a) the first search of the vault once the build sees a `create` without a `ref`, set in the builder's text, `rule-case-build`.
  - Answer: (a), as recommended.
- **Which per-kind searches the query always runs**
  - Recommended: (a) every kind every time, each with its pattern as written, in `rule-ask` for every caller.
  - Answer: (a), as recommended.
- **How the two parts are checked**
  - Recommended: (a) two sub-cases: a new Estimate on `rule-case-build` for the moment, and the Criteria of `estimate-ask-query-before-a-create` and `estimate-ask-searches-at-prespec` replaced for the recipe.
  - Answer: (a), as recommended.

## History

- 2026-10-31 created · raw/2026-10-31/1831/ledger.md#case-970
