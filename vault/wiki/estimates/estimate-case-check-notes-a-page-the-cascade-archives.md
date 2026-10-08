---
type: estimate
kind: QA
status: passed
target: "[[rule-case-check]]"
purpose: Whether the check of the file of a Case sends case-guppi a note once for an update of a page that the cascade of generate archives after an item of the file or of another Case of the session, by the judgment pre-spec prints
method: uv run pytest tests/test_casecheck.py -k cascade
origin: raw/2026-10-08/2134/ledger.md#case-739.2
sprint: migration
created: 2026-10-08
tags: [hooks, harness, workflow]
---

## Criterion

When:
`SubagentStop` fires when `case-guppi` writes a file of Cases, and `uv run guppi casecheck --subagent` reads the Cases of the file, the plan file of the session, `<plan>.checked.json` beside it and the session's `raw/<date>/<hi HHMM>/ledger.md`.
**＋** Or `tests/test_casecheck.py` runs it over a made-up file, plan file, store and ledger.

Then:
The hook judges the Cases of the file with the other Cases of the session, as `other_blocks` of `guppi/casecheck.py` gives them, by the function of `guppi/prespec.py` that prints the cascade notes of pre-spec, imported, not copied.
**＋** Which pages, items and Cases give a note is what `estimate-prespec-notes-a-page-the-cascade-archives` sets for that function; this check adds only who gets the note and how.
**＋** The note goes to `case-guppi` under the Case of the file it names, and asks it to drop the change or to give the reason in `context`.
**＋** The note is sent back once by exit 2 beside any findings, stored under `notes` in `<plan>.checked.json`, and not sent again for the same Case id.
**－** The note is no finding: the Case is stored with no finding for it, and the `Stop` check of `guppi casecheck` refuses no showing for it.
**－** Two other Cases of the session give the file no note.

## Result

2026-10-08, Retro, uv run pytest tests/test_casecheck.py -k cascade: 8 passed — an update of a lesson another planned or stored Case archives, an item of the file archiving a page another Case updates (stored under the Case of the file) and both inside the file give one note sent once, stored under notes with no finding; two other Cases give none; a create, delete or defer gives none

## History

- 2026-10-08 created · [[decision-case-739.2]]
- 2026-10-08 status: pending → passed · raw/2026-10-08/2134/ledger.md#L12
