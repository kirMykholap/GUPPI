---
type: estimate
kind: QA
status: passed
target: "[[rule-brief]]"
method: one reading by hand after the first librarian run, recorded in the estimate line
checked: 2026-09-18
origin: raw/2026-09-10/ledger.md#case-35.3
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
---

## Criterion

Given:
The librarian writes `brief.md` by the frame — the Render of `rule-brief` — after `generate`, from the yaml of the run, `handoff.md` and the output of `make lint`.
**＋** A fact no input carries — the status of an Estimate, the `severity` of an Insight — is read from the page, and the page is named in the report.
**－** The brief of `/carry` is the promise of `estimate-carry-over-writes`, not of this one.

When:
The librarian rewrites `vault/wiki/brief.md` at the end of its run.

Then:
The brief holds five sections in order: Where things stand, Readings due, Deferred, Flags, Readings at the close.
**＋** Where things stand — from "What actually got done" of `handoff.md` and the counts of the yaml: pages created and updated per category.
**＋** Readings due — every Estimate `pending` or `failed` after `generate`: the Estimate, the rule that stands `draft`, and where it is read — from the unticked `read` line of the session's Spec or from the page's `method`; a `failed` one first, with the result of its reading in one line; nothing from the previous brief.
**＋** Deferred — at most seven: the targets of the `defer` entries of this run, the items of the previous list whose decision no `supersedes` retired, every `open` Insight; never a target the sprint page names under a milestone or in its Backlog, whose count of briefs does not grow (case 229.4); ranked by `severity` — its own or that of the related Insight — then by the number of briefs the item stood in; an Insight's line carries its slug, `severity`, `pattern` and its Proposal in one or two sentences.
**＋** Flags, no limit: entries `incomplete`, `failed`, `near`, `unparsed`; `failed` Estimates; MOC candidates; stale defers; contradictions; the lint output; a handoff flag that asks for a change of the sprint, as a Case of the next Plan Mode.
**＋** Readings at the close — `make test`, `make lint`, page counts.
**－** The brief states no decision and no judgment of the work; a change of the sprint is a Case, never the librarian's edit.

## Result

2026-09-18, the brief of the 1119 run read by hand at /hi: five sections in order; Where things stand from the handoff and the yaml counts per category; Readings due the thirteen pending after generate, each with its draft rule and the place from the Spec line or the method, no failed; Deferred four items, ranked by severity then briefs, without rule-work-mode, rule-subagent-guppi and rule-spec-box, which the sprint page names; Flags with the synthesis, the render tick, the contradiction, the handoff flags as Cases and the lint output; Readings at the close with test, lint and page counts; no decision stated

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.3
- 2026-09-10 status: pending → passed · raw/2026-09-10/ledger.md#L92
- 2026-09-14 criterion: case 124.1 added · [[decision-case-124.1]]
- 2026-09-14 status: pending → passed · raw/2026-09-14/1229/ledger.md#L5
- 2026-09-14 status: passed → passed · raw/2026-09-14/1633/ledger.md#L1
- 2026-09-15 criterion: case 168 added · [[decision-case-168]]
- 2026-09-16 status: pending → passed · raw/2026-09-15/2225/ledger.md#L3
- 2026-09-16 updated: the Criterion replaced whole by this Case; its earlier blocks recut by point 1 at this touch (case 190.4) · [[decision-case-190.4]]
- 2026-09-16 updated: the Criterion replaced whole by case 197 — the head, 124.1 and 168 recut into one; the short shape of /carry left to estimate-carry-over-writes (case 197) · [[decision-case-197]]
- 2026-09-17 status: pending → passed · raw/2026-09-16/2238/ledger.md#L3
- 2026-09-17 updated: the last line of the Criterion — a change of the sprint is a Case, never the librarian's edit; the sprint flag lands in Flags (case 209.6) · [[decision-case-209.6]]
- 2026-09-18 updated: the Deferred line — never a target the sprint page names (case 229.4) · [[decision-case-229.4]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/1252/ledger.md#L3
