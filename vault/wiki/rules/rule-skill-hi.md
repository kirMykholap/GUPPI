---
type: rule
kind: MOC
purpose: Prevents a session from being loaded piecemeal by read-tool calls
status: draft
enforcement: render
governs: .claude/skills/hi/SKILL.md
render_mode: full
parent: rule-session-start
children: [rule-internal-context, rule-git-context, rule-github-issues, rule-ledger-tail]
estimates: [estimate-hi-no-read-calls, estimate-hi-writes-frontier]
deferred_by: [decision-case-106]
origin: raw/2026-09-09/ledger.md#case-11
sprint: migration
created: 2026-09-09
tags: [session, harness]
---

## Purpose

Prevents a session from being loaded piecemeal by read-tool calls. Bash substitutions in a
skill body resolve before the agent's first turn, so the context is simply present — there
is no step the agent can forget or reorder. The skill also leaves the `hi` mark in the
event log itself: a command typed by the person does not pass through the `Skill` tool, so
no hook would see it.

## Render

<!-- rule-skill-hi -->
---
name: hi
description: Open a working session — sprint, brief, git state, open issues, then the Frontier.
disable-model-invocation: true
---
Recorded: !`uv run guppi event hi --session "${CLAUDE_SESSION_ID:-}"`

<!-- rule-internal-context -->
<!-- rule-git-context -->
<!-- rule-github-issues -->
<!-- rule-ledger-tail -->


Assemble the Frontier from the above and present it as a list: tasks, problems, debt
carried over, where the sprint stands; on a plan branch the unfinished plan comes first;
what `guppi render --sync` printed at session start is an item when it shows a hand edit.
A failed pull or an unavailable `gh` is an item on that list, not a reason to stop. A `failed` reading or a lesson in the Tail above is an item; a decision line of the tail is not — its page comes with the next librarian. Write the same list to `vault/raw/<date>/<hi HHMM>/frontier.md` — the session's folder, `HHMM` the time of the `hi` line above (case 73) — one line per item:
`- [ ] F<n> — <title> · <source>`. Close a line when its item ends: `[x] … · case N`
when ratified, `[x] … · work` when it needs no decision, `[-] … · defer case N` when
deferred; an item the person adds is a new line. `/pre-task` fails on an open line. Wait
for the human to pick the order or defer items. Before any `create`, ask the vault first
(§3 of `vault/wiki/index.md`).
<!-- /rule-skill-hi -->

## How it works

Rendered in full into the skill file; the four children splice into the markers below, in
the order they are listed. Editing the skill directly is meaningless once the renderer
exists (Slice 2) — the next render overwrites it. Until then the file and this page are two
copies of one text, kept identical by hand.

`disable-model-invocation: true` in the frontmatter: only the person opens a working
session. `${CLAUDE_SESSION_ID:-}` passes the session id to the event log when the variable
exists inside a substitution and an empty string otherwise; the probe of Slice 1 measures
which. For that one session the skill file carries an extra `Probe:` line that is not part
of this render.

## Estimates

- [[estimate-hi-no-read-calls]]
- [[estimate-hi-writes-frontier]]

## Children

1. [[rule-internal-context]]
2. [[rule-git-context]]
3. [[rule-github-issues]]
4. [[rule-ledger-tail]]

## Parent

- [[rule-session-start]]

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
