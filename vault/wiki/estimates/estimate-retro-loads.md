---
type: estimate
kind: QA
status: passed
target: "[[rule-retro]]"
method: one reading by hand at the first /retro, recorded in the estimate line
checked: 2026-09-21
origin: raw/2026-09-10/ledger.md#case-38.1
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness]
---

## Criterion

Given:
Retro takes the readings of this session's Estimates whose work is finished and writes their lines; `generate` applies the entries of the yaml in ledger order — an `estimate` entry sets `status` and overwrites the Result (case 53.2); `built` is computed once every Estimate is `passed`.
**＋** An `update` of an Estimate replaces its Criterion whole and sets `pending`; the render of a Rule comes with the librarian, after Retro.
**＋** `estimate-retro-loads` is read by hand at the first `/retro` after the render.

When:
The person invokes `/retro`, and the agent takes the readings of the session's Estimates.

Then:
A reading measures the Criterion the page carries at the moment of the reading — the one ratified last; its line is written only when the work that Criterion names is built — rendered, written, run.
**＋** An Estimate whose Criterion a Case of this session replaced, and whose build is not finished at Retro, gets no reading in this session: the `read` line of the old Criterion in an earlier Spec is not debt and is not read; the reading of the new Criterion closes it, at the moment its `method` names; the handoff names the Estimate as one whose reading cannot be taken yet.
**－** Nothing in `generate` changes: an `update` and a reading of one slug in one session apply in ledger order, and the reading of a Criterion built in the session sets its status.
**－** Nothing else in Retro changes.

## Result

2026-09-21, the /retro of session 0019 read by hand, the Criterion of 283, the SKILL rendered by the librarian of 2106: four Estimates whose Criterion a Case of this session replaced — estimate-generate-ticks-the-spec (286), estimate-internal-context-loaded (288.1), estimate-case-protocol-loaded (288.2), estimate-claude-md-rendered (288.3) — and whose build waits for the librarian's pages and renders got no reading, their read lines of this Spec (56, 214, 251, 299) carried to the handoff as the moment their method names, no old-Criterion line in an earlier Spec read; the readings taken were of Criteria built before the session (estimate-case-protocol-ledger-line-form, L1) or by the render of 2106 (this one); the page, create, defer and render lines listed as waiting for the librarian; no superseded Case in the Tail; nothing else of Retro changed

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.1
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L86
- 2026-09-11 updated: the frontier, the four outcomes, the readings and the red-test paths added; pending until the next live /retro · [[decision-case-56]]
- 2026-09-12 updated: the Deferred heading (cases 59.5, 66) · [[decision-case-66]]
- 2026-09-12 status: pending → passed · raw/2026-09-12/ledger.md#L106
- 2026-09-12 criterion: case 73.6 added · [[decision-case-73.6]]
- 2026-09-13 criterion: case 109.1 added · [[decision-case-109.1]]
- 2026-09-14 status: pending → failed · raw/2026-09-14/0747/ledger.md#L50
- 2026-09-14 criterion: case 126 added · [[decision-case-126]]
- 2026-09-14 status: pending → failed · raw/2026-09-14/1029/ledger.md#L41
- 2026-09-14 status: failed → passed · raw/2026-09-14/1229/ledger.md#L30
- 2026-09-14 criterion: case 150 added · [[decision-case-150]]
- 2026-09-15 status: pending → failed · raw/2026-09-15/1110/ledger.md#L26
- 2026-09-15 criterion: case 169.3 added · [[decision-case-169.3]]
- 2026-09-15 criterion: case 150 removed · [[decision-case-169.3]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1809/ledger.md#L14
- 2026-09-18 updated: the Criterion replaced whole — the page and render lines are not debt (case 233.2) · [[decision-case-233.2]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L37
- 2026-09-18 updated: the Criterion replaced whole — a guppi sprint line waits for the librarian too (case 253.2) · [[decision-case-253.2]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/0527/ledger.md#L22
- 2026-09-20 updated: the Criterion replaced whole — the read line with its ledger line waits for the librarian (case 270.3) · [[decision-case-270.3]]
- 2026-09-20 updated: the Criterion replaced whole — the lines of a superseded Case are not counted (case 282) · [[decision-case-282]]
- 2026-09-20 status: pending → passed · raw/2026-09-20/1749/ledger.md#L20
- 2026-09-21 updated: the Criterion replaced whole — a replaced Criterion is not read at the Retro of its session; the reading of 270.3 written after 282 undone by this pending (case 283) · [[decision-case-283]]
- 2026-09-21 status: pending → passed · raw/2026-09-21/0019/ledger.md#L21
