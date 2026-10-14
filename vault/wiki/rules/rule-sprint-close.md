---
type: rule
kind: Leaf
purpose: Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow
status: built
enforcement: check
implementation_ref: [guppi/sprint_close.py, tests/test_sprint_close.py]
estimates: []
applies_to: ["[[entity-sprint]]"]
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [sprint, workflow]
core: true
---

## Purpose

Prevents a closed sprint from leaving its finished work among the live pages, so that the vault does not only grow: without a close, the Decision pages, the `actioned` Insights, the `error` lessons that joined no Insight, the sprint page and its Estimates of every past sprint stay among the pages that each search of the vault reads. The close also moves to the archive each session of `vault/raw/` whose ledger is fully turned into pages, whatever its day, and the event logs that the hooks of the open session no longer read, which git still leaves out there.

## History

- 2026-10-14 shipped with GUPPI
