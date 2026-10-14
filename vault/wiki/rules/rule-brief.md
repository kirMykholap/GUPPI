---
type: rule
kind: Leaf
purpose: Prevents the next session from starting without the facts and the flags of this one
status: built
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: partial
parent: "[[rule-documentation]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [harness, workflow, librarian]
core: true
---

## Purpose

Prevents the next session from starting without the facts and the flags of this one,
written to `brief`. `brief` is a shop window, not storage: every deferred item lives on as a page — a draft placeholder, or the open Insight itself — and `backlog.md` lists them all, so the brief carries no Deferred list; the flags have no cap, and nothing in the brief is a decision.

## Render

<!-- rule-brief -->
Brief. Run `make lint` and keep its output. Rewrite `vault/wiki/brief.md` in full,
with these sections in this order:
- Where things stand: from the "What actually got done" section of `handoff.md` and
  the counts of the yaml, pages created and updated per category.
- Readings due: after `generate`, every Estimate whose `status` is `pending` or `failed` — one line per Estimate: the Estimate, the rule that stands `draft`, and where it is read, from the unticked `- [ ] read …` line of the session's `spec.md` or, when there is none, from the page's `method`; for an Estimate whose `method` names the librarian's run, at the end of its line the facts its `method` and `## Criterion` name, as the steps of this run before the brief printed or left them, with no comparison and no passed or failed; a `failed` one first, with the result of its reading in one line; nothing from the previous brief. The fields are the page's own: an Estimate's `status`, its `target` — the rule — and its `method`, and the `status` of that rule.
- Flags, no limit: entries marked `incomplete`, `failed`, `near` or `unparsed`;
  failed Estimates; MOC candidates; stale defers; contradictions; the lint output; each read you made that your frame says your job does not need, one line each: what you read and which part of your job needed it, and the handoff when it asked for the read.
- Next session: three lists, one line per item, an item in one list only, a list with no item the line "none". `Cases`, what needs a decision: after a run whose `guppi sprint-close --apply` moved the sprint page, first the line `open the next sprint — no sprint is open since the close of <id>`, as `rule-sprint-close` sets it; a line of `## For the next session` of `handoff.md`, a handoff flag with a question or a request to change the sprint, a `failed` Estimate, each contradiction of Flags (one between pages in `vault/archive/` too; one that a line of `## For the next session` already carries stands in that line alone), a defect you found — what and from where; and, for each line of `## Debt` of `handoff.md` that names an Estimate whose reading cannot be taken yet, but one of the live sprint page, one whose `method` names the close of a sprint and one whose `method` waits for an event you have not seen, one line that names the Estimate by slug and proposes to defer it into `backlog.md`, since its session did not take its reading. `Work`, what is done without a decision: every `pending` reading of Readings due by its slug but one that `Ask the person` holds, one of an Estimate whose `target` is the live sprint page, one whose `method` names the close of a sprint, one whose `method` waits for an event you have not seen, one that a line of `Cases` proposes to defer and one of an Estimate with `deferred_by`, the unticked boxes of the Specs but the `read` box of such a reading, a ledger line this run did not apply, a dirty tree. `Ask the person`, a reading only the person can take: each line of `## Ask the person` of `handoff.md` — the Estimate by slug, the mark `needs the person` and its question, as the handoff wrote them — but one whose `method` names the close of a sprint. A `method` names the close of a sprint when it names the session that closes a sprint, its librarian's run or the session after it. A reading of an Estimate whose `target` is the live sprint page `entity-sprint-<id>`, or whose `method` names the close of a sprint, stands in Readings due and in no list of Next session, its `read` box in the Specs included, until its moment: the first is read at the Retro of the session that finishes its work or by the closing Case of `/sprint-close`, and, when its `method` names the person's answer, stands in `Ask the person` once that Retro named it under `## Ask the person` of `handoff.md`; the second at its moment. In the run whose `guppi sprint-close --apply` moved the sprint page, each `pending` reading whose `method` names the session after that close, or its `/hi`, stands under `Work`, or under `Ask the person` with the question its `method` names when its `method` names the person's answer. A `method` waits for an event when a part of it between two `;` opens with `after`, or with `by hand, after`, and names the event before a colon, such as `by hand, after a pull request from a second account: the hook's output read against the Criterion`. At each run, look for that event in `git log`, in the ledger and `handoff.md` of the session, and in the files its `method` names; once you see it, its reading stands under `Work`, or under `Ask the person` with the question its `method` names when its `method` names the person's answer; until then it stands in Readings due alone.
- Readings at the close: `make test`, `make lint`, page counts.
When a fact the brief needs is in no input — the status of an Estimate, the severity
of an Insight — read it from the page; the page is not named in the report. Write facts
and flags only. Add no decision and no judgment of the work. A handoff flag that asks for a change of the sprint goes into the `Cases` of Next session; the sprint page changes only by a Case, and `vault/wiki/sprint.md` is written by `guppi sprint`, never by you.

The brief has a second writer, the skill `carry` (`rule-carry-over`): it writes the same frame in the short shape — Where things stand names the conserved Spec by path, its Cases and what is not done on it; Readings due and Readings at the close are omitted; so is the Deferred list — the conserved Spec and its targets stand in `backlog.md`; Flags say what the vault does not know about this session; Next session keeps its three lists — `Work` the open `W` lines of the session's `frontier.md`, `Ask the person` its open `A` lines, `Cases` always the line "none", since a deferred decision reaches `/hi` through `backlog.md` and a sprint item through the sprint page — because `/hi` takes its Work list from Next session alone.
<!-- /rule-brief -->

## History

- 2026-10-14 shipped with GUPPI
