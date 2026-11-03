---
type: rule
kind: Leaf
purpose: Keeps raw/ to the sessions not yet turned into pages, by moving an applied session whole into the archive
status: built
enforcement: check
implementation_ref: [.guppi/guppi/archive.py, .guppi/tests/test_archive.py]
parent: "[[rule-documentation]]"
estimates: ["[[estimate-raw-archive]]", "[[estimate-raw-archive-files-a-session-by-its-sprint]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
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

- 2026-11-03 shipped with GUPPI
