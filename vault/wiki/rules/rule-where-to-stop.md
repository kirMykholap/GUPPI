---
type: rule
kind: Leaf
purpose: Prevents the run from /work to the librarian from stopping where the person is not needed, or going on where only the person can decide
status: built
enforcement: render
governs: vault/wiki/where-to-stop.md
render_mode: full
estimates: []
origin: guppi
sprint: guppi
created: 2026-10-14
tags: [session, workflow, harness, render]
core: true
---

## Purpose

Prevents the run from /work to the librarian from stopping where the person is not needed, or going on where only the person can decide. The person keeps three questions: what to do, the Cases of Plan Mode; what done means and how to check it, the Estimates; and where to stop, this page. `/work` and `/box` load its text by an import of `vault/wiki/where-to-stop.md`, `/hi` loads it for Plan Mode too, so the main agent promises the person no turn the run does not give, and the refusal of `rule-retro-onward` names the file. A hook on a single action, such as a push, may enforce a condition later; until then the text in the context is the guard.

## Render

<!-- rule-where-to-stop -->
# Where to stop

From the approved Spec to the librarian's report the run needs no person: `/box`, `/work`, the Work readings, `/retro` and `/handoff` run in one turn. Stop and ask the person only on one of these conditions:

1. A fork that changes a contract: the work needs a choice that no ratified Case makes, or a ratified Case turns out wrong — by a text you find wrong or too narrow, or by a finding of `uv run guppi prespec --check` on the plan after a Case ratified in Work Mode — so a new Case is needed, or that Case is fixed, as `orchestration.md` sets it; in a `/work` that `/box` calls no Case is built, as `rule-spec-box` sets it, and the choice goes to `handoff.md` as a line.
2. A hook refuses, and its text gives no step you can follow, or says that the refusal is a stop.
3. An action that git in this repository cannot undo, such as a push to a remote or a deletion outside the repository.
4. A task of the Spec whose text opens with `stop:`: stop before it runs, and run it after the person's word.
5. The branch is `main`: Work Mode does not start there; say so, and go on after the person moves to another branch.
6. `/box` cannot go on: its check `uv run guppi box --check` prints a reason, or one of its `git merge --ff-only` refuses; or a `git` or `gh` command of the merge tasks of the opening Case of a sprint, of the merge task of a review Case of `/pr-review`, or of the tasks of a merge Case of `/merge-main` refuses, or the merge of a merge Case leaves in conflict a file that the merge Case does not settle: show what stopped it, and go on after the person's word; a `git merge --no-ff --no-commit` of a merge Case that exits non-zero only on files the merge Case settles is no refusal.
7. The full `make test` run of `/work` after its last task finds a failing test that `## Baseline` of `work.md` does not hold, and its fix needs a choice that no ratified Case makes: name the test and its failure, and go on as the person's word says.
8. The auto mode classifier of Claude Code refuses a tool call that the run needs: give the person the shell command that does what the refused call would do, to type after `!` in the prompt, and go on after the person has run it.

To stop, end the reply with the question to the person. From the call of `/retro` until `handoff.md` stands, open that reply with `STOP:`, so that the hook of `rule-retro-onward` lets it end. Nothing else is a stop: a red test other than that of the seventh condition, a reading that only the person can take, an observation or a doubt goes on as a lesson or a line of `handoff.md`, as `/retro` says. After the person's answer, the run goes on from where it stopped.
<!-- /rule-where-to-stop -->

## History

- 2026-10-14 shipped with GUPPI
