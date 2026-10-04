---
type: rule
kind: Leaf
purpose: Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow
status: draft
enforcement: check
implementation_ref: [guppi/sprint_close.py, tests/test_sprint_close.py]
estimates: ["[[estimate-sprint-close-archives-the-decisions]]", "[[estimate-sprint-close-archives-done-insights-and-lone-lessons]]", "[[estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest]]", "[[estimate-sprint-close-settles-unread-estimates]]", "[[estimate-sprint-close-runs-in-the-librarian-run]]", "[[estimate-sprint-close-takes-the-readings-in-groups]]", "[[estimate-sprint-close-next-session-opens-the-sprint]]"]
applies_to: ["[[entity-sprint]]"]
origin: raw/2026-10-03/0317/ledger.md#case-612.1
sprint: migration
created: 2026-10-03
tags: [sprint, workflow]
---

## Purpose

Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow: without a close, the Decision pages, the `actioned` Insights, the `error` lessons that joined no Insight, the sprint page and its Estimates of every past sprint stay among the pages that each search of the vault reads (cases 612, 627.1, 632.1).

## History

- 2026-10-03 created · [[decision-case-612.1]]
- 2026-10-03 estimate estimate-sprint-close-archives-the-decisions added · [[decision-case-612.1]]
- 2026-10-03 estimate estimate-sprint-close-archives-done-insights-and-lone-lessons added · [[decision-case-612.2]]
- 2026-10-03 estimate estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest added · [[decision-case-612.3]]
- 2026-10-03 estimate estimate-sprint-close-settles-unread-estimates added · [[decision-case-612.4]]
- 2026-10-04 updated: the close is the command guppi sprint-close, its preview and its run with --apply, the choices by slug; the close goes ahead once each Estimate of the sprint page is read or archived unread, a failed reading settling it; the guard named; where the close runs pointed to How it works (case 627.1) · [[decision-case-627.1]]
- 2026-10-04 updated: where the close runs, in How it works: the librarian's run of a session of its own, from the closing Case's task line; the readings taken in groups first; the next sprint opened first by the next session; the Backlog of a closed sprint kept in backlog.md (case 628.1) · [[decision-case-628.1]]
- 2026-10-04 estimate estimate-sprint-close-runs-in-the-librarian-run added · [[decision-case-628.1]]
- 2026-10-04 estimate estimate-sprint-close-takes-the-readings-in-groups added · [[decision-case-628.2]]
- 2026-10-04 estimate estimate-sprint-close-next-session-opens-the-sprint added · [[decision-case-628.3]]
- 2026-10-04 updated: ## How it works left the Leaf: the mechanism in the docstring of guppi/sprint_close.py, the closing session in orchestration.md; the Purpose states the failure it prevents (case 632.1) · [[decision-case-632.1]]
