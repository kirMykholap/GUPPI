---
type: rule
kind: Leaf
purpose: Prevents an archived page from staying among the live ones
status: built
enforcement: check
implementation_ref: [guppi/cleanup.py, tests/test_cleanup.py]
parent: "[[rule-documentation]]"
estimates: ["[[estimate-cleanup-moves]]", "[[estimate-cleanup-files-a-session-by-its-sprint]]"]
origin: raw/2026-09-10/ledger.md#case-33
sprint: migration
created: 2026-09-10
tags: [harness, workflow]
---

## Purpose

Prevents an archived page from staying among the live ones. `archived` is a status the generator sets, and `guppi sprint-close` at the close of a sprint (`rule-sprint-close`, case 627.1). The file move
is this script's, so a page never disappears by an agent's hand. `raw/<date>/` is not
this script's: `guppi archive` moves an applied session ([[rule-raw-archive]]).

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-33
- 2026-09-10 estimate estimate-cleanup-moves added · raw/2026-09-10/ledger.md#case-33
- 2026-09-10 status: draft → built · cascade
- 2026-09-11 updated: four indexes; estimates lists of entities and rules only · [[decision-case-57]]
- 2026-09-13 updated: raw/ is guppi archive's, not cleanup's (case 100.4) · [[decision-case-100.4]]
- 2026-09-13 updated: the root is vault/archive/, the page lands under the session of the run (case 102.2) · [[decision-case-102.2]]
- 2026-09-13 status: built → draft · cascade
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 updated: cleanup rewrites no index; the files are gone (case 147.6) · [[decision-case-147.6]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-15 status: draft → built · cascade
- 2026-09-15 updated: unlink edits the field only, no section rebuilt (case 166.4) · [[decision-case-166.4]]
- 2026-09-15 status: built → draft · cascade
- 2026-09-15 status: draft → built · cascade
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-10-04 updated: guppi sprint-close also sets archived (case 627.1) · [[decision-case-627.1]]
- 2026-10-04 updated: ## How it works left the Leaf, its mechanism in the docstring of guppi/cleanup.py (case 632.1) · [[decision-case-632.1]]
- 2026-10-10 estimate estimate-cleanup-files-a-session-by-its-sprint added · [[decision-case-770]]
