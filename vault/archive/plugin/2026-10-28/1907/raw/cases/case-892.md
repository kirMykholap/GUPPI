## Case 892 — The tests hold no reference to a case outside a bracket

> **context:**
> `guppi ship --check` reads each file that the clean copy takes outside `vault/`. In a test file under `.guppi/tests/` it reads only the comments and the docstrings, and it flags any reference to a case that does not stand in a bracket of its own. `check`, `judged` and `leftovers` of `.guppi/guppi/ship.py` decide this, together with `outside` and `masked_strings` of `.guppi/guppi/pointers.py`. `masked_strings` puts aside every string that is not a docstring, but it does not put aside a code span inside a docstring. The tests that Case 890 added hold `Case 5` in the docstring of `built_again_sibling` and in the comment on the first line of `test_subagent_session_clash_with_a_case_built_again_takes_its_stored_value`. The number names the made-up Case of the test data, not a decision. The brief of session 0118 reports the result under Flags as `Lint: ship — .guppi/tests/test_casecheck.py:2695 and :2740, a reference to a case: Case 5`, and under Readings at the close as `uv run --project .guppi guppi check: 14 lines (exit 1), as in Flags`. `rule-clean-branch` says that a Case rewords such text at its source. The person chose to drop the number and call that Case the sibling Case, so that no fake pointer stands in a bracket. Neither Estimate of `rule-clean-branch` promised that the live test files pass the check. The Criterion of `estimate-clean-branch-code-holds-pointers-only-in-brackets` names `.guppi/guppi/`, `Makefile`, `pyproject.toml` and `.gitattributes`. The Criterion of `estimate-clean-branch-ships-the-tests` promises how the check reads a test file, not that the test files pass it. The person chose to widen the first Estimate to `.guppi/tests/`. This Case replaces its Criterion and sets its `purpose` and `method` anew, since both state the old set of folders. Three lines of the old Criterion are not carried word for word, and each one is replaced by its widened form. The `when` names `ship.py` by its path. The first `then` line adds `.guppi/tests/`. The first `－` line speaks of any rewording, no longer only of the bare case numbers in `.guppi/guppi/`. The other paths of that Criterion stay as the person's answer left them. `Makefile` and the root `pyproject.toml` are not in `ROOT_FILES` or `TREES` of `ship.py`, so `--check` prints no line on them. A Grep of the repository outside `vault/archive/` and `vault/raw/` for `estimate-clean-branch-code-holds-pointers-only-in-brackets` printed `vault/wiki/log.md` and `vault/wiki/rules/rule-clean-branch.md`, and no file under `.guppi/tests/`, so no test reads that page live. The line of `rule-clean-branch` that hits is its `estimates` field and a History line, and neither one changes. The person chose to fix only the two lines and add no earlier guard to Work Mode.

> **problem:**
> A docstring and a comment of `.guppi/tests/test_casecheck.py` name test data as `Case 5`, outside a bracket. `guppi ship --check` flags them, and `guppi check` reports them. No Estimate promises that the test files pass this check.

> **recommend:**
> - **How are the two lines reworded?**
>   - Recommended: (a) name the Case without its number, as the sibling Case.
>   - Answer: agreed, (a).
> - **Which Estimate checks the fix?**
>   - Recommended: (a) widen the Criterion of `estimate-clean-branch-code-holds-pointers-only-in-brackets` to cover `.guppi/tests/`.
>   - Answer: agreed, (a).
> - **Does this Case also stop a new test from bringing the defect back?**
>   - Recommended: (a) fix the two lines only.
>   - Answer: agreed, (a).

> **given:**
> `.guppi/tests/test_casecheck.py`: the tests whose docstring and comment name test data by a case number.
> **＋** `estimate-clean-branch-code-holds-pointers-only-in-brackets`: its Criterion, `purpose` and `method` are replaced.
> **＋** `rule-clean-branch`: the rule that a pointer stands in a bracket of its own and that a Case rewords such text at its source.
> **＋** `.guppi/guppi/ship.py`: the check `guppi ship --check`.
> **＋** `.claude/`: the harness, whose lines of `--check` stay out of this promise.
> **＋** `CLAUDE.md`: the root file whose lines of `--check` stay out of this promise.
> **＋** `rule-retro`: the rule that makes a red of `guppi check` a note for the handoff.

> **when:**
> At Retro of the session, `uv run --project .guppi guppi ship --check` of `.guppi/guppi/ship.py` judges the working tree, and `uv run --project .guppi guppi ship --review <folder>` builds the clean version into an empty folder.

> **then:**
> `uv run --project .guppi guppi ship --check` prints no line on a file under `.guppi/guppi/` or `.guppi/tests/`, on `Makefile`, on `pyproject.toml` or on `.gitattributes`, a bare case number in a comment or a docstring included.
> **＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as what a pointer sets, when a thing was measured or which session a pointer names.
> **＋** In `.guppi/tests/test_casecheck.py`, the docstring of `built_again_sibling` and the comment after `plan_with(working, PLANNED_5)` name the made-up Case of the test as the sibling Case, with no number.
> **－** The rewording changes no line but a comment or a docstring, and `uv run --project .guppi guppi test` has no failing test that it did not have before the change.
> **－** A line of `--check` on `.claude/` or `CLAUDE.md` is no part of this promise: it goes into the handoff with the pages, and the red of `uv run --project .guppi guppi check` it makes is a note for the handoff by `rule-retro`.

> **tasks:**
> - [ ] `.guppi/tests/test_casecheck.py`: the docstring of `built_again_sibling` opens with `The sibling Case stands in the plan as ratified`, and the comment after `plan_with(working, PLANNED_5)` reads `the plan's sibling Case sets status built`, in a code span as it stands; no other line changes.
> - [ ] update `estimate-clean-branch-code-holds-pointers-only-in-brackets`
>   - set:
>     ```
>     status: pending
>     purpose: Whether the code, the tests and the root files of this repository hold each pointer to a case, a decision or a session in a bracket of its own, and no case number without the word case before it, so that guppi ship --check prints no line on them and no bracket it removes from them holds a word the sentence needs
>     method: "by hand, at Retro: the lines of uv run --project .guppi guppi ship --check over the working tree, and of uv run --project .guppi guppi ship --review into an empty temporary folder, on .guppi/guppi/, .guppi/tests/, Makefile, pyproject.toml and .gitattributes, read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the tests under .guppi/tests/ hold pointers only in brackets too`
> - [ ] read `estimate-clean-branch-code-holds-pointers-only-in-brackets`

> **ratification:**
> ```
> - decision[case 892][update][estimate-clean-branch-code-holds-pointers-only-in-brackets]{ref:rule-clean-branch}
> ```
