---
type: rule
kind: MOC
purpose: Prevents a session from being loaded piecemeal by read-tool calls
status: built
enforcement: render
governs: .claude/skills/hi/SKILL.md
render_mode: full
parent: rule-session-start
children: [rule-internal-context, rule-git-context, rule-github-issues]
estimates: [estimate-hi-no-read-calls, estimate-hi-writes-frontier]
deferred_by: [decision-case-98]
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

Assemble the Frontier from the above and present it as a list: tasks, problems, debt
carried over, where the sprint stands; on a plan branch the unfinished plan comes first;
what `guppi render --sync` printed at session start is an item when it shows a hand edit.
A failed pull or an unavailable `gh` is an item on that list, not a reason to stop. Write the same list to `vault/raw/<date>/<hi HHMM>/frontier.md` — the session's folder, `HHMM` the time of the `hi` line above (case 73) — one line per item:
`- [ ] F<n> — <title> · <source>`. Close a line when its item ends: `[x] … · case N`
when ratified, `[x] … · work` when it needs no decision, `[-] … · defer case N` when
deferred; an item the person adds is a new line. `/pre-task` fails on an open line. Wait
for the human to pick the order or defer items. Before any `create`, ask the vault first
(§3 of `vault/wiki/index.md`).
<!-- /rule-skill-hi -->

## How it works

Rendered in full into the skill file; the three children splice into the markers below, in
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
