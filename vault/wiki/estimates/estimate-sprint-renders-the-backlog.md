---
type: estimate
kind: QA
status: pending
target: "[[rule-sprint]]"
purpose: guppi sprint writes sprint.md from the sprint page, one tick per item by the status of the page it names
method: pytest tests/test_sprint.py, plus one reading of the rendered sprint.md after the librarian's run
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
The file: `# Sprint`; `## <id>`; Purpose; `**Done when**` — as today; then `## Milestones`: a closed milestone as one line `### [x] <name>`; the current one as the heading `### [ ] <name>` and each item with its status and `deferred_by`, as today; each later one as one line `### [ ] <name> — N items`; then `## Backlog` — each item a line; then `## Closed` as it is.
**＋** An item `- [[slug]] — <text>` is ticked by the status of its page, as today; an item `- <text>` without a wikilink renders `- [ ] <text>` and is never ticked.
**＋** A milestone is closed when every item is `[x]`; with no item it is open.
**－** A slug with no live or archived page: stderr, exit 1, the file not written. `--check` (case 227) compares this same render.

## History

- 2026-09-17 created · [[decision-case-209.1]]
- 2026-09-18 updated: the Criterion replaced whole — the render by milestone (case 229.2) · [[decision-case-229.2]]
