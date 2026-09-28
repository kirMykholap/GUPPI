---
type: estimate
kind: QA
status: pending
target: "[[rule-documentation]]"
method: make test-documentation, the pipeline over tests/test_materialize.py, tests/test_generate.py and tests/test_cleanup.py; the live reading by hand
checked: 2026-09-27
origin: raw/2026-09-10/ledger.md#case-36
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, librarian]
---

## Criterion

When:
`librarian-guppi` starts after the handoff and runs to the end, in a clean context. Its frame is the Render of `rule-documentation`. Its inputs are the `handoff.md` of the session's folder, every `materialize.yaml` the walk named, and `tags.md`. The index lines are the Greps that `rule-index-check` and `rule-synthesis` name.

Then:
`make test-documentation` is green: materialize, generate and cleanup as one pipeline.
**＋** Live, after the run: every decision line of the session's ledger has a Decision page and its target page, and no page exists that no ledger line produced.
**＋** The librarian read only the following, and nothing else:
- `handoff.md`, the yamls that `guppi materialize` named, the index lines and `tags.md`;
- a file where the harness saved the output of one of the librarian's own commands because the output was too long to show;
- the wiki pages it names in the report, each with the outcome and one of the reasons of its frame (same or near; a candidate cluster; a script's error; a fact for the brief);
- a page under `vault/archive/` found by the Glob `vault/archive/**/<slug>.md` for a slug that a script named in an error, named in the report with the error;
- the unticked `- [ ]` lines of the `spec.md` files, for Readings due and Next session;
- of the ledger, only the count of its lines and the lines the yaml does not account for, named in the report.

It read no other part of a Spec, no plan, no Decision page, and no `materialize.yaml` that `guppi materialize` did not name. The `Makefile`, `guppi/` and `tests/` are the scripts' own files and may be read.
**＋** It edited no yaml entry beyond the marks and the entries of the index check and the synthesis. Its commands are in `event_log.md`, its commit is separate from the session's, and it did not stop to ask.
**＋** After `cleanup` and before the brief, it runs `uv run guppi render`, then `uv run guppi sprint`, then `uv run guppi backlog`, then `uv run guppi glossary`. Every line on their stderr is a flag. A file the render could not write is left to the next session start. `make lint` then passes its `render --check` step.
**＋** After the brief and before the close, it runs `uv run guppi archive`. Every line on its stderr is a flag. The units it moved and the units it kept, with the reason, go into the report. It skips the session of the run, which is the latest session folder of the run day or else the nearest date back, across midnight too. The commit picks the move up.
**－** The librarian refuses an instruction of the handoff to repair a yaml entry, to read the ledger beyond the one read above, a Spec beyond its `- [ ]` lines or a Decision page, to search the archive, or to open an archived page that no script named in an error. It names what was asked and why in the report, and the refusal does not stop the run.
**－** The librarian never searches `vault/archive/`: no Grep, `grep`, `find` or `ls` runs over it, and no Glob other than `vault/archive/**/<slug>.md` for a slug a script named in an error.

## Result

2026-09-27, make test-documentation and the event log of the librarian run of session 1819; 191 passed and the order render, sprint, backlog, glossary, brief, archive, commit held, but at 20:40:39 the run grepped vault/archive/ (grep -rln "status: clustered" raw archive) and at 20:39:28 read a file under ~/.claude/projects/…/938809b2-…, both outside the frame

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
- 2026-09-23 updated: the Criterion refuses a read of the ledger beyond the one allowed (case 357) · [[decision-case-357]]
- 2026-09-27 updated: the Criterion replaced whole — guppi backlog after guppi sprint, Given lifted into When and Then (case 451.13) · [[decision-case-451.13]]
- 2026-09-27 status: pending → failed · raw/2026-09-27/2050/ledger.md#L31
- 2026-09-28 updated: the Criterion replaced whole — an archived page found by the Glob of the slug a script named in an error, the archive never searched, the saved output of the librarian's own command allowed, no yaml that materialize did not name (case 474.1) · [[decision-case-474.1]]
