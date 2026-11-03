---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of the file of a Case sends case-guppi a note once for an update of a page that the cascade of generate archives after an item of the file or of another Case of the session, by the judgment pre-spec prints
method: uv run --project .guppi pytest .guppi/tests/test_casecheck.py -k cascade
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [hooks, harness, workflow]
core: true
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` writes a file of Cases, and `uv run --project .guppi guppi casecheck --subagent` reads the Cases of the file, the plan file of the session, `<plan>.checked.json` beside it and the session's `raw/<date>/<hi HHMM>/ledger.md`.
**＋** Or `.guppi/tests/test_casecheck.py` runs it over a made-up file, plan file, store and ledger.

Then:
The hook judges the Cases of the file with the other Cases of the session, as `other_blocks` of `.guppi/guppi/casecheck.py` gives them, by the function of `.guppi/guppi/prespec.py` that prints the cascade notes of pre-spec, imported, not copied.
**＋** Which pages, items and Cases give a note is what `estimate-prespec-notes-a-page-the-cascade-archives` sets for that function; this check adds only who gets the note and how.
**＋** The note goes to `case-guppi` under the Case of the file it names, and asks it to drop the change or to give the reason in `context`.
**＋** The note is sent back once by exit 2 beside any findings, stored under `notes` in `<plan>.checked.json`, and not sent again for the same Case id.
**－** The note is no finding: the Case is stored with no finding for it, and the `Stop` check of `guppi casecheck` refuses no showing for it.
**－** Two other Cases of the session give the file no note.

## Result

2026-10-08, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
