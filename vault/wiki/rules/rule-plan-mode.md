---
type: rule
kind: MOC
purpose: Prevents work being planned against stale or contradictory vault state
status: built
children: ["[[rule-ask]]", "[[rule-pretask-hook]]", "[[rule-pretask]]", "[[rule-spec-capture]]"]
estimates: ["[[estimate-plan-mode-verified]]", "[[estimate-plan-mode-names-its-estimates]]"]
origin: raw/2026-09-09/ledger.md#case-19
sprint: migration
created: 2026-09-09
tags: [session, workflow]
---

## Purpose

Prevents work being planned against stale or contradictory vault state — deciding to
build something that already exists, or ratifying decisions that conflict with each
other or with what is already there.

It also prevents a promise being sent for re-reading by derivation. Which Estimate a
ratified Case changes is the judgment of the Case, named in it by slug; only a
replaced Criterion sets an Estimate `pending`. An `update` of this page's `Purpose`
touches no Estimate; an `update` of a `Render` touches the Estimate of the live
reading of that Render (case 187).

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-19
- 2026-09-09 updated: rule-spec-capture is the fifth child · raw/2026-09-09/ledger.md#case-20
- 2026-09-12 updated: rule-case-protocol moved under rule-claude-md (case 66) · [[decision-case-66]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-15 deferred · [[decision-case-178]]
- 2026-09-16 defer by decision-case-178 superseded · [[decision-case-182]]
- 2026-09-16 deferred · [[decision-case-182]]
- 2026-09-16 estimate estimate-plan-mode-names-its-estimates added · [[decision-case-187]]
- 2026-09-16 updated: which Estimate a Case changes is the judgment of the Case, named by slug, not derived from a flag (case 187) · [[decision-case-187]]
- 2026-09-16 defer by decision-case-182 superseded · [[decision-case-191]]
- 2026-09-16 status: built → draft · cascade
- 2026-09-16 status: draft → built · cascade
