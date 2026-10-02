## Case 593 — The Spec box: three sub-cases of case 591 re-issued under new ids

> **context:**
> Case 591 was ratified, then built again on the findings of `/pre-spec` and ratified again. When it was built again, three Estimates of its sub-cases got new slugs: `estimate-hi-takes-a-saved-plan` became `estimate-hi-takes-a-conserved-spec` (591.2), `estimate-spec-box-runs-a-saved-plan` became `estimate-spec-box-runs-a-conserved-spec` (591.5), and `estimate-spec-box-refuses-a-stale-plan` became `estimate-spec-box-refuses-a-stale-spec` (591.6). The ledger hook only appends, so the session's ledger still holds the three `create` lines of the first ratification under the old slugs. `guppi prespec --check` reports each of them as a line with no item in the plan, and it refuses the exit from Plan Mode. A ledger line is retired only by a `{supersedes:case N}` block, which retires every line of Case N and needs Case N out of the plan (`check_lines` and `superseded_in_window` of `guppi/prespec.py`). The person refused a hand edit of the ledger, and chose to re-issue the three sub-cases as this Case.
>
> 593.1, 593.2 and 593.3 hold the content of 591.2, 591.5 and 591.6 as last ratified, whole. Two things change. Each decision line carries `{supersedes:case 591.x}` of the sub-case it replaces. The `change` line of each `update` and `create` names `case 593.x`, since History will point to the Decision page of 593.x. The line on `rule-spec-box` keeps its `{supersedes:case 207}` … `{supersedes:case 565}` blocks, so the five defers of `rule-spec-box` are still retired. The new texts of the pages keep "case 591" where they cite the design, because 591 stays as the parent of the other sub-cases. The frame, the searches and the Estimates that stand are those of the `context` of 591, in `raw/2026-10-02/1202/cases/case-591.md`.
>
> No body of another sub-case of 591 names 591.2, 591.5 or 591.6:
> - 591.4 names `rule-spec-box` as the last child of `rule-end-of-work`, a page that 593.2 now gives its `parent`.
> - 591.3, 591.7, 591.8, 591.9, 591.10 and 591.12 name `/box`, `.claude/skills/box/SKILL.md`, `guppi/box.py` or `uv run guppi box --check`, which 593.2 and 593.3 now build.
>
> They name pages, files and skills, never a Case id, so none of them changes. Only the `context` of 591 names 591.5 as the sub-case that sets the `parent`. It is a story section, the Spec keeps it as ratified, and 593.2 now sets that field.
>
> 593.1 and 593.3 share one condition, a session with no decision line of its own but a `defer`. They state it from two sides: the agent's text at the Frontier, and the refusal of the check.

> **problem:**
> Three `create` lines of the first ratification of 591 stand in the ledger under slugs that the Case built again no longer carries, and they block the exit from Plan Mode. The ratified content of 591.2, 591.5 and 591.6 must stand under Case ids whose lines retire the old ones.

> **recommend:**
> - **What happens to the page `rule-spec-box`**
>   - Recommended: (a) archive the page and keep the idea as a note in the sprint page's backlog list.
>   - Answer: (c), build it now. The person described a branch made at once for each saved Spec, which they enter to build it, or leave while work goes on in the shared branch. They said the documentation must be settled first, since merging branches brings conflicts, and asked for a proposal.
> - **Is the broken code fence of `decision-case-13` fixed in this Case**
>   - Recommended: (a) fix it here, as a sub-case.
>   - Answer: (a), agreed.
> - **When the branch of a saved plan is made, and what it is**
>   - Recommended: (a) a plain branch made by `/carry` from the commit that saves the plan; the session stays on the shared branch.
>   - Answer: (a), with one correction: the branch is made from the commit after the whole of `/carry` is done, the brief written and the rest.
> - **How the documentation stays free of merge conflicts**
>   - Recommended: (a) only the shared branch writes the vault. Before the work, the plan's branch takes in the shared branch, pre-spec checks the plan against today's pages, and only a Case on a page whose History has a line after the save is built again and ratified again.
>   - Answer: (a). The person first wrote "4) b", then said the numbers were mixed up and confirmed (a).
> - **Where taking up a saved plan starts**
>   - Recommended: (b) from Plan Mode at any point; the session's own Cases are saved by `/carry` with their branch, then the box runs the saved plan.
>   - Answer: (b), after the person asked whether this is all one session — `/carry`, then the box.
> - **Ordinary work and a saved plan at the same time**
>   - Recommended: (a) take turns: one session at a time, on one branch at a time.
>   - Answer: (a).
> - **Who merges the plan's branch back, and when**
>   - Recommended: (a) the box skill merges at its end, after `/handoff`, runs `make test`, and the librarian runs on the shared branch; on a conflict in code it stops and asks.
>   - Answer: (a). The person asked whether the box is in essence ordinary Work Mode with git branches.
> - **Is the box a new skill around `/work`, or `/work` itself**
>   - Recommended: (a) a new skill that does the branch steps and calls `/work` with the saved plan's folder.
>   - Answer: (a), agreed.
> - **Where a Case of the saved plan built again is written**
>   - Recommended: (a) into the saved plan's folder, its file and its ledger, by the two hooks taught to write there.
>   - Answer: (a), agreed.
> - **How much of this is built in this session**
>   - Recommended: (b) a first part now — the branch made by `/carry`, the box skill, the merge back and the fence fix. The check against changed pages (Q4, Q9) is put off as a backlog item, and until then the box refuses a saved plan whose pages changed after the save.
>   - Answer: (b), agreed.
> - **Where the box writes its records when this session's own Cases were saved**
>   - Recommended: (b) for now, the box runs only in a session with no Cases of its own. Its records go into the session's own folder, and Q5 (b) comes with the later part.
>   - Answer: (b), agreed.
> - **Change**
>   - Asked: the person refused a hand edit of the ledger and agreed to re-issue 591.2, 591.5 and 591.6 as a new Case. Each of its decision lines supersedes the sub-case it replaces, with the same content; the line of `rule-spec-box` keeps its five blocks of the defers; the other sub-cases of 591 stay.
>   - Taken: Case 593 with 593.1, 593.2 and 593.3, the content of 591.2, 591.5 and 591.6 whole. Each decision line carries `{supersedes:case 591.x}`, and the `change` lines name `case 593.x`.

### Case 593.1 — A conserved Spec is taken whole at the Frontier

> **given:**
> `rule-skill-hi` — the rule of `/hi`; its Render is the skill that assembles the Frontier
> **＋** `.claude/skills/hi/SKILL.md` — the skill, rendered in full from `rule-skill-hi`
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the Frontier and its closers
> **＋** `vault/wiki/backlog.md` — the list that names each conserved Spec and its `spec.md`
> **＋** `guppi/ratified.py` — the guard that lets the plan file be created with one title line only
> **＋** `# Session <hi HHMM> — runs the conserved Spec vault/raw/<date>/<HHMM>/spec.md` — the title line of the plan file of a box session
> **＋** `/box` — the skill that runs the conserved Spec
> **＋** `/pre-spec` — the check that closes Plan Mode
> **＋** `estimate-hi-takes-a-conserved-spec` — the new promise

> **when:**
> In a session that `/hi` opened from `.claude/skills/hi/SKILL.md` as rendered from `rule-skill-hi`, the person takes a conserved Spec of `## Cases` of `raw/<date>/<hi HHMM>/frontier.md`.

> **then:**
> The agent takes the Spec whole, to be run by `/box`, only while the session's ledger holds no decision line other than a `defer`, and after it ratifies no Case but a short-form defer.
> **＋** It closes the line of that Spec `[x] … · work`.
> **＋** It creates the plan file with one title line, `# Session <hi HHMM> — runs the conserved Spec vault/raw/<date>/<HHMM>/spec.md`, the path that `vault/wiki/backlog.md` names for that Spec.
> **＋** It closes each other open line under `## Cases` as left — `[-] … · backlog · kept`, `[-] … · sprint · defer` or `[-] … · defer case N` — and goes on to `/pre-spec`.
> **－** No Case of the conserved Spec is built again or ratified again in this session.
> **－** `.claude/skills/hi/SKILL.md` equals the Render of `rule-skill-hi` and is not edited by hand.

> **tasks:**
> - [ ] update `rule-skill-hi`
>   - old: `` Wait for the human to pick the order or defer items. Every Case is built by `case-guppi` (`rule-case-build`). ``
>   - new: `` Wait for the human to pick the order or defer items. Every Case is built by `case-guppi` (`rule-case-build`). A conserved Spec on `## Cases` is taken whole and run by `/box` (`rule-spec-box`, case 591): take it only while the session's ledger holds no decision line other than a `defer`, and ratify no Case after it but a short-form defer; close its line `[x] … · work`; create the plan file with one title line, `# Session <hi HHMM> — runs the conserved Spec vault/raw/<date>/<HHMM>/spec.md`, the path `backlog.md` names; close the other open lines under `## Cases` as left, and go on to `/pre-spec`. ``
>   - change: `a conserved Spec is taken whole at the Frontier, named in the title line of the plan file, and run by /box (case 593.1)`
> - [ ] create `estimate-hi-takes-a-conserved-spec`
>   - ref: `rule-skill-hi`
>   - kind: `QA`
>   - purpose: `Whether a session takes a conserved Spec of the Frontier whole — only with no decision line of its own but a defer, its line closed, the plan file created with a title line that names the conserved spec.md, the other lines closed as left`
>   - method: `uv run guppi render --check; by hand, at the first session whose person takes a conserved Spec at the Frontier: frontier.md, the title line of the plan file and the session's ledger read against the Criterion`
>   - tags: `[session, workflow, harness]`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] read `estimate-hi-takes-a-conserved-spec` — by hand, at the first session that takes a conserved Spec at the Frontier

> **ratification:**
> ```
> - decision[case 593.1][update][rule-skill-hi]{ref:rule-skill-hi}{supersedes:case 591.2}
> - decision[case 593.1][create][estimate-hi-takes-a-conserved-spec]{ref:rule-skill-hi}{tags:session,workflow,harness}{supersedes:case 591.2}
> ```

### Case 593.2 — /box runs a conserved Spec on its branch and merges it back

> **given:**
> `rule-spec-box` — the placeholder, built as the rule of `/box`; its Render is the skill
> **＋** `.claude/skills/box/SKILL.md` — the skill, rendered in full from `rule-spec-box`
> **＋** `rule-end-of-work` — the parent of `rule-spec-box`
> **＋** `vault/raw/<date>/<HHMM>/` — the folder of the conserved Spec, the argument of the skill
> **＋** `spec/<date>-<HHMM>` — the branch of the conserved Spec, made by `/carry`
> **＋** `rule-spec-capture` — the hook whose line after `ExitPlanMode` calls the skill
> **＋** `git switch`, `git merge --ff-only` and `git branch -d` — the branch steps of the skill
> **＋** `uv run guppi box --check` — the check the skill runs first
> **＋** `/work`, `/retro` and `/handoff` — the skills of the run the box calls
> **＋** `librarian-guppi` — the librarian, dispatched by the skill on the shared branch
> **＋** `vault/wiki/` — the pages, which the branch of the Spec does not write
> **＋** `entity-sprint-migration` — its Backlog line on `rule-spec-box`
> **＋** `estimate-spec-box-runs-a-conserved-spec` — the new promise

> **when:**
> The agent calls `/box` on `PreToolUse Skill` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec, on the line that the hook of `rule-spec-capture` printed after `ExitPlanMode`, and runs `.claude/skills/box/SKILL.md` as rendered from `rule-spec-box`.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/box/SKILL.md` equals the Render of `rule-spec-box`.
> **＋** The agent first runs `uv run guppi box --check` on the folder; when it prints a line, the agent changes nothing, shows the lines and asks the person.
> **＋** Otherwise the agent commits the tree, runs `git switch` to `spec/<date>-<HHMM>`, and brings that branch up to the branch it came from by `git merge --ff-only`; when the merge refuses, it switches back, shows the refusal and asks the person.
> **＋** It calls `/work` with the folder, and Work Mode, the Work readings, `/retro` and `/handoff` run in one turn.
> **＋** After `handoff.md` stands, it switches back, brings the branch it came from up to `spec/<date>-<HHMM>` by `git merge --ff-only`, deletes `spec/<date>-<HHMM>` by `git branch -d` and runs `make test`; a merge that refuses is a stop.
> **＋** Then it dispatches `librarian-guppi` with the path of the session's `handoff.md`, and shows the librarian's report unchanged with the exit code of `make test`.
> **－** Nothing under `vault/wiki/` is written on `spec/<date>-<HHMM>`, and the librarian runs once, on the branch the session came from.
> **－** No commit follows the handoff but the librarian's own.

> **tasks:**
> - [ ] update `rule-spec-box`
>   - set: `{kind: Leaf, enforcement: render, governs: .claude/skills/box/SKILL.md, render_mode: full, implementation_ref: [guppi/box.py, tests/test_box.py], parent: "[[rule-end-of-work]]", tags: [session, workflow, git, harness, render], purpose: "Prevents a conserved Spec from being built on a branch that lacks the current vault, or its pages from being written anywhere but on the shared branch"}`
>   - sections.Purpose:
>     ```
>     Prevents a conserved Spec from being built on a branch that lacks the current vault, and its pages from being written anywhere but on the shared branch. `/carry` conserves a Spec whose work is not done and makes its branch `spec/<date>-<HHMM>` at the commit that conserves it. A later session takes the Spec at the Frontier, and `/box` runs it: it checks the Spec, switches to its branch, brings that branch up to the shared branch by a fast-forward, runs `/work` on the Spec, and after `/handoff` brings the shared branch up to the Spec's branch by a fast-forward and hands the session to the librarian there. One session runs at a time, in one folder of the repository, so both merges are fast-forwards and the vault has one writer; the shared branch is never `main`. The check refuses a Spec whose pages changed after it was conserved, and a session that ratified a Case of its own: in this first part a Case of the Spec is not checked again or built again, and the readings, lessons and handoff of the session go into the session's own folder, which the librarian applies. Both wait for a second part, a line of the Backlog of `entity-sprint-migration` (case 591).
>     ```
>   - sections.Render:
>     ```
>     <!-- rule-spec-box -->
>     ---
>     name: box
>     description: Run a conserved Spec on its own branch — check it, switch to the branch and bring it up to date, run /work on it, merge the branch back and hand the session to the librarian. The agent calls it on the line that the hook of rule-spec-capture prints after ExitPlanMode.
>     ---
>
>
>     @vault/wiki/where-to-stop.md
>
>     Branch: !`git branch --show-current`
>
>     The argument is the folder of a conserved Spec, `vault/raw/<date>/<HHMM>/`, which the line printed after `ExitPlanMode` names. The branch above is the shared branch: the session leaves it here and comes back to it at the end. The branch of the Spec is `spec/<date>-<HHMM>`, the date and time of that folder, made by `/carry`. Nothing under `vault/wiki/` is written on the branch of the Spec: the librarian writes the pages once, on the shared branch.
>
>     1. Run `uv run guppi box --check <folder> --session <id>`, the id being the eight characters of the `hi:` line of this session. Each line it prints is a reason the Spec cannot run now. When it prints one, change nothing: show the lines and ask the person.
>     2. Commit the tree: `chore(session): session <hi HHMM> takes the conserved Spec of <folder>`.
>     3. Run `git switch spec/<date>-<HHMM>`, then `git merge --ff-only <shared branch>`. When the merge refuses, run `git switch <shared branch>`, show the refusal and ask the person.
>     4. Call `/work` with the folder as its argument. Work Mode, the Work readings, `/retro` and `/handoff` run as their skills say, in one turn; `/handoff` dispatches nothing and comes back here.
>     5. Run `git switch <shared branch>`, then `git merge --ff-only spec/<date>-<HHMM>`. When the merge refuses, show the refusal and ask the person. Then run `git branch -d spec/<date>-<HHMM>` and `make test`.
>     6. Dispatch the `librarian-guppi` agent with one line: `Materialize <hi date> from vault/raw/<hi date>/<hi HHMM>/handoff.md.`. Wait for its report and show it to the person unchanged, then one line with the exit code of `make test`. Do not commit after this, and write no `LEDGER` block.
>
>     The stops of steps 1, 3 and 5 are condition 6 of `vault/wiki/where-to-stop.md`.
>     <!-- /rule-spec-box -->
>     ```
>   - change: `built from the placeholder: /box runs a conserved Spec on its branch and merges it back before the librarian, first part; a child of rule-end-of-work (case 593.2)`
> - [ ] update `entity-sprint-migration`
>   - old: `- [[rule-spec-box]] — the Spec box, case 207, after Slice 3b`
>   - new: `- [[rule-spec-box]] — the Spec box, its second part: a conserved Spec checked against the pages changed after it was conserved, a Case on such a page built again, ratified again and written into the folder of the conserved Spec, and a conserved Spec taken after other Cases of its session (case 591)`
>   - change: `the Backlog line of rule-spec-box names its second part (case 593.2)`
> - [ ] create `estimate-spec-box-runs-a-conserved-spec`
>   - ref: `rule-spec-box`
>   - kind: `QA`
>   - purpose: `Whether /box checks a conserved Spec, runs it on its own branch brought up to the shared branch by a fast-forward, merges the branch back by a fast-forward after the handoff, and has the librarian write the pages on the shared branch, stopping when the check or a merge refuses`
>   - method: `uv run guppi render --check; by hand, the first session that takes a conserved Spec at the Frontier and runs it by /box: git log, the branches, the folders of the session and of the conserved Spec, the dispatch line and the librarian's commit, recorded in the estimate line`
>   - tags: `[session, workflow, git, harness]`
> - [ ] `uv run guppi render`: `.claude/skills/box/SKILL.md`
> - [ ] read `estimate-spec-box-runs-a-conserved-spec` — by hand, at the first session that runs a conserved Spec by `/box`

> **ratification:**
> ```
> - decision[case 593.2][update][rule-spec-box]{ref:rule-spec-box}{supersedes:case 207}{supersedes:case 219}{supersedes:case 232}{supersedes:case 532}{supersedes:case 565}{supersedes:case 591.5}
> - decision[case 593.2][update][entity-sprint-migration]{ref:entity-sprint-migration}{supersedes:case 591.5}
> - decision[case 593.2][create][estimate-spec-box-runs-a-conserved-spec]{ref:rule-spec-box}{tags:session,workflow,git,harness}{supersedes:case 591.5}
> ```

### Case 593.3 — guppi box --check refuses a conserved Spec that cannot run now

> **given:**
> `guppi/box.py` — the check of a conserved Spec
> **＋** `guppi/cli.py` — the table of the `guppi` commands
> **＋** `guppi/materialize.py` — `is_carried_over`, the one judgment of a folder marked by `carry.md`
> **＋** `tests/test_box.py` — the tests of the check
> **＋** `vault/raw/<date>/<HHMM>/spec.md` — the conserved Spec, its `then` blocks and its Case headings
> **＋** `vault/raw/<hi date>/<hi HHMM>/ledger.md` — the ledger of the session that runs the check
> **＋** `spec/<date>-<HHMM>` — the branch of the conserved Spec, made by `/carry`
> **＋** `main` — the branch that is never the shared branch
> **＋** `estimate-spec-box-refuses-a-stale-spec` — the new promise

> **when:**
> Someone runs `uv run guppi box --check <folder> --session <id>`, where `<folder>` is a folder `vault/raw/<date>/<HHMM>/` and `<id>` is the session id of a `hi` line.

> **then:**
> It prints one line for each reason the Spec cannot run now, and exits 1 when it prints any; with no reason it prints nothing and exits 0.
> **＋** A folder that `is_carried_over` of `guppi/materialize.py` does not judge marked is one reason, and so is a folder for which no branch `spec/<date>-<HHMM>` exists.
> **＋** A current branch `main` is one reason: the shared branch is never `main`.
> **＋** A decision line other than a `defer` in the ledger of the session's folder is one reason, naming its Case.
> **＋** A live page named by an `update`, `delete` or `defer` item of the folder's `spec.md` is one reason when a line of its History names the Decision page of a Case whose number, in its whole part, is higher than that of every Case of that Spec; the line names the page and that Decision page.
> **＋** A slug that a `create` item of that Spec names and a live page carries is one reason, naming the slug.
> **－** The check writes nothing, switches no branch, and opens no page beyond those the Spec names.

> **tasks:**
> - [ ] `guppi/box.py` — `check(project_dir, folder, session)` and `run`, by the `then` above; the folder judged by `is_carried_over` of `guppi/materialize.py`, the branches by `git branch --show-current` and `git branch --list`, the ledger window of the session the way `guppi prespec --check` finds it, the items by the parser of the `then` blocks that `guppi materialize` uses; the module docstring names `rule-spec-box`
> - [ ] `guppi/cli.py` — the command `box`
> - [ ] `tests/test_box.py` — each reason alone and its line; a clean folder, exit 0 and no output; a `defer` line of the session not counted; a History line of a Case of the Spec itself, and a `cascade` line, not counted
> - [ ] create `estimate-spec-box-refuses-a-stale-spec`
>   - ref: `rule-spec-box`
>   - kind: `QA`
>   - purpose: `Whether guppi box --check refuses a conserved Spec whose folder lacks carry.md or its branch, a run from main, a session that ratified a Case of its own, a page of the Spec changed by a later Case, and a page the Spec creates that now stands — and passes any other`
>   - method: `uv run pytest tests/test_box.py`
>   - tags: `[session, workflow, git, harness]`
> - [ ] read `estimate-spec-box-refuses-a-stale-spec` — `uv run pytest tests/test_box.py`, in a later session

> **ratification:**
> ```
> - decision[case 593.3][create][estimate-spec-box-refuses-a-stale-spec]{ref:rule-spec-box}{tags:session,workflow,git,harness}{supersedes:case 591.6}
> ```
