---
type: rule
kind: MOC
purpose: Prevents a session from being loaded piecemeal by read-tool calls
status: draft
enforcement: render
governs: .claude/skills/hi/SKILL.md
render_mode: full
parent: "[[rule-session-start]]"
children: ["[[rule-internal-context]]", "[[rule-git-context]]", "[[rule-github-issues]]", "[[rule-ledger-tail]]"]
estimates: ["[[estimate-hi-no-read-calls]]", "[[estimate-hi-writes-frontier]]"]
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
description: Open a working session — sprint, brief, git state, open issues, then the Frontier.
disable-model-invocation: true
---
<!-- rule-internal-context -->
<!-- rule-git-context -->
<!-- rule-github-issues -->
<!-- rule-ledger-tail -->


Assemble the Frontier from the above in two lists, the kind of each item by its source and no page opened (case 268.2). `## Cases`, what needs a decision: on a plan branch the unfinished plan, first; the items of the sprint's current milestone — the first with an open item or with none — and none of a later milestone, of the Backlog or of Closed (case 229.3); the `Cases` list of the brief's Next session; the brief's Deferred list; a hand edit shown by `Render:`; a `failed` reading or a lesson of the Tail; an item the person adds. `## Work`, what needs none: the `Work` list of the brief's Next session; a dirty tree in `Status:`. In the chat the Cases are the agenda of Plan Mode, one line each with its detail; the Work is one block; sub-cases are cut in Cases only;
the hand edit is what `guppi render --sync` printed at session start or on the `Render:` line above.
A failed pull or an unavailable `gh` is a Cases item when `sprint.md` names no decision on it, and not an item when it does; neither is a reason to stop. A `failed` reading or a lesson in the Tail above is an item; a decision line of the tail is not — its page comes with the next librarian. Write the same two lists, under `## Cases` and `## Work`, to `vault/raw/<date>/<hi HHMM>/frontier.md` — the session's folder, `HHMM` from the `hi:` line the `UserPromptSubmit` hook put in context (cases 73, 125) — one line per item:
`- [ ] C<n> — <title> · <source>` under `## Cases`, `- [ ] W<n> — <title> · <source>` under `## Work`. Close a line when its item ends, the closer appended and the source kept — `- [x] C2 — <title> · sprint · case 315` (case 314.1): `[x] … · case N`
when ratified, `[x] … · work` when it needs no decision, `[-] … · defer case N` when
deferred, `[-] … · sprint` when the item is a line of the sprint page left for a later session — no decision, no `deferred_by` (case 310.5); an item the person adds is a new Cases line; a `W` that turns out to need a decision closes `· case N`, a `C` that needs none closes `· work`. `/pre-spec` fails on an open line. Wait
for the human to pick the order or defer items. Before any `create`, ask the vault first
([[rule-ask]]).
<!-- /rule-skill-hi -->

## How it works

Rendered in full into the skill file; the four children splice into the markers below, in
the order they are listed. Editing the skill directly is meaningless once the renderer
exists (Slice 2) — the next render overwrites it. Until then the file and this page are two
copies of one text, kept identical by hand.

`disable-model-invocation: true` in the frontmatter: only the person opens a working
session. The skill writes no event line of its own since case 111.4: a `!` substitution never saw `CLAUDE_SESSION_ID` (every `hi` of sessions A–M carried `--------`), so the `hi` line is the `UserPromptSubmit` hook's, which reads the session id from its payload (`rule-event-log`, case 111.1).

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
