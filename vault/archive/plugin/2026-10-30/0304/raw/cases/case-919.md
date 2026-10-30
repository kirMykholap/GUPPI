## Case 919 — The code and the tests hold no stray pointer to a case

> **context:**
> `guppi ship --check`, a step of `uv run --project .guppi guppi check`, judges in place each file outside `vault/` that the clean version of GUPPI takes, and prints a line for each pointer to a case, a decision or a session that stands outside a bracket of its own, since the clean version drops such a bracket whole and a pointer outside one would reach it. In a test file it judges only the comments and the docstrings, by `masked_strings` and `outside` of `.guppi/guppi/pointers.py`, and `bare_numbers` of `.guppi/guppi/ship.py` adds each bare case number there. The last run, under `## Flags` of `vault/wiki/brief.md`, printed `ship: .guppi/tests/test_render.py:500: a reference to a case: Case 914` among its 11 lines: the docstring of `test_paths_in_a_child_process_ends_each_line_in_a_bare_line_feed`, added by Case 914, opens with the words `Case 914:`. Nothing caught it before the librarian's run: Work Mode runs `guppi check` once before the first change, the Retro skill says not to run it, and `guppi test`, `uv run --project .guppi pytest -q` by `guppi.toml`, skips each test with the mark `live` by the `addopts` of `.guppi/pyproject.toml`, the mark of a test that reads the live vault, which `plan` of `.guppi/guppi/ship.py` and so `check` read. Case 919.1 moves the pointer into a bracket at the end of the sentence, as `rule-clean-branch` sets it, and sets `estimate-clean-branch-code-holds-pointers-only-in-brackets` `pending` with its Criterion written back unchanged, since that Criterion already promises that `guppi ship --check` prints no line on a file under `.guppi/tests/`, its line on `.guppi/tests/test_casecheck.py` still holds by the docstring of `built_again_sibling` and the comment after `plan_with(working, PLANNED_5)`, and the reading at Retro gives it a fresh Result in place of a `passed` that the check made false. Case 919.2 adds a test without the mark `live` that judges each file under `.guppi/` by `judged` of `.guppi/guppi/ship.py`, the function `check` calls for each file, with empty sets of known and loose slugs, so it reads no page; the two sides part on two inputs: a marker line of a page without `core: true`, which `leftovers` judges only by the loose slugs that `plan` reads from the vault, and a file that a page without `core: true` renders, which `plan` leaves out, and the new sentence of `rule-clean-branch` and the `then` of Case 919.2 say that the test judges neither, so no answer of the test claims to be the whole check. A Grep of `.guppi/guppi/` for `import.*\bjudged\b|\bjudged\(|from guppi.pointers import|pointers\.outside|\boutside,` printed `.guppi/guppi/ship.py` and `.guppi/guppi/prespec.py`: the judgment of a pointer lives in `.guppi/guppi/pointers.py` and `judged` is its one caller for a file, so the test imports it and holds no copy, as `rule-one-judgment-one-implementation` sets it. A Grep of `.guppi/tests/` for `rule-clean-branch|estimate-clean-branch-code-holds|test_render\.py|test_ship\.py` printed `.guppi/tests/test_ship.py` alone, whose hits write files under a temporary root, so no test reads a file this Case changes live. `rule-clean-branch` keeps `deferred_by: decision-case-893.1`, the Frontier item C4: the `update` of Case 919.2 changes one sentence and leaves the defer to C4, and `check_backlog` of `.guppi/guppi/casecheck.py` judges only open Frontier lines whose source is `backlog`, which C4 is not. The session's ledger holds no `error` lesson, so no line carries a mark.

> **problem:**
> A test docstring holds a pointer to a case outside a bracket, so `guppi check` is red and the clean version would carry it; and no step before the librarian's run judges the code and the tests for such a pointer, so the next one is found as late as this one.

> **recommend:**
> - **How should the docstring be fixed?**
>   - Recommended: (a) move the pointer into a bracket at the end of the sentence.
>   - Answer: agreed, (a).
> - **How should the fix be checked?**
>   - Recommended: (a) set `estimate-clean-branch-code-holds-pointers-only-in-brackets` back to `pending`, its Criterion unchanged, and read it at Retro.
>   - Answer: agreed, (a).
> - **Should the Case also add a guard against a repeat?**
>   - Recommended: (a) fix this one docstring only.
>   - Answer: (b), also add a test that runs the pointer check over the live `.guppi/` folder.
> - **What should the guard test judge, and how does it run?**
>   - Recommended: (a) an unmarked test over the files of `.guppi/` alone, by `judged` of `.guppi/guppi/ship.py`, with no read of the vault.
>   - Answer: agreed, (a).
> - **How should the guard be checked?**
>   - Recommended: (a) a new Estimate on `rule-clean-branch`.
>   - Answer: agreed, (a).
> - **Should `rule-clean-branch` say that the guard exists?**
>   - Recommended: (a) add one sentence after the passage on `guppi ship --check`.
>   - Answer: agreed, (a).

### Case 919.1 — The docstring of the test of --paths holds its pointer in a bracket

> **given:**
> `.guppi/tests/test_render.py`: the docstring of `test_paths_in_a_child_process_ends_each_line_in_a_bare_line_feed`.
> **＋** `.guppi/guppi/ship.py`: `guppi ship --check`, which judges the docstring.
> **＋** `estimate-clean-branch-code-holds-pointers-only-in-brackets`: set `pending`, its Criterion written back unchanged.
> **＋** `rule-clean-branch`: sets the bracket of a pointer.

> **when:**
> `uv run --project .guppi guppi ship --check` of `.guppi/guppi/ship.py` judges `.guppi/tests/test_render.py` in the working tree.

> **then:**
> It prints no line on `.guppi/tests/test_render.py`.
> **＋** The docstring of `test_paths_in_a_child_process_ends_each_line_in_a_bare_line_feed` holds its pointer to a case in a bracket at the end of its sentence, as `rule-clean-branch` sets it.
> **－** The fix changes no line of `.guppi/tests/test_render.py` but that docstring.

> **tasks:**
> - [ ] `.guppi/tests/test_render.py`: the docstring of `test_paths_in_a_child_process_ends_each_line_in_a_bare_line_feed` reads `Run as the close command runs it, --paths writes no carriage return, on Windows too, so $(...) hands git add each path as it stands (case 914).`, its code spans kept as they stand, in two lines of at most 100 characters.
> - [ ] update `estimate-clean-branch-code-holds-pointers-only-in-brackets`
>   - set: `{status: pending}`
>   - sections.Criterion:
>     ```
>     When:
>     At Retro of the session, `uv run --project .guppi guppi ship --check` of `.guppi/guppi/ship.py` judges the working tree, and `uv run --project .guppi guppi ship --review <folder>` builds the clean version into an empty folder.
>
>     Then:
>     `uv run --project .guppi guppi ship --check` prints no line on a file under `.guppi/guppi/` or `.guppi/tests/`, on `Makefile`, on `pyproject.toml` or on `.gitattributes`, a bare case number in a comment or a docstring included.
>     **＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as what a pointer sets, when a thing was measured or which session a pointer names.
>     **＋** In `.guppi/tests/test_casecheck.py`, the docstring of `built_again_sibling` and the comment after `plan_with(working, PLANNED_5)` name the made-up Case of the test as the sibling Case, with no number.
>     **－** The rewording changes no line but a comment or a docstring, and `uv run --project .guppi guppi test` has no failing test that it did not have before the change.
>     **－** A line of `--check` on `.claude/` or `CLAUDE.md` is no part of this promise: it goes into the handoff with the pages, and the red of `uv run --project .guppi guppi check` it makes is a note for the handoff by `rule-retro`.
>     ```
>   - change: `pending again: guppi ship --check printed a line on .guppi/tests/test_render.py; the Criterion stands`
> - [ ] read `estimate-clean-branch-code-holds-pointers-only-in-brackets`

> **ratification:**
> ```
> - decision[case 919.1][update][estimate-clean-branch-code-holds-pointers-only-in-brackets]{ref:rule-clean-branch}
> ```

### Case 919.2 — guppi test judges the code and the tests for a stray pointer

> **given:**
> `.guppi/tests/test_ship.py`: the new tests of the live code.
> **＋** `.guppi/guppi/ship.py`: `judged`, `tree_files`, `read_text`, `LEFT_OUT` and `NOT_CLEANED`, which the tests call and read.
> **＋** `rule-clean-branch`: the page that states the guard.
> **＋** `estimate-clean-branch-tests-judge-the-live-code`: the new check of the guard.
> **＋** `rule-retro`: lets no red test stand at Retro.

> **when:**
> `uv run --project .guppi guppi test` runs the tests of `.guppi/tests/` in the repository of GUPPI.

> **then:**
> A test of `.guppi/tests/test_ship.py` walks the code and the tests under `.guppi/` by `tree_files`, leaves out `LEFT_OUT` and `NOT_CLEANED`, and runs `judged` of `.guppi/guppi/ship.py` over each file, the same judgment as the step of the clean version, and passes when `judged` returns nothing for every file.
> **＋** Where a comment or a docstring under `.guppi/` holds a pointer outside a bracket of its own or a bare case number, the test fails and shows the file and the line of each.
> **＋** The test carries no mark `live` and reads no page of the vault, so `uv run --project .guppi guppi test` runs it.
> **＋** A second test runs the same walk over a temporary folder whose test file has a docstring that opens with `Case 5:`, and finds that line.
> **－** It judges no file of the harness, no file at the root of the project and no marker line of a page without `core: true`; those stay with the step `--check` of `.guppi/guppi/ship.py`.

> **tasks:**
> - [ ] `.guppi/tests/test_ship.py`: a helper that walks the files under `.guppi/` of a root by `ship.tree_files`, but `ship.LEFT_OUT` and `ship.NOT_CLEANED`, reads each by `ship.read_text` and returns the lines of `ship.judged` with empty sets of known and loose slugs; a test with no mark `live` that asserts the helper returns no line on `REPO`; a test that asserts it returns the line of a docstring that opens with `Case 5:` in a test file under a temporary root; the name of each test holds `live_code`.
> - [ ] create `estimate-clean-branch-tests-judge-the-live-code`
>   - ref: `rule-clean-branch`
>   - kind: `QA`
>   - purpose: `Whether guppi test judges the code and the tests under .guppi/ for a pointer outside its bracket and a bare case number, with no read of the vault, so that a stray one goes red before the librarian's run`
>   - method: `uv run --project .guppi pytest .guppi/tests/test_ship.py -k live_code, and uv run --project .guppi guppi test, read against the Criterion at Retro`
>   - tags: `[plugin, tests]`
> - [ ] update `rule-clean-branch`
>   - old: `` and `uv run --project .guppi guppi check` runs it; ``
>   - new: `` and `uv run --project .guppi guppi check` runs it; a test of `.guppi/tests/test_ship.py` runs the same judgment, `judged` of `.guppi/guppi/ship.py`, over each file under `.guppi/` that the clean version holds, with no read of the vault and so no judgment of a marker line, and `uv run --project .guppi guppi test` fails on a pointer outside its bracket or a bare case number there before the librarian's run; ``
>   - change: `a test of guppi test judges the code and the tests under .guppi/ for a pointer outside its bracket`
> - [ ] read `estimate-clean-branch-tests-judge-the-live-code`

> **ratification:**
> ```
> - decision[case 919.2][create][estimate-clean-branch-tests-judge-the-live-code]{ref:rule-clean-branch}{tags:plugin,tests}
> - decision[case 919.2][update][rule-clean-branch]{ref:rule-clean-branch}
> ```
