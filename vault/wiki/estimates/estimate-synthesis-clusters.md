---
type: estimate
kind: QA
status: passed
target: "[[rule-synthesis]]"
method: one reading by hand of the yaml and the report after a live librarian run whose yaml holds at least two lesson entries
checked: 2026-09-29
origin: raw/2026-09-10/ledger.md#case-35.2
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Criterion

When:
`librarian-guppi` does the synthesis in a live run whose `materialize.yaml` holds at least two lesson entries.

Then:
The report names the Greps of the synthesis, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` and `^(pattern|deferred_by):` over `vault/wiki/insights/`, and the comparisons made against their lines, by meaning.
**＋** Two lessons with one root cause and no Insight give one `create` of an Insight with `pattern`, both children, the union of their tags, `Pattern` and `Proposal`, and one `update` per lesson with `set: {status: clustered, insight: <slug>}`.
**＋** A lesson whose root cause matches the pattern of a live Insight gives an `update` of that Insight with the lesson added to its `children`, and an `update` of the lesson.
**＋** Every entry the synthesis adds carries `librarian: synthesis`.
**＋** Every lesson page read at synthesis is named in the report with the outcome: the Insight it joined, or none and why.
**＋** A lesson without a pair stays `new`.
**－** The synthesis reads no file under `vault/archive/`: an actioned Insight stays live with its pattern in its index line.

## Result

2026-09-29, by hand at the /hi of session 1432, raw/2026-09-29/1134/materialize.yaml and the report of the run f9a27b8: the yaml holds two lesson entries, L69 and L70; the report names `^(root_cause|deferred_by):` over lessons/ (60 lines) and `^(pattern|deferred_by):` over insights/ (27 lines); L69 joined `insight-case-build-promise-lines-compared-by-no-check` by one update of the Insight (child added, reopened) and one update of the lesson (status clustered, insight set), both carrying `librarian: synthesis`; L70 stays `new`, its reason in the report; the pages agree; no pair of lessons without an Insight arose

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
