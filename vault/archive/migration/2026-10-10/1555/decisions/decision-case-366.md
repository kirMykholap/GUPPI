---
type: decision
case: "366"
status: archived
update: ["[[estimate-generate-fails-alone]]"]
origin: raw/2026-09-23/1126/ledger.md#case-366
sprint: migration
created: 2026-09-23
tags: [harness, workflow, ledger, tests]
---

## Context

On an `update` with no content — none of `set`, `sections`, `replace`, `change`, `rename`, `reword` — `guppi generate` changes no page, prints `generate: <slug>: an update with no content in the Spec; nothing applied` on stdout, leaves the exit code alone and marks the entry `applied`. The words "nothing applied" came with case 320, which took the `file` route out of the scripts. One line of the Criterion of `estimate-generate-fails-alone` still expects the old words "applied by hand", and the reading L58 set the Estimate `failed`. The same reading found that no test of `tests/test_generate.py` asserts the message, which is how the words drifted unseen.
`estimate-generate-fails-alone` stands `failed`, its target `rule-page-generation` (`draft`); the Purpose of the rule says nothing of an empty `update`, so the rule page does not change; no other Estimate of the rule speaks of this branch; no `create`.

## Problem

The Criterion describes a message the code no longer prints, and no test fixes the message that it prints.

## History

- 2026-09-23 created · raw/2026-09-23/1126/ledger.md#case-366
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
