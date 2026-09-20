---
type: rule
kind: Leaf
purpose: Prevents a Spec whose work was not done from being applied to the vault
status: built
enforcement: render
governs: .claude/skills/carry/SKILL.md
render_mode: full
parent: "[[rule-end-of-work]]"
estimates: ["[[estimate-carry-over-writes]]"]
origin: raw/2026-09-16/1034/ledger.md#case-190.1
sprint: migration
created: 2026-09-16
tags: [session, workflow, harness, render]
---

## Purpose

Prevents a Spec whose work was not done from being applied to the vault, and keeps a
planning session from ending with nothing the next session can pick up. A session may
reach a ratified Spec and stop there — the work is larger than the context left. The
ordinary exit dispatches the librarian, who writes the vault pages from the Spec; for
such a session that would make the vault claim behaviour no code implements.

## Render

<!-- rule-carry-over -->
---
name: carry
description: Conserve a ratified Spec whose work is not done — rewrite the brief, mark the session folder, commit; run nothing else. Called by the agent after the person chose to conserve at the fork ExitPlanMode prints.
---


Tree: !`git status --porcelain`

Called after `ExitPlanMode`, when the person answered the fork with "conserve". If Tree
above holds a path outside `vault/raw/<hi date>/<hi HHMM>/` and `vault/wiki/brief.md`,
stop and say: work was done, the ordinary exit applies — Work Mode, `/retro`, `/handoff`.

Otherwise:
1. Rewrite `vault/wiki/brief.md` by the frame of `rule-brief` (the Render in
   `.claude/agents/librarian-guppi.md`), in its short shape as that frame says: Where
   things stand names the conserved Spec — `vault/raw/<hi date>/<hi HHMM>/spec.md`, its
   Cases, what is not done on it; no Readings due, no Next session, no Readings at the close; Deferred is
   the previous brief's list as it stands plus the `defer` items of this Spec by slug, less the targets the sprint page names (case 229.4);
   Flags say what the vault does not know about this session. No cap, no ranking.
2. Write `vault/raw/<hi date>/<hi HHMM>/carry.md` with one line: `conserved — delete
   this file when the work of spec.md is done`. Its presence tells `guppi materialize`
   to pass the unit by.
3. Run `make style`, then commit `vault/raw/` and `vault/wiki/brief.md`:
   `docs(vault): Spec of session <HHMM> conserved, Cases <N>–<M>`.

Run nothing else: no Work Mode, no `/retro`, no `/handoff`, no librarian, no `guppi
materialize`, `generate`, `cleanup` or `render`; write no page under `vault/wiki/` but
the brief. The session that finishes the Spec deletes `carry.md`.
<!-- /rule-carry-over -->

## History

- 2026-09-16 created · [[decision-case-190.1]]
- 2026-09-16 estimate estimate-carry-over-writes added · [[decision-case-190.1]]
- 2026-09-16 updated: the Render written — the skill's text, called by the agent after the fork (case 196.1) · [[decision-case-196.1]]
- 2026-09-17 deferred · [[decision-case-223]]
- 2026-09-18 defer by decision-case-223 superseded · [[decision-case-225]]
- 2026-09-18 updated: the stray ref field removed by a one-off script (case 225) · [[decision-case-225]]
- 2026-09-18 updated: the /carry brief leaves out a target the sprint page names (case 233.4) · [[decision-case-233.4]]
- 2026-09-18 status: draft → built · cascade
- 2026-09-20 updated: the carry brief's list of omitted sections names Next session, as the carry sentence of rule-brief does (case 268.1) · [[decision-case-268.1]]
