---
type: estimate
kind: QA
status: pending
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

## Method

`make test-documentation`, the pipeline over tests/test_materialize.py, tests/test_generate.py and tests/test_cleanup.py; the live reading by hand

## Result

the librarian run of session H (2026-09-11 12:10–12:21, commit 10731cb) read again against the criterion of case 58: make test 158 green; every decision line of Cases 52–57 has its Decision page and targets, 79 entries none unapplied, none failed; every wiki page opened is named in the report with reason and outcome; no ledger, spec, plan, decision page or archive file read; the yaml edited only by the index check and synthesis entries; commands in the event log; commit separate, vault/ only; no stop; the one read outside the four inputs was the Makefile at 12:18:26, which the criterion now allows as the scripts' own file — Slice 3 closes

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36
- 2026-09-10 status: pending → failed · raw/2026-09-10/ledger.md#L89
- 2026-09-10 updated: a read beyond the four inputs is allowed for one of three named reasons; session artifacts, code and yaml repairs are not · raw/2026-09-10/ledger.md#case-44
- 2026-09-11 status: failed → failed · raw/2026-09-10/ledger.md#L123
- 2026-09-11 updated: four indexes; four reasons; outcome named · [[decision-case-54]]
- 2026-09-12 status: pending → failed · raw/2026-09-11/ledger.md#L74
- 2026-09-12 status: failed → passed · raw/2026-09-12/ledger.md#L35
- 2026-09-12 updated: the Makefile, guppi/ and tests/ leave the forbidden set; pending for the reading against the new criterion (case 58) · [[decision-case-58]]
