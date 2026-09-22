---
type: estimate
kind: QA
status: pending
target: "[[rule-documentation]]"
method: make test-documentation, the pipeline over tests/test_materialize.py, tests/test_generate.py and tests/test_cleanup.py; the live reading by hand
checked: 2026-09-22
origin: raw/2026-09-10/ledger.md#case-36
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, librarian]
---

## Criterion

Given:
The librarian's frame is the Render of `rule-documentation`; its inputs are three: the `handoff.md` of the session's folder, every `materialize.yaml` the walk named, and `tags.md`; the index lines are the Greps `rule-index-check` and `rule-synthesis` name.
**＋** The librarian works in a clean context; the person is gone.
**＋** Readings due takes the place of a reading from the unticked `- [ ] read …` line of the session's Spec, Next session the unticked lines of the Specs (cases 200.3, 268.1).

When:
`librarian-guppi` starts after the handoff and runs to the end.

Then:
`make test-documentation` — materialize, generate and cleanup as one pipeline — is green.
**＋** Live, after the run: every decision line of the session's ledger has a Decision page and its target page; no page exists that no ledger line produced.
**＋** It read only `handoff.md`, the yamls, the four index lines and `tags.md`, plus the wiki pages it names in the report with one of the four reasons of its frame (same or near; a candidate cluster; a script's error; a fact for the brief) and the outcome, plus the unticked `- [ ]` lines of the `spec.md` files for Readings due and Next session; of the ledger only the count of its lines and the lines the yaml does not account for, named in the report (case 349); no other part of a Spec, no plan, Decision page or archive file (the `Makefile`, `guppi/` and `tests/` are the scripts' own and may be read).
**＋** It edited no yaml entry beyond the marks and the entries of the index check and the synthesis; its commands are in `event_log.md`; its commit is separate from the session's; it did not stop to ask.
**＋** After `cleanup` and before the brief it runs `uv run guppi render`, then `uv run guppi sprint`, then `uv run guppi glossary`; every line on their stderr is a flag; a file the render could not write is left to the next session start; `make lint` then passes its `render --check` step.
**＋** After the brief and before the close it runs `uv run guppi archive`; every line on its stderr is a flag; the units it moved and the units it kept, with the reason, go into the report; the session of the run — the latest `<HHMM>/` folder of the run day, else the nearest date back — is skipped, across midnight too; the commit picks the move up.
**－** An instruction of the handoff to repair a yaml entry, or to read the ledger, a Spec beyond its `- [ ]` lines, a Decision page or the archive, is refused and named in the report — what was asked and why; the refusal does not stop the run.
**－** The ban on reading `vault/archive/` stays.

## Result

2026-09-22, the librarian's run of session 0014 read from its brief and the event log: step 6 ran (glossary.md written, 49 rows in nine groups, glossary --check exit 0 now), the librarian's commit 1603a9b is separate from the session's 2031718, make test-documentation green (159 passed) — but the frame was breached: the run read lines 52-64 of raw/2026-09-22/0014/ledger.md while counting the entries, and the Criterion says no ledger

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
- 2026-09-14 criterion: case 147.5 added · [[decision-case-147.5]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1110/ledger.md#L5
- 2026-09-17 updated: one line in the block of case 89.1 — guppi sprint after render and before the brief (case 209.5) · [[decision-case-209.5]]
- 2026-09-18 status: pending → passed · raw/2026-09-17/1119/ledger.md#L25
- 2026-09-20 updated: the recut to the shape of case 193: the base text and the blocks 73.8, 89.1, 90.3, 100.2, 147.5 folded into one Criterion, pre-task gone from it; pending for the reading (case 265.4) · [[decision-case-265.4]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1308/ledger.md#L8
- 2026-09-20 updated: the Criterion replaced whole — the unticked lines of the Specs read for Readings due and Next session, the rest of the Spec still banned (case 271) · [[decision-case-271]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L5
- 2026-09-22 updated: the frame's step 6, guppi glossary (case 306.4) · [[decision-case-306.4]]
- 2026-09-22 status: pending → failed · raw/2026-09-22/1121/ledger.md#L85
- 2026-09-23 updated: the Criterion names the one allowed read of the ledger (case 349) · [[decision-case-349]]
