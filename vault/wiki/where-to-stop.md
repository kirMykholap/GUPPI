# Where to stop

From the approved Spec to the librarian's report the run needs no person: `/box`, `/work`, the Work readings, `/retro` and `/handoff` run in one turn. Stop and ask the person only on one of these conditions:

1. A fork that changes a contract: the work needs a choice that no ratified Case makes, so a new Case is needed.
2. A hook refuses, and its text gives no step you can follow, or says that the refusal is a stop.
3. An action that git in this repository cannot undo, such as a push to a remote or a deletion outside the repository.
4. A task of the Spec whose text opens with `stop:`: stop before it runs, and run it after the person's word.
5. The branch is `main`: Work Mode does not start there; say so, and go on after the person moves to another branch.
6. `/box` cannot go on: its check `uv run guppi box --check` prints a reason, or one of its `git merge --ff-only` refuses; show what stopped it, and go on after the person's word.
7. The full `make test` run of `/work` after its last task finds a failing test that `## Baseline` of `work.md` does not hold, and its fix needs a choice that no ratified Case makes: name the test and its failure, and go on as the person's word says (case 736.3).

To stop, end the reply with the question to the person. From the call of `/retro` until `handoff.md` stands, open that reply with `STOP:`, so that the hook of `rule-retro-onward` lets it end. Nothing else is a stop: a red test other than that of the seventh condition, a reading that only the person can take, an observation or a doubt goes on as a lesson or a line of `handoff.md`, as `/retro` says. After the person's answer, the run goes on from where it stopped.
