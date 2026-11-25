---
type: decision
case: "1049"
status: current
children: ["[[decision-case-1049.1]]"]
origin: raw/2026-11-25/0605/ledger.md#case-1049
sprint: plugin
created: 2026-11-25
tags: [ci, plugin, git, harness, render, sprint, workflow]
---

## Problem

The copy of GUPPI that people install carries no license text, and a license file added to it would stop the install in each project that has a license of its own.

## Recommend

- **Whether the installed project carries the license notice**
  - Recommended: (b) at the root of the copy, and a second copy inside `.guppi/` that the install copies.
  - Answer: agreed, (b).

## History

- 2026-11-25 created · raw/2026-11-25/0605/ledger.md#case-1049
- 2026-11-25 child decision-case-1049.2 archived · cleanup
