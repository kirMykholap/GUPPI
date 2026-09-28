---
name: work
description: Work Mode on the approved Spec — check the branch, write the baseline, run the tasks in order and tick each box. The agent calls it when the person picks /work at the fork ExitPlanMode prints; the person types it to resume.
---


Branch: !`git branch --show-current`

Tests: !`make test`

Lint: !`make lint`

A line above can come back empty when the check of its command fails. When Branch is empty, run `git branch --show-current` yourself before anything else. When Tests or Lint is empty, run `make test` and `make lint` yourself before the first change, and use their result for the Baseline.

Work Mode runs the approved Spec, `vault/raw/<date>/<hi HHMM>/spec.md`, the session's folder. If the branch is `main`, stop and say so: Work Mode does not start on `main`. Write and change nothing until the person moves to another branch and `/work` runs again.

Otherwise, before the first change, write `vault/raw/<date>/<hi HHMM>/work.md` with two sections. `## Baseline`: the exit code of `make test` and of `make lint`, then each failing test and each lint finding line as printed. `## Expected red`: empty for now. When `work.md` already stands, because the person typed `/work` to resume, keep its Baseline as it is: the baseline is taken once, before the first change.

Run the tasks of the Spec in the order the Spec holds them. Tick each box of code, a test, a migration or a `by hand` check in `spec.md` in the reply that finishes the task. The lines of a page, a render, the sprint, the glossary and a reading are ticked by the librarian's scripts, not here.

When a task changes a check — `make lint` or one of its steps, or a hook of the working tree — that reads a page or a governed file this Spec updates, add one line under `## Expected red` in the same reply: the check, and the page or file it waits for. That check is red or refuses on that page or file until the librarian's run, and `/retro` ends that red as a note for the handoff.

Work Mode ends with `/retro`.
