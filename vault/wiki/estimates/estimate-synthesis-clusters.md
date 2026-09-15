---
type: estimate
kind: QA
status: passed
target: "[[rule-synthesis]]"
origin: raw/2026-09-10/ledger.md#case-35.2
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Context

A missed pair is a pattern nobody sees; an invented pair is an Insight nobody ratified the basis of.

## Criterion

After a live librarian run with at least two lesson entries: the report names the
comparisons made against lessons-index and insights-index; two lessons with one
root cause produced one insight create entry with pattern, both children, the union
of tags, Pattern and Proposal, and one update per lesson setting clustered and
insight; a lesson matching a live Insight's pattern produced an update of that
Insight and of the lesson; every added entry carries librarian: synthesis; no
archive file was read, and every lesson page read is named in the report with
the outcome: the Insight it joined, or none and why; a lesson without a pair stayed new.

### case 147.4

When:
The librarian does the synthesis.

Then:
"compare its `root_cause` with every index line of `lessons/` and of `insights/` — the Greps of 147.2 — by meaning"; "that Insight stays live with its pattern in its index line".

## Method

one reading by hand after the first librarian run, recorded in the estimate line

## Result

live 2026-09-15, the librarian's run of session Q read against the brief: four root causes compared against the Greps `^(root_cause|deferred_by):` over `lessons/` (27 lines) and `^(pattern|deferred_by):` over `insights/` (11 lines), both named with their counts; one insight create entry over the two retro lessons with pattern, both children, the union of tags, Pattern and Proposal, and one update per lesson setting clustered and insight; one live Insight (`insight-librarian-frame-omits-required-reads`) reopened by a matching lesson with the lesson's update; the page `insight-materialize-lift-loses-a-schema-field` opened and named with the outcome (not the same cause); `lesson-wiki-page-edited-by-hand-in-obsidian` without a pair stayed new; all 5 added entries carry librarian: synthesis; the day's event log holds no archive read; the refusal of the create by generate (124.2) is outside this criterion — frontier F3

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
