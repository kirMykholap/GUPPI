---
type: rule
kind: Leaf
purpose: Prevents the next session from starting without the facts and the flags of this one
status: built
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: partial
parent: "[[rule-documentation]]"
estimates: ["[[estimate-brief-written]]", "[[estimate-brief-carries-the-run-facts]]"]
origin: raw/2026-09-10/ledger.md#case-35.3
sprint: migration
created: 2026-09-10
tags: [harness, workflow, librarian]
core: true
---

## Purpose

Prevents the next session from starting without the facts and the flags of this one,
written to [[brief]]. [[brief]] is a shop window, not storage: every deferred item lives on as a page — a draft placeholder, or the open Insight itself — and `backlog.md` lists them all, so the brief carries no Deferred list (case 451.8); the flags have no cap, and nothing in the brief is a decision.

## Render

<!-- rule-brief -->
Brief. Run `make lint` and keep its output. Rewrite `vault/wiki/brief.md` in full,
with these sections in this order:
- Where things stand: from the "What actually got done" section of `handoff.md` and
  the counts of the yaml, pages created and updated per category.
- Readings due: after `generate`, every Estimate whose `status` is `pending` or `failed` — one line per Estimate: the Estimate, the rule that stands `draft`, and where it is read, from the unticked `- [ ] read …` line of the session's `spec.md` or, when there is none, from the page's `method` (case 200.3); for an Estimate whose `method` names the librarian's run, at the end of its line the facts its `method` and `## Criterion` name, as the steps of this run before the brief printed or left them, with no comparison and no passed or failed (case 508.4); a `failed` one first, with the result of its reading in one line; nothing from the previous brief (case 168). The fields are the page's own: an Estimate's `status`, its `target` — the rule — and its `method`, and the `status` of that rule (case 567.2).
- Flags, no limit: entries marked `incomplete`, `failed`, `near` or `unparsed`;
  failed Estimates; MOC candidates; stale defers; contradictions; the lint output; each read you made that your frame says your job does not need, one line each: what you read and which part of your job needed it, and the handoff when it asked for the read (cases 558.3, 567.2).
- Next session: three lists, one line per item, an item in one list only, a list with no item the line "none" (cases 268.1, 531.10). `Cases`, what needs a decision: after a run whose `guppi sprint-close --apply` moved the sprint page, first the line `open the next sprint — no sprint is open since the close of <id>` (`rule-sprint-close`, case 628.8); a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, each contradiction of Flags (one between pages in `vault/archive/` too; one that a line of `## For the next session` already carries stands in that line alone), a defect you found — what and from where (case 761); and, for each line of `## Debt` of `handoff.md` that names an Estimate whose reading cannot be taken yet, but one of the live sprint page, one whose `method` names the close of a sprint and one whose `method` waits for an event you have not seen, one line that names the Estimate by slug and proposes to defer it into `backlog.md`, since its session did not take its reading (case 781). `Work`, what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, one of an Estimate whose `target` is the live sprint page, one whose `method` names the close of a sprint, one whose `method` waits for an event you have not seen, one that a line of `Cases` proposes to defer and one of an Estimate with `deferred_by` (case 781), the unticked boxes of the Specs but the `read` box of such a reading, a ledger line this run did not apply, a dirty tree. `Ask the person`, a reading only the person can take: each line of `## Ask the person` of `handoff.md` — the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them — but one whose `method` names the close of a sprint. A `method` names the close of a sprint when it names the session that closes a sprint, its librarian's run or the session after it. A reading of an Estimate whose `target` is the live sprint page `entity-sprint-<id>`, or whose `method` names the close of a sprint, stands in Readings due and in no list of Next session, its `read` box in the Specs included, until its moment: the first is read at the Retro of the session that finishes its work or by the closing Case of `/sprint-close`, and, when its `method` names the person's answer, stands in `Ask the person` once that Retro named it under `## Ask the person` of `handoff.md`; the second at its moment. In the run whose `guppi sprint-close --apply` moved the sprint page, each `pending` reading whose `method` names the session after that close, or its `/hi`, stands under `Work`, or under `Ask the person` with the question its `method` names when its `method` names the person's answer (case 772.1). A `method` waits for an event when a part of it between two `;` opens with `after`, or with `by hand, after`, and names the event before a colon, such as `by hand, after a pull request from a second account: the hook's output read against the Criterion`. At each run, look for that event in `git log`, in the ledger and `handoff.md` of the session, and in the files its `method` names; once you see it, its reading stands under `Work`, or under `Ask the person` with the question its `method` names when its `method` names the person's answer; until then it stands in Readings due alone (case 781).
- Readings at the close: `make test`, `make lint`, page counts.
When a fact the brief needs is in no input — the status of an Estimate, the severity
of an Insight — read it from the page; the page is not named in the report (case 567.1). Write facts
and flags only. Add no decision and no judgment of the work. A handoff flag that asks for a change of the sprint goes into the `Cases` of Next session; the sprint page changes only by a Case (case 539.2), and `vault/wiki/sprint.md` is written by `guppi sprint`, never by you (case 209.6).

The brief has a second writer, the skill `carry` (`rule-carry-over`): it writes the same frame in the short shape — Where things stand names the conserved Spec by path, its Cases and what is not done on it; Readings due and Readings at the close are omitted; so is the Deferred list — the conserved Spec and its targets stand in `backlog.md`; Flags say what the vault does not know about this session; Next session keeps its three lists — `Work` the open `W` lines of the session's `frontier.md`, `Ask the person` its open `A` lines, `Cases` always the line "none", since a deferred decision reaches `/hi` through `backlog.md` and a sprint item through the sprint page — because `/hi` takes its Work list from Next session alone (cases 190.4, 451.8, 538.2).
<!-- /rule-brief -->

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-35.3
- 2026-09-10 estimate estimate-brief-written added · raw/2026-09-10/ledger.md#case-35.3
- 2026-09-10 status: draft → built · cascade
- 2026-09-11 updated: a fact no input carries is read from the page and named · [[decision-case-54]]
- 2026-09-12 updated: the Deferred list comes from the defer entries of the yamls and the previous brief, not from the handoff (case 59.5) · [[decision-case-59.5]]
- 2026-09-14 deferred · [[decision-case-119]]
- 2026-09-14 defer by decision-case-119 superseded · [[decision-case-124.1]]
- 2026-09-14 updated: every open Insight stands in the Deferred list of the brief, ranked by its severity, with a count of the briefs it stood in, and is a Case of the next Plan Mode (case 124.1) · [[decision-case-124.1]]
- 2026-09-14 updated: an open Insight in Deferred is a live page, not a draft placeholder (case 132) · [[decision-case-132]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 updated: the hub file linked for the graph (case 149.4) · [[decision-case-149.4]]
- 2026-09-15 updated: the second section is Readings due, sourced from the pending and failed Estimates after the run and the Spec's reading lines; What the next session does first retired (case 168) · [[decision-case-168]]
- 2026-09-15 status: built → draft · cascade
- 2026-09-16 status: draft → built · cascade
- 2026-09-16 updated: the brief has two writers — the librarian and /carry; the short shape omits the sections of a run that did not happen and names the conserved Spec (case 190.4) · [[decision-case-190.4]]
- 2026-09-16 status: built → draft · cascade
- 2026-09-16 updated: the second writer and the short shape of the brief, one paragraph at the end of the Render (case 196.3, the text of 190.4) · [[decision-case-196.3]]
- 2026-09-16 updated: Readings due one line per Estimate, no block, the page's method field (case 200.3) · [[decision-case-200.3]]
- 2026-09-17 updated: the librarian never edits sprint.md — a sprint change is a Case, the file is the render of guppi sprint (case 209.6) · [[decision-case-209.6]]
- 2026-09-18 updated: Deferred leaves out a target the sprint page names, in the librarian's brief and in the /carry brief alike (cases 229.4, 233) · [[decision-case-229.4]]
- 2026-09-18 status: draft → built · cascade
- 2026-09-20 updated: the section Next session between Flags and Readings at the close — the lists Cases and Work, the librarian's sort of what the next session decides and what it does; a handoff flag on the sprint goes there; the carry brief without it (case 268.1) · [[decision-case-268.1]]
- 2026-09-20 status: built → draft · cascade
- 2026-09-20 updated: pre-task → the vault query before a create (case 277.4) · [[decision-case-277.4]]
- 2026-09-20 status: draft → built · cascade
- 2026-09-23 updated: Flags name the items generate moved to the Backlog and the milestones it dropped (case 354.4) · [[decision-case-354.4]]
- 2026-09-23 status: built → draft · cascade
- 2026-09-23 status: draft → built · cascade
- 2026-09-27 updated: the brief carries no Deferred list and no cap; the deferred items stand in backlog.md (case 451.8) · [[decision-case-451.8]]
- 2026-09-27 status: built → draft · cascade
- 2026-09-27 status: draft → built · cascade
- 2026-09-29 updated: a Readings due line of an Estimate read at the librarian's run ends with the facts of the run, no verdict (case 508.4) · [[decision-case-508.4]]
- 2026-09-29 estimate estimate-brief-carries-the-run-facts added · [[decision-case-508.4]]
- 2026-09-29 status: built → draft · cascade
- 2026-09-29 status: draft → built · cascade
- 2026-09-30 updated: Next session gets a third list, Ask the person, from handoff.md; Cases take its For the next session (case 531.10) · [[decision-case-531.10]]
- 2026-09-30 status: built → draft · cascade
- 2026-09-30 updated: the brief of carry keeps Next session: Work and Ask the person from the open lines of the session's frontier.md, Cases the line none (case 538.2) · [[decision-case-538.2]]
- 2026-09-30 updated: Flags no longer name items moved to the Backlog or milestones dropped; the sprint page changes only by a Case (case 539.2) · [[decision-case-539.2]]
- 2026-09-30 status: draft → built · cascade
- 2026-09-30 updated: Flags carry each read of the librarian beyond the reads its frame names (case 558.3) · [[decision-case-558.3]]
- 2026-09-30 status: built → draft · cascade
- 2026-10-01 updated: a page read for a fact of the brief is not named in the report (case 567.1) · [[decision-case-567.1]]
- 2026-10-01 updated: Flags carry each read the frame says the job does not need; Readings due names the fields it reads (case 567.2) · [[decision-case-567.2]]
- 2026-10-01 status: draft → built · cascade
- 2026-10-04 updated: after a close, the opening of the next sprint is the first Cases line (case 628.8) · [[decision-case-628.8]]
- 2026-10-04 status: built → draft · cascade
- 2026-10-10 updated: Cases of Next session hold each contradiction of Flags, one between archived pages too, once (case 761) · [[decision-case-761]]
- 2026-10-10 updated: Work and Ask the person of Next session leave out a reading of the live sprint page whose work is not done, its read box included, and one whose method names the close of a sprint, until its moment (case 772.1) · [[decision-case-772.1]]
- 2026-10-12 updated: the brief holds a reading that waits for an event in Readings due until the librarian sees the event, proposes a defer into the backlog for a reading its session did not take, and leaves a deferred Estimate out of Work (case 781) · [[decision-case-781.5]]
- 2026-10-12 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
