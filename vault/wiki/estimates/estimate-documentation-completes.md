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
fact for the brief) and the outcome, and no ledger, Spec, plan, Decision page, archive file, or file under guppi/
or tests/; it edited no yaml entry beyond the marks and the entries of the index
check and the synthesis; its commands are in event_log.md; its commit is separate
from the session's; it did not stop to ask.

## Method

`make test-documentation`, the pipeline over tests/test_materialize.py, tests/test_generate.py and tests/test_cleanup.py; the live reading by hand

## Result

live 2026-09-10 session G, librarian run 16:00–16:12, commit 58301d8: make test 138 green; the 8 decision lines of Cases 44–51 have their decision pages and targets, no entry unapplied; the report names four pages opened with a reason (two hooks lessons for a synthesis candidate, two walks-dates estimates whose index lines are empty); no ledger, spec, plan, decision page, archive file or code was read; the yaml was edited once by its own script (near marks, synthesis entries); its 34 commands are in event_log.md; the commit is separate, 58 files all under vault/; it did not stop; failed on two reads after generate not named in the report and outside the three cases: 16:09:57 sed of its own insight-harness-yaml-entry-shape-assumed, 16:10:41 grep of status on estimate pages, both for the brief

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36
- 2026-09-10 status: pending → failed · raw/2026-09-10/ledger.md#L89
- 2026-09-10 updated: a read beyond the four inputs is allowed for one of three named reasons; session artifacts, code and yaml repairs are not · raw/2026-09-10/ledger.md#case-44
- 2026-09-11 status: failed → failed · raw/2026-09-10/ledger.md#L123
- 2026-09-11 updated: four indexes; four reasons; outcome named · [[decision-case-54]]
