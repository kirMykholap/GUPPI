---
type: rule
kind: MOC
purpose: Prevents work being planned against stale or contradictory vault state
status: built
children: ["[[rule-ask]]", "[[rule-pretask-hook]]", "[[rule-pretask]]", "[[rule-spec-capture]]"]
estimates: ["[[estimate-plan-mode-verified]]"]
deferred_by: ["[[decision-case-178]]"]
origin: raw/2026-09-09/ledger.md#case-19
sprint: migration
created: 2026-09-09
tags: [session, workflow]
---

## Purpose

Prevents work being planned against stale or contradictory vault state — deciding to build
something that already exists, or ratifying decisions that conflict with each other or
with what is already there.

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-19
- 2026-09-09 updated: rule-spec-capture is the fifth child · raw/2026-09-09/ledger.md#case-20
- 2026-09-12 updated: rule-case-protocol moved under rule-claude-md (case 66) · [[decision-case-66]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-15 deferred · [[decision-case-178]]
