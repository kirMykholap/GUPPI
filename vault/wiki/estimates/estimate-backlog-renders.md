---
type: estimate
kind: QA
status: passed
target: "[[rule-backlog]]"
purpose: guppi backlog writes backlog.md from the conserved Specs, the pages with deferred_by, the open Insights and the Backlog of each sprint page, live or archived, a line of a closed sprint left out once the live sprint takes it or its pages are finished, each item with its purpose and its count
method: uv run --project .guppi pytest .guppi/tests/test_backlog.py
checked: 2026-10-31
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, sprint]
core: true
---

## Criterion

When:
`uv run --project .guppi guppi backlog` runs over `vault/wiki/`, `vault/raw/` and `vault/archive/`. The librarian runs it after `guppi sprint`, and the skill `carry` runs it after it writes `carry.md`.
**＋** Or `.guppi/tests/test_backlog.py` runs `.guppi/guppi/backlog.py` over a made-up vault.

Then:
The script writes `vault/wiki/backlog.md`: the heading `# Backlog`, the line `N items`, then `## Conserved Specs` and `## Deferred`.
**＋** `## Conserved Specs` holds each session folder under `vault/raw/` that holds `carry.md`. Each has one line that names its `spec.md` and its Cases. Under that line stands one line per item of its `then` blocks, with the kind and the slug, read by the Spec reader of `.guppi/guppi/materialize.py`.
**＋** `## Deferred` holds one line per item. The items are each live page with a `deferred_by` that is not empty, each Insight whose `status` is `open`, and each line of the `## Backlog` of each `entity-sprint-<id>`, live under `vault/wiki/entities/` or archived under `vault/archive/`. A line holds the slug, the page's `purpose` (for an Insight, its `pattern` and `severity`) and the count. A Backlog line that names no page stands by its text.
**＋** The count of an item is the number of sessions whose `frontier.md`, under `vault/raw/` or `vault/archive/`, holds a `[-]` line that names its slug in a code span of its title. It is read by `generate.frontier_marks`, and `.guppi/guppi/backlog.py` holds no copy of that reader.
**＋** `N` counts the conserved Specs and the lines of `## Deferred`. A slug that stands under a conserved Spec does not stand again under `## Deferred`, and a slug of two sources stands once.
**＋** A folder whose `carry.md` is gone shows nothing. Its defers enter `## Deferred` through `deferred_by` once `materialize` and `generate` have applied them.
**－** A slug of a line of the `## Backlog` of an archived sprint page does not stand when the live sprint page names it in its `## Milestones` or its `## Backlog`, or when its page stands `built`, `passed` or `archived`, the statuses that tick an item in `.guppi/guppi/sprint.py`.
**－** A line of the `## Backlog` of an archived sprint page that names no page does not stand when the live sprint page holds a line of the same text.
**－** The script writes no page of `vault/wiki/` and no file but `vault/wiki/backlog.md`. The governed-files hook refuses a hand edit of that file.

## Result

2026-10-31, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
