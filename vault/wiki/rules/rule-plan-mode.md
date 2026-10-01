---
type: rule
kind: MOC
purpose: Prevents work being planned against stale or contradictory vault state
status: draft
parent: "[[rule-session]]"
children: ["[[rule-ask]]", "[[rule-prespec-hook]]", "[[rule-prespec]]", "[[rule-spec-capture]]", "[[rule-case-protocol]]", "[[rule-spec-write]]", "[[rule-spec-reconcile]]", "[[rule-case-build]]", "[[rule-case-check]]", "[[rule-skill-grill-me]]", "[[rule-skill-wait-what]]", "[[rule-prespec-onward]]"]
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
touches no Estimate; an `update` of a `Render` touches no Estimate of the live reading, which promises only that the file equals the Render and is loaded (case 378.5).

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
- 2026-09-20 ref `rule-pretask` → `rule-prespec` · [[decision-case-261]]
- 2026-09-20 ref `rule-pretask-hook` → `rule-prespec-hook` · [[decision-case-261]]
- 2026-09-20 updated: rule-case-protocol joins the children, last (case 273.1) · [[decision-case-273.1]]
- 2026-09-22 updated: the parent is rule-session, the MOC of the five phases (case 316) · [[decision-case-316]]
- 2026-09-23 updated: the live reading of a Render does not depend on its content (case 378.5) · [[decision-case-378.5]]
- 2026-09-24 child rule-spec-write added · [[decision-case-387.2]]
- 2026-09-24 child rule-spec-reconcile added · [[decision-case-387.3]]
- 2026-09-24 child rule-frame-check added · [[decision-case-391.1]]
- 2026-09-25 status: built → draft · cascade
- 2026-09-25 status: draft → built · cascade
- 2026-09-25 child rule-case-check added · [[decision-case-419.3]]
- 2026-09-25 ref `rule-frame-check` → `rule-case-build` · [[decision-case-425]]
- 2026-09-27 child rule-skill-grill-me added · [[decision-case-443.1]]
- 2026-09-28 child rule-skill-wait-what added · [[decision-case-477.2]]
- 2026-09-29 status: built → draft · cascade
- 2026-10-01 child rule-prespec-onward added · [[decision-case-561.5]]
