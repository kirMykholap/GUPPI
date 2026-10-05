---
type: estimate
kind: QA
status: passed
target: "[[rule-synthesis]]"
method: one reading by hand of the yaml and the report after a live librarian run whose yaml holds at least two lesson entries
checked: 2026-10-05
origin: raw/2026-09-10/ledger.md#case-35.2
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Criterion

When:
`librarian-guppi` does the synthesis in a live run whose `materialize.yaml` holds at least two lesson entries.

Then:
The brief names the Greps of the synthesis, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, with the number of lines each printed.
**＋** The brief gives one line for each lesson entry: its slug and the lesson or Insight it joined, or none and a few words on why no index line of either Grep shares its root cause.
**＋** Two lessons with one root cause and no Insight give one `create` of an Insight with `pattern`, both children, the union of their tags, `Pattern` and `Proposal`, and one `update` per lesson with `set: {status: clustered, insight: <slug>}`.
**＋** A lesson whose root cause matches the pattern of a live Insight gives an `update` of that Insight with the lesson added to its `children`, and an `update` of the lesson.
**＋** Every entry the synthesis adds carries `librarian: synthesis`.
**＋** Every page the librarian opens at synthesis to judge whether a lesson shares its root cause is named in the report with the outcome: the Insight it joined, or none and why. A read of its Trigger, Root cause, `root_cause`, Pattern or `pattern` outside the two Greps is such an opening.
**＋** A lesson without a pair stays `new`, and its line in the brief is no flag.
**－** A read at synthesis of only the fields `status`, `insight`, `children` and `tags` of a page under `vault/wiki/lessons/` or `vault/wiki/insights/`, made to learn which lessons are grouped or which lessons an Insight holds, is not named in the report and fails nothing here.
**－** A read of another session's `materialize.yaml` or of a page under `vault/archive/` fails nothing here: an actioned Insight stays live with its pattern in its index line until the close of its sprint, and the flag of such a read is the promise of `estimate-documentation-completes`.

## Result

2026-10-05, by hand at the /hi of session 1616: raw/2026-10-05/1343/materialize.yaml, brief.md and the report of the librarian run of 1343 (agent a7869c913e9461fdd, transcript f5706873); the yaml holds three lesson entries (L42–L44); the brief names `^(root_cause|deferred_by):` over lessons/ (81 lines) and `^(pattern|deferred_by):` over insights/ (31 lines) and gives one line per lesson, each joined to a live Insight; each join is one update of the Insight with the lesson added to `children` and one update of the lesson (status clustered, insight set), all six entries `librarian: synthesis`; at synthesis the librarian opened three pages, insight-harness-one-rule-implemented-twice-drifts, insight-workflow-case-schema-silent-on-what-the-scripts-accept and insight-case-show-built-case-retyped-by-hand (calls 16–18), and no lesson page; the report names all three with their outcome; its read of the 0311 yaml was a handoff check, outside the synthesis

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.2
- 2026-09-10 status: pending → failed · raw/2026-09-10/ledger.md#L91
- 2026-09-10 updated: a lesson page is read for the Insight it feeds and named in the report; the archive stays closed · raw/2026-09-10/ledger.md#case-44
- 2026-09-11 status: failed → failed · raw/2026-09-10/ledger.md#L124
- 2026-09-11 updated: a lesson page read is named with its outcome, clustered or not · [[decision-case-54]]
- 2026-09-12 status: pending → passed · raw/2026-09-11/ledger.md#L75
- 2026-09-12 status: passed → passed · raw/2026-09-12/ledger.md#L169
- 2026-09-14 criterion: case 147.4 added · [[decision-case-147.4]]
- 2026-09-15 status: pending → passed · raw/2026-09-15/1448/ledger.md#L2
- 2026-09-28 updated: the Criterion replaced whole — the ban on the archive is the synthesis's, not the whole run's; the base text and the block of case 147.4 folded into one Criterion (case 474.2) · [[decision-case-474.2]]
- 2026-09-29 status: pending → passed · raw/2026-09-29/1432/ledger.md#L3
- 2026-09-30 updated: the Criterion replaced whole — a read of another session's yaml or of the archive fails nothing here; its flag is the promise of estimate-documentation-completes (case 558.2) · [[decision-case-558.2]]
- 2026-10-03 status: pending → failed · raw/2026-10-02/2300/ledger.md#L1
- 2026-10-03 updated: the Criterion replaced whole — the brief gives one line per lesson entry with its outcome against both Greps, or none and why (case 602) · [[decision-case-602]]
- 2026-10-03 status: pending → passed · raw/2026-10-03/0317/ledger.md#L1
- 2026-10-04 updated: the Criterion replaced whole — an actioned Insight stays live until the close of its sprint (case 627.5) · [[decision-case-627.5]]
- 2026-10-05 status: pending → failed · raw/2026-10-05/0311/ledger.md#L1
- 2026-10-05 updated: the Criterion replaced whole — a page is named in the report when it is opened to judge a shared cause; a read of only its status, insight, children and tags is not (case 654) · [[decision-case-654]]
- 2026-10-05 status: pending → passed · raw/2026-10-05/1616/ledger.md#L5
