## Case 857 — The close commit takes each file the render writes

> **context:**
> At the end of its run the librarian makes one commit, by the command that the Render of `rule-close` writes into `.claude/agents/librarian-guppi.md`: `git add vault CLAUDE.md .claude guppi.toml`, and never a path outside those four. The render writes each file that a live Rule page names in `governs` (`plan` and `write_all` of `.guppi/guppi/render.py`), and since case 818.1 one of them, `plugin/skills/install/SKILL.md` of `rule-plugin-install`, lies outside the four paths. The brief of session 0342 reports it under Flags: "The render wrote `plugin/skills/install/SKILL.md`, which lies outside the four paths of the close commit (`vault`, `CLAUDE.md`, `.claude`, `guppi.toml`); it stays modified after this run's commit." `git status` shows that file modified now; the Work item of the Frontier on the dirty tree commits it, and this Case does not.
>
> The person chose that `guppi render` gets an option `--paths`, which prints each file the render writes, and that the commit adds `vault` and those files. A fixed list that names `plugin` was turned down: `rule-close` has `core: true` and ships, a project that installs GUPPI has no `plugin/` folder since `rule-plugin-install` does not ship, and the sentence would hold only in the repository of GUPPI, against the third `Then` line of `estimate-clean-branch-ships-neutral-texts`. The new Render holds no pointer to a case, so no bracket is needed for `guppi ship`. `--paths` prints the keys of `plan`, the same function that decides what the render writes, so the list is no second copy of that judgment (`rule-one-judgment-one-implementation`). A Grep for `governs` over `.guppi/guppi/` printed 68 matches in nine files: `generate.py`, `lint.py`, `sprint.py`, `guard.py`, `backlog.py`, `ship.py`, `glossary.py`, `prespec.py` and `render.py`. `governed_paths` of `prespec.py`, the map of `guard.py` and `governed` of `ship.py` answer other questions (the rule of a path named in a Spec, the guard of a hand edit, the files of the pages with `core: true`), and the task calls none of them and copies none.
>
> `estimate-close-commits` (passed) names the four paths in its `purpose` and its Criterion, and its last line forbids any other path, so this Case replaces its Criterion whole and sets its `purpose` and `method` anew. No old line of that Criterion is carried word for word: each one that names the four paths is written again with `vault/` and the list of `--paths`, and the lines on the single commit, its message, `--amend` and the report keep their meaning in the new wording. Claude Code loads an agent file when the agent is dispatched, so the librarian's run of this session still commits by the old command, and the first commit by the new one comes at the next librarian run after the render of `.claude/agents/librarian-guppi.md`: the `method` waits for that event. The Estimates of `rule-render-harness` speak of the render without a flag, with `--check` and with `--sync`, and not of `--paths`, so they stand. A Grep for `git add vault` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/rules/rule-close.md`, `vault/wiki/estimates/estimate-close-commits.md` and `.claude/agents/librarian-guppi.md`: the two pages enter this Case, and the rendered agent file follows the render. A Grep for `librarian-guppi` over `.guppi/tests/` printed `test_grepguard.py`, which uses the name only as an agent type and does not read the file. `test_render.py` builds its vault under `tmp_path`. The last output of `guppi check` that the brief reports names no finding on these pages.

> **problem:**
> The close commit of the librarian names four fixed paths, and the render writes a file outside them, so that file stays uncommitted after the run.

> **recommend:**
> - **How should the close commit find the files the render wrote?**
>   - Recommended: (b) a command prints the files the render writes, and the commit adds `vault` and those files.
>   - Answer: agreed, (b).
> - **How is the fix checked?**
>   - Recommended: (a) replace the Criterion of `estimate-close-commits` whole.
>   - Answer: agreed, (a).

> **given:**
> `rule-close`: its Render sets the close commit of the librarian in `.claude/agents/librarian-guppi.md`.
> **＋** `estimate-close-commits`: its Criterion is replaced whole.
> **＋** `vault/`: the folder of the pages, which the commit takes whole.
> **＋** `.guppi/guppi/render.py`: `guppi render`, which gains the option `--paths`.
> **＋** `.guppi/tests/test_render.py`: the tests of the render.
> **＋** `rule-plugin-install`: renders `plugin/skills/install/SKILL.md`, outside `vault`, `CLAUDE.md`, `.claude` and `guppi.toml`.
> **＋** `rule-one-judgment-one-implementation`: the list of files comes from the code that writes them.
> **＋** `estimate-clean-branch-ships-neutral-texts`: a shipped sentence holds in any project.

> **when:**
> After a live run, the librarian commits at the close, as `.claude/agents/librarian-guppi.md` says, with the list that `uv run --project .guppi guppi render --paths` prints.

> **then:**
> `uv run --project .guppi guppi render --paths` prints each file that `guppi render` writes, one path per line, and writes nothing.
> **＋** `git log` shows one commit after the Retro commit, separate from the session's, with the message `docs(vault): librarian, <date>`, and never `--amend`.
> **＋** The commit takes `vault/` and each file of that list: `git add vault $(uv run --project .guppi guppi render --paths)`.
> **＋** After the commit, `git status` shows no file that `.guppi/guppi/render.py` wrote as modified or untracked.
> **＋** The report reaches the main agent with the counts, the flags and the lint total, in twenty lines or fewer.
> **－** The commit takes no path that neither `vault/` nor that list names.
> **－** In a project without `rule-plugin-install`, the list and the commit name no `plugin/skills/install/SKILL.md`.

> **tasks:**
> - [ ] update `rule-close`
>   - old: `` files the render wrote: `git add vault CLAUDE.md .claude guppi.toml && git commit -m "docs(vault): librarian, <date>"`, never `--amend`, never a path outside those four. After the commit, no file the render wrote stands untracked. ``
>   - new: `` files the render wrote: `git add vault $(uv run --project .guppi guppi render --paths) && git commit -m "docs(vault): librarian, <date>"`, never `--amend`, never a path that neither `vault` nor that list names. After the commit, no file the render wrote stands modified or untracked. ``
>   - change: `the commit takes vault and each file that guppi render --paths prints, in place of four fixed paths`
> - [ ] update `estimate-close-commits`
>   - set:
>     ```
>     status: pending
>     purpose: The librarian's run ends in one separate commit of vault and each file the render writes, with no rendered file left modified or untracked, and a report of twenty lines or fewer
>     method: "uv run --project .guppi pytest .guppi/tests/test_render.py -k paths; by hand, after the librarian's run of the next session, whose .claude/agents/librarian-guppi.md holds the new Render of rule-close: git log shows its commit and the paths it touched, git status shows no file the render wrote as modified or untracked, and the report is read in the transcript"
>     ```
>   - change: `the Criterion replaced whole — the commit takes vault and each file that guppi render --paths prints`
> - [ ] `.guppi/guppi/render.py`: the option `--paths`, in the group of `--check` and `--sync`, prints the keys of `plan`, one per line, writes nothing, ticks nothing and exits 0; a render error goes to stderr with exit 1 and prints no path; the docstring names the option and the close commit that reads it.
> - [ ] `.guppi/tests/test_render.py`: tests `paths` — a vault with a `full` and a `partial` page on two files prints each `governs` path once and writes nothing; a render error prints no path and exits 1.
> - [ ] `uv run --project .guppi guppi render`: `.claude/agents/librarian-guppi.md`
> - [ ] read `estimate-close-commits`

> **ratification:**
> ```
> - decision[case 857][update][rule-close]{ref:rule-close}
> - decision[case 857][update][estimate-close-commits]{ref:rule-close}
> ```
