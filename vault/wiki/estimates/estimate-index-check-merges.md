---
type: estimate
kind: QA
status: passed
target: "[[rule-index-check]]"
purpose: The librarian's index check turns a create whose thing already has a page into an update of that page and marks a near one, comparing within one category by the Grep of its index lines
method: by hand on the report of a later librarian's run, against its materialize.yaml
checked: 2026-09-29
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, librarian]
core: true
---

## Criterion

When:
The librarian's run does the index check of `.claude/agents/librarian-guppi.md`, as rendered from `rule-index-check`, over the `create` entries of each `materialize.yaml`.

Then:
For each `create` other than an Estimate, the librarian runs the Grep of its category under `vault/wiki/`: `^(purpose|deferred_by):`, `root_cause` for lessons, `pattern` for insights. It compares the entry's `purpose`, or `root_cause` for a lesson, with every line the Grep returns.
**＋** The report names each Grep and the number of lines compared.
**＋** A `create` whose thing already has a page becomes an `update` of that slug with `change: "merged by librarian: <why>"` and `librarian: merged`, every other field of the entry as it was.
**＋** A page that is close but not the same keeps the entry and adds `near: <slug>`.
**＋** Every page opened is named in the report, with the index line that did not settle same or near.
**－** No comparison crosses categories.

## Result

2026-09-29, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
