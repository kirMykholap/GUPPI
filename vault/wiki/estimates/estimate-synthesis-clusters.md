---
type: estimate
kind: QA
status: pending
target: "[[rule-synthesis]]"
method: one reading by hand of the yaml and the report after a live librarian run whose yaml holds at least two lesson entries
checked: 2026-10-02
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
**＋** Every lesson page read at synthesis is named in the report with the outcome: the Insight it joined, or none and why.
**＋** A lesson without a pair stays `new`, and its line in the brief is no flag.
**－** A read of another session's `materialize.yaml` or of a page under `vault/archive/` fails nothing here: an actioned Insight stays live with its pattern in its index line, and the flag of such a read is the promise of `estimate-documentation-completes`.

## Result

2026-10-02, by hand at the /hi of session 2300, raw/2026-10-02/2049/materialize.yaml and the report of the run 8a30dae6 (its answer and brief.md); the yaml holds two lesson entries, lines 25 and 31; the report names `^(root_cause|deferred_by):` over lessons/ (76 lines) and `^(pattern|deferred_by):` over insights/ (31 lines); no entry added, both lessons stay `new`, the pages agree; the report gives the reason against the insights only for `lesson-prespec-onward-re-ratification-out-after-its-stretch` and none for `lesson-case-check-question-line-without-colon-unseen`

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
