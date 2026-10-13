---
type: decision
case: "786"
status: current
children: ["[[decision-case-786.1]]", "[[decision-case-786.2]]"]
origin: raw/2026-10-12/2349/ledger.md#case-786
sprint: plugin
created: 2026-10-12
tags: [harness, workflow, ledger, session]
---

## Problem

A defer of an Insight, a Lesson or a Decision page that does not exist makes `guppi generate` write a stand-in page with `status: draft`, which the format of that page does not allow. Nothing in the session reports such a defer.

## Recommend

- **What should a defer of an Insight that has no page do?**
  - Recommended: (a) write no page and fail that entry alone, as for a defer of a check with no page.
  - Answer: agreed, (a).
- **Which kinds of page does the fix cover?**
  - Recommended: (b) every kind except a rule or an entity: a stand-in page is written only for a rule or an entity, and a defer of any other kind with no page fails alone.
  - Answer: agreed, (b).
- **Should `/pre-spec` also report such a defer before the librarian's run?**
  - Recommended: (a) yes, by the same test of whether a page exists that `guppi generate` uses; the Case becomes two parts, each rewriting one existing check.
  - Answer: agreed, (a).

## History

- 2026-10-13 created · raw/2026-10-12/2349/ledger.md#case-786
