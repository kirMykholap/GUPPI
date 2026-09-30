---
type: rule
kind: Leaf
purpose: "Prevents a deferred item from dropping out of sight: a defer, an open Insight, a sprint item without a turn or a conserved Spec that no list shows to the next session"
status: draft
enforcement: check
implementation_ref: [guppi/backlog.py, tests/test_backlog.py]
governs: vault/wiki/backlog.md
parent: "[[rule-documentation]]"
estimates: ["[[estimate-backlog-renders]]", "[[estimate-backlog-checks-the-file]]"]
origin: raw/2026-09-27/1255/ledger.md#case-451.4
sprint: migration
created: 2026-09-27
tags: [session, workflow, harness, librarian, sprint]
---

## Purpose

Prevents a deferred item from dropping out of sight. Before case 451 the brief carried at most seven deferred items, and an item cut off the seven stood on no list the next session read; a Spec conserved by `carry` stood only in the brief `carry` wrote. `vault/wiki/backlog.md` is not a document: `guppi backlog` writes it from what the vault already stores — each session folder under `raw/` that holds `carry.md`, with the targets of its Spec; each live page with `deferred_by`; each open Insight; each line of the `## Backlog` of the sprint page — one line per item with its `purpose`, or an Insight's `pattern` and `severity`, and the count of the sessions whose Frontier put it off. The count reads the Frontier files by `generate.frontier_marks`, and the Specs by the reader of `materialize`, one judgment in one module (`rule-one-judgment-one-implementation`). The librarian runs the script after `guppi sprint`, and `carry` after it writes `carry.md`; `/hi` loads the file, and the Frontier writes its count and names the items near a Frontier item. An item leaves when its source changes: a Case that decides it names its page on a decision line and supersedes its defer (case 467.3), an Insight is actioned, a line leaves the sprint page's `## Backlog`, or the session that finishes a conserved Spec deletes `carry.md`. `governs` names the file, so the governed-files hook refuses a hand edit; `guppi backlog --check` renders in memory and names the file when it differs, and `make lint` runs it.

## History

- 2026-09-27 created · [[decision-case-451.4]]
- 2026-09-27 estimate estimate-backlog-renders added · [[decision-case-451.4]]
- 2026-09-27 estimate estimate-backlog-checks-the-file added · [[decision-case-451.5]]
- 2026-09-27 status: draft → built · cascade
- 2026-09-27 updated: an item leaves when the Case that decides it names its page and supersedes its defer (case 467.3) · [[decision-case-467.3]]
- 2026-09-30 updated: the reader of the count named without the sprint move, removed by case 539.1 (case 539.3) · [[decision-case-539.3]]
- 2026-09-30 status: built → draft · cascade
