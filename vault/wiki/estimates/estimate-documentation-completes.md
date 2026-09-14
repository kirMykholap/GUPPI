---
type: estimate
kind: QA
status: passed
target: rule-documentation
origin: raw/2026-09-10/ledger.md#case-36
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, librarian]
---

## Context

The phase either turns every ledger line into a page, or the vault and the ledger disagree silently.

## Criterion

make test-documentation runs the tests of materialize, generate and cleanup as one
pipeline, green. Live, after a librarian run: every decision line of the session's
ledger has a Decision page and its target page; no page exists that no ledger line
produced; the agent read only handoff.md, the yamls materialize named, the four
indexes and tags.md, plus the wiki pages it names in the report with one of the
four reasons of its frame (same or near; a candidate cluster; a script's error; a
fact for the brief) and the outcome, and no ledger, Spec, plan, Decision page or archive file (the Makefile,
guppi/ and tests/ are the scripts' own and may be read); it edited no yaml entry beyond the marks and the entries of the index
check and the synthesis; its commands are in event_log.md; its commit is separate
from the session's; it did not stop to ask.

### case 73.8

When:
`librarian-guppi` starts.

Then:
Its first input is the `handoff.md` the dispatch names, `raw/<hi date>/<hi HHMM>/handoff.md`;
the other three inputs are unchanged.

### case 89.1

When:
The librarian reaches the end of its run.

Then:
After `cleanup` and before the brief it runs `uv run guppi render`, and the governed
files are written from the pages of that same run.
**＋** Every line on its stderr is a flag for the brief.
**＋** `make lint` at the close then passes its `render --check` step.
**－** A file the render could not write is left to the next session start; the librarian
does not write it by hand.

### case 90.3

When:
The handoff tells the librarian to do what the criterion of `rule-documentation` forbids
— repair an entry of the yaml, or read `ledger.md`, a Spec, a decision page or the
archive.

Then:
The librarian does not do it.
**＋** It names the instruction in the report: what was asked, and why it was refused.
**－** The handoff itself is checked by nothing: it is written from memory, and the
refusal is the librarian's work, not its author's.
**－** A refusal does not stop the run: the librarian asks no questions, the person is
gone.

### case 100.2

When:
The librarian works by its frame (the Render of `rule-documentation`).

Then:
A step between Brief and Close (shown again at pre-task: the brief reads the yamls the walk named, so the archive runs after it): "Archive. Run `uv run guppi archive`. Every line on its stderr is a flag; the units it moved and the units it kept, with the reason, go into the report." The brief is already written; the commit picks the move up.
**＋** `rule-raw-archive` is the sixth child of `rule-documentation`, after `rule-cleanup`.
**＋** The ban on reading `vault/archive/` stays.
**＋** The session of the run is found as `cleanup` finds it — the latest `<HHMM>/` folder of the run day, else the nearest date back — and is skipped even when dated before the run day (a session across midnight).
**＋** `estimate-documentation-completes` gets a `### case 100.2` block, `pending`.

## Method

`make test-documentation`, the pipeline over tests/test_materialize.py, tests/test_generate.py and tests/test_cleanup.py; the live reading by hand

## Result

block 100.2 against the librarian's run of session M: Archive ran after Brief (10:04:23 brief, 10:04:32 archive), moved raw/2026-09-13 and raw/2026-09-13/0652 to archive/migration/<date>/[0652/]raw, kept raw/2026-09-14/0747 as the session of the run, exit 0, stderr empty, all reported in the brief's Flags; rule-raw-archive is the sixth child of rule-documentation, after rule-cleanup

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36
- 2026-09-10 status: pending → failed · raw/2026-09-10/ledger.md#L89
- 2026-09-10 updated: a read beyond the four inputs is allowed for one of three named reasons; session artifacts, code and yaml repairs are not · raw/2026-09-10/ledger.md#case-44
- 2026-09-11 status: failed → failed · raw/2026-09-10/ledger.md#L123
- 2026-09-11 updated: four indexes; four reasons; outcome named · [[decision-case-54]]
- 2026-09-12 status: pending → failed · raw/2026-09-11/ledger.md#L74
- 2026-09-12 status: failed → passed · raw/2026-09-12/ledger.md#L35
- 2026-09-12 updated: the Makefile, guppi/ and tests/ leave the forbidden set; pending for the reading against the new criterion (case 58) · [[decision-case-58]]
- 2026-09-12 criterion: case 73.8 added · [[decision-case-73.8]]
- 2026-09-12 status: pending → failed · raw/2026-09-12/ledger.md#L168
- 2026-09-12 criterion: case 89.1 added · [[decision-case-89.1]]
- 2026-09-12 criterion: case 90.3 added · [[decision-case-90.3]]
- 2026-09-13 criterion: case 100.2 added · [[decision-case-100.2]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1029/ledger.md#L2
