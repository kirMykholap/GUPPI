---
type: decision
case: "18.3"
status: archived
update: [estimates-schema]
origin: raw/2026-09-09/ledger.md#case-18.3
sprint: migration
created: 2026-09-09
tags: []
---

## When

```
update:
  slug: estimates-schema
  file: vault/wiki/estimates/schema.md
  change: the `## Method` row becomes — "How it is checked. On a Leaf target: the test file that performs the check, by path (`tests/test_x.py`); a check no file can perform — a live reading of a session start — says so, and is the exception. On a MOC target: the make target that runs the children's checks as one pipeline, by name; the target depends on the children's targets, so the MOC's check is the sequence, never a new test. Research: what is being measured or investigated, and how."
```

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-18.3
- 2026-09-11 migrated: targets to kind and target_slug, Now to Given, Then to When · [[decision-case-52.1]]
- 2026-09-12 fields kind and target_slug folded into create, update, delete, defer · [[decision-case-59.4]]
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
