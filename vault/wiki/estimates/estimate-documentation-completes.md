---
type: estimate
kind: QA
status: failed
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
produced; the agent read only handoff.md, the yamls materialize named, the five
indexes and tags.md, plus the wiki pages it names in the report with one of the
three reasons of its frame (same or near, the lessons of an Insight, a script's
error), and no ledger, Spec, plan, Decision page, archive file, or file under guppi/
or tests/; it edited no yaml entry beyond the marks and the entries of the index
check and the synthesis; its commands are in event_log.md; its commit is separate
from the session's; it did not stop to ask.

## Method

`make test-documentation`, the pipeline over tests/test_materialize.py, tests/test_generate.py and tests/test_cleanup.py; the live reading by hand

## Result

make test-documentation green inside the 132; live 2026-09-10: decision-case-43 and its five targets exist, the lesson-born and synthesis pages trace to line 80, the commit 8bbfa10 is separate and touches only vault/, its 44 commands are in event_log.md, it did not stop to ask; failed on the read constraint: at 11:49:55 it read vault/wiki/lessons/lesson-agents-loaded-at-session-start.md and at 11:50:08–11:50:15 guppi/generate.py three times, before any script had reported a problem; after the generate crash it also edited materialize.yaml lines 2306 and 2356 by sed and reran

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36
- 2026-09-10 status: pending → failed · raw/2026-09-10/ledger.md#L89
- 2026-09-10 updated: a read beyond the four inputs is allowed for one of three named reasons; session artifacts, code and yaml repairs are not · raw/2026-09-10/ledger.md#case-44
