---
type: estimate
kind: QA
status: pending
target: "[[rule-documentation]]"
method: make test-documentation, the pipeline over tests/test_materialize.py, tests/test_generate.py and tests/test_cleanup.py; the live reading by hand
checked: 2026-09-17
origin: raw/2026-09-10/ledger.md#case-36
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, librarian]
---

## Criterion

Given:
The librarian's frame is the Render of `rule-documentation`; its inputs are three: the `handoff.md` of the session's folder, every `materialize.yaml` the walk named, and `tags.md`; the index lines are the Greps `rule-index-check` and `rule-synthesis` name.
**＋** The librarian works in a clean context; the person is gone.

When:
`librarian-guppi` starts after the handoff and runs to the end.

Then:
`make test-documentation` — materialize, generate and cleanup as one pipeline — is green.
**＋** Live, after the run: every decision line of the session's ledger has a Decision page and its target page; no page exists that no ledger line produced.
**＋** It read only `handoff.md`, the yamls, the four index lines and `tags.md`, plus the wiki pages it names in the report with one of the four reasons of its frame (same or near; a candidate cluster; a script's error; a fact for the brief) and the outcome; no ledger, Spec, plan, Decision page or archive file (the Makefile, `guppi/` and `tests/` are the scripts' own and may be read).
**＋** It edited no yaml entry beyond the marks and the entries of the index check and the synthesis; its commands are in `event_log.md`; its commit is separate from the session's; it did not stop to ask.
**＋** After `cleanup` and before the brief it runs `uv run guppi render`, then `uv run guppi sprint`; every line on their stderr is a flag; a file the render could not write is left to the next session start; `make lint` then passes its `render --check` step.
**＋** After the brief and before the close it runs `uv run guppi archive`; every line on its stderr is a flag; the units it moved and the units it kept, with the reason, go into the report; the session of the run — the latest `<HHMM>/` folder of the run day, else the nearest date back — is skipped, across midnight too; the commit picks the move up.
**－** An instruction of the handoff to repair a yaml entry, or to read the ledger, a Spec, a Decision page or the archive, is refused and named in the report — what was asked and why; the refusal does not stop the run.
**－** The ban on reading `vault/archive/` stays.

## Result

2026-09-17, `make test-documentation` 111 passed; live, the librarian's run of 2238 per its brief and commit be891c1: materialize, index check, synthesis, generate, cleanup, render, sprint, brief, archive, commit in that order, no stderr from any script, 27 Decision pages for the 27 Cases of the ledger, every entry `applied`, the commit separate from the session's a4c3509, `render --check` exit 0 at `/hi`; the inputs read as the frame names them, by the librarian's own report — no refusal reported

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
