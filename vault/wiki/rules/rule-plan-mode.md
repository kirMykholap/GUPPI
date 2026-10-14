---
type: rule
kind: MOC
purpose: Prevents work being planned against stale or contradictory vault state
status: built
parent: "[[rule-session]]"
children: ["[[rule-ask]]", "[[rule-prespec-hook]]", "[[rule-prespec]]", "[[rule-spec-capture]]", "[[rule-case-protocol]]", "[[rule-spec-write]]", "[[rule-spec-reconcile]]", "[[rule-case-build]]", "[[rule-case-check]]", "[[rule-skill-grill-me]]", "[[rule-skill-wait-what]]", "[[rule-prespec-onward]]", "[[rule-orchestration]]", "[[rule-ratification]]", "[[rule-case-example]]", "[[rule-skill-sprint-close]]", "[[rule-skill-pr-review]]", "[[rule-skill-merge-main]]"]
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, workflow]
core: true
---

## Purpose

Prevents work being planned against stale or contradictory vault state — deciding to
build something that already exists, or ratifying decisions that conflict with each
other or with what is already there.

It also prevents a promise being sent for re-reading by derivation. Which Estimate a
ratified Case changes is the judgment of the Case, named in it by slug; only a
replaced Criterion sets an Estimate `pending`. An `update` of this page's `Purpose`
touches no Estimate; an `update` of a `Render` touches no Estimate of the live reading, which promises only that the file equals the Render and is loaded.

## History

- 2026-10-14 shipped with GUPPI
