---
type: decision
case: "901"
status: current
children: ["[[decision-case-901.1]]", "[[decision-case-901.2]]", "[[decision-case-901.3]]", "[[decision-case-901.4]]", "[[decision-case-901.5]]"]
origin: raw/2026-10-29/0327/ledger.md#case-901
sprint: plugin
created: 2026-10-29
tags: [sprint, workflow, ledger, session, harness, tests]
---

## Problem

Shipped Estimates hold a Criterion sentence that is false or empty in a project that installed GUPPI. A Criterion replaced now sets its Estimate `pending` and its rule `draft` until its reading, so only the Estimates read in this session are rewritten now.

## Recommend

- **Which Criteria the Case rewrites**
  - Recommended: (a) rewrite the ten that fail the yardstick of Case 898; the four that hold keep their Criterion and their status, and the Case says why each one stands.
  - Answer: agreed, (a).
- **A sentence that names an Estimate the clean copy leaves out**
  - Recommended: (a) the line says what it needs in its own words, or drops the pointer where the line reads whole without it.
  - Answer: agreed, (a).
- **The two sentences on an old path that a later Case removes**
  - Recommended: (b) a Case of its own removes the two old paths and the two sentences together; this Case leaves them on the reading's list.
  - Answer: agreed, (b).
- **Estimates whose new Criterion waits for a live reading**
  - Recommended: (a) rewrite all ten now; each is `pending` until its reading, and those that wait for a live event leave the clean copy until then.
  - Answer: agreed, (a).
- **Change**
  - Asked: at `/pre-spec`, narrow the Case to the Estimates whose reading runs in this session, by a test or at its Retro; the others go back on the list of the reading, and the defer of `decision-case-893.1` stays for them.
  - Taken: five Estimates stay, seven leave, and the Case is built again as Case 901 with marks that retire each sub-case of Case 899.
- **Change**
  - Asked: at `/pre-spec`, add `estimate-ask-query-before-a-create` and `estimate-compact-recall-reloads` by the same rule.
  - Taken: both wait for a live reading, so both leave with the defer, and the `context` says why.

## History

- 2026-10-29 created · raw/2026-10-29/0327/ledger.md#case-901
