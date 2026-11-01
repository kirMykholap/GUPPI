## Case 983 — The backlog check passes the put-offs of the running session

> **context:**
> `guppi backlog` writes `vault/wiki/backlog.md`, and each line of it carries the number of sessions whose Frontier put the item off. `put_off_count` in `.guppi/guppi/backlog.py` counts the `[-]` lines of every `frontier.md` under `vault/raw/` and `vault/archive/`, read once by `sessions_of` through `frontiers` and `frontier_marks` of `.guppi/guppi/generate.py`; the Frontier of the running session is among them. The librarian writes the file after the session, but `guppi backlog --check` (the branch `if args.check` of `run`) renders in memory from the same sources and compares. So a session that puts off an item already on the list sees `backlog: vault/wiki/backlog.md differs from its sources` in its Work Mode Baseline until its librarian's run. The handoff of session 0141 found this cause on a copy of commit `cdfeb988`: exit 0 without the Frontier of session 2307, exit 1 with it, the difference being the three counts the librarian of 2307 then wrote. Retro takes such a red as red before the work (`rule-retro`), so it is noise, not debt; the brief of 0141 reports that its closing `guppi check` printed 13 lines and no `backlog.md differs from its sources` line. The person chose that the check accepts the file in either of two forms: the render with every Frontier, or the render without the Frontier of the newest session, the first entry of `frontiers`, which sorts newest first. A check step gets no session stamp: `run` of `.guppi/guppi/check.py` starts each step with no stdin and only `CLAUDE_PROJECT_DIR` added to the environment, so the newest Frontier stands for the running session, whose `frontier.md` `/hi` writes before any Baseline. The writer does not change, so the Criterion of `estimate-backlog-renders`, which speaks of the count the writer puts in the file, stands; the Criterion of `estimate-backlog-checks-the-file` says the check prints when the file differs from the render of its sources, which this change makes false, so the Case replaces it, and its `purpose`, which states the old promise. The Frontier is still read once, by `frontier_marks`; the second render drops the newest entry of the list `sessions_of` returns, so no second reader of a Frontier line is written (`rule-one-judgment-one-implementation`). A Grep of `backlog --check|backlog.md differs|differs from (the render of )?its sources` over `vault/wiki/`, `.claude/`, `.guppi/guppi/` and `.guppi/tests/` printed `rule-lint.md`, `rule-harness.md`, `rule-backlog.md`, `estimate-backlog-checks-the-file.md`, `estimate-clean-branch-writes-the-session-files.md`, `estimate-harness-pipeline.md`, `estimate-lint-runs-every-step.md`, `estimate-retro-red-in-the-baseline-is-not-charged.md`, `log.md`, `brief.md`, `backlog.py`, `test_backlog.py` and `test_check.py`. `rule-lint`, `estimate-lint-runs-every-step` and `test_check.py` name only the order of the steps; `estimate-harness-pipeline` and `estimate-clean-branch-writes-the-session-files` want the check to exit 0 on a committed tree or a clean version, which a check that accepts more still does; the hit of `rule-harness` is a History line and that of `estimate-retro-red-in-the-baseline-is-not-charged` a Result, and the hits of `log.md` and `brief.md` are not read. The two tests of `--check` that expect exit 1 write a file by hand or none, which matches neither render, so they stand. In `.guppi/links.md`, the block of `rule-backlog` names `estimate-backlog-checks-the-file`, `estimate-backlog-renders`, `rule-one-judgment-one-implementation`, `rule-sprint-close`, `rule-case-protocol` and the skills and the agent that run the command; none of them states what the check accepts. The blocks of `.guppi/guppi/backlog.py` and `.guppi/tests/test_backlog.py` name only `rule-backlog` and `entity-guppi`. The session's ledger holds no `error` lesson.

> **problem:**
> `guppi backlog --check` goes red in the Baseline of any session that puts off an item already on the list, though only the librarian's run of that session can write the new count, so every such session explains the same red again.

> **recommend:**
> - **What should the check do with the put-offs of the session that is running**
>   - Recommended: (b) the check accepts the file in either of two forms: the render with every Frontier, or the render without the Frontier of the newest session; the writer does not change.
>   - Answer: agreed, (b).

> **given:**
> `rule-backlog`: the rule of the backlog file, whose Purpose says what the check compares.
> **＋** `estimate-backlog-checks-the-file`: the check of `--check`, whose Criterion is replaced whole.
> **＋** `.guppi/guppi/backlog.py`: the writer and the check of the file.
> **＋** `.guppi/tests/test_backlog.py`: the tests of the writer and the check.
> **＋** `.guppi/guppi/generate.py`: `frontiers` and `frontier_marks`, the one reader of the Frontier files, read only.
> **＋** `rule-one-judgment-one-implementation`: one reader of a Frontier line.
> **＋** `vault/wiki/backlog.md`: the file the check compares.

> **when:**
> Someone runs `uv run --project .guppi guppi backlog --check`, by hand or through `uv run --project .guppi guppi check`, over `vault/wiki/backlog.md` and the `frontier.md` files that `frontiers` of `.guppi/guppi/generate.py` finds.

> **then:**
> The check renders the file in memory once with every Frontier file and once without the Frontier file of the newest session, the first in the order of `frontiers` of `.guppi/guppi/generate.py`.
> **＋** When `vault/wiki/backlog.md` equals either render, the check is silent and exits 0.
> **＋** When it equals neither, the check prints one line on stdout that names the file and exits 1.
> **＋** `uv run --project .guppi guppi backlog` without `--check` writes the render with every Frontier file.
> **＋** `uv run --project .guppi guppi check` runs it after `sprint --check` and before `glossary --check`.
> **－** The check writes no file in either case.
> **－** `uv run --project .guppi guppi check` writes nothing to the tree.
> **－** The check reads each Frontier file once, by `frontier_marks` of `.guppi/guppi/generate.py`.

> **tasks:**
> - [ ] update `rule-backlog`
>   - old: `` `guppi backlog --check` renders in memory and names the file when it differs, and `uv run --project .guppi guppi check` runs it. ``
>   - new: `` `guppi backlog --check` renders in memory and names the file when it differs from the render with every Frontier and from the render without the Frontier of the newest session, since the put-offs of the running session enter the file only at the librarian's run (as set in case 983). `uv run --project .guppi guppi check` runs it. ``
>   - change: `the check accepts the file without the put-offs of the newest session`
> - [ ] update `estimate-backlog-checks-the-file`
>   - set: `{status: pending, purpose: "guppi backlog --check names backlog.md when it differs from the render with every Frontier and from the render without the Frontier of the newest session, exit 1, and writes nothing", method: "uv run --project .guppi pytest .guppi/tests/test_backlog.py"}`
>   - change: `the Criterion replaced whole — the check accepts the file without the put-offs of the newest session`
> - [ ] `.guppi/guppi/backlog.py`: `render` takes the list of sessions as an argument; the branch `--check` of `run` reads `sessions_of` once and passes when the file equals the render of that list or of that list without its first entry; the docstring says so.
> - [ ] `.guppi/tests/test_backlog.py`: `--check` is silent on a file written before the newest session put an item off, red when the put-off of an older session is missing from the file, and reads each Frontier once by `frontier_marks`.
> - [ ] read `estimate-backlog-checks-the-file`

> **ratification:**
> ```
> - decision[case 983][update][rule-backlog]{ref:rule-backlog}
> - decision[case 983][update][estimate-backlog-checks-the-file]{ref:rule-backlog}
> ```
