---
type: estimate
kind: QA
status: passed
target: "[[rule-sprint]]"
purpose: guppi sprint writes sprint.md from the sprint page, one tick per item by the status of the page it names
method: pytest .guppi/tests/test_sprint.py, plus one reading of the rendered sprint.md after the librarian's run
checked: 2026-09-27
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, sprint]
core: true
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

2026-09-27, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
