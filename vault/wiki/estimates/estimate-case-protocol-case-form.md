---
type: estimate
kind: QA
status: failed
target: "[[rule-case-protocol]]"
purpose: A Case in the chat carries the whole contract in given, when and then
method: one reading by hand of the Cases of a session, at its close
checked: 2026-09-27
origin: raw/2026-09-16/1034/ledger.md#case-188
sprint: migration
created: 2026-09-16
tags: [session, workflow]
---

## Criterion

When:
The main agent shows in the chat a Case that `case-guppi` built, at its first showing or again.

Then:
The Case opens with the heading `## Case N — name`, a sub-case with `### Case N.M — name` under its parent, and holds its sections in the order of the Sections table of `vault/wiki/case-schema.md`, each one blockquote whose first line is `**name:**`.
**＋** `context` is prose: the mechanism in plain words first, then the state of the pages the Case changes, the vault's answer, what `case-guppi` found in the frame and why an Estimate of the rule is not touched; a case number stands in `context` or `problem` only when the Case is about that case, and a count of items stands in none of the story sections unless the Case is about that count.
**＋** `given` holds the frame, one thing per line — each page, module, file and test the Case touches and the rule that constrains, its slug or path in a code span and its role — and no state.
**＋** In `given`, `when` and `then` each line after the first opens with `**＋**` or `**－**`, a `**－**` line names something of `given` or `when`, and `then` holds behaviour only.
**＋** `tasks` names by slug each Estimate the Case creates or replaces, and under a line whose item writes content that content stands as sub-points; no `contract` line and no "block N" line.
**＋** A pair under `replace` or `reword` stands only when the Case says what the sentence around each match names; a Case that changes the behaviour of a page gives an `update` to each Estimate of that page whose Criterion speaks of the change.
**＋** `ratification` holds only the preview of the ledger lines in an untagged fence; the agent's own text stands after the Case, after one horizontal rule, and the reply ends with a plain question.
**＋** A Case with sub-cases is shown in one reply: the parent's `context`, `problem` and `recommend`, then each sub-case whole.

## Result

2026-09-27, by hand, the Cases of session 2300 shown in the chat; the headings, section order, ratification fences, one-reply showing of 443, 444 and 445 and the closing questions hold, and no context shown holds a list, but the context of Case 446 carries a count of items ("in three places only") and case numbers it is not about (378.5, 428.1), and the context of Case 444 names nine Estimates by count-free list yet the problem of Case 445 cites case 410, which the Case is not about

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
