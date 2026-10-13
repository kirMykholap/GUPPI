---
type: decision
case: "785"
status: current
update: ["[[rule-case-build]]", "[[estimate-case-build-finds-an-existing-judgment]]"]
origin: raw/2026-10-12/2349/ledger.md#case-785
sprint: plugin
created: 2026-10-12
tags: [session, workflow, harness]
---

## Problem

`case-guppi` can name an existing function as the judgment that both sides share without reading the function the other side calls, so the two sides may still answer differently.

## Recommend

- **Where should the fix go?**
  - Recommended: (a) a new sentence in the instructions of `case-guppi` only: it reads the function each side calls and judges whether they answer alike, and `context` names both and what it found.
  - Answer: agreed, (a).
- **What should `case-guppi` do when the two functions answer differently?**
  - Recommended: (a) ask the person which answer is right: name neither function as shared, and show in a round the input where they part and what each answers there.
  - Answer: agreed, (a).
- **Should a test prove that both sides agree?**
  - Recommended: (a) a test over the input where they parted, which runs both sides and asserts they answer alike.
  - Answer: agreed, (a).
- **Which check confirms the fix?**
  - Recommended: (a) rewrite the Criterion of `estimate-case-build-finds-an-existing-judgment` whole, its purpose with it.
  - Answer: agreed, (a).

## History

- 2026-10-13 created · raw/2026-10-12/2349/ledger.md#case-785
