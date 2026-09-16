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
The cascade of `generate` computes `built` on an Entity or a Rule once each of its Estimates is `passed`; `cleanup` sets `archived`.
**＋** The guard refuses `Edit` and `Write` of a file a live Rule page names in `governs`.
**＋** `sprint_id` reads the first `## <id>` heading of `sprint.md`.
**＋** Order is the content of a page, not a field of an Entity MOC (`index.md` §6).
**－** The script writes no page of `wiki/`: it reads statuses and writes one file.

When:
`guppi sprint` runs with a live page `entity-sprint-migration`.

Then:
The file `vault/wiki/sprint.md` gets: `# Sprint`; `## <id>`, the id being the page's slug without `entity-sprint-`; the text of the page's `## Purpose` as it is; `**Done when**` — one line per Estimate of the page's `estimates`: `- [x]` when `passed`, `- [ ]` otherwise, then the Estimate's `purpose` and its status.
**＋** Then the page's `## Backlog`: each `### <Slice>` as a heading, each item line `- [[slug]] — <text>` as `- [x]` when the page `slug` is `built`, `passed` or `archived`, `- [ ]` otherwise, with its status and, when present, its `deferred_by` after ` · `.
**＋** A Slice whose every item is `[x]` gets `[x]` in its heading; a Slice without items stays open.
**＋** The page's `## Closed` section is copied as it is, after the backlog.
**－** An item whose `slug` has no live or archived page: one line on stderr, exit 1, the file not written.
**－** The file holds nothing beyond this: no line by hand, no history.

## History

- 2026-09-17 created · [[decision-case-209.1]]
