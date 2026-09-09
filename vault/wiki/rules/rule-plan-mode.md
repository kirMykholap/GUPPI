---
type: rule
kind: MOC
purpose: Prevents work being planned against stale or contradictory vault state
status: draft
children: [rule-case-protocol, rule-ask, rule-pretask-hook, rule-pretask, rule-spec-capture]
estimates: [estimate-plan-mode-verified]
origin: raw/2026-09-09/ledger.md#case-19
sprint: migration
created: 2026-09-09
tags: [session, workflow]
---

## Purpose

Prevents work being planned against stale or contradictory vault state — deciding to build
something that already exists, or ratifying decisions that conflict with each other or
with what is already there.

## Estimates

- [[estimate-plan-mode-verified]]

## Children

1. [[rule-case-protocol]]
2. [[rule-ask]]
3. [[rule-pretask-hook]]
4. [[rule-pretask]]
5. [[rule-spec-capture]]

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-19
- 2026-09-09 updated: rule-spec-capture is the fifth child · raw/2026-09-09/ledger.md#case-20
