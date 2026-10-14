---
type: rule
kind: Leaf
purpose: Prevents the sprint's backlog from drifting from the pages it names
status: built
enforcement: check
implementation_ref: [guppi/sprint.py, tests/test_sprint.py, guppi/generate.py, tests/test_generate.py]
governs: vault/wiki/sprint.md
parent: "[[rule-documentation]]"
estimates: []
applies_to: ["[[entity-sprint]]"]
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, workflow, harness, librarian, sprint]
core: true
---

## Purpose

Prevents the sprint's backlog from drifting from the pages it names. The sprint is
a page — an Entity Leaf `entity-sprint-<id>` under the MOC `entity-sprint`, whose `estimates` are its Definition of done, read before its close, one that has not passed by then going to the archive with the sprint page, its status kept in the record of the close, as `rule-sprint-close` sets it — rendered under Done when and never written as an item line of a milestone or of the Backlog, so that each milestone holds exactly the items whose closing closes it — and whose `## Milestones` lists the Slices in order and whose `## Backlog` the items without a turn, each a wikilink to a page or a plain line. `vault/wiki/sprint.md`
is not a document: `guppi sprint` writes it from that page, one tick per item by the status of the page it names; the `## Milestones` of the page render in order — a closed one as one line, the current one whole, a later one as one line with its count and its items by slug; the `## Backlog` of the page, the items without a turn, is not rendered here — `guppi backlog` shows it in `backlog.md`; an item names its pages by every `[[slug]]` before the first ` — `, and is ticked when each of them is `built`, `passed` or `archived`, the statuses after ` · ` in the order of the slugs; a wikilink after the ` — ` is text. A line with no wikilink before the ` — ` is a note — a task not yet cut into pages: `- [ ] <text>`, no status, never ticked, keeping its milestone open until the `update` of the Case that cuts it into items or removes it. The librarian runs the script after `cleanup` and
`render`, before the brief, so the file shows the pages of that same run; `/hi`
reads the file as before. `governs` names the file, so the governed-files hook
refuses a hand edit; the milestones and the backlog change only by an `update` of the sprint page, a Case: `generate` moves no line of the page, however many sessions put an item off.
The first `## <id>` heading of the file is the sprint id `sprint_id`, `cleanup` and `archive` read, unchanged. With no live sprint page, after the close of a sprint, the script writes the file as `# Sprint`, the heading `## <id> — closed` and one line that no sprint is open since the close of `<id>`, the id the file named before, and exits 0; `sprint_id` reads `<id>` from it, and the hook of `rule-skill-sprint-open` reads the mark. `guppi sprint --check` renders in memory and names the file when it differs, exit 1, writing nothing; `make lint` runs it after `render --check`. Once the plain `guppi sprint` wrote the file and exits 0, it ticks every unticked task line that opens with a code span holding `guppi sprint` — never a `read` line that names the command later, nor a line whose code span holds `guppi sprint-close`, which that command ticks — in the `spec.md` of every unit under `raw/` whose yaml is applied whole; `--check` and an exit 1 tick nothing.

## History

- 2026-10-14 shipped with GUPPI
