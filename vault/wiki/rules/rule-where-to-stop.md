---
type: rule
kind: Leaf
purpose: Prevents the run from /work to the librarian from stopping where the person is not needed, or going on where only the person can decide
status: built
enforcement: render
governs: vault/wiki/where-to-stop.md
render_mode: full
estimates: ["[[estimate-where-to-stop-stops-only-on-its-conditions]]"]
origin: raw/2026-09-29/2024/ledger.md#case-531.7
sprint: migration
created: 2026-09-29
tags: [session, workflow, harness, render]
core: true
---

## Purpose

Prevents the run from /work to the librarian from stopping where the person is not needed, or going on where only the person can decide. The person keeps three questions: what to do, the Cases of Plan Mode; what done means and how to check it, the Estimates; and where to stop, this page (case 531.7). `/work` and `/box` load its text by an import of `vault/wiki/where-to-stop.md` (case 591), `/hi` loads it for Plan Mode too, so the main agent promises the person no turn the run does not give (case 689.1), and the refusal of `rule-retro-onward` names the file. A hook on a single action, such as a push, may enforce a condition later; until then the text in the context is the guard.

## Render

<!-- rule-where-to-stop -->
# Where to stop

From the approved Spec to the librarian's report the run needs no person: `/box`, `/work`, the Work readings, `/retro` and `/handoff` run in one turn. Stop and ask the person only on one of these conditions:

1. A fork that changes a contract: the work needs a choice that no ratified Case makes, or a ratified Case turns out wrong — by a text you find wrong or too narrow, or by a finding of `uv run --project .guppi guppi prespec --check` on the plan after a Case ratified in Work Mode — so a new Case is needed, or that Case is fixed, as `orchestration.md` sets it; in a `/work` that `/box` calls no Case is built, as `rule-spec-box` sets it, and the choice goes to `handoff.md` as a line (case 806.4).
2. A hook refuses, and its text gives no step you can follow, or says that the refusal is a stop.
3. An action that git in this repository cannot undo, such as a push to a remote or a deletion outside the repository.
4. A task of the Spec whose text opens with `stop:`: stop before it runs, and run it after the person's word.
5. The branch is `main`: Work Mode does not start there; say so, and go on after the person moves to another branch.
6. `/box` cannot go on: its check `uv run --project .guppi guppi box --check` prints a reason, or one of its `git merge --ff-only` refuses; or a `git` or `gh` command of the merge tasks of the opening Case of a sprint, of the merge task of a review Case of `/pr-review`, or of the tasks of a merge Case of `/merge-main` refuses, or the merge of a merge Case leaves in conflict a file that the merge Case does not settle: show what stopped it, and go on after the person's word; a `git merge --no-ff --no-commit` of a merge Case that exits non-zero only on files the merge Case settles is no refusal (cases 775.3, 789.3).
7. The full `uv run --project .guppi guppi test` run of `/work` after its last task finds a failing test that `## Baseline` of `work.md` does not hold, and its fix needs a choice that no ratified Case makes: name the test and its failure, and go on as the person's word says (case 736.3).
8. The auto mode classifier of Claude Code refuses a tool call that the run needs: give the person the shell command that does what the refused call would do, to type after `!` in the prompt, and go on after the person has run it (case 741).

To stop, end the reply with the question to the person. From the call of `/retro` until `handoff.md` stands, open that reply with `STOP:`, so that the hook of `rule-retro-onward` lets it end. Nothing else is a stop: a red test other than that of the seventh condition, a reading that only the person can take, an observation or a doubt goes on as a lesson or a line of `handoff.md`, as `/retro` says. After the person's answer, the run goes on from where it stopped.
<!-- /rule-where-to-stop -->

## History

- 2026-09-30 created · [[decision-case-531.7]]
- 2026-09-30 estimate estimate-where-to-stop-stops-only-on-its-conditions added · [[decision-case-531.7]]
- 2026-10-01 status: draft → built · cascade
- 2026-10-02 updated: /box imports the file, and its stops — a reason of its check, a fast-forward merge that refuses — are condition 6 (case 591.10) · [[decision-case-591.10]]
- 2026-10-02 status: built → draft · cascade
- 2026-10-04 status: draft → built · cascade
- 2026-10-06 updated: /hi loads the file for Plan Mode (case 689.1) · [[decision-case-689.1]]
- 2026-10-08 updated: a new red test of the full run of /work whose fix needs a new Case is a stop (case 736.3) · [[decision-case-736.3]]
- 2026-10-08 updated: a refusal of the auto mode classifier is a stop: the person runs the command after ! (case 741) · [[decision-case-741]]
- 2026-10-11 updated: condition 6 also covers a refused merge or branch deletion in the merge tasks of the opening Case of a sprint · [[decision-case-775.3]]
- 2026-10-13 updated: condition 6 covers a refused git or gh command in the merge tasks of the opening Case of a sprint, of a review Case and of a merge Case, and a conflict that a merge Case does not settle · [[decision-case-789.3]]
- 2026-10-13 updated: ships in the clean version (case 804) · [[decision-case-804.5]]
- 2026-10-14 updated: the first condition also covers a ratified Case found wrong, by a text the agent finds wrong or by a finding of the check of the plan in Work Mode; under /box no Case is built (case 806.4) · [[decision-case-806.4]]
- 2026-10-15 reworded: `uv run guppi` → `uv run --project .guppi guppi` · [[decision-case-819.1]]
- 2026-10-15 reworded: `make test` → `uv run --project .guppi guppi test` · [[decision-case-820.7]]
