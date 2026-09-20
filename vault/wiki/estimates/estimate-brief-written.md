---
type: estimate
kind: QA
status: pending
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
The librarian writes `brief.md` by the frame — the Render of `rule-brief`; `/hi` reads `sprint.md`, `brief.md`, the tail of the ledger, `git status` and the output of its own commands — and nothing else.
**＋** `prespec.check_frontier`: the id is the first token after `[ ]`, the closer the last segment after ` · `; a line without `[ ]` is not checked.
**＋** The reading of `estimate-brief-written` is by hand after the librarian's run; of `estimate-hi-writes-frontier` by hand at the first `/hi` of the next session.

When:
The librarian rewrites `vault/wiki/brief.md` at the end of its run.

Then:
The brief holds six sections in order: Where things stand, Readings due, Deferred, Flags, Next session, Readings at the close.
**＋** Where things stand, Readings due, Deferred, Flags and Readings at the close are as today, their content unchanged.
**＋** Next session — two lists. `Cases`: what needs a decision — a handoff flag with a question or a request to change the sprint, a `failed` Estimate, a contradiction, a defect the librarian found; one line per item, what and from where. `Work`: what is done without a decision — every `pending` reading of Readings due by its slug, the unticked boxes of the Specs, a ledger line this run did not apply, a dirty tree; one line per item.
**＋** An item stands in one of the two lists, never in both; a list with no item is the line "none".
**－** The brief still states no decision: the sort by kind is not a judgment of the work.
**－** The brief of `/carry` keeps its short shape, without Next session — `rule-brief` and `rule-carry-over` both say so.

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
- 2026-09-20 updated: the Criterion replaced whole — six sections, Next session with the lists Cases and Work (case 268.1) · [[decision-case-268.1]]
