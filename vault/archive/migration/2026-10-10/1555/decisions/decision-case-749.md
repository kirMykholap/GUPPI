---
type: decision
case: "749"
status: archived
create: ["[[estimate-case-check-sends-back-a-ratified-case-with-a-changed-create-line]]"]
update: ["[[rule-case-protocol]]", "[[insight-ledger-ratified-line-never-withdrawn]]"]
origin: raw/2026-10-09/0200/ledger.md#case-749
sprint: migration
created: 2026-10-09
tags: [hooks, harness, workflow, session, ledger]
---

## Problem

A Case that is ratified, built again and ratified again with a new parent or new tags for a page it creates leaves two `create` lines in the ledger. The librarian builds the page from the first, stale line, and no check before the Spec says so.

## Recommend

- **Where the fix lives**
  - Recommended: (a) the check of the case file sends the rebuilt Case back with a new number and the marks that retire the old lines, as it does for a dropped page.
  - Answer: agreed, (a).
- **Which parts of a line count as a change**
  - Recommended: (b) the parent page and the tags.
  - Answer: agreed, (b).
- **Whether the pattern page closes**
  - Recommended: (a) this Case marks `insight-ledger-ratified-line-never-withdrawn` handled, and the librarian archives the lesson of this item with it.
  - Answer: agreed, (a).
- **How the new check is checked**
  - Recommended: (a) a new Estimate of its own on `rule-case-check`; `estimate-case-check-sends-back-a-ratified-case-without-a-target` stands unchanged.
  - Answer: agreed, (a).
- **Whether the order of the tags counts**
  - Recommended: (a) order does not count; only a tag added or removed is a change.
  - Answer: agreed, (a).
- **What the send-back offers**
  - Recommended: (a) the same two ways as for a dropped page: write the line back as the ledger holds it, or move the Case to the new number with the marks, by `Edit` alone.
  - Answer: agreed, (a).

## History

- 2026-10-09 created · raw/2026-10-09/0200/ledger.md#case-749
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
