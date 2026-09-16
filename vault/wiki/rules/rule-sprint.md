---
type: rule
kind: Leaf
purpose: Prevents the sprint's backlog from drifting from the pages it names
status: draft
enforcement: check
implementation_ref: [guppi/sprint.py, tests/test_sprint.py]
governs: vault/wiki/sprint.md
parent: "[[rule-documentation]]"
estimates: ["[[estimate-sprint-renders-the-backlog]]"]
origin: raw/2026-09-16/2238/ledger.md#case-209
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness, librarian, sprint]
---

## Purpose

Prevents the sprint's backlog from drifting from the pages it names. The sprint is
a page — an Entity MOC whose `estimates` are its Definition of done and whose
`## Backlog` lists the open Slices, each item a wikilink to a page. `vault/wiki/sprint.md`
is not a document: `guppi sprint` writes it from that page, one tick per item by the
status of the page it names. The librarian runs the script after `cleanup` and
`render`, before the brief, so the file shows the pages of that same run; `/hi`
reads the file as before. `governs` names the file, so the governed-files hook
refuses a hand edit; the backlog changes by an `update` of the sprint page, a Case.
The first `## <id>` heading of the file is the sprint id `sprint_id`, `cleanup` and
`archive` read, unchanged.

## History

- 2026-09-17 created · [[decision-case-209]]
- 2026-09-17 estimate estimate-sprint-renders-the-backlog added · [[decision-case-209.1]]
