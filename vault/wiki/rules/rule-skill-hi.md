---
type: rule
kind: MOC
purpose: Prevents a session from being loaded piecemeal by read-tool calls
status: built
enforcement: render
governs: .claude/skills/hi/SKILL.md
render_mode: full
parent: "[[rule-session-start]]"
children: ["[[rule-internal-context]]", "[[rule-git-context]]", "[[rule-ledger-tail]]"]
estimates: ["[[estimate-hi-no-read-calls]]", "[[estimate-hi-writes-frontier]]", "[[estimate-hi-takes-its-readings]]"]
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness]
---

## Purpose

Prevents a session from being loaded piecemeal by read-tool calls. Bash substitutions in a
skill body resolve before the agent's first turn, so the context is simply present — there
is no step the agent can forget or reorder. The `hi` mark in the event log is left by the `UserPromptSubmit` hook `guppi event prompt` (`rule-event-log`, case 111.1), which sees the session id; the skill's own `!` substitution could not (case 111.4). A command typed by the person does not pass through the `Skill` tool, so no `PreToolUse` hook sees it. It puts [[brief]] and [[sprint]] into the context before the first turn.

## Render

<!-- rule-skill-hi -->
---
name: hi
description: Open a working session — sprint, brief, git state, then the Frontier.
disable-model-invocation: true
allowed-tools: Bash(uv run guppi render --sync), Bash(git branch --show-current), Bash(git status --short), Bash(uv run guppi tail)
---
<!-- rule-internal-context -->
<!-- rule-git-context -->
<!-- rule-ledger-tail -->


Assemble the Frontier from the above in three lists, the kind of each item by its source and no page opened (case 268.2). `## Cases`, what needs a decision: on a plan branch the unfinished plan, and each conserved Spec `backlog.md` names, one line each with the source `backlog`, first; the items of the sprint's current milestone — the first with an open item or with none — and none of a later milestone, of the Backlog or of Closed (case 229.3); the `Cases` list of the brief's Next session; a hand edit shown by `Render:`; a `failed` reading or a lesson of the Tail; an item the person adds. `## Work`, what needs none: the `Work` list of the brief's Next session; a dirty tree in `Status:`. `## Ask`, what only the person can answer: the `Ask the person` list of the brief's Next session, one line per reading with its question (case 531.11). The other items of `backlog.md` are no lines of their own: `## Cases` ends with the line `Backlog: N items`, N the items `backlog.md` counts, and under a Cases line an indented line `- near` names, by slug in a code span, each backlog item whose `purpose` is near that line in meaning — the agent's own judgment from `backlog.md` in its context, no `ask-guppi`; an item the person brings onto the Frontier is a Cases line of its own, source `backlog`, its title opening with its slug in a code span, so that `guppi backlog` counts it (case 451.1). In the chat the Cases are the agenda of Plan Mode, shown as a checklist: each line as `frontier.md` holds it, `- [ ] C<n> — <title> · <source>`, its detail on an indented line under it and the `- near` line under that, the line `Backlog: N items` last; no Case stands as a bold line or with its detail as a paragraph (case 508.2); the Work is one block; sub-cases are cut in Cases only;
the hand edit is what `guppi render --sync` printed at session start or on the `Render:` line above.
A `failed` reading or a lesson in the Tail above is an item; a decision line of the tail is not — its page comes with the next librarian. Write the same three lists, under `## Cases`, `## Work` and `## Ask`, to `vault/raw/<date>/<hi HHMM>/frontier.md` — the session's folder, `HHMM` from the `hi:` line the `UserPromptSubmit` hook put in context (cases 73, 125) — one line per item:
`- [ ] C<n> — <title> · <source>` under `## Cases`, `- [ ] W<n> — <title> · <source>` under `## Work`, `` - [ ] A<n> — `<slug>` — <question> · brief `` under `## Ask`. An item of the sprint's milestone is a line of its own whose title opens with the slug of each page it names, each in a code span — ``- [ ] C1 — `rule-x`, <milestone> · sprint``. Close a line when its item ends, the closer appended and the source kept — `- [x] C2 — <title> · sprint · case 315` (case 314.1). `[x]` is an item ended: `[x] … · case N` when ratified, `[x] … · work` when it needs no decision. `[-]` is an item put off: `[-] … · sprint · defer` when the item is a line of the sprint page left for a later session — no Case, no ledger line, no `deferred_by`, never `· defer case N` (cases 310.5, 356.2); `[-] … · backlog · kept` when an item of `backlog.md` is left as it stands — no Case, no ledger line, it stays in the backlog; `[-] … · defer case N` when a decision of any other source is put off — a short-form Case and its ledger line, and its target enters `backlog.md` through `deferred_by` (case 451.1); an item the person adds is a new Cases line; a `W` that turns out to need a decision closes `· case N`, a `C` that needs none closes `· work`. `/pre-spec` fails on an open line under `## Cases`, not on one under `## Work` or `## Ask`; a `W` or an `A` line closes `· work` when its work is done, where it is done: at `/hi`, in Work Mode or at Retro (cases 356.1, 508.2). Claude Code's plan mode does not stop this: the agent writes `frontier.md` and closes its lines while plan mode is on — a working file of the session (`rule-permissions`, case 363). Before the question on the order, in the same reply, take each reading of an open `W` line whose `method` names the `/hi` of a session or the librarian's run and whose whole method can be done now: from the brief, `git log`, `git status`, the commands the method names, and the transcript of the previous session for the librarian's report. The Frontier is still assembled with no page opened; this step opens the page of each Estimate it reads and judges the reading against its `## Criterion`. Close those lines `[x] … · work` in `frontier.md` first, then write the reading lines in a `LEDGER` block of the reply, which ends in text. A reading whose `method` also names a later moment waits for that moment, its `/hi` part read then from the session's first turn; a reading whose `method` asks for a `/hi` run of its own is not taken here (case 508.1). Then put each open `A` line to the person as a question, in the same reply, before the question on the order: the Estimate by slug and its question. When the person answers one, close its line `[x] … · work` in `frontier.md` first, then write its reading line in a `LEDGER` block of the reply, which ends in text, the answer as its result (case 531.13). Wait for the human to pick the order or defer items. Every Case is built by `case-guppi` (`rule-case-build`).
<!-- /rule-skill-hi -->

## How it works

Rendered in full into the skill file; the three children splice into the markers below, in
the order they are listed. Editing the skill directly is meaningless once the renderer
exists (Slice 2) — the next render overwrites it. Until then the file and this page are two
copies of one text, kept identical by hand.

`disable-model-invocation: true` in the frontmatter: only the person opens a working session, and only in plan mode: the hook of `rule-event-log` refuses a `/hi` whose `permission_mode` is not `plan`, missing or empty included, writes no `hi` line, and Claude Code blocks the prompt (case 445.6). `defaultMode: plan` in `.claude/settings.json` does not hold when the mode changes before `/hi`; a session begun outside plan mode once wrote its plan file under a second name. A session repaired without `/hi` stays possible: it holds no Case. `allowed-tools` names the four `!` commands of the skill: since client 2.1.282 the Bash check is server-side and a `!` substitution the person types gets no verdict ("The server-side auto mode classifier gave no verdict for Bash: the request that produced this action did not ask for one", session 1b191eaf, 2026-09-26), so a command no rule allows is refused and `/hi` does not open; a matching rule needs no classifier. The skill writes no event line of its own since case 111.4: a `!` substitution never saw `CLAUDE_SESSION_ID` (every `hi` of sessions A–M carried `--------`), so the `hi` line is the `UserPromptSubmit` hook's, which reads the session id from its payload (`rule-event-log`, case 111.1).

## History

- 2026-09-09 created · raw/2026-09-09/ledger.md#case-11
- 2026-09-10 status: draft → built · cascade
- 2026-09-12 updated: the Frontier is written to raw/<date>/frontier.md and closed line by line; estimate-hi-writes-frontier added · [[decision-case-59.2]]
- 2026-09-12 updated: a hand edit shown by render --sync at session start is a Frontier item (case 59.7) · [[decision-case-59.7]]
- 2026-09-12 status: built → draft · cascade
- 2026-09-12 updated: the Frontier lands in the session's folder (case 73.3) · [[decision-case-73.3]]
- 2026-09-12 status: draft → built · cascade
- 2026-09-12 deferred · [[decision-case-98]]
- 2026-09-13 child rule-ledger-tail added · [[decision-case-101.2]]
- 2026-09-13 updated: rule-ledger-tail the fourth child; its marker after rule-github-issues, the tail in the context without a read call (case 101.3) · [[decision-case-101.3]]
- 2026-09-13 updated: a failed reading or a lesson of the tail is a Frontier item, a decision line is not (case 101.4) · [[decision-case-101.4]]
- 2026-09-13 defer by decision-case-98 superseded · [[decision-case-106]]
- 2026-09-13 deferred · [[decision-case-106]]
- 2026-09-13 status: built → draft · cascade
- 2026-09-14 updated: the Recorded substitution removed and the CLAUDE_SESSION_ID paragraph replaced; the hi line is the UserPromptSubmit hook's (case 111.4) · [[decision-case-111.4]]
- 2026-09-14 updated: the Frontier sentence covers the Render line of /hi (case 115.2) · [[decision-case-115.2]]
- 2026-09-14 defer by decision-case-106 superseded · [[decision-case-115]]
- 2026-09-14 status: draft → built · cascade
- 2026-09-14 updated: the time of the session's folder comes from the hook's hi line in context, not from a line the skill no longer prints (case 125) · [[decision-case-125]]
- 2026-09-14 updated: the hub file linked for the graph (case 149.4) · [[decision-case-149.4]]
- 2026-09-18 updated: the Frontier takes the current milestone of the sprint only (case 229.3) · [[decision-case-229.3]]
- 2026-09-18 status: built → draft · cascade
- 2026-09-18 status: draft → built · cascade
- 2026-09-20 updated: the Frontier in two lists, Cases and Work, the kind of an item by its source — sprint, the brief's Next session and Deferred, the tail, git status, the person; pull and gh not an item when sprint.md names their decision; C<n> and W<n> lines (case 268.2) · [[decision-case-268.2]]
- 2026-09-20 status: built → draft · cascade
- 2026-09-20 status: draft → built · cascade
- 2026-09-22 updated: the closer `· sprint` for a sprint item left for later (case 310.5) · [[decision-case-310.5]]
- 2026-09-22 updated: the closer is appended, the source of a line stays (case 314.1) · [[decision-case-314.1]]
- 2026-09-22 updated: the vault query is named by rule-ask (case 318) · [[decision-case-318]]
- 2026-09-22 status: built → draft · cascade
- 2026-09-23 deferred · [[decision-case-352]]
- 2026-09-23 updated: a sprint item in the Frontier is one line, its title opening with its slugs in code spans (case 354.3) · [[decision-case-354.3]]
- 2026-09-23 defer by decision-case-352 superseded · [[decision-case-356.1]]
- 2026-09-23 updated: pre-spec fails on an open Cases line; a W line closes when its work is done (case 356.1, supersedes 352) · [[decision-case-356.1]]
- 2026-09-23 updated: a sprint line never closes defer case N (case 356.2) · [[decision-case-356.2]]
- 2026-09-23 updated: plan mode does not stop the write of frontier.md or the closing of its lines (case 363) · [[decision-case-363]]
- 2026-09-23 status: draft → built · cascade
- 2026-09-25 updated: the Case is built by case-guppi, which asks the vault itself (case 419.1) · [[decision-case-419.1]]
- 2026-09-25 updated: the closer kept for a deferred item left as it stands (case 421.4) · [[decision-case-421.4]]
- 2026-09-25 status: built → draft · cascade
- 2026-09-25 status: draft → built · cascade
- 2026-09-26 updated: the allowed-tools line of the Render frontmatter allows the six ! commands of /hi; the server-side classifier of client 2.1.282 gives no verdict for a substitution the person types (commit 54509ed) · [[decision-case-439]]
- 2026-09-27 updated: the page says /hi opens a session only in plan mode, refused by the hook of rule-event-log (case 445.7) · [[decision-case-445.7]]
- 2026-09-27 updated: the Frontier closes a line [x] for an item ended and [-] for one put off — sprint · defer, backlog · kept, defer case N; conserved Specs first, the backlog counted and its near items named (case 451.1) · [[decision-case-451.1]]
- 2026-09-27 status: built → draft · cascade
- 2026-09-27 status: draft → built · cascade
- 2026-09-28 status: built → draft · cascade
- 2026-09-29 updated: /hi takes the readings of /hi and of the librarian's run in its first reply (case 508.1) · [[decision-case-508.1]]
- 2026-09-29 estimate estimate-hi-takes-its-readings added · [[decision-case-508.1]]
- 2026-09-29 updated: the Cases shown in the chat at /hi as a checklist, the detail on an indented line; a W line closes where its work is done, at /hi, in Work Mode or at Retro (case 508.2, supersedes 507) · [[decision-case-508.2]]
- 2026-09-29 status: draft → built · cascade
- 2026-09-30 updated: the frame without the pull and the issues: description, allowed-tools and the marker of rule-github-issues (case 528.3) · [[decision-case-528.3]]
- 2026-09-30 updated: the Frontier gets the list ## Ask from the brief's Ask the person, three lists in all; the rule for a failed pull or gh gone, carried from case 528.4 (case 531.11, supersedes 528.4) · [[decision-case-531.11]]
- 2026-09-30 updated: /hi puts each open Ask line to the person; the answer becomes the reading line (case 531.13) · [[decision-case-531.13]]
- 2026-09-30 status: built → draft · cascade
- 2026-09-30 child rule-github-issues archived · cleanup
- 2026-09-30 updated: a sprint line keeps its slugs in code spans; the count by generate, removed by case 539.1, is no longer its reason (case 539.3) · [[decision-case-539.3]]
- 2026-09-30 status: draft → built · cascade
