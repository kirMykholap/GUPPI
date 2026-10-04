---
name: work
description: Work Mode on the approved Spec — check the branch, write the baseline, run the tasks in order and tick each box. The agent calls it when the person picks /work at the fork ExitPlanMode prints; the person types it to resume; /box calls it with the folder of a conserved Spec.
---


@vault/wiki/where-to-stop.md

Branch: !`git branch --show-current`

Tests: !`make test`

Lint: !`make lint`

A line above can come back empty when the check of its command fails. When Branch is empty, run `git branch --show-current` yourself before anything else. When Tests or Lint is empty, run `make test` and `make lint` yourself before the first change, and use their result for the Baseline.

Work Mode runs the approved Spec, `vault/raw/<date>/<hi HHMM>/spec.md`, the session's folder. When `/box` calls it with the folder of a conserved Spec, `vault/raw/<date>/<HHMM>/`, the Spec below is that folder's `spec.md`, and `work.md` still stands in the session's folder (case 591). If the branch is `main`, stop and say so: Work Mode does not start on `main`. Write and change nothing until the person moves to another branch and `/work` runs again.

Otherwise, before the first change, write `vault/raw/<date>/<hi HHMM>/work.md` with two sections, or three with a folder from `/box`. `## Baseline`: the exit code of `make test` and of `make lint`, then each failing test and each lint finding line as printed. `## Expected red`: empty for now. With a folder from `/box`, the third, `## Conserved Spec`: the folder, on one line. When `work.md` already stands, because the person typed `/work` to resume, keep its Baseline as it is: the baseline is taken once, before the first change.

Run the tasks of the Spec in the order the Spec holds them. Tick each box of code, a test, a migration or a `by hand` check in `spec.md` in the reply that finishes the task. The lines of a page, a render, the sprint, the glossary and a reading are ticked by the librarian's scripts, not here. A task line that opens with a code span holding `guppi sprint-close` is neither run nor ticked here: the librarian runs it, and the command ticks it (`rule-sprint-close`, case 628.4).

When a task changes a check — `make lint` or one of its steps, or a hook of the working tree — that reads a page or a governed file this Spec updates, add one line under `## Expected red` in the same reply: the check, and the page or file it waits for. That check is red or refuses on that page or file until the librarian's run, and `/retro` ends that red as a note for the handoff.

When the last task is done, delete the `carry.md` of a folder from `/box`, then take the Work readings before `/retro`: in the order of `frontier.md`, each reading of an open `W` line whose work is built and whose moment, as its `method` names it, has come; a moment of an earlier session, such as the librarian's run, has come. Leave a reading of an Estimate this session creates or updates — with a folder from `/box`, one that a decision line of that folder's `ledger.md` creates or updates too — and one whose moment has not come: its line stays open. Close the line of each reading taken `[x] … · work` in `frontier.md` first; tick no `read` box. Write no `LEDGER` block here: the line of each reading stands in the one reply that ends Retro (case 531.8). Run the tasks, the readings and `/retro` in one turn, with tool calls and no reply that ends, except at a stop that `vault/wiki/where-to-stop.md` names. Work Mode ends by calling `/retro`.
