---
type: lesson
kind: knowledge
root_cause: "materialize folds an `estimate[...]` reading into the live `create` entry of its slug, and when that entry is skipped or marked superseded the reading lands nowhere and no `estimate` entry of its own is made; case 309 promises that second path, but the 0014 yaml carries entries for lines 1–51, 58 and 60 of a 64-line ledger with `unparsed: []`, so the yaml is not a complete record of the ledger and cannot answer which line a run did not apply."
status: new
source: vault/raw/2026-09-22/0014/materialize.yaml
origin: raw/2026-09-22/2046/ledger.md#L22
sprint: migration
created: 2026-09-22
tags: [harness, ledger]
---

## Trigger

the brief of the 0014 walk had to name the ledger lines the run did not apply, and the yaml held no entry for them — the librarian read the ledger instead and flagged the breach.

## Root cause

materialize folds an `estimate[...]` reading into the live `create` entry of its slug, and when that entry is skipped or marked superseded the reading lands nowhere and no `estimate` entry of its own is made; case 309 promises that second path, but the 0014 yaml carries entries for lines 1–51, 58 and 60 of a 64-line ledger with `unparsed: []`, so the yaml is not a complete record of the ledger and cannot answer which line a run did not apply.

## History

- 2026-09-23 created · raw/2026-09-22/2046/ledger.md#L22
