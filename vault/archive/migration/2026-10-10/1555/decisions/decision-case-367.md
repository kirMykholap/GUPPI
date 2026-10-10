---
type: decision
case: "367"
status: archived
update: ["[[estimate-sprint-migration-rule-class-files-dissolved]]"]
origin: raw/2026-09-23/1126/ledger.md#case-367
sprint: migration
created: 2026-09-23
tags: [sprint, workflow, harness]
---

## Context

The `method` and the When of `estimate-sprint-migration-rule-class-files-dissolved` ask for `make lint` exit 0 at the close of Slice 3f. `make lint` checks the whole vault, and in this session it gave 100 findings, exit 2: 62 on the legacy Decision pages of Cases 1–28, 31 `unread`, 3 on `rule-spec-box`, 3 `deferred`, 1 `unmigrated` — none on what Slice 3f did, the schemas, the glossary, `index.md`, the `file` route. The exit 0 is the promise of `estimate-sprint-migration-lint-clean`, at the close of the sprint, when the legacy Decision pages go to the archive. So the Estimate of a closed Slice cannot pass before the sprint closes. Apart from that, the grep of the `method` does not catch the word "Rule-class", which Case 365 takes out of the docstrings and test names, and nothing would check it.
Both Estimates stand `pending`, their target `entity-sprint-migration` (`draft`); `-lint-clean` is not touched; the "Done when" line of `sprint.md` takes the `purpose`, which does not change; no `create`.

## Problem

The Estimate of one Slice waits for a clean lint of the whole sprint, and its grep does not see the term the Slice retired.

## History

- 2026-09-23 created · raw/2026-09-23/1126/ledger.md#case-367
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
