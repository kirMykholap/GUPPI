---
type: decision
case: "143"
status: archived
update: ["[[insight-librarian-frame-omits-required-reads]]"]
origin: raw/2026-09-14/1633/ledger.md#case-143
sprint: migration
created: 2026-09-14
tags: [harness, librarian]
---

## Context

An Insight of severity 2, `open`, two children of sessions F and G (2026-09-10…11): the librarian's frame named the reads it allows one by one, and the list was shorter than the judgments; the agent either broke a clause (read `generate.py`, read a lesson page against the ban of `rule-synthesis`) or judged on an index line alone. Pattern: the reads the work needs were found while the work ran, not when the frame was written. Proposal: derive the read clauses from the judgments — one clause per judgment, the page and the field; change every Rule that names a read in one pass; the readings of `estimate-documentation-completes` and `estimate-synthesis-clusters` after the next run show whether the list is complete.

## Problem

The Proposal was carried out by Case 54 and after it. The frame (`rule-documentation`) holds exactly four reasons to open a page — one per judgment: same or near at a `create`; a shared root cause of a lesson "with another lesson or an Insight"; why a script failed an entry; a fact the brief needs (the status of an Estimate, the severity of an Insight). The children's clauses agree: `rule-index-check` ("open the page and name it in the report"), `rule-synthesis` ("read the Trigger and Root cause of the candidate", the ban lifted by 54), `rule-brief` ("read it from the page and name the page"); 58 added `Makefile`, `guppi/`, `tests/`; 90.3 — an instruction of the handoff outside the frame is refused and named in the report. No two clauses answer one act differently today (`ask-guppi`). Both Estimates `passed`; nine librarian runs since session H — no new lesson of the class; the brief of O: "the handoff's instructions were all within the frame; none was refused". Decide: the Insight `actioned`.

## Given

`insight-librarian-frame-omits-required-reads`: `open`, severity 2, children `lesson-librarian-reads-beyond-the-four-inputs`, `lesson-frame-read-clauses-omit-candidate-check-and-brief`, both `clustered`; the cascade of 104.2 archives them on `actioned`.
**＋** `rule-documentation` `built`, `estimate-documentation-completes` `passed` (last reading block 100.2, 2026-09-14): "Open a page under `vault/wiki/` for four reasons only: …" — same or near; a root cause "with another lesson or an Insight"; a page a script names in an error; a fact the brief needs; "Name every page you open in the report"; the ban on `ledger.md`, `spec.md`, `plan.md`, `wiki/decisions/`, `vault/archive/`; `Makefile`, `guppi/`, `tests/` — "read them when a command's output is not enough" (58); the refusal of a handoff instruction outside the frame (90.3); the archive root (102.4).
**＋** `rule-index-check` `built`, `estimate-index-check-merges`: "When the index line does not settle same or near, open the page and name it in the report". `rule-synthesis` `built`, `estimate-synthesis-clusters` `passed` (2026-09-12, J: every page opened named with its outcome): "read the Trigger and Root cause of the candidate … Do not read the archive" (54). `rule-brief` `built`: "read it from the page and name the page in the report".
**＋** History of the clauses after 54: `rule-documentation` only (58, 73.8, 90.3, 102.4); `rule-index-check`, `rule-synthesis`, `rule-brief` — no change of a read clause. No two Rules answer one act differently.
**＋** Librarian runs H…O: no new lesson about a read outside the frame; in O no page was opened for the index check, two `near` marks with their reason on index lines — within reason 1 (opening is a right, not a duty).
**－** `rule-cleanup`, `rule-materialize`, `rule-page-generation`, `rule-raw-archive`, `rule-close` carry no read clause of the agent — nothing to compare.
**－** An Insight is not a Leaf: no `contract`, no Estimate. No Rule changes; `librarian-guppi.md` is not rendered again.

## History

- 2026-09-14 created · raw/2026-09-14/1633/ledger.md#case-143
- 2026-10-10 status: current → archived · the close of sprint migration (sprint-close)
- 2026-10-10 archived · cleanup
