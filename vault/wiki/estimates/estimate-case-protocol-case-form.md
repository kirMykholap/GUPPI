---
type: estimate
kind: QA
status: failed
target: "[[rule-case-protocol]]"
purpose: A built Case carries the whole contract in given, when and then, in the file the person is sent
method: one reading by hand of the Cases of a session, at its close
checked: 2026-10-05
origin: raw/2026-09-16/1034/ledger.md#case-188
sprint: migration
created: 2026-09-16
tags: [session, workflow]
---

## Criterion

When:
`case-guppi` writes a Case it built into `raw/<date>/<hi HHMM>/cases/case-<N>.md`, the hook of `rule-case-check` checks it, and the main agent sends that file to the person, at its first showing or again.

Then:
The file opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds the sections of each Case in the order of the Sections table of `vault/wiki/case-schema.md`, each one blockquote whose first line is `**name:**`.
**＋** `context` and `problem` are plain prose that explains briefly — `context` opens with the mechanism in plain words, then gives the state of the pages the Case changes, the vault's answer, what `case-guppi` found in the frame and why an Estimate of the rule is not touched, and leaves out a part with nothing to say — `recommend` is the list the Sections table of `vault/wiki/case-schema.md` sets, each item plain prose, and the person raised no complaint in the session about their length or clarity.
**＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state.
**＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, `then` holds behaviour only, and none of them holds a count of items — pages, lines, Estimates, Cases, tests; a number that states a condition or a limit stands.
**＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
**＋** `tasks` holds no `by hand` box whose moment comes after Work Mode of the Case's own session — the librarian's run of that session or a later session; such a check stands as the reading of an Estimate or is left to the `make lint` of the librarian's run.
**＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change.
**＋** `ratification` holds only the preview of the ledger lines in an untagged fence; in the chat the Case stands as the short text and that `ratification` of `estimate-orchestration-shows-the-built-case`, and the reply ends with a plain question.
**＋** A Case with sub-cases stands in one file and is sent in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole, with its own `recommend` when it has one.
**－** A case number, a count, a line number or a quotation in `context`, `problem` or `recommend` is no fault of the form.

## Result

2026-10-05, by hand at the Work readings of session 1343, cases/case-650.md to case-656.md against vault/wiki/case-schema.md: headings, sub-cases in one file, sections in the order of the table each one blockquote, context opening with the mechanism, recommend as the table sets, ＋/－ lines, tasks naming each Estimate with sub-points and no by-hand box after Work Mode, one untagged fence of ledger lines, a plain question at each showing, no complaint of the person; failed: `given` holds two things on a line in 650.1, 650.2 (`guppi/ratified.py` and `tests/test_ratified.py`), 653.1 and 654, and states state in 656 ("on the allow list", "with `permissionMode: acceptEdits`") and 653.1; `then` of 652 holds a count ("both tests of `tests/test_case_schema.py` fail"); the passed reading of 2026-10-03 accepted paired `given` lines of the same form in cases 607–610

## History

- 2026-09-16 created · [[decision-case-188]]
- 2026-09-16 updated: the Criterion replaced whole by case 208.2 — the text of 188 with the given recut and the line on a written Criterion (case 208.2) · [[decision-case-208.2]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L41
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-20 updated: the line on context replaced: the mechanism first, the bookkeeping one closing sentence, a case number only when the Case is about it, no cap of sentences; the other lines as 208.2 left them; pending for the reading (case 267) · [[decision-case-267]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0958/ledger.md#L31
- 2026-09-20 updated: the Criterion replaced whole — case-schema.md the Render of rule-case-protocol loaded by /hi, not a Rule-class file by hand; CLAUDE.md no longer the carrier (case 277.5) · [[decision-case-277.5]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1308/ledger.md#L55
- 2026-09-22 updated: the Criterion names the Renders, not the file route (case 320) · [[decision-case-320]]
- 2026-09-23 updated: the Criterion names ratification as the ledger preview alone (case 355.1) · [[decision-case-355.1]]
- 2026-09-23 updated: the Criterion names the sub-cases shown in one reply (case 355.2) · [[decision-case-355.2]]
- 2026-09-23 updated: the Given names no removed file (case 364.2) · [[decision-case-364.2]]
- 2026-09-23 updated: the Criterion names the heading of a Case in the chat (case 368) · [[decision-case-368]]
- 2026-09-23 updated: the Criterion names the sub-points of an item's content in the chat (case 370) · [[decision-case-370]]
- 2026-09-23 updated: the When names the showing again after the agent's own finding (case 373) · [[decision-case-373]]
- 2026-09-25 updated: the Criterion replaced whole — the form of a Case in the chat by the model of case 378, the line of case 353 taken from estimate-case-protocol-loaded (case 396.1) · [[decision-case-396.1]]
- 2026-09-25 updated: the Criterion replaced whole — the line on context names no count of items in the story sections; the rest as case 396.1 wrote it (case 406) · [[decision-case-406]]
- 2026-09-25 updated: the Criterion replaced whole — the line on the frame of when and then left to estimate-prespec-checks-the-frame (case 415) · [[decision-case-415]]
- 2026-09-25 status: pending → failed · raw/2026-09-25/0051/ledger.md#L19
- 2026-09-25 updated: the Criterion replaced whole — a Case built by case-guppi, and its context says what case-guppi found in the frame (case 431) · [[decision-case-431]]
- 2026-09-26 status: pending → failed · raw/2026-09-26/1745/ledger.md#L34
- 2026-09-27 status: failed → failed · raw/2026-09-26/2300/ledger.md#L35
- 2026-09-27 updated: the Criterion replaced whole — the form stands in the file of a built Case; context, problem and recommend brief plain prose judged by the person's complaint, a case number, a count, a line number or a quotation there no fault; no count of items in given, when and then (case 449) · [[decision-case-449]]
- 2026-09-27 status: pending → passed · raw/2026-09-27/2050/ledger.md#L34
- 2026-09-30 updated: the Criterion replaced whole — recommend is the list of the schema, a sub-case with its own (case 544.11) · [[decision-case-544.11]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/1736/ledger.md#L39
- 2026-10-02 ref `estimate-case-protocol-shows-the-built-case` → `estimate-orchestration-shows-the-built-case` · [[decision-case-595.11]]
- 2026-10-03 updated: the Criterion replaced whole — tasks hold no by hand box whose moment comes after Work Mode of the Case's session; the other lines as case 544.11 left them (case 606.1) · [[decision-case-606.1]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/0115/ledger.md#L17
- 2026-10-05 updated: the Criterion replaced whole — case-guppi writes the file of the Case and the hook checks it (case 645.10) · [[decision-case-645.10]]
- 2026-10-05 status: pending → failed · raw/2026-10-05/1343/ledger.md#L38
- 2026-10-05 deferred · [[decision-case-665]]
