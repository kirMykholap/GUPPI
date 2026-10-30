## Case 914 — The list of rendered files ends each line with a bare line feed, on Windows too

> **context:**
> At its close the librarian commits the vault with the command of the Render of `rule-close`: `git add vault $(uv run --project .guppi guppi render --paths) && git commit ...`. `run` of `.guppi/guppi/render.py` prints each path of `--paths` by `print(governs, file=stdout)`, and `main` of `.guppi/guppi/cli.py` sets only the encoding of the output, to UTF-8. On Windows the output of Python ends each line with a carriage return and a line feed. The shell keeps the carriage return on each path. `case-guppi` read the run at its source, the saved chat of the librarian of session 1930 (`subagents/agent-a9b114d335b9583a3.jsonl` under `7f200512-38a4-43be-9723-2cbf3756ed67`): the command as written printed `Exit code 128` and `fatal: pathspec '.claude/agents/ask-guppi.md?' did not match any files`, and the next call ran the same command with `| tr -d '\\r'` after `--paths`. The report of that run, the last message of the main chat, says the same. `estimate-close-commits` was read `passed` at the /hi of this session from the end state alone: one separate commit and a clean tree. Its tests in `.guppi/tests/test_render.py` call `render.run` with an in-memory stream and split its output into lines, so they never see a line ending. The Python documentation of `io` (https://docs.python.org/3/library/io.html) says that on output `newline=None` translates each line feed to `os.linesep`, that `''` or `'\n'` translates nothing, and that `reconfigure` may change `newline` on a stream that nothing was read from. The person chose to fix the output of `--paths` alone, at its source (Q1): a Grep `\$\(uv run[^)]*guppi` over the repository outside `vault/raw/` printed `vault/wiki/rules/rule-close.md`, `.claude/agents/librarian-guppi.md`, `vault/wiki/estimates/estimate-close-commits.md` and nine files under `vault/archive/`, each hit the close command or a copy of it, so no other shell command reads the output of a `guppi` command. The fix is in code, so it holds at the librarian's run of this session, whose frame still holds the old close command, which then works as written; the Render of `rule-close` does not change. `rule-render-harness` lists `.guppi/guppi/render.py` in its `implementation_ref`, but a Grep `--paths` over `vault/wiki/estimates/estimate-render-*.md`, the files of its three Estimates, printed nothing; `estimate-close-commits`, whose target is `rule-close`, holds that promise since case 857. This Case replaces its Criterion whole (Q2): each old line stands, but its first line, on what `--paths` prints, which is not carried word for word, since the new first line adds the bare line feed to it, and a new line says that the close command as written passes each path as it stands. It also sets its `purpose` anew, since the old one does not name the close command as written; its `method` gains the test that runs `--paths` as a child process and reads its output as bytes, and keeps its reading by hand of the commit after a librarian's run. The main agent writes a new reading `failed` of the Estimate before this Case's decision lines (Q3), so that the failure lands in its Result before this update sets it `pending`. A failed close command does not go into the librarian's report by this Case (Q4); the report is the frame of Case 913, which changes another sentence of the same Render. A Grep `estimate-close-commits|render --paths` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/brief.md`, `vault/wiki/log.md`, `.claude/agents/librarian-guppi.md`, `vault/wiki/rules/rule-close.md`, `vault/wiki/estimates/estimate-close-commits.md`, `vault/wiki/lessons/lesson-brief-lists-transcript-readings-under-work.md` and `.guppi/tests/test_render.py`. `brief.md` and `log.md` are not read; the lesson records a reading of an earlier session and stands; the close command in `rule-close` and `librarian-guppi.md` stays true once `--paths` prints bare line feeds.

> **problem:**
> On Windows the list that the close command passes to `git add` carries a carriage return on each path, so the command as written fails, and the librarian ran a changed command. The Estimate of the commit passed on the end state, and its tests cannot see a line ending.

> **recommend:**
> - **Where the line ending is fixed**
>   - Recommended: (a) `--paths` alone prints bare line feeds, set on its own output before it prints.
>   - Answer: agreed, (a).
> - **How the fix is checked**
>   - Recommended: (a) replace the Criterion of `estimate-close-commits` with the line ending and the close command as written; a new test runs `--paths` as a real process and asserts no carriage return; the page goes back to `pending`.
>   - Answer: agreed, (a).
> - **What happens to the reading of passed**
>   - Recommended: (a) the main agent writes a new reading `failed` from the saved chat, before this Case's decision lines.
>   - Answer: agreed, (a).
> - **Whether a failed close command goes into the report**
>   - Recommended: (a) left out of this Case.
>   - Answer: agreed, (a).

> **given:**
> `estimate-close-commits`: its Criterion is replaced whole, its `purpose` and `method` set anew.
> **＋** `.guppi/guppi/render.py`: `run` prints the list of `--paths`.
> **＋** `.guppi/tests/test_render.py`: the tests of `guppi render --paths`.
> **＋** `rule-close`: the rule whose Render writes the close command, the target of the Estimate.
> **＋** `.claude/agents/librarian-guppi.md`: the frame of the librarian, where the close command stands.
> **＋** `rule-plugin-install`: the rule whose file the list names only in a project that holds it.
> **＋** `plugin/skills/install/SKILL.md`: the file of `rule-plugin-install` that the list may name.
> **＋** `vault/`: the folder the commit takes beside the list.

> **when:**
> After a live run, the librarian commits at the close, as `.claude/agents/librarian-guppi.md` says, with the list that `uv run --project .guppi guppi render --paths` prints.

> **then:**
> `uv run --project .guppi guppi render --paths` prints each file that `guppi render` writes, one path per line, each line ended by a bare line feed with no carriage return, on Windows too, and writes nothing.
> **＋** The close command, as `.claude/agents/librarian-guppi.md` writes it, passes each path of that list to `git add` as the path stands, with no filter added to it.
> **＋** `git log` shows one commit after the Retro commit, separate from the session's, with the message `docs(vault): librarian, <date>`, and never `--amend`.
> **＋** The commit takes `vault/` and each file of that list: `git add vault $(uv run --project .guppi guppi render --paths)`.
> **＋** After the commit, `git status` shows no file that `.guppi/guppi/render.py` wrote as modified or untracked.
> **－** The commit takes no path that neither `vault/` nor that list names.
> **－** In a project without `rule-plugin-install`, the list and the commit name no `plugin/skills/install/SKILL.md`.

> **tasks:**
> - [ ] `.guppi/guppi/render.py`: in `run`, the `--paths` branch sets its output stream to `newline="\n"` by `reconfigure` where the stream has it, before it prints; the docstring of `--paths` says each line ends in a bare line feed.
> - [ ] `.guppi/tests/test_render.py`: a test whose name holds `paths` runs `guppi render --paths` as a child process over a small vault in a temp folder and asserts that its output, read as bytes, holds no carriage return and one line per `governs` path.
> - [ ] update `estimate-close-commits`
>   - set:
>     ```
>     status: pending
>     purpose: "The librarian's run ends in one separate commit of vault and each file the render writes, by the close command as its frame writes it, with no rendered file left modified or untracked"
>     method: "uv run --project .guppi pytest .guppi/tests/test_render.py -k paths, on Windows too, where the test that runs guppi render --paths as a child process reads its output as bytes; by hand, after a librarian's run whose .claude/agents/librarian-guppi.md, when the run starts, holds the Render of rule-close: git log shows the commit of that run and the paths it touched, and git status shows no file the render wrote as modified or untracked"
>     ```
>   - change: `the Criterion replaced whole — guppi render --paths ends each line with a bare line feed, on Windows too, and the close command passes each path to git add as it stands`
> - [ ] read `estimate-close-commits`

> **ratification:**
> ```
> - decision[case 914][update][estimate-close-commits]{ref:rule-close}
> ```
