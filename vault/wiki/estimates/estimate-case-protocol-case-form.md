---
type: estimate
kind: QA
status: pending
target: "[[rule-case-protocol]]"
purpose: A Case in the chat carries the whole contract in given, when and then
method: one reading by hand of the Cases of a session, at its close
checked: 2026-09-20
origin: raw/2026-09-16/1034/ledger.md#case-188
sprint: migration
created: 2026-09-16
tags: [session, workflow]
---

## Criterion

Given:
`index.md`, `estimates/schema.md` and `schema.yaml` are the Renders of their rule pages (case 304); `case-schema.md` is the Render of `rule-case-protocol`, loaded by `/hi` (case 273).
**＋** An `update` of the Render of `rule-case-protocol` touches the Estimate of the live reading of that Render (187).
**＋** The reading of `estimate-case-protocol-case-form` is the Cases of this session at its close, by hand.

When:
The agent writes a Case in the chat — at its first showing, when shown again after the owner's change, and with sub-cases.

Then:
`given` holds the conditions of the behaviour; the state of the pages the Case changes goes to `context`.
**＋** `context` opens with the mechanism in plain words — what the thing does today and where it goes wrong — and closes with one sentence of bookkeeping: the state of the pages, the vault's answer, the Estimates of the rule the Case touches and the ones it does not; a case number stands in `context` or `problem` only when the Case is about that case; no count of sentences — the shape of each story section bounds it (case 267).
**＋** `given`, `when` and `then` together are the Criterion of the Estimate, copied whole and replacing what stood there.
**＋** An item that writes `sections: Criterion` itself signs that text, on a `create` and on an `update` alike; the Case's `given`, `when`, `then` are the Criterion of the one Estimate that writes none; that is how one Case touches two Estimates.
**＋** The Case names by slug the Estimate it changes.
**＋** `tasks` carries no `contract` line and no "block N" line.
**－** A `create` carries no `method`, `estimate_kind` or `estimate_slug`: a new promise is an explicit `create` of an Estimate with its own slug.
**－** The eight sections of the chat form do not change.

## Result

2026-09-20, the Cases 270–277 of session 1308 read by hand at its close: each opens context with the mechanism and closes with one sentence of bookkeeping, given holds conditions only, the Estimate named by slug, tasks without a contract line, a case number in context only when the Case is about it; two departures — the three amendments to signed text after pre-spec went as a numbered block outside the Case form, and the given of 273.1 needed a correction at pre-spec

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
