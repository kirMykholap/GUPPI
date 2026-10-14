---
type: rule
kind: Leaf
purpose: Prevents implementation starting before the plan, branch and baseline exist
status: draft
enforcement: render
governs: .claude/skills/work/SKILL.md
render_mode: full
parent: "[[rule-session]]"
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, workflow, harness, render]
core: true
---

## Purpose

Prevents implementation starting before the plan, branch and baseline exist. Work Mode runs the approved Spec of the session, or the conserved Spec whose folder `/box` gives it. Its skill `/work` starts after `ExitPlanMode`: the agent calls it when the person picks `/work` at the fork, and the person types it to resume a session that stopped in the middle. It stops on `main`. Before the first change it writes the baseline, the result of `make test` and `make lint`, into `raw/<date>/<hi HHMM>/work.md`, so that Retro charges to the session only a red the baseline does not hold. A substitution of the skill can come back empty when the model call that checks it fails, so the agent then runs the command itself. It runs the tasks in the order of the Spec and ticks each box. After the last task it runs `make test` in full against the baseline, and a new failing test whose fix needs a choice that no ratified Case makes stops the run for the person. A task that changes a check that reads a page or a governed file the same Spec updates writes a mark of an expected red into the same file, naming the check and the page or file, and Retro reads it. Subagents in Work Mode, the test of each Estimate written first and the rest of the model are not decided yet.

## Render

<!-- rule-work-mode -->
---
name: work
description: Work Mode on the approved Spec — check the branch, write the baseline, run the tasks in order and tick each box. The agent calls it when the person picks /work at the fork ExitPlanMode prints; the person types it to resume; /box calls it with the folder of a conserved Spec.
---


@vault/wiki/where-to-stop.md

Branch: !`git branch --show-current`

Tests: !`make test`

Lint: !`make lint`

A line above can come back empty when the check of its command fails. When Branch is empty, run `git branch --show-current` yourself before anything else. When Tests or Lint is empty, run `make test` and `make lint` yourself before the first change, and use their result for the Baseline.

Work Mode runs the approved Spec, `vault/raw/<date>/<hi HHMM>/spec.md`, the session's folder. When `/box` calls it with the folder of a conserved Spec, `vault/raw/<date>/<HHMM>/`, the Spec below is that folder's `spec.md`, and `work.md` still stands in the session's folder. If the branch is `main`, stop and say so: Work Mode does not start on `main`. Write and change nothing until the person moves to another branch and `/work` runs again.

Otherwise, before the first change, write `vault/raw/<date>/<hi HHMM>/work.md` with two sections, or three with a folder from `/box`. `## Baseline`: the exit code of `make test` and of `make lint`, then each failing test and each lint finding line as printed. `## Expected red`: empty for now. With a folder from `/box`, the third, `## Conserved Spec`: the folder, on one line. When `work.md` already stands, because the person typed `/work` to resume, keep its Baseline as it is: the baseline is taken once, before the first change.

Run the tasks of the Spec in the order the Spec holds them. Tick each box of code, a test, a migration or a `by hand` check in `spec.md` in the reply that finishes the task. The lines of a page, a render, the sprint, the glossary and a reading are ticked by the librarian's scripts, not here. A task line that opens with a code span holding `guppi sprint-close` is neither run nor ticked here: the librarian runs it, and the command ticks it, as `rule-sprint-close` sets it. When a Case is ratified in this Work Mode — a new Case that replaces a sub-case of a ratified Case, as `vault/wiki/orchestration.md` sets it — run `uv run guppi prespec --check <the plan file> --session <id>`, the session id of the `hi:` line as `/pre-spec` takes it, after the reply that acknowledges that Case and before its first task. Each line it prints that does not open with `note:` is a finding: stop as the first condition of `vault/wiki/where-to-stop.md` sets it, and send the finding to the `case-guppi` of that Case, which fixes it under its own number while none of its tasks has run; the person ratifies it again, and the run goes on once the check prints no finding. Tick a task of the new Case whose work already stands, done under the sub-case it replaces, and do not run it again. The reply that acknowledges such a Case ends the turn, since no hook sends the agent on once `spec.md` stands: the run goes on at the person's next message, the check first. In a `/work` that `/box` calls no Case is built: a fork stops the run, as `rule-spec-box` sets it, and the choice goes to `handoff.md` as a line.

When a task changes a check — `make lint` or one of its steps, or a hook of the working tree — that reads a page or a governed file this Spec updates, add one line under `## Expected red` in the same reply: the check, and the page or file it waits for. That check is red or refuses on that page or file until the librarian's run, and `/retro` ends that red as a note for the handoff.

When the last task is done, run `make test` in full and hold each failing test against `## Baseline` of `work.md`. A failing test that the Baseline holds was red before the work and goes on. Fix a new one when the fix finishes ratified work; when its fix needs a choice that no ratified Case makes, stop as the seventh condition of `vault/wiki/where-to-stop.md` sets; any other new failing test goes on to `/retro`, which fixes it or reverts it. Then delete the `carry.md` of a folder from `/box`, and take the Work readings before `/retro`: in the order of `frontier.md`, each reading of an open `W` line whose work is built and whose moment, as its `method` names it, has come; a moment of an earlier session, such as the librarian's run, has come. Leave a reading of an Estimate this session creates or updates — with a folder from `/box`, one that a decision line of that folder's `ledger.md` creates or updates too — and one whose moment has not come: its line stays open; Retro reads an Estimate this session or that folder creates or updates, or sets it `failed`, and closes its line. Close the line of each reading taken `[x] … · work` in `frontier.md` first; tick no `read` box. Write no `LEDGER` block here: the line of each reading stands in the one reply that ends Retro. Run the tasks, the readings and `/retro` in one turn, with tool calls and no reply that ends, except at a stop that `vault/wiki/where-to-stop.md` names. Work Mode ends by calling `/retro`.
<!-- /rule-work-mode -->

## History

- 2026-10-14 shipped with GUPPI
