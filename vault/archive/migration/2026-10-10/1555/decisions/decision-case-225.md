---
type: decision
case: "225"
status: archived
update: ["[[rule-carry-over]]"]
supersedes: ["[[decision-case-223]]"]
origin: raw/2026-09-17/1119/ledger.md#case-225
sprint: migration
created: 2026-09-17
tags: [session, workflow, harness, render]
---

## Context

`rule-carry-over` (`draft`, parent `rule-end-of-work`) carries a `ref: rule-end-of-work` field beside `parent` — the same lift as on the 15 Estimate pages of case 210 (`lesson-materialize-item-ref-lifted-as-a-page-field`), on a rule page; `rules/schema.yaml` names no `ref`. Case 214.1 keeps `ref` off every page from now on; case 210 named the Estimate pages only, and Work Mode left this one as it stood. Case 223 deferred it to this Plan Mode; today it is the one live page of `wiki/` with `ref:` in its frontmatter — a grep over every category. `set` in `generate` assigns a value and cannot remove a key; an `update` with `change` alone it applies — a History line with the pointer, the page saved. The Case touches no Estimate: no rule changes; `estimate-carry-over-writes` stands `pending` for its own reason.

## Problem

One live rule page carries a field nobody ratified; the one-off of 210 did not cover it, and Retro ratifies no update. `deferred_by: decision-case-223` on the page is cleared only by a ledger line with `{supersedes:case 223}` — and case 210 had no ledger line at all, so its form cannot simply be repeated.

## History

- 2026-09-18 created · raw/2026-09-17/1119/ledger.md#case-225
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
