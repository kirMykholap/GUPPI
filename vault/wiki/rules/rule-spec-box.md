---
type: rule
kind: Leaf
purpose: Prevents a conserved Spec from being built on a branch that lacks the current vault, or its pages from being written anywhere but on the shared branch
status: built
enforcement: render
implementation_ref: [.guppi/guppi/box.py, .guppi/tests/test_box.py]
governs: .claude/skills/box/SKILL.md
render_mode: full
parent: "[[rule-end-of-work]]"
estimates: ["[[estimate-spec-box-runs-a-conserved-spec]]", "[[estimate-spec-box-refuses-a-stale-spec]]"]
origin: guppi
sprint: guppi
created: 2026-11-03
tags: [session, workflow, git, harness, render]
core: true
---

## Purpose

Prevents a conserved Spec from being built on a branch that lacks the current vault, and its pages from being written anywhere but on the shared branch. `/carry` conserves a Spec whose work is not done and makes its branch `spec/<date>-<HHMM>` at the commit that conserves it. A later session takes the Spec at the Frontier, and `/box` runs it: it checks the Spec, switches to its branch, brings that branch up to the shared branch by a fast-forward, runs `/work` on the Spec, and after `/handoff` brings the shared branch up to the Spec's branch by a fast-forward and hands the session to the librarian there. One session runs at a time, in one folder of the repository, so both merges are fast-forwards and the vault has one writer; the shared branch is never `main`. The check refuses a Spec whose pages changed after it was conserved, and a session that ratified a Case of its own: in this first part a Case of the Spec is not checked again or built again, and the readings, lessons and handoff of the session go into the session's own folder, which the librarian applies. Both wait for a second part.

## Render

<!-- rule-spec-box -->
---
name: box
description: Run a conserved Spec on its own branch — check it, switch to the branch and bring it up to date, run /work on it, merge the branch back and hand the session to the librarian. The agent calls it on the line that the hook of rule-spec-capture prints after the approval of the Spec, by ExitPlanMode or by /approve-spec.
---


@vault/wiki/where-to-stop.md

Branch: !`git branch --show-current`

The argument is the folder of a conserved Spec, `vault/raw/<date>/<HHMM>/`, which the line printed after the approval of the Spec, by `ExitPlanMode` or by `/approve-spec`, names. The branch above is the shared branch: the session leaves it here and comes back to it at the end. The branch of the Spec is `spec/<date>-<HHMM>`, the date and time of that folder, made by `/carry`. Nothing under `vault/wiki/` is written on the branch of the Spec: the librarian writes the pages once, on the shared branch.

1. Run `uv run --project .guppi guppi box --check <folder> --session <id>`, the id being the eight characters of the `hi:` line of this session. Each line it prints is a reason the Spec cannot run now. When it prints one, change nothing: show the lines and ask the person.
2. Commit the tree: `chore(session): session <hi HHMM> takes the conserved Spec of <folder>`.
3. Run `git switch spec/<date>-<HHMM>`, then `git merge --ff-only <shared branch>`. When the merge refuses, run `git switch <shared branch>`, show the refusal and ask the person.
4. Call `/work` with the folder as its argument. Work Mode, the Work readings, `/retro` and `/handoff` run as their skills say, in one turn; `/handoff` dispatches nothing and comes back here.
5. Run `git switch <shared branch>`, then `git merge --ff-only spec/<date>-<HHMM>`. When the merge refuses, show the refusal and ask the person. Then run `git branch -d spec/<date>-<HHMM>` and `uv run --project .guppi guppi test`.
6. Dispatch the `librarian-guppi` agent with one line: `Materialize <hi date> from vault/raw/<hi date>/<hi HHMM>/handoff.md.`. Wait for its report. Read `vault/raw/<hi date>/<hi HHMM>/report.md`, which a hook writes from that report, and show its text to the person unchanged, or, when no `report.md` stands there, the returned report unchanged and one line that says that `report.md` is missing; then one line with the exit code of `uv run --project .guppi guppi test`. When `report.md` stands, commit it alone: `git add vault/raw/<hi date>/<hi HHMM>/report.md && git commit -m "docs(vault): librarian report, <hi date>"`, never `--amend`. Make no other commit after this, and write no `LEDGER` block.

The stops of steps 1, 3 and 5 are condition 6 of `vault/wiki/where-to-stop.md`.
<!-- /rule-spec-box -->

## History

- 2026-11-03 shipped with GUPPI
