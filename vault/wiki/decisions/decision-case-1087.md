---
type: decision
case: "1087"
status: current
children: ["[[decision-case-1087.1]]", "[[decision-case-1087.2]]", "[[decision-case-1087.3]]", "[[decision-case-1087.4]]", "[[decision-case-1087.5]]", "[[decision-case-1087.6]]", "[[decision-case-1087.7]]", "[[decision-case-1087.8]]", "[[decision-case-1087.9]]", "[[decision-case-1087.10]]", "[[decision-case-1087.11]]", "[[decision-case-1087.12]]", "[[decision-case-1087.13]]", "[[decision-case-1087.14]]"]
origin: raw/2026-11-27/2214/ledger.md#case-1087
sprint: plugin
created: 2026-11-27
tags: [hooks, harness, workflow, session, plugin, render, ledger]
---

## Problem

The plan view that the person approves shows every ratified Case in full below the map, while the person wants it to show the map alone.

## Recommend

- **Where the Cases stand from ratification to approval**
  - Recommended: (a) a file beside the plan file until the approval; the approval hook writes the map and then those Cases into `spec.md`.
  - Answer: the person first asked why not `spec.md` itself, holding the Cases whole as the plan file did while the plan file shown for approval is the map; after the round set the two side by side, agreed to (a).
- **What the session's spec.md holds after the approval**
  - Recommended: (a) the map and the Cases, as today.
  - Answer: agreed, (a); the person's own picture also had `spec.md` hold the Cases whole.

## History

- 2026-11-28 created · raw/2026-11-27/2214/ledger.md#case-1087
