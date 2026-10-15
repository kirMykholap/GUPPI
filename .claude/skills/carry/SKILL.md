---
name: carry
description: Conserve a ratified Spec whose work is not done — rewrite the brief, mark the session folder, run `guppi backlog`, commit, make the branch of the Spec; run nothing else. Called by the agent after the person chose to conserve at the fork ExitPlanMode prints.
---


Tree: !`git status --porcelain`

Called after `ExitPlanMode`, when the person answered the fork with "conserve". If Tree
above holds a path outside `vault/raw/<hi date>/<hi HHMM>/` and `vault/wiki/brief.md`,
stop and say: work was done, the ordinary exit applies — Work Mode, `/retro`, `/handoff`.

Otherwise:
1. Rewrite `vault/wiki/brief.md` by the frame of `rule-brief` — the text between the `rule-brief` markers of `.claude/agents/librarian-guppi.md` — in its short shape as that frame says: Where
   things stand names the conserved Spec — `vault/raw/<hi date>/<hi HHMM>/spec.md`, its
   Cases, what is not done on it; no Readings due, no Readings at the close, no Deferred list — the conserved Spec and its targets stand in `backlog.md` (case 451.9); Flags say what the vault does not know about this session; Next session keeps its three lists, one line per item, a list with no item the line "none": `Cases` always the line "none" — a deferred decision reaches `/hi` through `backlog.md`, a sprint item through the sprint page; `Work` each open `W` line of `vault/raw/<hi date>/<hi HHMM>/frontier.md`; `Ask the person` each open `A` line of it, with its Estimate by slug, the mark `needs the person` and its question. `/hi` takes its Work list from Next session alone, so a line left out is lost to the next session (case 538.1).
2. Write `vault/raw/<hi date>/<hi HHMM>/carry.md` with one line: `conserved — delete
   this file when the work of spec.md is done`. Its presence tells `guppi materialize` to pass the unit by, and `guppi backlog` to show the Spec under its conserved Specs. Then run `uv run --project .guppi guppi backlog`; every line on its stderr goes into the reply.
3. Run `uv run --project .guppi guppi style`, then commit `vault/raw/`, `vault/wiki/brief.md` and `vault/wiki/backlog.md`:
   `docs(vault): Spec of session <HHMM> conserved, Cases <N>–<M>`.
4. Make the branch of the Spec at that commit: `git branch spec/<hi date>-<hi HHMM>`. Stay on the current branch: the Spec waits on its branch until a later session takes it at the Frontier and `/box` runs it, as `rule-spec-box` sets it (case 591).

Run nothing else: no Work Mode, no `/retro`, no `/handoff`, no librarian, no `guppi
materialize`, `generate`, `cleanup` or `render`; write no page under `vault/wiki/` but the brief; `vault/wiki/backlog.md` is written by `guppi backlog` alone. The session that finishes the Spec deletes `carry.md`.
