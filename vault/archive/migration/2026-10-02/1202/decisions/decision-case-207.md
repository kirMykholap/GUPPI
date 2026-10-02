---
type: decision
case: "207"
status: archived
defer: ["[[rule-spec-box]]"]
superseded_by: ["[[decision-case-591.5]]", "[[decision-case-593.2]]"]
origin: raw/2026-09-16/1955/ledger.md#case-207
sprint: migration
created: 2026-09-16
tags: []
---

## Context

`/carry` (`rule-carry-over`, `draft`) conserves a Spec whose work is not done: `carry.md` in `raw/<date>/<HHMM>/`, the brief rewritten, a commit; `materialize` passes the unit by; "the session that finishes the Spec deletes `carry.md`" — where and how that session runs is unsaid. `rule-end-of-work` knows two ends of a session, the ordinary one and `/carry`. `rule-documentation` and `rule-close`: the librarian is the only writer to `wiki/` and ends in its own commit; `guppi gate` refuses `/handoff` on a dirty tree; the ledger hook refuses without a `hi` in the session's window. `rule-work-mode` and `rule-subagent-guppi` are placeholders (case 206). The vault was asked: `rule-spec-box` is free in `wiki/` and in the archive; no page speaks of a worktree or of a session started from a conserved folder; `lesson-subagents-parallel-on-one-tree-red-mid-flight` says two writers on one tree make readings meaningless. The wider question was named in session 1651 and left without a defer.

## Problem

A session ends in a brief that the next session must work off, so the sessions run one after another even when the work of a Spec has no decision left in it. Work Mode is where the time goes and where nothing is decided; it could run in parallel — one conserved Spec per session, each in a git worktree. What keeps it from racing is already the rule: the librarian alone writes `wiki/`, each session writes its own `raw/` folder, `generate` applies only what is unapplied, a superseded Case is skipped. What is missing is the session itself: how it opens a box, where its hook writes, how it ends, and who runs the librarian after the merge. This leans on Work Mode (Slice 3b) and is discussed after it.

## Deferred

### [[rule-spec-box]]

A Spec box: a session that opens a conserved Spec — a `raw/<date>/<HHMM>/` folder with
`carry.md` — in a git worktree on its own branch, and runs its Work Mode. Not `/hi`,
not Plan Mode: a skill lists the boxes, the person picks one, the agent executes it.
It writes only into that folder — ticks `spec.md`, readings into its `ledger.md`,
`handoff.md` — and into the code; it never touches `wiki/` and never runs the
librarian. It ends with `/retro` and `/handoff`; done is `handoff.md` present and
`carry.md` removed. At a fork it stops and returns the question, as a subagent does.
The branch is merged into the main branch; the librarian runs once there, over every
unapplied unit and every handoff, and writes one brief. Open: the skill and its
conditions; the ledger hook and `guppi gate` inside a worktree with its own
`event_log.md`; the cut of a Spec into boxes that share no file and no page; a third
end of a session in `rule-end-of-work`; whether the box is a subagent of the main
session with `isolation: worktree` or a session the person starts. After Slice 3b
(case 206).

## History

- 2026-09-16 created · raw/2026-09-16/1955/ledger.md#case-207
- 2026-10-02 superseded by decision-case-591.5 · [[decision-case-591.5]]
- 2026-10-02 superseded by decision-case-593.2 · [[decision-case-593.2]]
- 2026-10-02 archived · superseded
- 2026-10-02 archived · cleanup
