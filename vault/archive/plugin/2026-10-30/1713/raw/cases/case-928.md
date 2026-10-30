## Case 928 — The reading of the clean code runs by guppi ship --check --review

> **context:**
> `estimate-clean-branch-code-holds-pointers-only-in-brackets` checks that the code and the tests hold each pointer to a case in a bracket of its own. Its `method` builds the clean copy by `uv run --project .guppi guppi ship --review` into an empty folder. In `run` of `.guppi/guppi/ship.py`, a build into a folder first calls `drafts`, which lists each page that `is_draft_core` accepts. When the list is not empty and `--allow-draft` is not passed, `run` prints the list and returns 1 before it reads a tag or writes the copy. The brief reports the last `guppi check` (`## Flags` of `vault/wiki/brief.md`): "Lint (`guppi check`, exit 1, 13 lines): 12 pages with `core: true` stand `draft`". So the reading as its `method` writes it gives no lines. The handoff of session 0304 says that Retro ran it with `--allow-draft`, and "The `method` does not name the flag". The `When` of the Criterion has the same gap: it says that `ship --review <folder>` builds the clean version, which it does not do while such a page stands.
>
> The person chose to read by `uv run --project .guppi guppi ship --check --review`. In `run`, `--check` calls `check` and never calls `drafts` or `version`, and `--review` adds the bracket lines whatever the path. `check` and `settled` both judge a file by `judged`. For a file under `.guppi/`, `plan` maps its path in the copy to the same path in the tree, and `ship` copies it by `shutil.copyfile` and changes only `CLAUDE.md` and the manifest before it judges, so both paths list the same lines for those files. I read `run`, `check`, `ship`, `settled`, `judged`, `plan`, `drafts` and `version` of `.guppi/guppi/ship.py` whole for these claims. No test runs `--check` and `--review` together. A Grep of `"--check"` over `.guppi/tests/test_ship.py` printed 11 lines, and none of them passes `--review` beside `--check`. A Grep of `--check.*--review|--review.*--check` over `.guppi/tests/` printed `.guppi/tests/test_ship.py`, whose hit is its module docstring, which names the two options apart. The reading at Retro shows the pair live.
>
> The Case replaces the Criterion whole and sets the Estimate `pending`, and the reading of this session at Retro checks it. The new `When` names the new command. The `Then` lines stand as they were, with three changes. The first line speaks of a line on a pointer outside its bracket, since the run now prints the `--review` lines on the same files too. A new `－` line says that a draft page and a missing tag do not stop the run. The line on the rewording now names what it rewords, so that it reads without the earlier Case. The line on `.claude/` speaks of a line of the run rather than of `--check` alone. A Criterion line names `Makefile` and `pyproject.toml`. `plan` takes neither the `Makefile` nor the root `pyproject.toml` into the copy (`ROOT_FILES` holds `CLAUDE.md` and `.gitattributes`), so neither command judges them. That line was true before and stays true, so it stands. The `purpose` speaks of what `guppi ship --check` prints and of the brackets it removes, which both still hold, so it stands. The `method` is set anew.
>
> A Grep of `ship --review` over `vault/wiki/` and `.claude/` printed `vault/wiki/estimates/estimate-clean-branch-pages-hold-pointers-only-in-brackets.md`, `vault/wiki/estimates/estimate-clean-branch-refuses-a-draft-core-page.md`, `vault/wiki/estimates/estimate-clean-branch-writes-a-clean-copy.md`, `vault/wiki/estimates/estimate-clean-branch-code-holds-pointers-only-in-brackets.md`, `vault/wiki/rules/rule-clean-branch.md` and `vault/wiki/brief.md`. The Estimate of the pages reads the pages under `vault/`, which `--check` does not judge. Its `method` still names no `--allow-draft`, and by the person's answer this Case does not change it, so that defect stays open. The Estimate of the draft refusal and the Estimate of the clean copy set what the folder build does, and this Case does not change that. `rule-clean-branch` says that `--review` lists the brackets and that `--check` judges in place, and neither sentence ties `--review` to a folder, so both stand. The `brief.md` hit is not read. No test under `.guppi/tests/` reads this Estimate page live. The ledger of this session holds no `error` lesson, so no line carries `{addresses:...}`.

> **problem:**
> The reading of the clean code, as its `method` and its Criterion write it, exits 1 and writes nothing while any page with `core: true` stands `draft`.

> **recommend:**
> - **How the reading of the clean code runs while a core page stands draft**
>   - Recommended: (c) read by `guppi ship --check --review` in the `method` and in the `When`.
>   - Answer: agreed, (c).
> - **Whether the Estimate of the pages gets the same fix**
>   - Recommended: (a) this Case changes only the Estimate of the code.
>   - Answer: agreed, (a).

> **given:**
> `estimate-clean-branch-code-holds-pointers-only-in-brackets`: its Criterion is replaced whole and its `method` set anew.
> **＋** `.guppi/guppi/ship.py`: the command `guppi ship`, whose `--check` and `--review` the reading runs.
> **＋** `.guppi/guppi/` and `.guppi/tests/`: the code and the tests the reading judges.
> **＋** `.guppi/tests/test_casecheck.py`: the test whose docstring and comment the reading reads.
> **＋** `.claude/` and `CLAUDE.md`: the harness files the run also judges, outside this promise.
> **＋** `rule-retro`: sets Retro and what a red check of the handoff is.

> **when:**
> At Retro of the session, `uv run --project .guppi guppi ship --check --review` of `.guppi/guppi/ship.py` judges the working tree in place and writes no folder.

> **then:**
> It prints no line on a pointer outside its bracket in a file under `.guppi/guppi/` or `.guppi/tests/`, on `Makefile`, on `pyproject.toml` or on `.gitattributes`, a bare case number in a comment or a docstring included.
> **＋** Each line of `--review` on those files shows a bracket that holds only pointers and the words that go with them, such as what a pointer sets, when a thing was measured or which session a pointer names.
> **＋** In `.guppi/tests/test_casecheck.py`, the docstring of `built_again_sibling` and the comment after `plan_with(working, PLANNED_5)` name the made-up Case of the test as the sibling Case, with no number.
> **－** A page with `core: true` that stands `draft` does not stop the run, and no tag `prod-x.y.z` is needed.
> **－** A rewording of a comment or a docstring in those files that moves a pointer into its bracket changes no other line, and `uv run --project .guppi guppi test` has no failing test that it did not have before the change.
> **－** A line of the run on `.claude/` or `CLAUDE.md` is no part of this promise: it goes into the handoff with the pages, and the red of `uv run --project .guppi guppi check` it makes is a note for the handoff by `rule-retro`.

> **tasks:**
> - [ ] update `estimate-clean-branch-code-holds-pointers-only-in-brackets`
>   - set: `{status: pending, method: "by hand, at Retro: the lines of uv run --project .guppi guppi ship --check --review over the working tree on .guppi/guppi/, .guppi/tests/, Makefile, pyproject.toml and .gitattributes, read against the Criterion"}`
>   - change: `the Criterion replaced whole — the reading runs by guppi ship --check --review, which no draft page with core: true stops`
> - [ ] read `estimate-clean-branch-code-holds-pointers-only-in-brackets`

> **ratification:**
> ```
> - decision[case 928][update][estimate-clean-branch-code-holds-pointers-only-in-brackets]{ref:rule-clean-branch}
> ```
