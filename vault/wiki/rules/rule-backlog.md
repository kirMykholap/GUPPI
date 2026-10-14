---
type: rule
kind: Leaf
purpose: "Prevents a deferred item from dropping out of sight: a defer, an open Insight, a sprint item without a turn or a conserved Spec that no list shows to the next session"
status: built
enforcement: check
implementation_ref: [guppi/backlog.py, tests/test_backlog.py]
governs: vault/wiki/backlog.md
parent: "[[rule-documentation]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, workflow, harness, librarian, sprint]
core: true
---

## Purpose

Prevents a deferred item from dropping out of sight. `vault/wiki/backlog.md` is not a document: `guppi backlog` writes it from what the vault already stores — each session folder under `raw/` that holds `carry.md`, with the targets of its Spec; each live page with `deferred_by`; each open Insight; each line of the `## Backlog` of each sprint page, live or under `vault/archive/`, so that the Backlog of a closed sprint stays in the list, as `rule-sprint-close` sets it, but for a line the live sprint page takes into its `## Milestones` or its `## Backlog` and a line whose pages are all `built`, `passed` or `archived` — one line per item with its `purpose`, or an Insight's `pattern` and `severity`, and the count of the sessions whose Frontier put it off. The count reads the Frontier files by `generate.frontier_marks`, and the Specs by the reader of `materialize`, one judgment in one module (`rule-one-judgment-one-implementation`). The librarian runs the script after `guppi sprint`, and `carry` after it writes `carry.md`; `/hi` loads the file, and the Frontier writes its count and names the items near a Frontier item. An item leaves when its source changes: a Case that decides it supersedes its defer under the condition that `rule-case-protocol` sets, an Insight is actioned, a line leaves the sprint page's `## Backlog`, a line of a closed sprint is taken by the live sprint or its pages are finished, or the session that finishes a conserved Spec deletes `carry.md`. `governs` names the file, so the governed-files hook refuses a hand edit; `guppi backlog --check` renders in memory and names the file when it differs, and `make lint` runs it.

## History

- 2026-10-14 shipped with GUPPI
