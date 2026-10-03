---
type: rule
kind: Leaf
purpose: Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow
status: draft
estimates: ["[[estimate-sprint-close-archives-the-decisions]]", "[[estimate-sprint-close-archives-done-insights-and-lone-lessons]]", "[[estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest]]", "[[estimate-sprint-close-settles-unread-estimates]]"]
applies_to: ["[[entity-sprint]]"]
origin: raw/2026-10-03/0317/ledger.md#case-612.1
sprint: migration
created: 2026-10-03
tags: [sprint, workflow]
---

## Purpose

Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow. The close of `entity-sprint-<id>` reads the Estimates the sprint page lists first, and its pages move only once each of them has passed. Then the Decision pages of the sprint go to the archive, but a Decision page that a live page names in `deferred_by` or `addressed_by` stays (case 612.1). The `actioned` Insights of the sprint go, and its `error` lessons that joined no Insight; its `knowledge` lessons, its `open` Insights and their lessons stay (case 612.2). The sprint page and the Estimates it lists go; every other `passed` Estimate stays, the contract of its rule (case 612.3). Before anything moves, each Estimate that stands `pending` or `failed` is put to the person, who has it read, carries it into the next sprint, or archives it unread (case 612.4). Where the close runs, and how the next sprint opens, are not decided: the Case that decides them gives this rule its guard, and changes the texts that say a lesson, an Insight or a Decision page leaves only through its own event, or that an `actioned` Insight stays live for a later lesson: `rule-insights-schema`, `rule-lessons-schema`, `rule-decisions-schema`, `rule-synthesis`, `estimate-synthesis-clusters` and `estimate-synthesis-keeps-actioned-by-the-mark`.

## History

- 2026-10-03 created · [[decision-case-612.1]]
- 2026-10-03 estimate estimate-sprint-close-archives-the-decisions added · [[decision-case-612.1]]
- 2026-10-03 estimate estimate-sprint-close-archives-done-insights-and-lone-lessons added · [[decision-case-612.2]]
- 2026-10-03 estimate estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest added · [[decision-case-612.3]]
- 2026-10-03 estimate estimate-sprint-close-settles-unread-estimates added · [[decision-case-612.4]]
