## Case 859 — The starter session files open the sprint at the first /hi in a git repository

> **context:**
> `guppi ship` writes starter session files into the clean version of GUPPI in place of the session files of this repository: a closed sprint page, a backlog, a glossary, a brief that opens the next sprint and a log. With them, the first `/hi` of a new project starts `/sprint-open`. `estimate-clean-branch-writes-the-session-files` checks this. Its reading at the Retro of session 0104 passed every line but the last. In an empty folder with no git repository, the first `/hi` stopped on `fatal: not a git repository`. After `git init`, the next `/hi` started `/sprint-open` before the Frontier (its `## Result`). Since the render of session 0342, `/hi` in a folder with no git runs `uv run --project .guppi guppi gitstate`, asks whether to run `git init -b main`, and ends after either answer. Only the next `/hi` starts `/sprint-open` (the Render of `rule-git-context`, as set in case 851.1). So the last line of the Criterion, "the first `/hi` starts `/sprint-open`", cannot pass in a folder with no git, even when the starter files are right. Case 855 put the Estimate off until that render, which has run. The brief of session 0342 reports it under Flags: "Lint: `unread: failed` — `estimate-clean-branch-ships-neutral-texts`, `estimate-clean-branch-writes-the-session-files`."
>
> The person chose to replace the Criterion whole. Its last `Then` line now speaks of the first `/hi` whose `Branch:` line names a branch. A `－` line leaves the `/hi` that reads `none: this folder is no git repository` out of this promise. `estimate-git-context-offers-git-init` already checks that `/hi`, and that the next `/hi` starts `/sprint-open`. Nothing is signed twice (`rule-case-protocol`), so this Estimate does not repeat the git step. The `When` says that the person types `/hi` again after the git step where the folder has no git, so that the Criterion reads without the Case. Two lines change: the `＋` line of the `When` on the install and `/hi`, and the last `＋` line of the `Then` on the first `/hi`. The other lines keep their words. The `purpose` names the old promise, so it is set anew in the same `update`. The `method` is set anew too. Its hand reading waits for the librarian's run of this session, since the new Criterion lands on the page only then. The reading shares the copy and the empty folder with no git of the reading of `estimate-git-context-offers-git-init`. The third `/hi` of that reading is the first `/hi` in a git repository. Both readings belong to the install session that Frontier item C3 plans, after that run, and this Case does not take up C3. Keeping the Criterion and narrowing only the method was turned down: the words would still promise the first `/hi` in any empty project. Dropping the line was turned down too: this Estimate would no longer check that the starter files open a sprint.
>
> The person chose to take up the defer now. The decision line carries `{supersedes:case 855}` and names the Estimate, so `generate` retires the defer and `backlog.md` drops the Estimate at the next `guppi backlog`. The mark retires the one defer of `decision-case-855`, so the cascade archives that page after this Case. Case 858 of this session would have added an `updated:` History line to that page. The person took it back by the short Case 863, so no History line is added, and `decision-case-855` goes to the archive without a correction. It stays the record of what was true when the defer was signed.
>
> How it is checked: this Case replaces the Criterion of `estimate-clean-branch-writes-the-session-files`, which sets it `pending`.
>
> Searches. A Grep for `writes-the-session-files` over the repository outside `vault/raw/` and `vault/archive/` printed `vault/wiki/brief.md`, `vault/wiki/backlog.md`, `vault/wiki/log.md`, `vault/wiki/rules/rule-clean-branch.md` and `vault/wiki/estimates/estimate-clean-branch-writes-a-clean-copy.md`. The brief and the log are records. `guppi backlog` rewrites the backlog. The rule lists the Estimate in `estimates`, which stays true. The other Estimate points to this one for the files it writes in place of the session files, and that part does not change. A Grep for `writes-the-session-files` over `.guppi/tests/` printed nothing, so no test reads the page live. A Grep for ``first `?/hi`?`` over `vault/wiki/rules/` printed `rule-clean-branch.md`, `rule-git-context.md`, `rule-plugin-install.md` and `rule-morph.md`. The Purpose of `rule-clean-branch` says that the first `/hi` finds each file it loads, which holds in either folder. It says that `/hi`, not the first `/hi`, starts `/sprint-open`, so it stands. The `How it works` of `rule-git-context` tells the history of the git error and stands. `rule-plugin-install` says that the first `/hi` renders the harness, which this Case does not touch. `rule-morph` is `draft`, and its setup Case, which comes at the first `/hi` before the first sprint, is not built. Case 851 set the git step before it, and this Case does not change that order. `estimate-morph-sets-up-the-project-at-the-first-hi` (`pending`, target `rule-morph`) speaks of the same first `/hi`. Its `When` is the `/hi` typed after `/guppi:install` and a reopen. Its `Then` puts the setup Case first, then `/sprint-open` in the same session, and takes the name of the main branch from git. In a folder with no git, that `/hi` ends at the git step, so its Criterion has the same fault as the line this Case replaces. It stands in this Case for two reasons. Its `method` waits for the session whose Work Mode builds the setup skill of `rule-morph`, so no reading of it runs before that skill is built. Also, the Case that builds that skill writes the setup step and can set where it stands beside the git step. This Case changes no promise of `rule-morph`.

> **problem:**
> The last promise of `estimate-clean-branch-writes-the-session-files` says that the first `/hi` in an empty project starts `/sprint-open`. Since the git step of `/hi`, that `/hi` ends in a folder with no git, so the Estimate cannot pass there, and it stays failed and put off although the event its defer waited for has come.

> **recommend:**
> - **What should the last promise say about the first `/hi`?**
>   - Recommended: (a) the first `/hi` in a git repository: replace the Criterion whole, its last line on the first `/hi` whose `Branch:` line names a branch, with the purpose and the method written again to match.
>   - Answer: agreed, (a).
> - **Should the Estimate leave the backlog now?**
>   - Recommended: (a) take it up now: retire the defer, and run the reading in the same empty folder with no git as the reading of `estimate-git-context-offers-git-init`.
>   - Answer: agreed, (a). Before the answer, the main agent noted that the new Criterion lands on the page only at the librarian's run of this session, so the hand reading runs in the install session of item C3, after that run.

> **given:**
> `estimate-clean-branch-writes-the-session-files`: its Criterion is replaced whole, and the defer of `decision-case-855` is retired.
> **＋** `rule-clean-branch`: `guppi ship` writes the starter session files into the clean version.
> **＋** `vault/wiki/sprint.md`, `vault/wiki/backlog.md`, `vault/wiki/glossary.md`, `vault/wiki/brief.md` and `vault/wiki/log.md`: the starter session files, the first written by `closed_form` of `.guppi/guppi/sprint.py`.
> **＋** `/guppi:install`: the skill of the plugin that copies GUPPI into a project, as `rule-plugin-install` sets it.
> **＋** `rule-git-context`: the `Branch:` line of `/hi`, which runs `uv run --project .guppi guppi gitstate`, and the git step outside a repository.
> **＋** `estimate-git-context-offers-git-init`: checks the `/hi` in a folder with no git, and its reading shares the install.
> **＋** `rule-skill-sprint-open`: its hook on `/hi` asks for `/sprint-open` before the Frontier.

> **when:**
> `uv run --project .guppi guppi ship <folder>`, as `rule-clean-branch` sets it, builds the clean version of the project from its working tree into an empty folder.
> **＋** Or, in an empty project, the person installs the plugin `guppi` from such a copy, types `/guppi:install`, reopens Claude Code there and types `/hi`, and types `/hi` again after the git step of `rule-git-context` where the folder is no git repository.

> **then:**
> It writes `vault/wiki/sprint.md` as `closed_form` of `.guppi/guppi/sprint.py` writes it for the sprint `guppi`, so its first `## ` heading carries the mark of a closed sprint.
> **＋** It writes `vault/wiki/backlog.md` and `vault/wiki/glossary.md` as `guppi backlog` and `guppi glossary` write them over the clean version, by their own code.
> **＋** It writes a `vault/wiki/brief.md` whose `Cases` of its `## Next session` open with the line `open the next sprint — no sprint is open since the close of guppi`, and a `vault/wiki/log.md` that holds its heading and the paragraph under it alone.
> **＋** Over the clean version, `guppi sprint --check`, `guppi backlog --check` and `guppi glossary --check` print nothing and exit 0.
> **＋** In that project, the first `/hi` whose `Branch:` line, the output of `uv run --project .guppi guppi gitstate`, names a branch starts `/sprint-open` before the Frontier.
> **－** A `/hi` whose `Branch:` line reads `none: this folder is no git repository` is no part of this promise.
> **－** It writes no `sprint.md`, `backlog.md`, `brief.md`, `glossary.md` or `log.md` of the project it builds from.

> **tasks:**
> - [ ] update `estimate-clean-branch-writes-the-session-files`
>   - set:
>     ```
>     status: pending
>     purpose: Whether guppi ship writes sprint.md in the closed form of the sprint guppi, backlog.md and glossary.md by their writers, a brief.md that opens the next sprint and a log.md with its heading alone, so that the checks of those files pass and the first /hi of a new project in a git repository starts /sprint-open
>     method: "uv run --project .guppi pytest .guppi/tests/test_ship.py -k skeleton; by hand, after the librarian's run of the session that set this method, with a tag prod-x.y.z in the history of HEAD: in an empty folder that is no git repository, guppi installed from a copy that uv run --project .guppi guppi ship --allow-draft wrote into a local folder, the copy and the folder being those of the reading of estimate-git-context-offers-git-init where that reading runs at the same commit, /guppi:install typed, Claude Code reopened, /hi typed until its git step has run git init -b main, the next /hi typed, and guppi sprint --check, guppi backlog --check and guppi glossary --check run over the copy, read against the Criterion"
>     ```
>   - change: `the Criterion replaced whole — the first /hi whose Branch: line names a branch starts /sprint-open, and the /hi of the git step is no part of the promise; the defer of case 855 retired`
> - [ ] read `estimate-clean-branch-writes-the-session-files`

> **ratification:**
> ```
> - decision[case 859][update][estimate-clean-branch-writes-the-session-files]{ref:rule-clean-branch}{supersedes:case 855}
> ```
