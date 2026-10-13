---
type: rule
kind: Leaf
purpose: Prevents a session from reaching the librarian on work nobody reviewed
status: built
enforcement: render
governs: .claude/skills/retro/SKILL.md
render_mode: full
parent: "[[rule-end-of-work]]"
estimates: ["[[estimate-retro-loads]]", "[[estimate-retro-runs-on-to-the-handoff]]", "[[estimate-retro-red-check-of-an-updated-page-is-a-handoff-note]]", "[[estimate-retro-red-in-the-baseline-is-not-charged]]", "[[estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case]]"]
origin: raw/2026-09-10/ledger.md#case-38.1
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, render]
core: true
---

## Purpose

Prevents a session from reaching the librarian on work nobody reviewed, or on a change that traces to no decision. Retro is an analysis of this session only, written by the agent for the librarian and the next session: it runs in the turn of `/work`, with no stop for the person, and its report is `handoff.md` (case 531.1). The tests and the style check load before the first turn of the skill. The scope rule is mechanical: an edit is allowed when it finishes work a line of this session's ledger ratified, and is new scope otherwise; in a session that `/box` runs, the lines of the conserved Spec's ledger count as this session's (case 591). Retro opens by two paths, both behind `guppi gate`: the agent's call on `PreToolUse Skill` at the end of `/work`, and the person's typed `/retro` on `UserPromptSubmit`; each checks the Spec against the ledger and leaves the mark `retro`, and a refused typed prompt is not expanded (case 169.3, supersedes 150).

## Render

<!-- rule-retro -->
---
name: retro
description: Review this session's work — tests, style, readings, lessons — commit it and go on to /handoff, in the turn that /work runs, with no stop for the person.
---


Tests: !`make test`

Style: !`make style`

Ledger: !`uv run guppi tail`

Retro is an analysis of this session for the librarian and the next session, not planning, and it runs without the person: `/work` calls it in the same turn, and you stop only on a condition of `vault/wiki/where-to-stop.md`, which `/work` loaded (case 531.1). Show no report and ask for no approval. Read `vault/raw/<date>/<hi HHMM>/work.md` when it stands, which `/work` wrote (case 479.3): when you wrote or changed it yourself in this turn, the text you hold counts as read; otherwise open it with the Read tool (case 569.2). When `work.md` holds `## Conserved Spec`, this session runs that conserved Spec by `/box`, and builds it: below, the Spec of this session is the `spec.md` of the folder that section names, and the decision lines of that folder's `ledger.md` count as lines of this session's ledger — for the boxes, for the scope of an edit and for the readings of the Estimates this session creates or updates; the ledger hook sees only this session's own lines (cases 591, 670.2). Sort the unticked boxes of the `tasks` of the Spec — `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73), or the `spec.md` of the folder of `## Conserved Spec`. A `create`, `update` or `defer` line of a page, a `guppi render` line, a `guppi sprint` line, a `guppi sprint-close` line (`rule-sprint-close`, case 628.1), a `read` line whose `estimate[...]` stands in the Tail above and a `read` line whose reading you take in this turn wait for the librarian, whose scripts tick them (cases 226, 250, 270); they are not debt. A `read` line whose `failed` line you write in this turn waits for the librarian as a reading does. A `read` line of an Estimate whose reading only the person can take, named under `## Ask the person` of `handoff.md`, waits for the person; it is neither debt nor the librarian's (case 670.2). Another `read` line without its line in the Tail is debt, and so is a box of code, a test, a command or a migration left unticked. The lines of a Case that a `{supersedes:case N}` line of the Tail names, and of its sub-cases, are not counted at all; its work stands under the superseding Case (case 282).

Each finding ends in one of three ways: a `- lesson[...]` line, which you decide on; a `- estimate[...]` line, a reading of an Estimate whose work is finished; or a line of `handoff.md` in the section of its kind, which `/handoff` writes. Retro writes no short defer and ratifies no decision: what needs a decision is a line of `## For the next session` of `handoff.md`, and a `create`, `update` or `delete` waits for the next Plan Mode (case 531.1).

Edit code only when the edit finishes work that traces to a line of this session's ledger.
Red tests: fix now when the fix finishes ratified work; otherwise save the change with `git diff` into `raw/<hi date>/<hi HHMM>/patch-<slug>.diff`, the session's folder, revert it, write a `- lesson[error][...]` line whose root cause says why Retro was reached with a regression, and name the patch in `## Debt` of `handoff.md`; the commit still needs green. A failing test or a lint finding line that `## Baseline` of `work.md` already holds was red before the work, whatever `## Expected red` names: it is a line of `## Observations` of `handoff.md`, named as red before the work; it is not debt, nothing is fixed or reverted for it, and no lesson is written for it (case 479.4).
`gh` is not available: name a bug that needs a decision in `## For the next session` of `handoff.md`, so the brief carries it.
Do not run `make lint` here: the vault is written after handoff, by the librarian. A check that reads a page or a governed file this session's Spec updates — `make lint` or one of its steps, or a hook of the working tree — is red or refuses in Work Mode until the librarian's run writes the page or renders the file, and the `make lint` of that run is its reading: `/work` marks such a red under `## Expected red` of `work.md` when the task that changes the check runs, one line naming the check and the page or file it waits for. A red or a refusal of that check on a page or file a line names is a line of `## Observations` of `handoff.md` that names the check and the page or file it waits for, and it is not debt; a red or a refusal on a page or file no line names is debt, even when another line names the same check, unless `## Baseline` holds its line. In a session with no `work.md`, such a red is a line of `## Observations` by your judgment. A red test is never an expected red: it is fixed or reverted as above (cases 473.1, 479.3).

Take the readings of the Estimates whose work is finished and that this session neither creates nor updates — by a decision line of its slug, or by an `update` that renames a page to it. A reading measures the Criterion the page carries at the moment of the reading, the one ratified last, and its line is written only when the work that Criterion names is built. Read each Estimate this session creates or updates — by a decision line of its slug, or by an `update` that renames a page to it — in this turn, on the Criterion of the Spec: the `when` and `then` of its Case, or the Criterion its item writes; the ledger hook writes such a reading only after Retro opens (cases 670.1, 670.2). For an Estimate of a rule whose Render a Case of the Spec changes, read the new text of the Render in the Spec against that Criterion: the harness file follows at the librarian's render, and its `make lint` checks the file. An Estimate whose `update` sets `passed` or `failed` by the person's decision and writes its Criterion back unchanged, and one whose `update` names one part of the page alone, is neither read nor set `failed`. The `read` line of an old Criterion in an earlier Spec is not debt and is not read (case 283). An Estimate whose `target` is the live sprint page, `entity-sprint-<id>`, and whose work is not done yet is neither read, nor put to the person, nor set `failed`: it stays `pending` for the Retro of the session that finishes its work or for the closing Case of `/sprint-close`, its `read` line waits for that moment and is neither debt nor the librarian's, and `handoff.md` names it with that moment; once its work is done, the Retro of that session reads it, or, when its `method` names the person's answer, names it under `## Ask the person` as below (case 772.2). An Estimate this session creates or updates whose `method` waits for an event — a part of it that opens with `after`, or with `by hand, after`, and names the event before a colon — and whose event has not come in this session is neither read, nor put to the person, nor set `failed`: it stays `pending`, its `read` line waits for that event and is neither debt nor the librarian's, and `handoff.md` names it with its event; once the librarian sees the event, it puts the reading under `Work`, or under `Ask the person` when its `method` names the person's answer. When the event came in this session, read it (case 781). A reading whose `method` names the person's word is not yours to take: it is a line of `## Ask the person` of `handoff.md`, with the question the person answers (case 531.1). Each other Estimate this session creates or updates that you cannot read gets a `failed` line in the same `LEDGER` block, its result opening with the date, the words `Retro, not read` and the reason; the next session shows it as a Case. Close the open `W` line of each Estimate you read or set `failed` `[x] … · work` in `frontier.md` (case 670.7). A problem seen live in a later session is a lesson of that session, not a reading, but for the reading of an Estimate whose `method` waits for an event, which a later session takes once the event has come (case 781). `handoff.md` names every Estimate whose reading cannot be taken yet.

When the review is done, commit the work: `make style` clean, `make test` green but for the tests that `## Baseline` of `work.md` holds. Then end the reply: one sentence in the language of the chat that names the commit of the work, then one `LEDGER` block that holds every reading and lesson of this turn, those of the Work readings of `/work` included. The reply holds nothing else — no heading, no list and no other paragraph — since `handoff.md` is the report of Retro, and it asks the person nothing (case 569.1). When a condition of `vault/wiki/where-to-stop.md` holds at that point, open the reply with `STOP:` and ask the person instead. The hook of `rule-retro-onward` then sends you on: commit the session folder, then call `/handoff`, which writes the report into `handoff.md`. Write no `LEDGER` block after that reply, except to answer a refusal of the ledger hook: that reply holds only a `LEDGER` block with the refused record lines written again, and the hook of `rule-retro-onward` then sends you on again (case 596). A refused line of the block that is no record — one that does not open with `- decision[`, `- estimate[` or `- lesson[` — is left out; when no line is left to write, that reply holds no `LEDGER` block, and in it you commit the session folder and call `/handoff` (case 695.2).
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
- 2026-09-29 deferred · [[decision-case-509]]
- 2026-09-30 defer by decision-case-505 superseded · [[decision-case-531.1]]
- 2026-09-30 defer by decision-case-509 superseded · [[decision-case-531.1]]
- 2026-09-30 updated: taken up: Retro shows no report and waits for no approval; it writes its readings and lessons in one reply, commits on green and calls /handoff; no short defer; a red test it cannot fix is a patch, a lesson and a Debt line; a reading that needs the person goes to Ask the person of handoff.md; the defers of cases 505 and 509 retired (case 531.1) · [[decision-case-531.1]]
- 2026-09-30 ref `estimate-retro-report-holds-each-fact-once` → `estimate-retro-runs-on-to-the-handoff` · [[decision-case-531.1]]
- 2026-10-01 updated: the reply that ends Retro holds one sentence in the language of the chat that names the commit, then the LEDGER block, and nothing else (case 569.1) · [[decision-case-569.1]]
- 2026-10-01 updated: work.md that the agent wrote or changed itself in the same turn counts as read; otherwise Retro opens it with the Read tool (case 569.2) · [[decision-case-569.2]]
- 2026-10-02 updated: in a session that /box runs, the conserved Spec is the Spec Retro reviews, and its decision lines count as this session's (case 591.8) · [[decision-case-591.8]]
- 2026-10-02 updated: the reply that answers a refusal of the ledger hook after the reply that ends Retro holds only the refused lines written again (case 596.2) · [[decision-case-596.2]]
- 2026-10-04 status: draft → built · cascade
- 2026-10-04 updated: a guppi sprint-close line waits for the librarian and is not debt (case 628.1) · [[decision-case-628.1]]
- 2026-10-05 estimate estimate-retro-leaves-out-the-sub-cases-of-a-superseded-case added · [[decision-case-660.4]]
- 2026-10-05 updated: a supersedes tag leaves the sub-cases of its Case out of the debt (case 660.4) · [[decision-case-660.4]]
- 2026-10-05 status: built → draft · cascade
- 2026-10-05 updated: Retro reads each Estimate the session creates or updates on the Criterion of the Spec, or sets it failed; a reading that needs the person waits for the person (case 670.2) · [[decision-case-670.2]]
- 2026-10-05 status: draft → built · cascade
- 2026-10-07 updated: the answer to a refusal of the ledger hook after Retro leaves out a refused line that is no record, and goes on to /handoff when nothing is left to write · [[decision-case-695.2]]
- 2026-10-10 updated: Retro leaves an Estimate of the live sprint page whose work is not done pending, its read line neither debt nor the librarian's, and names it under Ask the person once its work is done when the person's answer reads it (case 772.2) · [[decision-case-772.2]]
- 2026-10-12 updated: Retro leaves an Estimate whose method waits for an event that has not come pending, its read line neither debt nor the librarian's, and the handoff names it with its event (case 781) · [[decision-case-781.3]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
