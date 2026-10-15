---
name: box
description: Run a conserved Spec on its own branch — check it, switch to the branch and bring it up to date, run /work on it, merge the branch back and hand the session to the librarian. The agent calls it on the line that the hook of rule-spec-capture prints after ExitPlanMode.
---


@vault/wiki/where-to-stop.md

Branch: !`git branch --show-current`

The argument is the folder of a conserved Spec, `vault/raw/<date>/<HHMM>/`, which the line printed after `ExitPlanMode` names. The branch above is the shared branch: the session leaves it here and comes back to it at the end. The branch of the Spec is `spec/<date>-<HHMM>`, the date and time of that folder, made by `/carry`. Nothing under `vault/wiki/` is written on the branch of the Spec: the librarian writes the pages once, on the shared branch.

1. Run `uv run --project .guppi guppi box --check <folder> --session <id>`, the id being the eight characters of the `hi:` line of this session. Each line it prints is a reason the Spec cannot run now. When it prints one, change nothing: show the lines and ask the person.
2. Commit the tree: `chore(session): session <hi HHMM> takes the conserved Spec of <folder>`.
3. Run `git switch spec/<date>-<HHMM>`, then `git merge --ff-only <shared branch>`. When the merge refuses, run `git switch <shared branch>`, show the refusal and ask the person.
4. Call `/work` with the folder as its argument. Work Mode, the Work readings, `/retro` and `/handoff` run as their skills say, in one turn; `/handoff` dispatches nothing and comes back here.
5. Run `git switch <shared branch>`, then `git merge --ff-only spec/<date>-<HHMM>`. When the merge refuses, show the refusal and ask the person. Then run `git branch -d spec/<date>-<HHMM>` and `uv run --project .guppi guppi test`.
6. Dispatch the `librarian-guppi` agent with one line: `Materialize <hi date> from vault/raw/<hi date>/<hi HHMM>/handoff.md.`. Wait for its report and show it to the person unchanged, then one line with the exit code of `uv run --project .guppi guppi test`. Do not commit after this, and write no `LEDGER` block.

The stops of steps 1, 3 and 5 are condition 6 of `vault/wiki/where-to-stop.md`.
