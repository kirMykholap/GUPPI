---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: guppi sprint writes sprint.md from the sprint page, one tick per item by the status of the page it names
method: pytest .guppi/tests/test_sprint.py, plus one reading of the rendered sprint.md after the librarian's run
checked: 2026-09-27
origin: raw/2026-09-16/2238/ledger.md#case-209.1
sprint: migration
created: 2026-09-16
tags: [harness, sprint]
---

## Criterion

When:
`uv run --project .guppi guppi sprint` runs with a live page `entity-sprint-<id>` and reads its `estimates`, `## Purpose`, `## Milestones` and `## Closed`.

Then:
The file `vault/wiki/sprint.md` holds, in order: `# Sprint`; `## <id>`; Purpose; `**Done when**`, one line per Estimate; then `## Milestones`; then `## Closed` as it is. Under `## Milestones`: a closed milestone is one line `### [x] <name>`. The current one is the heading `### [ ] <name>` and each item with its status and `deferred_by`. Each later one is one line `### [ ] <name> — N items: ` with its items separated by commas; an item with a wikilink stands as `[[slug]]`, an item without one by its text, with no tick and no status.
**＋** Every heading of the file stands between blank lines: a blank line follows each `### ` line, collapsed or whole.
**＋** An item is ticked by the statuses of every page its `[[slug]]` before the first ` — ` names. It is `[x]` when each is `built`, `passed` or `archived`, with the statuses after ` · ` in the order of the slugs. A wikilink after the ` — ` is text. A line with no wikilink before the ` — ` is a note, `- [ ] <text>`, never ticked, and it keeps its milestone open.
**＋** A milestone is closed when every item is `[x]`. With no item it is open.
**－** The `## Backlog` of the page is not written into the file. `vault/wiki/backlog.md` shows it.
**－** A slug with no live or archived page gives one line on stderr and exit 1, and the file is not written. `--check` compares this same render.
**－** The script writes no page of `vault/wiki/`, `entity-sprint-<id>` included.

## Result

2026-09-27, uv run pytest tests/test_sprint.py: 20 passed; by hand, vault/wiki/sprint.md as the librarian run of e229e99 wrote it: # Sprint, ## migration, Purpose, Done when, ## Milestones with the current Slice 3g whole and Slices 4 and 5 one line each, ## Closed; no ## Backlog; every heading between blank lines

## History

- 2026-09-17 created · [[decision-case-209.1]]
- 2026-09-18 updated: the Criterion replaced whole — the render by milestone (case 229.2) · [[decision-case-229.2]]
- 2026-09-18 updated: the Criterion replaced whole — the collapsed line of a later milestone names its items (case 236) · [[decision-case-236]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1957/ledger.md#L2
- 2026-09-22 updated: the Criterion names the pages of an item and the note (case 313) · [[decision-case-313]]
- 2026-09-22 status: pending → passed · raw/2026-09-22/1121/ledger.md#L86
- 2026-09-24 updated: the Criterion replaced whole — a blank line after every milestone heading (case 386) · [[decision-case-386]]
- 2026-09-27 updated: the Criterion replaced whole — the Backlog of the page is not rendered into sprint.md (case 451.6) · [[decision-case-451.6]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/1819/ledger.md#L30
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
