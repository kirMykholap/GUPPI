---
type: estimate
kind: QA
status: passed
target: "[[rule-carry-over]]"
purpose: /carry writes the brief and the mark, runs guppi backlog, commits, makes the branch of the Spec at that commit, and runs nothing else
method: uv run --project .guppi guppi render --check; by hand, a /carry after the fork of ExitPlanMode — the tree, vault/wiki/brief.md, carry.md, vault/wiki/backlog.md, the commit and git branch read
checked: 2026-10-03
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, harness]
core: true
---

## Criterion

When:
The agent calls the skill `/carry` on `PreToolUse Skill`, after the person answered "conserve" at the fork `ExitPlanMode` prints. The person never types it.

Then:
The skill reads the tree. When the tree holds changes outside the session folder and `vault/wiki/brief.md`, the skill stops and says that work was done and the ordinary exit applies.
**＋** Otherwise it rewrites `vault/wiki/brief.md` in the short shape, with no Deferred list.
**＋** The short shape holds Where things stand, Flags and Next session, with no Readings due and no Readings at the close.
**＋** Next session holds `Cases`, `Work` and `Ask the person`, one line per item, a list with no item the line "none": `Cases` is always the line "none", since a deferred decision reaches `/hi` through `vault/wiki/backlog.md` and a sprint item through `vault/wiki/sprint.md`; `Work` holds each open `W` line of `raw/<hi date>/<hi HHMM>/frontier.md`, and `Ask the person` each open `A` line with its Estimate by slug, the mark `needs the person` and its question.
**＋** It puts `carry.md` into the session folder: one line, a flag for `materialize` and `guppi backlog`, not a document. The session that finishes the work deletes it.
**＋** It runs `uv run --project .guppi guppi backlog`, and `vault/wiki/backlog.md` then shows the conserved Spec with its targets.
**＋** It runs `uv run --project .guppi guppi style` and commits `vault/raw/`, `vault/wiki/brief.md` and `vault/wiki/backlog.md`.
**＋** After that commit it runs `git branch spec/<hi date>-<hi HHMM>`, so the branch of the Spec points at the commit that holds the whole of `/carry`.
**－** No open `W` or `A` line of `frontier.md` is left out of Next session, so the next `/hi` takes each one into its Frontier.
**－** It runs no Work Mode, `/retro`, `/handoff`, librarian, `materialize`, `generate`, `cleanup` or `render`, and it writes no decision. It writes no page of `vault/wiki/`.
**－** It switches to no branch: the session stays on the branch it ran on.
**－** The work stays sequential, session after session: one conserved Spec, no parallel work.
**－** `.claude/skills/carry/SKILL.md` equals the Render of the page and is not edited by hand.

## Result

2026-10-03, passed in the repository of GUPPI.

## History

- 2026-11-03 shipped with GUPPI
