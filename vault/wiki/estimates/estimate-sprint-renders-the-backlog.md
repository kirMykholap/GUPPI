---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: guppi sprint writes sprint.md from the sprint page, one tick per item by the status of the page it names
method: pytest tests/test_sprint.py, plus one reading of the rendered sprint.md after the librarian's run
checked: 2026-09-22
origin: raw/2026-09-16/2238/ledger.md#case-209.1
sprint: migration
created: 2026-09-16
tags: [harness, sprint]
---

## Criterion

Given:
The cascade of `generate` sets `built`; `cleanup` sets `archived`; `sprint_id` reads the first `## <id>` heading.
**＋** The current milestone is the first `### ` under `## Milestones` with an item not done, or with no item.
**＋** `tests/test_sprint.py` fixes the behaviour on a temp vault.
**－** The script writes no page of `wiki/`.

When:
`guppi sprint` runs with a live page `entity-sprint-<id>`.

Then:
The file: `# Sprint`; `## <id>`; Purpose; `**Done when**` — as today; then `## Milestones`: a closed milestone as one line `### [x] <name>`; the current one as the heading `### [ ] <name>` and each item with its status and `deferred_by`, as today; each later one as one line `### [ ] <name> — N items: ` and its items separated by commas, an item with a wikilink as `[[slug]]`, an item without one by its text, with no tick and no status; then `## Backlog` — each item a line; then `## Closed` as it is.
**＋** An item is ticked by the statuses of every page its `[[slug]]` before the first ` — ` names — `[x]` when each is `built`, `passed` or `archived`, the statuses after ` · ` in the order of the slugs; a wikilink after the ` — ` is text. A line with no wikilink before the ` — ` is a note: `- [ ] <text>`, never ticked, keeping its milestone open (case 313).
**＋** A milestone is closed when every item is `[x]`; with no item it is open.
**－** A slug with no live or archived page: stderr, exit 1, the file not written. `--check` (case 227) compares this same render.

## Result

2026-09-22, uv run pytest tests/test_sprint.py: 18 passed — an item of two pages ticks on both, a wikilink after the dash holds no tick back, a note renders - [ ] and keeps its milestone open; guppi sprint --check exit 0

## History

- 2026-09-17 created · [[decision-case-209.1]]
- 2026-09-18 updated: the Criterion replaced whole — the render by milestone (case 229.2) · [[decision-case-229.2]]
- 2026-09-18 updated: the Criterion replaced whole — the collapsed line of a later milestone names its items (case 236) · [[decision-case-236]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1957/ledger.md#L2
- 2026-09-22 updated: the Criterion names the pages of an item and the note (case 313) · [[decision-case-313]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L86
