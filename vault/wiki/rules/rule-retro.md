---
type: rule
kind: Leaf
purpose: Prevents a session from closing on work nobody reviewed, or on a change that traces to no decision
status: draft
enforcement: render
governs: .claude/skills/retro/SKILL.md
render_mode: full
parent: "[[rule-end-of-work]]"
estimates: ["[[estimate-retro-loads]]", "[[estimate-retro-report-holds-each-fact-once]]", "[[estimate-retro-red-check-of-an-updated-page-is-a-handoff-note]]", "[[estimate-retro-red-in-the-baseline-is-not-charged]]"]
deferred_by: ["[[decision-case-505]]"]
origin: raw/2026-09-10/ledger.md#case-38.1
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, render]
---

## Purpose

Prevents a session from closing on work nobody reviewed, or on a change that traces
to no decision. Retro is a conversation over this session only. The tests and the
style check load before the first turn, so the person reads the result instead of
waiting for it. The scope rule is mechanical: an edit is allowed when it finishes work a line of this session's ledger ratified, and is new scope otherwise. Retro opens by two paths, both behind `guppi gate`: the person's typed `/retro` on `UserPromptSubmit`, the agent's call on `PreToolUse Skill`; each checks the Spec against the ledger and leaves the mark `retro`, and a refused typed prompt is not expanded (case 169.3, supersedes 150).

## Render

<!-- rule-retro -->
---
name: retro
description: Review this session's work — tests, style, the ledger — before the commit and the handoff.
---


Tests: !`make test`

Style: !`make style`

Ledger: !`uv run guppi tail`

Retro is an analysis of this session, not planning. Open with the frontier, in one message and with no read call but the Read of `vault/raw/<date>/<hi HHMM>/work.md` when it stands, which `/work` wrote (case 479.3). First sort the unticked boxes of the `tasks` of `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73). A `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line and a `read` line whose `estimate[...]` stands in the Tail above wait for the librarian, whose scripts tick them (cases 226, 250, 270); they are not debt. A `read` line whose slug this session creates or updates, by a decision line of that slug or by an `update` that renames a page to it, waits for a later session; it is neither debt nor the librarian's (case 428.4). Another `read` line without its line in the Tail is debt, and so is a box of code, a test, a command or a migration left unticked. The lines of a Case that a `{supersedes:case N}` line of the Tail names are not counted at all; its work stands under the superseding Case (case 282). The frontier is one numbered list of what needs an end in this Retro: each box that is debt, and what you noticed during Work Mode — bugs, forks, a contract that turned out imprecise. Under the list write two lines, not numbered: the count of the boxes that wait for the librarian, with no list of them, and the slugs of the `read` lines that wait for a later session. The frontier names no box that waits for the librarian one by one and holds no list of the ratifications (case 468.1). An item of the frontier is its text alone: it names no end, and no Case, reading or lesson that ends it; its end stands only in What is not done (case 483). The person adds their own observations. Every item, theirs or
yours, ends in one of four ways: a `- lesson[...]` line; a `- estimate[...]` line, a
reading of an Estimate whose work is finished; a short defer; or a note for the
handoff. Retro ratifies no other decision: a `create`, `update` or `delete` waits for
the next Plan Mode.

A short defer is a Case in the short form, appended to `vault/raw/<date>/<hi HHMM>/spec.md` under the `## Deferred` heading before its ledger line: `## Case N`, `context`, `problem`,
and a `defer` block with `purpose`; no `recommend`, `given`, `when` or `then`. A defer
line without its Case is marked incomplete by materialize.

Edit code only when the edit finishes work that traces to a line of this session's ledger.
Red tests: fix now when the fix finishes ratified work; otherwise save the change
with `git diff` into `raw/<hi date>/<hi HHMM>/patch-<slug>.diff`, the session's folder, revert it, and write a short
defer naming the patch. Either way write a `- lesson[error][...]` line whose root
cause says why Retro was reached with a regression; the handoff still needs green. A failing test or a lint finding line that `## Baseline` of `work.md` already holds was red before the work, whatever `## Expected red` names: it is an item of the frontier that ends as a note for the handoff, named as red before the work; it is not debt, nothing is fixed or reverted for it, and no lesson is written for it (case 479.4).
`gh` is not available: name a deferred bug in the handoff, so the brief carries it.
Do not run `make lint` here: the vault is written after handoff, by the librarian. A check that reads a page or a governed file this session's Spec updates — `make lint` or one of its steps, or a hook of the working tree — is red or refuses in Work Mode until the librarian's run writes the page or renders the file, and the `make lint` of that run is its reading: `/work` marks such a red under `## Expected red` of `work.md` when the task that changes the check runs, one line naming the check and the page or file it waits for. A red or a refusal of that check on a page or file a line names is an item of the frontier that ends as a note for the handoff, naming the check and the page or file it waits for, and it is not debt; a red or a refusal on a page or file no line names is debt, even when another line names the same check, unless `## Baseline` holds its line. In a session with no `work.md`, such a red ends as a note for the handoff by your judgment, as before. A red test is never an expected red: it is fixed or reverted as above (cases 473.1, 479.3).

Take the readings of the Estimates whose work is finished and that this session neither creates nor updates — by a decision line of its slug, or by an `update` that renames a page to it — and write their lines; name in the handoff any Estimate whose reading cannot be taken yet, and every Estimate this session creates or updates. A reading measures the Criterion the page carries at the moment of the reading, the one ratified last, and its line is written only when the work that Criterion names is built. What a session changes, it does not measure: an Estimate this session creates or updates has no reading in this session, built or not, and the ledger hook refuses one (case 428.1); the `read` line of its old Criterion in an earlier Spec is not debt and is not read, and the reading of the new Criterion closes it in a later session, at the moment its `method` names (cases 283, 428.3).

Close with three parts, each fact in one part only. Ratified: one line with the ids of the Cases ratified, by the Tail above, this session's folder first, a Case that a `{supersedes:case N}` line names not counted, and no page. What got done: only what no other part holds — the commit, the code files and tests changed, the result of `make test` and `make style`, the readings and lessons written by their ledger line numbers, except a reading or a lesson that is the end of an item of the frontier; no Case and no item of the frontier restated. What is not done: each number of the frontier with the end you propose, a short defer with its Case id, with no text of the item, no ledger line number and no repeat of the two lines under the frontier. The frontier and the close stand in one reply, and the person approves or changes the ends there; the lines of the ends are written after it (case 483). No Case, box, reading or lesson is named in two parts of the report (case 468.1). The report has this form, its labels in the language of the chat (case 483):

```
1. <text of the item>
2. <text of the item>

<N> boxes wait for the librarian.
Read in a later session: `<slug>`, `<slug>`.

Ratified: <ids of the Cases>.
What got done: <commit>; <code files and tests>; make test <result>; make style <result>; <readings and lessons by L<n>>.
What is not done:
- 1 — <end>
- 2 — <end>
```

When the person approves, commit (`make style` clean, `make test` green but for the tests that `## Baseline` of `work.md` holds), then call `/handoff`.
<!-- /rule-retro -->

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-38.1
- 2026-09-10 estimate estimate-retro-loads added · raw/2026-09-10/ledger.md#case-38.1
- 2026-09-10 updated: Retro ends with the commit, then /handoff (the Render of case 38.1 already carries it) · raw/2026-09-10/ledger.md#case-40
- 2026-09-10 deferred · raw/2026-09-10/ledger.md#case-50
- 2026-09-10 status: draft → built · cascade
- 2026-09-11 deferred_by decision-case-50 set · [[decision-case-52.3]]
- 2026-09-11 updated: a Retro Case is appended to spec.md under ## Retro before its ledger line; a bare defer is forbidden · [[decision-case-52.2]]
- 2026-09-11 defer by decision-case-50 superseded · [[decision-case-56]]
- 2026-09-11 updated: Retro opens with the frontier; every item ends as a lesson, a reading, a short defer or a handoff note; red tests are fixed or reverted into a patch; readings are a step · [[decision-case-56]]
- 2026-09-11 status: built → draft · cascade
- 2026-09-12 updated: Retro counts the unticked tasks of spec.md instead of judging done against the Spec (case 59.3) · [[decision-case-59.3]]
- 2026-09-12 updated: the short-form Cases of Retro go under · [[decision-case-59.5]]
- 2026-09-12 status: draft → built · cascade
- 2026-09-12 updated: Retro reads and appends the session's Spec (case 73.6) · [[decision-case-73.6]]
- 2026-09-12 status: built → draft · cascade
- 2026-09-13 updated: Retro reads the session ledgers of the day (and the date-level one while it exists); the revert patch goes to the session folder (case 109.1) · [[decision-case-109.1]]
- 2026-09-14 deferred · [[decision-case-118]]
- 2026-09-14 defer by decision-case-118 superseded · [[decision-case-126]]
- 2026-09-14 updated: the Retro ledger is the unmaterialized tail printed by guppi tail, not a cat over a date-level file the model of case 103 no longer has (case 126) · [[decision-case-126]]
- 2026-09-14 updated: the scope rule names this session's ledger, as 109.1 promised (case 132) · [[decision-case-132]]
- 2026-09-14 updated: the Recorded line dropped; guppi gate writes the stamped retro mark (case 136.1) · [[decision-case-136.1]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 updated: disable-model-invocation dropped: a typed or agent-called /retro passes the Skill tool, so guppi gate sees it and writes the retro mark (case 150) · [[decision-case-150]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-15 updated: the two paths of Retro, typed and called, both behind the gate; supersedes 150 (case 169.3) · [[decision-case-169.3]]
- 2026-09-15 status: draft → built · cascade
- 2026-09-18 updated: the page and render lines of the Spec wait for the librarian and are not debt at Retro (case 233.2) · [[decision-case-233.2]]
- 2026-09-18 status: built → draft · cascade
- 2026-09-18 status: draft → built · cascade
- 2026-09-18 updated: a guppi sprint line of the Spec waits for the librarian and is not debt at Retro (case 253.2) · [[decision-case-253.2]]
- 2026-09-18 status: built → draft · cascade
- 2026-09-20 status: draft → built · cascade
- 2026-09-20 updated: a read line whose reading stands in the ledger waits for the librarian, not debt (case 270.3) · [[decision-case-270.3]]
- 2026-09-20 status: built → draft · cascade
- 2026-09-20 updated: the lines of a superseded Case are not debt at Retro (case 282) · [[decision-case-282]]
- 2026-09-20 status: draft → built · cascade
- 2026-09-21 updated: a reading measures the last ratified Criterion; an Estimate whose Criterion this session replaced and whose build is not finished has no reading at this Retro (case 283) · [[decision-case-283]]
- 2026-09-21 status: built → draft · cascade
- 2026-09-21 status: draft → built · cascade
- 2026-09-23 deferred · [[decision-case-375]]
- 2026-09-23 defer by decision-case-375 superseded · [[decision-case-376]]
- 2026-09-23 updated: the report of /retro holds each fact once — the ratifications in the closing list only, the unticked boxes inside the numbered list of what is not done (case 376) · [[decision-case-376]]
- 2026-09-23 estimate estimate-retro-report-holds-each-fact-once added · [[decision-case-376]]
- 2026-09-23 status: built → draft · cascade
- 2026-09-25 updated: Retro takes no reading of an Estimate the session creates or updates, built or not (case 428.3) · [[decision-case-428.3]]
- 2026-09-25 updated: the opening list of Retro marks a read line of a change of the session as waiting for a later session (case 428.4) · [[decision-case-428.4]]
- 2026-09-27 updated: the report of /retro holds each fact once — the frontier numbers only what needs an end, the librarian's boxes one count line, the close three parts: the Case ids, what got done, the numbers with their ends (case 468.1) · [[decision-case-468.1]]
- 2026-09-28 updated: a check red in Work Mode because it reads a page or a file the same Spec updates is a note for the handoff, not debt; a red test stays under the green rule (case 473.1) · [[decision-case-473.1]]
- 2026-09-28 estimate estimate-retro-red-check-of-an-updated-page-is-a-handoff-note added · [[decision-case-473.1]]
- 2026-09-28 updated: Retro reads work.md, and a red on a page or file that its Expected red names ends as a note for the handoff; any other such red is debt unless the Baseline holds it; with no work.md the judgment of case 473.1 stands (case 479.3) · [[decision-case-479.3]]
- 2026-09-28 updated: a red that the Baseline of work.md holds is a note for the handoff under any Expected red, not debt, and the commit does not wait for it (case 479.4) · [[decision-case-479.4]]
- 2026-09-28 estimate estimate-retro-red-in-the-baseline-is-not-charged added · [[decision-case-479.4]]
- 2026-09-28 updated: a frontier item is its text alone; its end, with the Case id of a defer, stands only in What is not done, with no ledger line number; the frontier and the close stand in one reply, in the form of a skeleton (case 483) · [[decision-case-483]]
- 2026-09-29 updated: the closing fence of the report skeleton stands alone on its line, and the commit sentence follows as its own paragraph (case 486) · [[decision-case-486]]
- 2026-09-29 deferred · [[decision-case-505]]
