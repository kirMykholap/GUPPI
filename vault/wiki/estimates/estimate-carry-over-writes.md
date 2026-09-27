---
type: estimate
kind: QA
status: pending
target: "[[rule-carry-over]]"
purpose: /carry writes the brief and the mark and runs guppi backlog and nothing else
method: pytest over the skill's render, plus one live reading of a carried-over session
checked: 2026-09-18
origin: raw/2026-09-16/1034/ledger.md#case-190.1
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness]
---

## Criterion

When:
The agent calls the skill `/carry` on `PreToolUse Skill`, after the person answered "conserve" at the fork `ExitPlanMode` prints. The person never types it.

Then:
The skill reads the tree. When the tree holds changes outside the session folder and `vault/wiki/brief.md`, the skill stops and says that work was done and the ordinary exit applies.
**＋** Otherwise it rewrites `vault/wiki/brief.md` in the short shape, with no Deferred list.
**＋** It puts `carry.md` into the session folder: one line, a flag for `materialize` and `guppi backlog`, not a document. The session that finishes the work deletes it.
**＋** It runs `uv run guppi backlog`, and `vault/wiki/backlog.md` then shows the conserved Spec with its targets.
**＋** It runs `make style` and commits `vault/raw/`, `vault/wiki/brief.md` and `vault/wiki/backlog.md`.
**－** It runs no Work Mode, `/retro`, `/handoff`, librarian, `materialize`, `generate`, `cleanup` or `render`, and it writes no decision. It writes no page of `vault/wiki/`.
**－** The work stays sequential, session after session: one conserved Spec, no parallel work.
**－** `.claude/skills/carry/SKILL.md` equals the Render of the page and is not edited by hand.

## Result

2026-09-18, the live /carry of session 2054 after ExitPlanMode and the person's "conserve": Tree held only raw/2026-09-18/2054/; brief.md rewritten in the short shape, carry.md one line, make style clean, commit ba0240b of vault/raw/ and vault/wiki/brief.md; nothing else run, no page of wiki/ but the brief; the fork line of guppi spec was not visible in the ExitPlanMode result — the agent asked the fork itself

## History

- 2026-09-16 created · [[decision-case-190.1]]
- 2026-09-16 updated: the Criterion replaced whole by case 196.1 — the agent's call after the fork, the brief, the flag, the commit, nothing else run (case 196.1) · [[decision-case-196.1]]
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-18 updated: the Render changed under it — the Deferred paragraph; the Criterion stands as it was (case 233.4) · [[decision-case-233.4]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/2054/ledger.md#L12
- 2026-09-23 updated: the Render changed under it — step 1 names the place of the frame; the Criterion stands (case 347) · [[decision-case-347]]
- 2026-09-27 updated: the Criterion replaced whole — no Deferred list, guppi backlog run and backlog.md committed (case 451.9) · [[decision-case-451.9]]
