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

## Method

`make test-documentation`, the pipeline over tests/test_materialize.py, tests/test_generate.py and tests/test_cleanup.py; the live reading by hand

## Result

make test-documentation 67 green; live 2026-09-12, the librarian's run of session J (15:57:15–16:08:31, commit 8836953): its first input was vault/raw/2026-09-12/1156/handoff.md, the session folder the dispatch named (case 73.8); all 49 decision cases of today's ledger have their Decision page and their target page; the event log of the window holds no read of a ledger, a Spec, a plan, a Decision page or an archive file, every wiki page it opened is named in the report with a reason and an outcome, its commands are in the event log, its commit is separate from the session's and touches vault/ only, and it did not stop to ask; one clause does not hold — it edited three yaml entries by hand (slug on the derived updates of cases 73.10 and 73.3, fields.source on lesson-hooks-blocked-pretooluse-leaves-no-posttooluse-event), the repair item 2 of the handoff named by slug and the criterion of case 44 forbids

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
