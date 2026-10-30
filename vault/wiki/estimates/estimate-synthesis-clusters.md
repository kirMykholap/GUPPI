---
type: estimate
kind: QA
status: passed
target: "[[rule-synthesis]]"
method: "by hand, after a librarian's run whose `materialize.yaml` holds at least two lesson entries: the yaml and the report read against the Criterion"
checked: 2026-10-30
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
**－** A read of another session's `materialize.yaml` or of a page under `vault/archive/` fails nothing here: an actioned Insight stays live with its pattern in its index line until the close of its sprint, and, in the repository of GUPPI, the flag of such a read is the promise of `estimate-documentation-completes`.

## Result

2026-10-30, Work readings of session 2005: raw/2026-10-30/1713/materialize.yaml holds 2 lesson entries (L29, L30); brief.md names ^(root_cause|deferred_by): over lessons/ (52 lines) and ^(pattern|deferred_by): over insights/ (12 lines) and gives one line per lesson, each none with why; both lessons stay new and stand under Synthesis, not under Flags; the synthesis added no entry; the librarian (agent a3bfe59073516787c of session 5c343872) opened insight-case-build-sibling-texts-unchecked-before-the-showing and lesson-frontier-sprint-line-closed-by-a-case-that-updates-no-sprint-page, and its report names both with the outcome; it also printed line 4, the root_cause index line, of three lesson pages whose lines the Grep had printed as "[Omitted long matching line]", read here as the output of the Grep, not as an opening

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
- 2026-10-30 updated: the Criterion replaced whole — the flag of a read is named in the repository of GUPPI only; the method names its event · [[decision-case-920.4]]
- 2026-10-30 status: pending → passed · raw/2026-10-30/2005/ledger.md#L52
