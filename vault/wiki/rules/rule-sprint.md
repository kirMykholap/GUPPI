---
type: rule
kind: Leaf
purpose: Prevents the sprint's backlog from drifting from the pages it names
status: built
enforcement: check
implementation_ref: [guppi/sprint.py, tests/test_sprint.py]
governs: vault/wiki/sprint.md
parent: "[[rule-documentation]]"
estimates: ["[[estimate-sprint-renders-the-backlog]]", "[[estimate-sprint-checks-the-file]]"]
origin: raw/2026-09-16/2238/ledger.md#case-209
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness, librarian, sprint]
---

## Purpose

Prevents the sprint's backlog from drifting from the pages it names. The sprint is
a page — an Entity Leaf `entity-sprint-<id>` under the MOC `entity-sprint` (case 241), whose `estimates` are its Definition of done and whose `## Milestones` lists the Slices in order and whose `## Backlog` the items without a turn, each a wikilink to a page or a plain line (case 229). `vault/wiki/sprint.md`
is not a document: `guppi sprint` writes it from that page, one tick per item by the status of the page it names; the `## Milestones` of the page render in order — a closed one as one line, the current one whole, a later one as one line with its count and its items by slug (case 236) — and the `## Backlog`, the items without a turn, as a list; an item without a wikilink is a plain line, never ticked (case 229.2). The librarian runs the script after `cleanup` and
`render`, before the brief, so the file shows the pages of that same run; `/hi`
reads the file as before. `governs` names the file, so the governed-files hook
refuses a hand edit; the backlog changes by an `update` of the sprint page, a Case.
The first `## <id>` heading of the file is the sprint id `sprint_id`, `cleanup` and `archive` read, unchanged. `guppi sprint --check` renders in memory and names the file when it differs, exit 1, writing nothing; `make lint` runs it after `render --check` (case 227).

## History

- 2026-09-17 created · [[decision-case-209]]
- 2026-09-17 estimate estimate-sprint-renders-the-backlog added · [[decision-case-209.1]]
- 2026-09-18 estimate estimate-sprint-checks-the-file added · [[decision-case-227]]
- 2026-09-18 updated: sprint --check, run by make lint, names a drifted sprint.md (case 227) · [[decision-case-227]]
- 2026-09-18 updated: the render by milestone — the current one whole, the others one line, the Backlog a list, a plain item never ticked; the Purpose names the two sections (cases 229.2, 233) · [[decision-case-229.2]]
- 2026-09-18 updated: a later milestone's line names its items by slug after the count (case 236) · [[decision-case-236]]
- 2026-09-18 updated: the sprint page is a Leaf under the MOC entity-sprint (case 241) · [[decision-case-241]]
- 2026-09-18 status: draft → built · cascade
