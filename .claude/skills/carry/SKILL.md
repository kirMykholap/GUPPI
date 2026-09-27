---
name: carry
description: Conserve a ratified Spec whose work is not done — rewrite the brief, mark the session folder, run `guppi backlog`, commit; run nothing else. Called by the agent after the person chose to conserve at the fork ExitPlanMode prints.
---


Tree: !`git status --porcelain`

Called after `ExitPlanMode`, when the person answered the fork with "conserve". If Tree
above holds a path outside `vault/raw/<hi date>/<hi HHMM>/` and `vault/wiki/brief.md`,
stop and say: work was done, the ordinary exit applies — Work Mode, `/retro`, `/handoff`.

Otherwise:
1. Rewrite `vault/wiki/brief.md` by the frame of `rule-brief` — the text between the `rule-brief` markers of `.claude/agents/librarian-guppi.md` — in its short shape as that frame says: Where
   things stand names the conserved Spec — `vault/raw/<hi date>/<hi HHMM>/spec.md`, its
   Cases, what is not done on it; no Readings due, no Next session, no Readings at the close, no Deferred list — the conserved Spec and its targets stand in `backlog.md` (case 451.9); Flags say what the vault does not know about this session.
2. Write `vault/raw/<hi date>/<hi HHMM>/carry.md` with one line: `conserved — delete
   this file when the work of spec.md is done`. Its presence tells `guppi materialize` to pass the unit by, and `guppi backlog` to show the Spec under its conserved Specs. Then run `uv run guppi backlog`; every line on its stderr goes into the reply.
3. Run `make style`, then commit `vault/raw/`, `vault/wiki/brief.md` and `vault/wiki/backlog.md`:
   `docs(vault): Spec of session <HHMM> conserved, Cases <N>–<M>`.

Run nothing else: no Work Mode, no `/retro`, no `/handoff`, no librarian, no `guppi
materialize`, `generate`, `cleanup` or `render`; write no page under `vault/wiki/` but the brief; `vault/wiki/backlog.md` is written by `guppi backlog` alone. The session that finishes the Spec deletes `carry.md`.
