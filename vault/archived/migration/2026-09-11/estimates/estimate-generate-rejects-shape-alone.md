---
type: estimate
kind: QA
status: archived
target: rule-page-generation
origin: raw/2026-09-10/ledger.md#case-47
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
ref: rule-page-generation
criterion: An entry whose field has a shape the script does not expect (a mapping under replace, a string where a list is due) or in which any exception is raised is marked failed, reported on stderr and skipped; every other entry of the yaml applies; the exit code is 1; no entry ends the run.
method: tests/test_generate.py with a replace mapping and an entry that raises; live at the next librarian run
---

## Result

tests/test_generate.py 19 green with the replace-mapping and the injected-exception tests, make test 138; live 2026-09-10: the librarian's generate applied all 34 new entries and 8 decision groups with none failed, so the isolation path was not exercised live; the walk over 2026-09-09 went on past the old-harness entry, exit 0 on a rerun

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-47
- 2026-09-11 status: pending → passed · raw/2026-09-10/ledger.md#L126
- 2026-09-11 deleted · [[decision-case-53.2]]
- 2026-09-11 archived · cleanup
