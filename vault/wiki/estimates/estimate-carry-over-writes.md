---
type: estimate
kind: QA
status: pending
target: "[[rule-carry-over]]"
purpose: /carry writes the brief and the mark, runs guppi backlog, commits, makes the branch of the Spec at that commit, and runs nothing else
method: uv run guppi render --check; by hand, the first /carry after the fork of ExitPlanMode — the tree, vault/wiki/brief.md, carry.md, vault/wiki/backlog.md, the commit and git branch read
checked: 2026-09-30
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
**＋** The short shape holds Where things stand, Flags and Next session, with no Readings due and no Readings at the close.
**＋** Next session holds `Cases`, `Work` and `Ask the person`, one line per item, a list with no item the line "none": `Cases` is always the line "none", since a deferred decision reaches `/hi` through `vault/wiki/backlog.md` and a sprint item through `vault/wiki/sprint.md`; `Work` holds each open `W` line of `raw/<hi date>/<hi HHMM>/frontier.md`, and `Ask the person` each open `A` line with its Estimate by slug, the mark `needs the person` and its question.
**＋** It puts `carry.md` into the session folder: one line, a flag for `materialize` and `guppi backlog`, not a document. The session that finishes the work deletes it.
**＋** It runs `uv run guppi backlog`, and `vault/wiki/backlog.md` then shows the conserved Spec with its targets.
**＋** It runs `make style` and commits `vault/raw/`, `vault/wiki/brief.md` and `vault/wiki/backlog.md`.
**＋** After that commit it runs `git branch spec/<hi date>-<hi HHMM>`, so the branch of the Spec points at the commit that holds the whole of `/carry`.
**－** No open `W` or `A` line of `frontier.md` is left out of Next session, so the next `/hi` takes each one into its Frontier.
**－** It runs no Work Mode, `/retro`, `/handoff`, librarian, `materialize`, `generate`, `cleanup` or `render`, and it writes no decision. It writes no page of `vault/wiki/`.
**－** It switches to no branch: the session stays on the branch it ran on.
**－** The work stays sequential, session after session: one conserved Spec, no parallel work.
**－** `.claude/skills/carry/SKILL.md` equals the Render of the page and is not edited by hand.

## Result

2026-09-30, uv run guppi render --check (exit 0), git show --stat 8e4c918 and the event log of session 876c4080 from 01:32:52 to 01:33:35: /carry was called after the fork of ExitPlanMode; brief.md was rewritten in the short shape with no Deferred list; carry.md holds one line; guppi backlog ran and backlog.md shows the conserved Spec with its targets; make style ran; the commit holds only vault/raw/, brief.md and backlog.md; no Work Mode, retro, handoff, librarian, materialize, generate, cleanup or render ran. The short shape dropped the Work list by the rule's own text; that is lesson-carry-short-brief-drops-the-work-list and the defer of case 533, not a fault of this run

## History

- 2026-09-16 created · [[decision-case-190.1]]
- 2026-09-16 updated: the Criterion replaced whole by case 196.1 — the agent's call after the fork, the brief, the flag, the commit, nothing else run (case 196.1) · [[decision-case-196.1]]
- 2026-09-17 ref removed · one-off migration · raw/2026-09-16/2238/spec.md#case-210
- 2026-09-18 updated: the Render changed under it — the Deferred paragraph; the Criterion stands as it was (case 233.4) · [[decision-case-233.4]]
- 2026-09-18 status: pending → passed · raw/2026-09-18/2054/ledger.md#L12
- 2026-09-23 updated: the Render changed under it — step 1 names the place of the frame; the Criterion stands (case 347) · [[decision-case-347]]
- 2026-09-27 updated: the Criterion replaced whole — no Deferred list, guppi backlog run and backlog.md committed (case 451.9) · [[decision-case-451.9]]
- 2026-09-27 updated: the method names render --check and a reading by hand; no test targets the carry skill (case 465) · [[decision-case-465]]
- 2026-09-30 status: pending → passed · raw/2026-09-30/0138/ledger.md#L3
- 2026-09-30 updated: the Criterion replaced whole — the short brief keeps Next session: Work and Ask the person from the open lines of frontier.md, Cases the line none · [[decision-case-538.1]]
- 2026-10-02 updated: the Criterion replaced whole — /carry makes the branch of the Spec after its commit (case 591.1) · [[decision-case-591.1]]
