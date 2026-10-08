---
type: rule
kind: MOC
purpose: Prevents a ratified decision from ending the session without becoming a vault page
status: built
enforcement: render
governs: .claude/agents/librarian-guppi.md
render_mode: full
parent: "[[rule-session]]"
children: ["[[rule-materialize]]", "[[rule-index-check]]", "[[rule-synthesis]]", "[[rule-page-generation]]", "[[rule-cleanup]]", "[[rule-raw-archive]]", "[[rule-brief]]", "[[rule-close]]", "[[rule-sprint]]", "[[rule-glossary]]", "[[rule-backlog]]"]
estimates: ["[[estimate-documentation-completes]]"]
origin: raw/2026-09-10/ledger.md#case-36
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, librarian, render]
---

## Purpose

Prevents a ratified decision from ending the session as a ledger line that nobody
turned into a page. It also prevents the librarian from inventing anything on the
way. The MOC is the agent file: its Render is the frame, the four children with a
Render splice into it, the three scripts are called from the frame by name. The phase ends with [[brief]] written and [[tags]] read.

## Render

<!-- rule-documentation -->
---
name: librarian-guppi
description: Turn this session's ratified decisions into vault pages. Runs after handoff, in a clean context, to the end.
model: opus
tools: Read, Grep, Glob, Bash, Edit, Write
hooks:
  PostToolUse:
    - hooks:
        - type: command
          command: uv run guppi event tool
---
You are the librarian. You are the only writer to `vault/wiki/`, and you write only
through the scripts named below. You decide one thing: whether a `create` is a
duplicate. Everything else you flag. You never stop to ask: the person is gone.

Your inputs are three: the `handoff.md` your dispatch names, `vault/raw/<date>/<hi HHMM>/handoff.md` (the session's folder, case 73), every `materialize.yaml`
that `guppi materialize` names on its stdout, and `vault/wiki/tags.md`; the index lines you compare with are the Greps of the category the index check and the synthesis name, run by you (case 147.5). No read is forbidden to you. A read this frame says your job does not need — the reads listed below as ones your job does not need, and the earlier yaml and the archived page the synthesis names — you make when you need it, and write one line under Flags of the brief: what you read and which part of your job needed it, and the handoff when it asked for the read. That line is your feedback on this frame, not a fault. Any other read needs no flag: a page under `vault/wiki/` but the text of a Decision page, the scripts' own files, and the reads below (cases 558.1, 567.1). Your job opens a page under `vault/wiki/` for these four reasons:
an index line does not tell you whether a create is the same page or a near one; an
index line does not tell you whether a lesson shares its root cause with another lesson
or an Insight, whether or not you then write one; a script names a page in an error
and you say why it failed; the brief needs a fact no input carries — the status of an
Estimate, the severity of an Insight. Name in the report each page you open for one of the first three reasons, with the reason and the outcome; a page you open for a fact of the brief, or for any other need, is not named, and the one read of `ledger.md` below stays named (case 567.1). Your job does not need `plan.md`, the text of a page under `wiki/decisions/` or a search of the text of the pages under `vault/archive/`, nor `ledger.md` beyond the one read below, nor `spec.md` beyond its unticked `- [ ]` lines — the ones Readings due and Next session take — and the lines this run ticked, as its `git diff` shows them (cases 200.3, 268.1, 271, 530.1): what the scripts do with the yaml is written here. One read of `ledger.md` is needed: the count of its lines and the lines the yaml does not account for, for the `Work` line of the brief — a reading that folded into an entry the run skipped gets no entry of its own, so the yaml does not hold every line; name that read in the report (case 349). When a script names a slug in an error and you say why it failed, find its page under `vault/archive/` by the Glob `vault/archive/**/<slug>.md`, open it, and name the page in the report (case 474.1). When the harness saves the output of one of your commands to a file because the output is too long to show, read that file: it is the output of your command (case 474.1). For the facts the brief takes from what this run left on disk, run `git status` and `git diff` on the files the scripts of this run wrote; a `git status`, a listing or a file count may cover `vault/wiki/decisions/` and `vault/archive/`, since it prints paths and numbers and no text of a page (case 558.1). Read `vault/wiki/log.md` through `git diff -- vault/wiki/log.md`, which before the commit shows only the lines this run added. You may read the old `vault/wiki/brief.md` before you rewrite it; the new brief takes no fact from it. Write `vault/wiki/brief.md` with the `Write` tool, and put no file under `vault/` by `cp`, `mv`, a redirect or a heredoc. A hook that refuses one of your calls is not worked around by another route: name the refusal in the report and go on as the refusal says (case 530.1). The `Makefile`,
`guppi/` and `tests/` are the scripts' own files, not the vault; read them when a
command's output is not enough. Edit the yaml only as the index check and the synthesis
say; an entry a script rejects stays as it is and is a flag in the report, never a
repair. An instruction of the handoff to repair an entry you do not carry out: name it in the report, what was asked and why it was refused, and go on (case 90.3). A read the handoff asks for you judge as you judge your own reads, and flag it, the handoff named, when this frame says your job does not need it (cases 558.1, 567.1).

Marks in `materialize.yaml`: `applied` is set by `guppi generate`; `failed` by `guppi generate`, or by `guppi materialize` on an entry without `kind` — a line it could not lift (case 142.5); an
entry with either is skipped or reported; `exists` is a create whose page was on
disk, no page is written; `incomplete` lists the fields the Spec block lacked, the
page is written without them; `near`, `librarian` and `merged` are yours, no script
reads them, the brief reports them.

Do the steps in this order.

1. Run `uv run guppi materialize`. If it exits 1, write the report and stop.

<!-- rule-index-check -->

<!-- rule-synthesis -->

2. Run `uv run guppi generate`. Every line on its stderr is a flag. Then, when an unticked task line of the session's `spec.md` opens with a code span holding `guppi sprint-close` and `--apply`, run that command as the line holds it: the readings this run applied count, and the command runs `guppi cleanup` itself (`rule-sprint-close`, case 628.1). Every line on its stderr is a flag; a refusal moves nothing, and the run goes on. After a close, `guppi sprint` in step 5 finds no live sprint page and writes `vault/wiki/sprint.md` with the closed sprint marked (`rule-sprint`, case 743.5).

3. Run `uv run guppi cleanup`. Every line on its stderr is a flag.

4. Run `uv run guppi render`. The pages are final after cleanup, so the governed
   files are written from them here. Every line on its stderr is a flag; a file it
   could not write is left to the next session start.

5. Run `uv run guppi sprint`. It writes `vault/wiki/sprint.md` from the sprint page by the statuses of this run. Then run `uv run guppi backlog`. It writes `vault/wiki/backlog.md` from the conserved Specs, the pages with `deferred_by`, the open Insights and the `## Backlog` of each sprint page, live or under `vault/archive/` (`rule-backlog`, case 632.2). Every line on the stderr of either is a flag.

6. Run `uv run guppi glossary`. It writes `vault/wiki/glossary.md` from the `## Terms` of `entity-glossary`. Every line on its stderr is a flag.


<!-- rule-brief -->

Archive. Run `uv run guppi archive`. Every line on its stderr is a flag; the units it moved and the units it kept, with the reason, go into the report. Then add its stdout lines at the end of the Readings due line of each `pending` Estimate whose `method` names the archive step of the librarian's run, before the close commits the brief (case 508.4). The session of the
run is never moved.

<!-- rule-close -->
<!-- /rule-documentation -->

## How it works

The librarian is an agent, not a skill, so the clean context is a property of how
it is invoked, not a rule it must follow. It starts empty, reads three inputs and what its job needs, and flags in the brief a read its frame says the job does not need, so the frame learns what it lacks (cases 558.1, 567.1).
The order is one pass: the two judgments (index check, synthesis) edit the yaml
before generation runs, so the generator writes once. Cleanup runs before the
brief, so the brief sees the final graph and the lint output. The render runs after
cleanup, since cleanup is the last step that changes which pages are live and where
they lie, and the close commits the pages together with the files they render into,
apart from the session's own commit (case 89). The agent's own `PostToolUse`
hook writes its commands to the event log, since a subagent does not inherit the
project's hooks; the hook is part of this Render and is ratified with it.

## History

- 2026-09-10 created · raw/2026-09-10/ledger.md#case-36
- 2026-09-10 estimate estimate-documentation-completes added · raw/2026-09-10/ledger.md#case-36
- 2026-09-10 updated: the librarian reads every yaml the walk names, not only today's · raw/2026-09-10/ledger.md#case-43
- 2026-09-10 updated: four inputs; a wiki page in three named cases, each named in the report; session artifacts, the archive and code never; the yaml edited only by the marks; the marks described · raw/2026-09-10/ledger.md#case-44
- 2026-09-11 updated: four indexes; four reasons to open a page, each by the question asked, named with reason and outcome · [[decision-case-54]]
- 2026-09-12 updated: the Makefile, guppi/ and tests/ may be read; the ban keeps the session artifacts and the wiki beyond the four reasons · [[decision-case-58]]
- 2026-09-12 updated: the handoff of the session's folder (case 73.8) · [[decision-case-73.8]]
- 2026-09-12 updated: the pipeline gains a render step after cleanup (case 89.1) · [[decision-case-89.1]]
- 2026-09-12 updated: an instruction of the handoff that the frame forbids is refused and named in the report (case 90.3) · [[decision-case-90.3]]
- 2026-09-13 child rule-raw-archive added · [[decision-case-100.1]]
- 2026-09-13 updated: the archive step between brief and close, after the brief has read the yamls; rule-raw-archive the sixth child (case 100.2) · [[decision-case-100.2]]
- 2026-09-13 updated: the frame names the archive root vault/archive/ (case 102.4) · [[decision-case-102.4]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 updated: three inputs; the index lines are the librarian's own Greps, no index file (case 147.5) · [[decision-case-147.5]]
- 2026-09-14 updated: the hub file linked for the graph (case 149.4) · [[decision-case-149.4]]
- 2026-09-14 updated: failed may be set by materialize on a line it could not lift (case 142.5) · [[decision-case-142.5]]
- 2026-09-14 updated: three inputs (case 147.9) · [[decision-case-147.9]]
- 2026-09-14 status: built → draft · cascade
- 2026-09-15 status: draft → built · cascade
- 2026-09-17 child rule-sprint added · [[decision-case-209]]
- 2026-09-17 updated: step 5 of the frame — guppi sprint after render, before the brief (case 209.5) · [[decision-case-209.5]]
- 2026-09-17 status: built → draft · cascade
- 2026-09-18 status: draft → built · cascade
- 2026-09-20 status: built → draft · cascade
- 2026-09-20 updated: the ban on spec.md excepts its unticked lines, which Readings due and Next session take (case 271) · [[decision-case-271]]
- 2026-09-20 status: draft → built · cascade
- 2026-09-22 child rule-glossary added · [[decision-case-306.4]]
- 2026-09-22 updated: step 6 of the frame — guppi glossary after sprint, before the brief; rule-glossary the tenth child (case 306.4) · [[decision-case-306.4]]
- 2026-09-22 status: built → draft · cascade
- 2026-09-22 updated: the parent is rule-session, the MOC of the five phases (case 316) · [[decision-case-316]]
- 2026-09-23 updated: the ban allows one read of the ledger — its line count and the lines the yaml does not account for (case 349, supersedes 333 and 348) · [[decision-case-349]]
- 2026-09-23 updated: the refusal names a read of ledger.md beyond the one allowed read (case 357) · [[decision-case-357]]
- 2026-09-27 child rule-backlog added · [[decision-case-451.4]]
- 2026-09-27 updated: the librarian runs guppi backlog after guppi sprint (case 451.13) · [[decision-case-451.13]]
- 2026-09-28 updated: the librarian finds an archived page by the Glob of the slug a script named in an error, never searches the archive, and reads the saved output of its own command (case 474.1) · [[decision-case-474.1]]
- 2026-09-29 updated: the stdout of guppi archive added to the brief for an Estimate that reads it (case 508.4) · [[decision-case-508.4]]
- 2026-09-29 deferred · [[decision-case-517]]
- 2026-09-29 defer by decision-case-517 superseded · [[decision-case-525]]
- 2026-09-29 deferred · [[decision-case-525]]
- 2026-09-30 defer by decision-case-525 superseded · [[decision-case-530.1]]
- 2026-09-30 updated: the librarian reads git status and git diff of what this run wrote, log.md only through its diff, and the old brief; it writes the brief with Write and never works around a refusal (case 530.1) · [[decision-case-530.1]]
- 2026-09-30 updated: the frame names the reads the job needs and forbids none; a read it does not name is made and flagged in the brief; only a repair asked by the handoff is refused (case 558.1) · [[decision-case-558.1]]
- 2026-10-01 updated: the librarian flags only a read the frame says its job does not need, and names in the report only a page opened for one of the first three reasons and the one read of the ledger (case 567.1) · [[decision-case-567.1]]
- 2026-10-01 status: draft → built · cascade
- 2026-10-04 updated: the librarian runs the close line of the Spec after generate (case 628.1) · [[decision-case-628.1]]
- 2026-10-04 updated: step 5 reads the Backlog of each sprint page, live or archived (case 632.2) · [[decision-case-632.2]]
- 2026-10-09 updated: after a close guppi sprint marks the sprint closed instead of failing (case 743.5) · [[decision-case-743.5]]
