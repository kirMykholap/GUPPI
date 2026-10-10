---
type: decision
case: "353"
status: archived
update: ["[[rule-case-protocol]]", "[[estimate-case-protocol-loaded]]"]
supersedes: ["[[decision-case-341]]", "[[decision-case-342]]"]
origin: raw/2026-09-22/2046/ledger.md#case-353
sprint: migration
created: 2026-09-22
tags: [session, workflow, ledger]
---

## Context

Cases 341 and 342 of this plan both change one paragraph of the Render of `rule-case-protocol` — the one that describes an `update` — and both add a line to the Criterion of `estimate-case-protocol-loaded`. As a pair they carry three faults. Each writes into the live text the number of the Case it replaced, 337 and 340, whose edits never land and whose Decision pages go to the archive marked superseded, so a reader of `case-schema.md` is sent to a Case that did nothing. They judge one position by opposite standards: 341 puts the requirement for signing a pair — a step of the author — right after the words "it carries no `contract`.", while the `context` of 342 argues that text at that anchor reads as a condition on the shape of an `update` and not as a step of the author. And two `given` lines carry traces: 342's says the paragraph turns to `delete` and `defer` after the anchor, while the next sentence is the one on one promise per Case; 341's names the anchor of case 340, which is gone.
`rule-case-protocol` stands `draft`; the live reading of its Render is `estimate-case-protocol-loaded`, `passed`; the page's three other Estimates are not touched. `estimate-case-protocol-case-form` stands `pending` and its Criterion already says that a Case names by slug the Estimate it changes; this Case does not change that Criterion, and its reading over the Cases of a session will meet the new step when it is taken.

## Problem

Two Cases divide one paragraph between them, cite the Cases they replaced, and disagree on where a step of the author belongs.

## History

- 2026-09-23 created · raw/2026-09-22/2046/ledger.md#case-353
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
