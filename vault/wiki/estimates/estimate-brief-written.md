---
type: estimate
kind: QA
status: passed
target: "[[rule-brief]]"
method: "by hand at the Retro of the session that changes it: the new Render of rule-brief in raw/<date>/<hi HHMM>/spec.md read against the Criterion, recorded in the estimate line"
checked: 2026-10-12
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [harness, workflow, librarian]
core: true
---

## Criterion

When:
The librarian rewrites `vault/wiki/brief.md` at the end of its run.

Then:
The brief holds, in order: Where things stand, Readings due, Flags, Next session, Readings at the close.
**＋** It holds no Deferred list and no cap on deferred items; they stand in `vault/wiki/backlog.md`. Where things stand, Readings due and Readings at the close are as before, and Readings due takes from each Estimate page its `status`, `target` and `method`, and from the target rule its `status`.
**＋** Flags keep their kinds of lines — marked entries, failed Estimates, MOC candidates, stale defers, contradictions, the lint output — and a read that the librarian's frame says its job does not need, with what was read, the part of the job it served, and the handoff when the handoff asked for it.
**＋** Next session holds `Cases`, `Work` and `Ask the person`, one line per item, an item in one list only, a list with no item the line "none". `Cases` is what needs a decision: after a run whose `guppi sprint-close --apply` moved the sprint page, first the line `open the next sprint — no sprint is open since the close of <id>`; a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, each contradiction of Flags, one between pages that stand in `vault/archive/` too, a defect the librarian found, with what and from where; and, for each line of `## Debt` of `handoff.md` that names an Estimate whose reading cannot be taken yet, but one of the live sprint page, one whose `method` names the close of a sprint and one whose `method` waits for an event the librarian has not seen, one line that names the Estimate by slug and proposes to defer it into `vault/wiki/backlog.md`.
**＋** `Work` is what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, one of an Estimate whose `target` is the live sprint page `entity-sprint-<id>`, one whose `method` names the close of a sprint — the session that closes a sprint, its librarian's run or the session after it —, one whose `method` waits for an event the librarian has not seen, one that a line of `Cases` proposes to defer and one of an Estimate with `deferred_by`; the unticked boxes of the Specs but the `read` box of such a reading; a ledger line this run did not apply, a dirty tree.
**＋** `Ask the person` holds each line of `## Ask the person` of `handoff.md` — the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them — but one whose `method` names the close of a sprint. A check of the live sprint page whose `method` names the person's answer stands there once the Retro of the session that finished its work named it in `handoff.md`.
**＋** In the run whose `guppi sprint-close --apply` moved the sprint page, each `pending` reading whose `method` names the session after that close, or its `/hi`, stands under `Work`, or under `Ask the person` with the question its `method` names when its `method` names the person's answer.
**＋** The brief of the skill `carry` keeps a short shape: Where things stand, Flags and Next session, without Readings due, Readings at the close and a Deferred list. In its Next session, `Work` and `Ask the person` take the open `W` and `A` lines of the session's `frontier.md`, and `Cases` is the line "none", since a deferred decision stands in `vault/wiki/backlog.md` and a sprint item on `vault/wiki/sprint.md`. `rule-brief` and `rule-carry-over` both say so.
**－** A reading left out of `Work` and `Ask the person` keeps its line under Readings due.
**－** A reading whose `method` waits for an event — a part of it between two `;` that opens with `after`, or with `by hand, after`, and names the event before a colon — stands in Readings due alone until the librarian sees that event in `git log`, in the ledger or `handoff.md` of the session, or in the files its `method` names; then it stands under `Work`, or under `Ask the person` with the question its `method` names when its `method` names the person's answer.
**－** A contradiction of Flags that a line of `## For the next session` of `handoff.md` already carries gets no second line in `Cases`.
**－** The brief states no decision: the sort by kind is not a judgment of the work.

## Result

2026-10-12, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
