---
type: estimate
kind: QA
status: pending
target: "[[rule-backlog]]"
purpose: guppi backlog writes backlog.md from the conserved Specs, the pages with deferred_by, the open Insights and the Backlog of the sprint page, each item with its purpose and its count
method: uv run pytest tests/test_backlog.py, plus one reading of vault/wiki/backlog.md after the librarian's run
origin: raw/2026-09-27/1255/ledger.md#case-451.4
sprint: migration
created: 2026-09-27
tags: [harness, sprint]
---

## Criterion

When:
`uv run guppi backlog` runs over `vault/wiki/`, `vault/raw/` and `vault/archive/`. The librarian runs it after `guppi sprint`, and the skill `carry` runs it after it writes `carry.md`.

Then:
The script writes `vault/wiki/backlog.md`: the heading `# Backlog`, the line `N items`, then `## Conserved Specs` and `## Deferred`.
**＋** `## Conserved Specs` holds each session folder under `vault/raw/` that holds `carry.md`. Each has one line that names its `spec.md` and its Cases. Under that line stands one line per item of its `then` blocks, with the kind and the slug, read by the Spec reader of `guppi/materialize.py`.
**＋** `## Deferred` holds one line per item. The items are each live page with a `deferred_by` that is not empty, each Insight whose `status` is `open`, and each line of the `## Backlog` of `entity-sprint-<id>`. A line holds the slug, the page's `purpose` (for an Insight, its `pattern` and `severity`) and the count. A Backlog line that names no page stands by its text.
**＋** The count of an item is the number of sessions whose `frontier.md`, under `vault/raw/` or `vault/archive/`, holds a `[-]` line that names its slug in a code span of its title. It is read by `generate.frontier_marks`, the reader of the sprint move.
**＋** `N` counts the conserved Specs and the lines of `## Deferred`. A slug that stands under a conserved Spec does not stand again under `## Deferred`, and a slug of two sources stands once.
**＋** A folder whose `carry.md` is gone shows nothing. Its defers enter `## Deferred` through `deferred_by` once `materialize` and `generate` have applied them.
**－** The script writes no page of `vault/wiki/` and no file but `vault/wiki/backlog.md`. The governed-files hook refuses a hand edit of that file.

## History

- 2026-09-27 created · [[decision-case-451.4]]
