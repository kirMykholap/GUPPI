---
type: estimate
kind: QA
status: pending
target: rule-page-generation
origin: raw/2026-09-10/ledger.md#case-47
sprint: migration
created: 2026-09-10
tags: [harness, workflow, ledger]
ref: rule-page-generation
criterion: An entry whose field has a shape the script does not expect (a mapping under replace, a string where a list is due) or in which any exception is raised is marked failed, reported on stderr and skipped; every other entry of the yaml applies; the exit code is 1; no entry ends the run.
method: tests/test_generate.py with a replace mapping and an entry that raises; live at the next librarian run
---

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-47
