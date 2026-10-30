---
type: rule
kind: Leaf
purpose: Keeps raw/ to the sessions not yet turned into pages, by moving an applied session whole into the archive
status: built
enforcement: check
implementation_ref: [.guppi/guppi/archive.py, .guppi/tests/test_archive.py]
parent: "[[rule-documentation]]"
estimates: ["[[estimate-raw-archive]]", "[[estimate-raw-archive-files-a-session-by-its-sprint]]"]
origin: raw/2026-09-13/ledger.md#case-100.1
sprint: migration
created: 2026-09-13
tags: [harness, librarian, ledger]
core: true
---

## Purpose

Keeps `raw/` to the sessions that are not yet fully turned into pages. A session
whose `materialize.yaml` is applied to the last entry and whose `ledger.md` has no
line outside the yaml is done; nothing reads it again, so it moves whole into the
archive of its date. A session with an entry still to apply stays, and is named
with the reason, so the debt is in view at every run until the entry is fixed in
Plan Mode.

## History

- 2026-09-13 created · [[decision-case-100.1]]
- 2026-09-13 estimate estimate-raw-archive added · [[decision-case-100.1]]
- 2026-09-13 status: draft → built · cascade
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-10-09 updated: the close of a sprint moves each done unit whatever its date (case 743.1) · [[decision-case-743.1]]
- 2026-10-09 updated: a unit goes to the archive folder of the sprint its own yaml records (case 743.2) · [[decision-case-743.2]]
- 2026-10-09 estimate estimate-raw-archive-files-a-session-by-its-sprint added · [[decision-case-743.2]]
- 2026-10-09 updated: the close of a sprint moves the old event logs (case 743.3) · [[decision-case-743.3]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: the slug of rule-sprint-close stands outside the brackets of its pointers · [[decision-case-809]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `guppi/` → `.guppi/guppi/` · [[decision-case-819.1]]
- 2026-10-15 reworded: `tests/` → `.guppi/tests/` · [[decision-case-819.1]]
- 2026-10-26 updated: the close of a sprint keeps the event logs from the start date of the open session · [[decision-case-886]]
- 2026-10-30 updated: ## How it works left the Leaf, its mechanism in the docstring of .guppi/guppi/archive.py · [[decision-case-942.1]]
