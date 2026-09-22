---
type: rule
kind: Leaf
purpose: Prevents the sprint's backlog from drifting from the pages it names
status: draft
enforcement: check
implementation_ref: [guppi/sprint.py, tests/test_sprint.py, guppi/generate.py, tests/test_generate.py]
governs: vault/wiki/sprint.md
parent: "[[rule-documentation]]"
estimates: ["[[estimate-sprint-renders-the-backlog]]", "[[estimate-sprint-checks-the-file]]", "[[estimate-sprint-ticks-the-spec]]", "[[estimate-sprint-moves-a-passed-over-item]]", "[[estimate-sprint-drops-an-emptied-milestone]]"]
applies_to: ["[[entity-sprint]]"]
origin: raw/2026-09-16/2238/ledger.md#case-209
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness, librarian, sprint]
---

## Purpose

Prevents the sprint's backlog from drifting from the pages it names. The sprint is
a page — an Entity Leaf `entity-sprint-<id>` under the MOC `entity-sprint` (case 241), whose `estimates` are its Definition of done and whose `## Milestones` lists the Slices in order and whose `## Backlog` the items without a turn, each a wikilink to a page or a plain line (case 229). `vault/wiki/sprint.md`
is not a document: `guppi sprint` writes it from that page, one tick per item by the status of the page it names; the `## Milestones` of the page render in order — a closed one as one line, the current one whole, a later one as one line with its count and its items by slug (case 236) — and the `## Backlog`, the items without a turn, as a list; an item names its pages by every `[[slug]]` before the first ` — `, and is ticked when each of them is `built`, `passed` or `archived`, the statuses after ` · ` in the order of the slugs; a wikilink after the ` — ` is text. A line with no wikilink before the ` — ` is a note — a task not yet cut into pages: `- [ ] <text>`, no status, never ticked, keeping its milestone open until the `update` of the Case that cuts it into items or removes it (cases 229.2, 313). The librarian runs the script after `cleanup` and
`render`, before the brief, so the file shows the pages of that same run; `/hi`
reads the file as before. `governs` names the file, so the governed-files hook
refuses a hand edit; the backlog changes by an `update` of the sprint page, a Case, and by one move of `generate`: a milestone item passed over in three sessions in a row goes to the Backlog, and a milestone the move left with no line leaves the Milestones (cases 354.1, 354.2).
The first `## <id>` heading of the file is the sprint id `sprint_id`, `cleanup` and `archive` read, unchanged. `guppi sprint --check` renders in memory and names the file when it differs, exit 1, writing nothing; `make lint` runs it after `render --check` (case 227). Once the plain `guppi sprint` wrote the file and exits 0, it ticks every unticked task line that opens with a code span holding `guppi sprint` — never a `read` line that names the command later — in the `spec.md` of every unit under `raw/` whose yaml is applied whole; `--check` and an exit 1 tick nothing (case 250.2).

## History

- 2026-09-17 created · [[decision-case-209]]
- 2026-09-17 estimate estimate-sprint-renders-the-backlog added · [[decision-case-209.1]]
- 2026-09-18 estimate estimate-sprint-checks-the-file added · [[decision-case-227]]
- 2026-09-18 updated: sprint --check, run by make lint, names a drifted sprint.md (case 227) · [[decision-case-227]]
- 2026-09-18 updated: the render by milestone — the current one whole, the others one line, the Backlog a list, a plain item never ticked; the Purpose names the two sections (cases 229.2, 233) · [[decision-case-229.2]]
- 2026-09-18 updated: a later milestone's line names its items by slug after the count (case 236) · [[decision-case-236]]
- 2026-09-18 updated: the sprint page is a Leaf under the MOC entity-sprint (case 241) · [[decision-case-241]]
- 2026-09-18 status: draft → built · cascade
- 2026-09-18 updated: sprint, once it wrote sprint.md and exits 0, ticks the guppi sprint lines of every applied Spec under raw/ (case 250.2) · [[decision-case-250.2]]
- 2026-09-18 estimate estimate-sprint-ticks-the-spec added · [[decision-case-250.2]]
- 2026-09-18 status: built → draft · cascade
- 2026-09-20 status: draft → built · cascade
- 2026-09-22 updated: the first edge Rule → Entity — rule-sprint is the guard of entity-sprint (cases 240.2, 305.4) · [[decision-case-305.4]]
- 2026-09-22 updated: an item names one or more pages before the ` — `; a note keeps its box and is never ticked (case 313) · [[decision-case-313]]
- 2026-09-23 updated: a milestone item passed over in three sessions in a row goes to the Backlog by generate (case 354.1) · [[decision-case-354.1]]
- 2026-09-23 estimate estimate-sprint-moves-a-passed-over-item added · [[decision-case-354.1]]
- 2026-09-23 updated: a milestone the move left with no line leaves the Milestones (case 354.2) · [[decision-case-354.2]]
- 2026-09-23 estimate estimate-sprint-drops-an-emptied-milestone added · [[decision-case-354.2]]
- 2026-09-23 status: built → draft · cascade
