---
type: rule
kind: Leaf
purpose: Prevents implementation starting before the plan, branch and baseline exist
status: draft
enforcement: render
governs: .claude/skills/work/SKILL.md
render_mode: full
parent: "[[rule-session]]"
estimates: ["[[estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline]]", "[[estimate-work-mode-takes-the-work-readings]]"]
deferred_by: ["[[decision-case-540]]"]
origin: raw/2026-09-10/ledger.md#case-29
sprint: migration
created: 2026-09-10
tags: [session, workflow, harness, render]
---

## Purpose

Prevents implementation starting before the plan, branch and baseline exist. Work Mode runs the approved Spec of the session. Its skill `/work` starts after `ExitPlanMode`: the agent calls it when the person picks `/work` at the fork, and the person types it to resume a session that stopped in the middle. It stops on `main`. Before the first change it writes the baseline, the result of `make test` and `make lint`, into `raw/<date>/<hi HHMM>/work.md`, so that Retro charges to the session only a red the baseline does not hold. A substitution of the skill can come back empty when the model call that checks it fails, so the agent then runs the command itself. It runs the tasks in the order of the Spec and ticks each box. A task that changes a check that reads a page or a governed file the same Spec updates writes a mark of an expected red into the same file, naming the check and the page or file, and Retro reads it. Subagents in Work Mode, the test of each Estimate written first and the rest of the model are not decided yet (case 479.2).

## Render

<!-- rule-work-mode -->
---
name: work
description: Work Mode on the approved Spec — check the branch, write the baseline, run the tasks in order and tick each box. The agent calls it when the person picks /work at the fork ExitPlanMode prints; the person types it to resume.
---


@vault/wiki/where-to-stop.md

Branch: !`git branch --show-current`

Tests: !`make test`

Lint: !`make lint`

A line above can come back empty when the check of its command fails. When Branch is empty, run `git branch --show-current` yourself before anything else. When Tests or Lint is empty, run `make test` and `make lint` yourself before the first change, and use their result for the Baseline.

Work Mode runs the approved Spec, `vault/raw/<date>/<hi HHMM>/spec.md`, the session's folder. If the branch is `main`, stop and say so: Work Mode does not start on `main`. Write and change nothing until the person moves to another branch and `/work` runs again.

Otherwise, before the first change, write `vault/raw/<date>/<hi HHMM>/work.md` with two sections. `## Baseline`: the exit code of `make test` and of `make lint`, then each failing test and each lint finding line as printed. `## Expected red`: empty for now. When `work.md` already stands, because the person typed `/work` to resume, keep its Baseline as it is: the baseline is taken once, before the first change.

Run the tasks of the Spec in the order the Spec holds them. Tick each box of code, a test, a migration or a `by hand` check in `spec.md` in the reply that finishes the task. The lines of a page, a render, the sprint, the glossary and a reading are ticked by the librarian's scripts, not here.

When a task changes a check — `make lint` or one of its steps, or a hook of the working tree — that reads a page or a governed file this Spec updates, add one line under `## Expected red` in the same reply: the check, and the page or file it waits for. That check is red or refuses on that page or file until the librarian's run, and `/retro` ends that red as a note for the handoff.

When the last task is done, take the Work readings before `/retro`: in the order of `frontier.md`, each reading of an open `W` line whose work is built and whose moment, as its `method` names it, has come; a moment of an earlier session, such as the librarian's run, has come. Leave a reading of an Estimate this session creates or updates, and one whose moment has not come: its line stays open. Close the line of each reading taken `[x] … · work` in `frontier.md` first; tick no `read` box. Write no `LEDGER` block here: the line of each reading stands in the one reply that ends Retro (case 531.8). Run the tasks, the readings and `/retro` in one turn, with tool calls and no reply that ends, except at a stop that `vault/wiki/where-to-stop.md` names. Work Mode ends by calling `/retro`.
<!-- /rule-work-mode -->

## History

- 2026-09-10 deferred, placeholder · raw/2026-09-10/ledger.md#case-29
- 2026-09-11 deferred_by decision-case-29 set · [[decision-case-52.3]]
- 2026-09-12 defer by decision-case-29 superseded · [[decision-case-64]]
- 2026-09-12 deferred · [[decision-case-64]]
- 2026-09-12 defer by decision-case-64 superseded · [[decision-case-78]]
- 2026-09-12 deferred · [[decision-case-78]]
- 2026-09-12 defer by decision-case-78 superseded · [[decision-case-93]]
- 2026-09-12 deferred · [[decision-case-93]]
- 2026-09-13 defer by decision-case-93 superseded · [[decision-case-107]]
- 2026-09-13 deferred · [[decision-case-107]]
- 2026-09-14 defer by decision-case-107 superseded · [[decision-case-116]]
- 2026-09-14 deferred · [[decision-case-116]]
- 2026-09-14 defer by decision-case-116 superseded · [[decision-case-129]]
- 2026-09-14 deferred · [[decision-case-129]]
- 2026-09-14 defer by decision-case-129 superseded · [[decision-case-141]]
- 2026-09-14 deferred · [[decision-case-141]]
- 2026-09-14 defer by decision-case-141 superseded · [[decision-case-152]]
- 2026-09-14 deferred · [[decision-case-152]]
- 2026-09-15 defer by decision-case-152 superseded · [[decision-case-162]]
- 2026-09-15 deferred · [[decision-case-162]]
- 2026-09-15 defer by decision-case-162 superseded · [[decision-case-170]]
- 2026-09-15 deferred · [[decision-case-170]]
- 2026-09-15 defer by decision-case-170 superseded · [[decision-case-176]]
- 2026-09-15 deferred · [[decision-case-176]]
- 2026-09-16 defer by decision-case-176 superseded · [[decision-case-183]]
- 2026-09-16 deferred · [[decision-case-183]]
- 2026-09-16 deferred · [[decision-case-206]]
- 2026-09-17 deferred · [[decision-case-218]]
- 2026-09-18 deferred · [[decision-case-231]]
- 2026-09-18 deferred · [[decision-case-242]]
- 2026-09-18 deferred · [[decision-case-248]]
- 2026-09-18 deferred · [[decision-case-252]]
- 2026-09-18 deferred · [[decision-case-254]]
- 2026-09-20 deferred · [[decision-case-260]]
- 2026-09-20 deferred · [[decision-case-263]]
- 2026-09-20 deferred · [[decision-case-269]]
- 2026-09-20 deferred · [[decision-case-276]]
- 2026-09-20 deferred · [[decision-case-281]]
- 2026-09-21 deferred · [[decision-case-285]]
- 2026-09-21 deferred · [[decision-case-289]]
- 2026-09-21 deferred · [[decision-case-293]]
- 2026-09-22 deferred · [[decision-case-303]]
- 2026-09-22 deferred · [[decision-case-307]]
- 2026-09-22 updated: the parent is rule-session, the MOC of the five phases (case 316) · [[decision-case-316]]
- 2026-09-22 deferred · [[decision-case-322]]
- 2026-09-27 deferred · [[decision-case-447]]
- 2026-09-28 defer by decision-case-183 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-206 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-218 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-231 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-242 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-248 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-252 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-254 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-260 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-263 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-269 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-276 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-281 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-285 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-289 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-293 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-303 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-307 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-322 superseded · [[decision-case-479.2]]
- 2026-09-28 defer by decision-case-447 superseded · [[decision-case-479.2]]
- 2026-09-28 updated: taken up: the skill /work — the branch, the baseline in work.md with the agent's own run when a substitution is empty, the tasks in order with their ticks, the mark of an expected red; every defer retired (case 479.2) · [[decision-case-479.2]]
- 2026-09-28 estimate estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline added · [[decision-case-479.2]]
- 2026-09-29 updated: /work takes the open W readings after the last task, before /retro (case 508.3) · [[decision-case-508.3]]
- 2026-09-29 estimate estimate-work-mode-takes-the-work-readings added · [[decision-case-508.3]]
- 2026-09-30 updated: /work loads the stops of rule-where-to-stop by an import of vault/wiki/where-to-stop.md (case 531.7) · [[decision-case-531.7]]
- 2026-09-30 updated: the tasks, the Work readings and /retro run in one turn; the reading lines go to the reply that ends Retro (case 531.8) · [[decision-case-531.8]]
- 2026-09-30 deferred · [[decision-case-540]]
