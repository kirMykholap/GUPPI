---
type: decision
case: "233.4"
status: current
update: ["[[rule-carry-over]]", "[[estimate-carry-over-writes]]"]
origin: raw/2026-09-17/1119/ledger.md#case-233.4
sprint: migration
created: 2026-09-17
tags: [session, workflow, harness, render]
---

## Context

`pretask --check` was clean after three corrections of form: the defer of `index` had no `file:`, F5 ended in the wrong word, F9 pointed at a defer of another plan — closed as `work`. `ask-guppi` read the Spec against the vault and found ten places: five sentences the ratified Cases left stale on the same or a neighbouring page, three promises the Cases did not name, two Cases disagreeing with each other. Every `replace` occurs on its page once. Known and left alone: `estimate-lint-catches` ("`make lint` runs it after `render --check`; neither writes") stays true with three steps; `estimate-documentation-completes` ("`make lint` passes its `render --check` step") too; `estimate-generate-fails-alone` ("a rerun writes nothing") holds because a rerun applies nothing; `rule-lint` "lint runs with the renderer, in no phase of the session" is true. Six corrections went into the ratified Cases in place, without a new line: 224.2 (the "Work Mode ticks the boxes" sentence of `rule-case-protocol` and the line in `estimate-case-protocol-loaded`), 224.3 (the Insight's `pattern`, the new lesson not its child), 226.2 (`rule-render-harness` Purpose: the librarian's step), 229.2 (`rule-sprint` Purpose: the two sections), 229.3 ("or with none"), 229.4 (the `/carry` paragraph of `rule-brief`). Five are new updates, each with its line. One touches `index.md`, which Case 230 defers: by case 186.2 a finding, shown here — the defer is about the definitions of §1 and §6, the change a table row on `sprint.md` and a word in §2.

## Problem

A ratified Case leaves a sentence false on a page it did not name, or a promise unnamed; the vault would say two things.

## History

- 2026-09-18 created · raw/2026-09-17/1119/ledger.md#case-233.4
