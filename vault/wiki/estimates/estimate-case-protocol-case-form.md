---
type: estimate
kind: QA
status: passed
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
`index.md`, `case-schema.md`, `estimates/schema.md` and `schema.yaml` are Rule-class files: an `update` with `file` and `change`, applied by hand in Work Mode.
**＋** `CLAUDE.md` is rendered from `rule-case-protocol`; an `update` of the Render touches the Estimate of the live reading of that Render (187).
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

2026-09-20, the Cases of session 0958 read by hand at its close: 267, 268, 268.1, 268.2 and the changes after pre-spec open context with the mechanism and close with one sentence of bookkeeping, name a case number only when the Case is about it, run past no cap; given holds conditions only, every Case names its Estimate by slug, tasks carry no contract line; 264–266 were written before the rule and keep the old density

## History

- 2026-09-16 created · [[decision-case-188]]
- 2026-09-16 updated: the Criterion replaced whole by case 208.2 — the text of 188 with the given recut and the line on a written Criterion (case 208.2) · [[decision-case-208.2]]
- 2026-09-16 status: pending → passed · raw/2026-09-16/1955/ledger.md#L41
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-20 updated: the line on context replaced: the mechanism first, the bookkeeping one closing sentence, a case number only when the Case is about it, no cap of sentences; the other lines as 208.2 left them; pending for the reading (case 267) · [[decision-case-267]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0958/ledger.md#L31
