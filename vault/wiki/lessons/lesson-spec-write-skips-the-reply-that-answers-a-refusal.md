---
type: lesson
kind: knowledge
root_cause: the Stop hook `guppi ratified` returns 0 at once when the payload holds `stop_hook_active`, so a Case shown again in the reply that answers a refusal of a Stop hook is never written; it is written only from a reply to a new prompt of the person, and orchestration.md does not say so
status: new
source: guppi/ratified.py:821
origin: raw/2026-10-05/0109/ledger.md#L24
sprint: migration
created: 2026-10-05
tags: [workflow, hooks]
---

## Trigger

Case 642 shown again in the reply that answered the refusal of `guppi ratified` was not written into the plan file, though the reply carried its ledger line; the person saw the Case a third time.

## Root cause

the Stop hook `guppi ratified` returns 0 at once when the payload holds `stop_hook_active`, so a Case shown again in the reply that answers a refusal of a Stop hook is never written; it is written only from a reply to a new prompt of the person, and orchestration.md does not say so

## History

- 2026-10-05 created · raw/2026-10-05/0109/ledger.md#L24
