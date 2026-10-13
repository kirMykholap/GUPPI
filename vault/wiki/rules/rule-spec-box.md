---
type: rule
kind: Leaf
purpose: Prevents a conserved Spec from being built on a branch that lacks the current vault, or its pages from being written anywhere but on the shared branch
status: built
enforcement: render
implementation_ref: [guppi/box.py, tests/test_box.py]
governs: .claude/skills/box/SKILL.md
render_mode: full
parent: "[[rule-end-of-work]]"
estimates: ["[[estimate-spec-box-runs-a-conserved-spec]]", "[[estimate-spec-box-refuses-a-stale-spec]]"]
origin: raw/2026-09-16/1955/ledger.md#case-207
sprint: migration
created: 2026-09-16
tags: [session, workflow, git, harness, render]
core: true
---

## Purpose

Prevents a conserved Spec from being built on a branch that lacks the current vault, and its pages from being written anywhere but on the shared branch. `/carry` conserves a Spec whose work is not done and makes its branch `spec/<date>-<HHMM>` at the commit that conserves it. A later session takes the Spec at the Frontier, and `/box` runs it: it checks the Spec, switches to its branch, brings that branch up to the shared branch by a fast-forward, runs `/work` on the Spec, and after `/handoff` brings the shared branch up to the Spec's branch by a fast-forward and hands the session to the librarian there. One session runs at a time, in one folder of the repository, so both merges are fast-forwards and the vault has one writer; the shared branch is never `main`. The check refuses a Spec whose pages changed after it was conserved, and a session that ratified a Case of its own: in this first part a Case of the Spec is not checked again or built again, and the readings, lessons and handoff of the session go into the session's own folder, which the librarian applies. Both wait for a second part, a line of the Backlog of `entity-sprint-migration` (case 591).

## Render

<!-- rule-spec-box -->
---
name: box
description: Run a conserved Spec on its own branch — check it, switch to the branch and bring it up to date, run /work on it, merge the branch back and hand the session to the librarian. The agent calls it on the line that the hook of rule-spec-capture prints after ExitPlanMode.
---


@vault/wiki/where-to-stop.md

Branch: !`git branch --show-current`

The argument is the folder of a conserved Spec, `vault/raw/<date>/<HHMM>/`, which the line printed after `ExitPlanMode` names. The branch above is the shared branch: the session leaves it here and comes back to it at the end. The branch of the Spec is `spec/<date>-<HHMM>`, the date and time of that folder, made by `/carry`. Nothing under `vault/wiki/` is written on the branch of the Spec: the librarian writes the pages once, on the shared branch.

1. Run `uv run guppi box --check <folder> --session <id>`, the id being the eight characters of the `hi:` line of this session. Each line it prints is a reason the Spec cannot run now. When it prints one, change nothing: show the lines and ask the person.
2. Commit the tree: `chore(session): session <hi HHMM> takes the conserved Spec of <folder>`.
3. Run `git switch spec/<date>-<HHMM>`, then `git merge --ff-only <shared branch>`. When the merge refuses, run `git switch <shared branch>`, show the refusal and ask the person.
4. Call `/work` with the folder as its argument. Work Mode, the Work readings, `/retro` and `/handoff` run as their skills say, in one turn; `/handoff` dispatches nothing and comes back here.
5. Run `git switch <shared branch>`, then `git merge --ff-only spec/<date>-<HHMM>`. When the merge refuses, show the refusal and ask the person. Then run `git branch -d spec/<date>-<HHMM>` and `make test`.
6. Dispatch the `librarian-guppi` agent with one line: `Materialize <hi date> from vault/raw/<hi date>/<hi HHMM>/handoff.md.`. Wait for its report and show it to the person unchanged, then one line with the exit code of `make test`. Do not commit after this, and write no `LEDGER` block.

The stops of steps 1, 3 and 5 are condition 6 of `vault/wiki/where-to-stop.md`.
<!-- /rule-spec-box -->

## History

- 2026-09-16 deferred, placeholder · [[decision-case-207]]
- 2026-09-17 deferred · [[decision-case-219]]
- 2026-09-18 deferred · [[decision-case-232]]
- 2026-09-30 deferred · [[decision-case-532]]
- 2026-10-01 deferred · [[decision-case-565]]
- 2026-10-02 defer by decision-case-207 superseded · [[decision-case-591.5]]
- 2026-10-02 defer by decision-case-219 superseded · [[decision-case-591.5]]
- 2026-10-02 defer by decision-case-232 superseded · [[decision-case-591.5]]
- 2026-10-02 defer by decision-case-532 superseded · [[decision-case-591.5]]
- 2026-10-02 defer by decision-case-565 superseded · [[decision-case-591.5]]
- 2026-10-02 updated: built from the placeholder: /box runs a conserved Spec on its branch and merges it back before the librarian, first part; a child of rule-end-of-work (case 593.2) · [[decision-case-593.2]]
- 2026-10-02 estimate estimate-spec-box-runs-a-conserved-spec added · [[decision-case-593.2]]
- 2026-10-02 estimate estimate-spec-box-refuses-a-stale-spec added · [[decision-case-593.3]]
- 2026-10-04 status: draft → built · cascade
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
