## Case 591 — The Spec box: a conserved Spec runs on its own branch, first part

> **context:**
> `rule-spec-box` held one idea, put off in five sessions: a session that runs a conserved Spec on a branch of its own. A defer copied `tags` onto the page. Lint therefore does not judge it a placeholder, and it prints three findings on it: missing `kind`, missing `estimates`, and orphan. These findings keep `estimate-sprint-migration-lint-clean` red. The defer of case 532 also names the missing parent. In the rounds the person chose to build the box now (Q1), and to build it in a first part (Q10).
>
> Today `/carry` conserves a Spec: it writes `carry.md`, rewrites the brief, runs `guppi backlog` and commits. The librarian passes the folder by while `carry.md` stands, and `/hi` lists each conserved Spec first under `## Cases`. But no skill runs a conserved Spec, and no branch holds one. The defer of case 540 on `rule-work-mode` names the same gap: `/work` does not say which `spec.md` it runs, where it ticks the boxes, or when it deletes `carry.md`.
>
> After this Case, `/carry` makes the branch `spec/<date>-<HHMM>` at its commit (Q3). A later session takes the conserved Spec at the Frontier, but only while it has ratified no Case of its own (Q11). The title line of its plan file names the conserved `spec.md`, and the hook of `rule-spec-capture` then prints a line that leads to `/box` in place of the fork. `/box` does these steps:
> - it checks the Spec and commits;
> - it switches to the Spec's branch and brings it up to the shared branch by a fast-forward;
> - it calls `/work` with the folder (Q8);
> - after `/handoff`, it fast-forwards the shared branch to the Spec's branch and deletes that branch;
> - it runs `make test` and dispatches the librarian there (Q7).
>
> Nothing under `vault/wiki/` is written on the branch (Q4). One session runs at a time (Q6), so both merges are fast-forwards. They refuse only when the other branch holds a commit of its own, and that refusal is a stop. `/box` loads `vault/wiki/where-to-stop.md` as `/work` does. Its check refuses `main` as the shared branch.
>
> The check also refuses a Spec when a page it changes has a History line that names a decision of a later Case, or when a page it creates now stands. Two things are the second part, a line of the Backlog of `entity-sprint-migration` (Q10, Q11): checking such a Case again and building it again (Q4, Q9), and taking a conserved Spec after other Cases of the session (Q5).
>
> Q8 put the baseline of `/work` into the Spec's folder. Q11 then put every record of the session into the session's own folder: the baseline, the readings, the lessons and the handoff. The Case follows Q11. `/work` ticks the conserved `spec.md`, deletes its `carry.md`, and names the folder under `## Conserved Spec` of `work.md`. That section is the one signal of a box session for `/work`, `/retro` and `/handoff`.
>
> `/work` and `/retro` count the decision lines of the conserved Spec as this session's: for the boxes, for the scope of an edit and for the readings, since this session builds that Spec. The ledger hook sees only this session's lines, so the text is the guard. `/handoff` dispatches nothing in a box session, and `vault/wiki/where-to-stop.md` gets the stops of `/box`. Sub-case 591.7 carries `{supersedes:case 540}`, since it answers that defer. Sub-case 591.11 closes the code fence of `decision-case-13`, which the defer of case 565 tied to this item (Q2).
>
> `rule-spec-box` becomes a child of `rule-end-of-work`, after `rule-retro-onward`, which answers the missing parent of case 532. `generate` writes a parent's `children` only on a `create`, so 591.4 sets the list on `rule-end-of-work` beside the `parent` that 591.5 sets.
>
> In the frame, the guard of `guppi/ratified.py` lets the agent create the plan file only with one line that opens with `# `. So the conserved Spec is named in that title line. `guppi gate` refuses `/retro` in a session with no `spec.md` and no record line. The hook of `rule-spec-capture` copies the title line into the session's `spec.md`, so that file stands. `.gitignore` keeps `vault/raw/*/event_log.md` out of git, and `/box` commits the tree before each switch, so the writes of the hooks do not block a switch. No hook registration in `.claude/settings.json` changes. `guppi spec` prints and refuses nothing, and no reader refuses a text it reads, so no old form is kept.
>
> After the librarian's run, `rule-spec-box` carries `kind`, `estimates`, `tags` and `parent`, and its Estimates name it in `target`. Its three findings go, and its new Estimates print `unread` lines by design. The pre-spec finding on this Spec says that 589.1 and 590.1 delete two of the seven placeholders that print `deferred` lines. The other five still keep `estimate-sprint-migration-lint-clean` red, so its Criterion stands. Every `create` carries a `ref`, so the vault query for a `create` without a `ref` did not run. A Glob of `vault/**/estimate-{spec-box,hi-takes}*` printed only `estimate-hi-takes-its-readings`, so the three new slugs are free.
>
> These searches were run:
> - The pattern `/carry` over `vault/wiki/rules/` printed `rule-brief`, `rule-case-protocol`, `rule-session`, `rule-permissions`, `rule-spec-capture`, `rule-carry-over` and `rule-end-of-work`. Over `.claude/` it printed `.claude/settings.json` (its `carry.md` allow line) and `.claude/skills/carry/SKILL.md`. Over `vault/wiki/estimates/` it printed `estimate-brief-written`, `estimate-case-protocol-asks-in-the-grill-me-shape`, `estimate-case-protocol-puts-the-harness-before-plan-mode`, `estimate-session-phases-in-order`, `estimate-carry-over-writes`, `estimate-end-of-work-order` and `estimate-spec-capture-offers-the-fork`.
> - The pattern `ExitPlanMode` over `vault/wiki/rules/` printed `rule-ledger-write`, `rule-case-protocol`, `rule-session`, `rule-prespec-hook`, `rule-hook-registry`, `rule-spec-capture`, `rule-carry-over` and `rule-work-mode`. Over `.claude/` it printed `.claude/skills/work/SKILL.md`, `.claude/settings.json` and `.claude/skills/carry/SKILL.md`.
> - The pattern `librarian-guppi` over `vault/wiki/rules/` printed `rule-documentation`, `rule-brief`, `rule-synthesis`, `rule-carry-over`, `rule-handoff`, `rule-index-check` and `rule-close`. The pattern `librarian-guppi|Materialize` over `.claude/` printed `.claude/skills/handoff/SKILL.md`, `.claude/agents/librarian-guppi.md` and `.claude/skills/carry/SKILL.md`.
> - The pattern `work\.md` over `guppi/` printed nothing.
> - The pattern `spec-box` over `vault/wiki/` printed `entity-sprint-migration`, `brief.md`, `backlog.md`, `log.md`, the Decision pages of cases 207, 219, 232, 244, 305.1–305.5, 367, 428.1–428.4, 465, 478.1, 478.2, 479.1–479.5, 532 and 565, and the Result sections of `estimate-rules-schema-checked` and `estimate-retro-red-in-the-baseline-is-not-charged`.
>
> Outside History, `log.md` and `brief.md`, the sentences made false are these: the pair in `rule-end-of-work` on the question asked when leaving Plan Mode; the Purpose of `rule-spec-capture`; the import sentence of `rule-where-to-stop`; and the Backlog line of `entity-sprint-migration`. Each enters a sub-case. The choice between `/work` and `/carry` in `rule-case-protocol` and its two Estimates holds wherever that choice is asked; a box session asks none.
>
> These Estimates stand:
> - `estimate-session-phases-in-order`: the marks still rise in time, and the commit of `/box` sits between `spec.md` and the Retro commit.
> - `estimate-hi-writes-frontier`: the line of a conserved Spec and the closers do not change.
> - `estimate-spec-capture-appends`: the copy of the plan does not change.
> - `estimate-retro-runs-on-to-the-handoff`: the hook of `rule-retro-onward` does not change.
> - `estimate-lint-checks-the-statuses`: the placeholder judgment does not change.
> - `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note`: it speaks of the Spec of the session and the pages that Spec updates. 591.8 makes the conserved Spec that Spec in a box session, and each line of its Criterion stays true of it.

> **problem:**
> The placeholder `rule-spec-box` keeps `make lint` red, and the person chose to build the Spec box rather than archive it. The questions were: how a conserved Spec runs on a branch of its own without the vault conflicting at the merge, how a session takes it up, and how much of that is built now.

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

### Case 591.1 — /carry makes the branch of the Spec after its commit

> **given:**
> `rule-carry-over` — the rule of `/carry`; its Render is the skill
> **＋** `.claude/skills/carry/SKILL.md` — the skill, rendered in full from `rule-carry-over`
> **＋** `raw/<hi date>/<hi HHMM>/frontier.md` — the open lines that Next session takes
> **＋** `vault/wiki/brief.md` — the brief that `/carry` rewrites
> **＋** `vault/wiki/backlog.md` — the backlog that `guppi backlog` writes
> **＋** `vault/wiki/sprint.md` — the sprint file, through which a sprint item reaches `/hi`
> **＋** `/hi` — the start of the next session, which reads the brief
> **＋** `vault/raw/` — the session folders that `/carry` commits
> **＋** `git branch spec/<hi date>-<hi HHMM>` — the command that makes the branch of the Spec
> **＋** `/retro` and `/handoff` — the end skills that `/carry` does not run
> **＋** `vault/wiki/` — the pages, which `/carry` does not write
> **＋** `rule-spec-box` — the box that runs the Spec from its branch
> **＋** `estimate-carry-over-writes` — its Criterion replaced whole

> **when:**
> The agent calls the skill `/carry` on `PreToolUse Skill`, after the person answered "conserve" at the fork `ExitPlanMode` prints. The person never types it.

> **then:**
> The skill reads the tree. When the tree holds changes outside the session folder and `vault/wiki/brief.md`, the skill stops and says that work was done and the ordinary exit applies.
> **＋** Otherwise it rewrites `vault/wiki/brief.md` in the short shape, with no Deferred list.
> **＋** The short shape holds Where things stand, Flags and Next session, with no Readings due and no Readings at the close.
> **＋** Next session holds `Cases`, `Work` and `Ask the person`, one line per item, a list with no item the line "none": `Cases` is always the line "none", since a deferred decision reaches `/hi` through `vault/wiki/backlog.md` and a sprint item through `vault/wiki/sprint.md`; `Work` holds each open `W` line of `raw/<hi date>/<hi HHMM>/frontier.md`, and `Ask the person` each open `A` line with its Estimate by slug, the mark `needs the person` and its question.
> **＋** It puts `carry.md` into the session folder: one line, a flag for `materialize` and `guppi backlog`, not a document. The session that finishes the work deletes it.
> **＋** It runs `uv run guppi backlog`, and `vault/wiki/backlog.md` then shows the conserved Spec with its targets.
> **＋** It runs `make style` and commits `vault/raw/`, `vault/wiki/brief.md` and `vault/wiki/backlog.md`.
> **＋** After that commit it runs `git branch spec/<hi date>-<hi HHMM>`, so the branch of the Spec points at the commit that holds the whole of `/carry`.
> **－** No open `W` or `A` line of `frontier.md` is left out of Next session, so the next `/hi` takes each one into its Frontier.
> **－** It runs no Work Mode, `/retro`, `/handoff`, librarian, `materialize`, `generate`, `cleanup` or `render`, and it writes no decision. It writes no page of `vault/wiki/`.
> **－** It switches to no branch: the session stays on the branch it ran on.
> **－** The work stays sequential, session after session: one conserved Spec, no parallel work.
> **－** `.claude/skills/carry/SKILL.md` equals the Render of the page and is not edited by hand.

> **tasks:**
> - [ ] update `rule-carry-over`
>   - old: `` description: Conserve a ratified Spec whose work is not done — rewrite the brief, mark the session folder, run `guppi backlog`, commit; run nothing else. ``
>   - new: `` description: Conserve a ratified Spec whose work is not done — rewrite the brief, mark the session folder, run `guppi backlog`, commit, make the branch of the Spec; run nothing else. ``
>   - old: `` `docs(vault): Spec of session <HHMM> conserved, Cases <N>–<M>`. ``
>   - new:
>     ```
>     `docs(vault): Spec of session <HHMM> conserved, Cases <N>–<M>`.
>     4. Make the branch of the Spec at that commit: `git branch spec/<hi date>-<hi HHMM>`. Stay on the current branch: the Spec waits on its branch until a later session takes it at the Frontier and `/box` runs it (`rule-spec-box`, case 591).
>     ```
>   - change: `/carry makes the branch spec/<hi date>-<hi HHMM> at its commit and stays on the current branch (case 591.1)`
> - [ ] update `estimate-carry-over-writes`
>   - set: `{status: pending, purpose: "/carry writes the brief and the mark, runs guppi backlog, commits, makes the branch of the Spec at that commit, and runs nothing else", method: "uv run guppi render --check; by hand, the first /carry after the fork of ExitPlanMode — the tree, vault/wiki/brief.md, carry.md, vault/wiki/backlog.md, the commit and git branch read"}`
>   - change: `the Criterion replaced whole — /carry makes the branch of the Spec after its commit (case 591.1)`
> - [ ] `uv run guppi render`: `.claude/skills/carry/SKILL.md`
> - [ ] read `estimate-carry-over-writes` — by hand, at the first `/carry` of a later session

> **ratification:**
> ```
> - decision[case 591.1][update][rule-carry-over]{ref:rule-carry-over}
> - decision[case 591.1][update][estimate-carry-over-writes]{ref:rule-carry-over}
> ```

### Case 591.2 — A conserved Spec is taken whole at the Frontier

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
>   - change: `a conserved Spec is taken whole at the Frontier, named in the title line of the plan file, and run by /box (case 591.2)`
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
> - decision[case 591.2][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 591.2][create][estimate-hi-takes-a-conserved-spec]{ref:rule-skill-hi}{tags:session,workflow,harness}
> ```

### Case 591.3 — After ExitPlanMode the hook leads a box session to /box

> **given:**
> `rule-spec-capture` — the rule of the hook `guppi spec` on `PostToolUse ExitPlanMode`; its Purpose, on the fork
> **＋** `guppi/spec.py` — the hook that copies the plan and prints the line
> **＋** `raw/<hi date>/<hi HHMM>/spec.md` — the Spec of the session, which the hook writes
> **＋** `vault/raw/` — the session folders, among them the folders of conserved Specs
> **＋** `/hi` — opens the session; without its `hi` line the hook writes no Spec
> **＋** `vault/wiki/case-schema.md` — a Case is ratified by the person's reply, never by a picker tool
> **＋** `guppi/box.py` — the module of `/box`; it holds the judgment whether a plan names a conserved Spec
> **＋** `guppi/materialize.py` — `is_carried_over`, the one judgment of a folder marked by `carry.md`
> **＋** `tests/test_spec.py` — the tests of the printed line
> **＋** `.claude/skills/box/SKILL.md`, `.claude/skills/work/SKILL.md` and `.claude/skills/carry/SKILL.md` — the skills the line names
> **＋** `estimate-spec-capture-appends` — the copy of the plan, which stands
> **＋** `estimate-spec-capture-offers-the-fork` — its Criterion replaced whole

> **when:**
> `guppi spec` has run on `PostToolUse` of `ExitPlanMode` and written the Spec, or found it already there.

> **then:**
> The stdout of the hook is one JSON object, `hookSpecificOutput` with `hookEventName: PostToolUse` and `additionalContext`, that holds one line with the session folder and the Spec file `raw/<hi date>/<hi HHMM>/spec.md`.
> **＋** For `PostToolUse` Claude Code adds to the agent's context only `hookSpecificOutput.additionalContext` from a JSON object on stdout; plain stdout with exit 0 goes to the debug log.
> **＋** The agent sees this line in the `ExitPlanMode` result.
> **＋** When the approved plan names the `spec.md` of a folder under `vault/raw/` that `is_carried_over` of `guppi/materialize.py` judges marked by `carry.md`, the line names that folder and tells the agent to call `.claude/skills/box/SKILL.md` with it, and to ask the person nothing.
> **＋** For any other plan the line is the fork. The fork line tells the agent to ask the person by `AskUserQuestion` with two options, `/work` (Work Mode on the Spec now) and `/carry` (the Spec conserved for a later session), and to start nothing until the person answers.
> **＋** On the answer, the agent calls `.claude/skills/work/SKILL.md` or `.claude/skills/carry/SKILL.md`, the skill of the option picked.
> **－** A `PostToolUse` hook blocks nothing: the tool has run.
> **－** Without a Spec, nothing, as before.
> **－** The path "no `/hi` for this session" — stderr, exit 2 — does not change.
> **－** A Case is still ratified by the person's reply in the chat, never by a picker tool, as `vault/wiki/case-schema.md` says: the picker is for the end of the session only.
> **－** The writing of the Spec does not change: that is the promise of `estimate-spec-capture-appends`.

> **tasks:**
> - [ ] update `rule-spec-capture`
>   - old: `the person picks, and the agent calls the skill picked (cases 190.5, 479.1).`
>   - new: `` the person picks, and the agent calls the skill picked (cases 190.5, 479.1). When the approved plan names the `spec.md` of a conserved Spec — a folder under `vault/raw/` that holds `carry.md` — the hook prints in place of the fork a line that names that folder and tells the agent to call `/box` with it and to ask the person nothing: the person took that Spec at the Frontier (`rule-spec-box`, case 591). ``
>   - change: `a plan that names a conserved Spec gets a line that leads to /box in place of the fork (case 591.3)`
> - [ ] update `estimate-spec-capture-offers-the-fork`
>   - set: `{status: pending, purpose: "The hook prints one line after the Spec is written: for a plan that names a conserved Spec, the call of /box with its folder and no question; otherwise the fork, asked by AskUserQuestion with /work and /carry, and the skill picked called", method: "uv run pytest tests/test_spec.py -k 'fork or box'; by hand, the first ExitPlanMode of a session after the render, and the first ExitPlanMode of a session that took a conserved Spec"}`
>   - change: `the Criterion replaced whole — a plan that names a conserved Spec leads to /box, any other gets the fork (case 591.3)`
> - [ ] `guppi/box.py` — `conserved_spec_named(plan, project_dir)`: the folder `vault/raw/<date>/<HHMM>/` whose `spec.md` the plan names and that `is_carried_over` of `guppi/materialize.py` judges marked, or `None`; the module docstring names `rule-spec-box`
> - [ ] `guppi/spec.py` — when `conserved_spec_named` returns a folder, the line names it and tells the agent to call `/box` with it and to ask nothing; otherwise `fork_line` as before; the module docstring says so
> - [ ] `tests/test_spec.py` — `-k box`: a plan whose title line names the `spec.md` of a folder with `carry.md` gets the line of `/box` with that folder and no `AskUserQuestion`; a folder without `carry.md`, or no such path, gets the fork
> - [ ] read `estimate-spec-capture-offers-the-fork` — `uv run pytest tests/test_spec.py -k 'fork or box'`, and by hand at the first `ExitPlanMode` of a session that took a conserved Spec

> **ratification:**
> ```
> - decision[case 591.3][update][rule-spec-capture]{ref:rule-spec-capture}
> - decision[case 591.3][update][estimate-spec-capture-offers-the-fork]{ref:rule-spec-capture}
> ```

### Case 591.4 — A box session is asked nothing on leaving Plan Mode and ends the ordinary way

> **given:**
> `rule-end-of-work` — the MOC of the ends of a session; its Purpose, on the question when leaving Plan Mode, and its `children`
> **＋** `rule-retro`, `rule-retro-commit`, `rule-handoff`, `rule-carry-over` and `rule-retro-onward` — the children of `rule-end-of-work`, in their order
> **＋** `rule-spec-box` — the box that runs a conserved Spec and merges its branch back, the new last child
> **＋** `/box`, `/handoff` and `/carry` — the skills of the ends
> **＋** `vault/raw/<date>/<hi HHMM>/` and `vault/raw/<date>/event_log.md` — the session folder and the day's event log
> **＋** `git log` — the commits of the session
> **＋** `estimate-end-of-work-order` — its Criterion replaced whole

> **when:**
> A session ends, and someone reads its folder `vault/raw/<date>/<hi HHMM>/`, the day's event log `vault/raw/<date>/event_log.md` and `git log`.

> **then:**
> The session ended one of two ways: Work Mode, Retro, the commit, the handoff and the librarian; or `/carry` straight after Plan Mode.
> **＋** In the ordinary way the order holds: `/handoff` is refused while the tree is dirty; `handoff.md` exists before the librarian is dispatched; no other commit stands between the handoff and the librarian's commit.
> **＋** On leaving Plan Mode the agent asks the person which of the two ends, and starts nothing until it is answered.
> **＋** A session that took a conserved Spec at the Frontier is asked nothing on leaving Plan Mode: `/box` runs the ordinary way on the branch of that Spec, and the shared branch takes that branch by a fast-forward after `handoff.md` exists and before the librarian is dispatched.
> **＋** `rule-carry-over` is a child of `rule-end-of-work`, after `rule-handoff`.
> **＋** `rule-spec-box` is a child of `rule-end-of-work`, after `rule-retro-onward`.

> **tasks:**
> - [ ] update `rule-end-of-work`
>   - set: `{children: ["[[rule-retro]]", "[[rule-retro-commit]]", "[[rule-handoff]]", "[[rule-carry-over]]", "[[rule-retro-onward]]", "[[rule-spec-box]]"]}`
>   - old: `On leaving Plan Mode the agent asks the person which of the two ends and starts nothing until it is answered (case 190.2).`
>   - new: `` On leaving Plan Mode the agent asks the person which of the two ends and starts nothing until it is answered (case 190.2). A session that took a conserved Spec at the Frontier is asked nothing there: `/box` runs it the ordinary way on the branch of that Spec, and merges the branch back by a fast-forward after `handoff.md` stands and before the librarian (`rule-spec-box`, case 591). ``
>   - change: `a session that took a conserved Spec is asked nothing on leaving Plan Mode and ends the ordinary way through /box; rule-spec-box a child after rule-retro-onward (case 591.4)`
> - [ ] update `estimate-end-of-work-order`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — a box session is asked nothing on leaving Plan Mode, its branch merged back by a fast-forward before the librarian; rule-spec-box the last child (case 591.4)`
> - [ ] read `estimate-end-of-work-order` — `make test-end-of-work`, and by hand at the close of the first session that `/box` runs

> **ratification:**
> ```
> - decision[case 591.4][update][rule-end-of-work]{ref:rule-end-of-work}
> - decision[case 591.4][update][estimate-end-of-work-order]{ref:rule-end-of-work}
> ```

### Case 591.5 — /box runs a conserved Spec on its branch and merges it back

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
>   - change: `built from the placeholder: /box runs a conserved Spec on its branch and merges it back before the librarian, first part; a child of rule-end-of-work (case 591.5)`
> - [ ] update `entity-sprint-migration`
>   - old: `- [[rule-spec-box]] — the Spec box, case 207, after Slice 3b`
>   - new: `- [[rule-spec-box]] — the Spec box, its second part: a conserved Spec checked against the pages changed after it was conserved, a Case on such a page built again, ratified again and written into the folder of the conserved Spec, and a conserved Spec taken after other Cases of its session (case 591)`
>   - change: `the Backlog line of rule-spec-box names its second part (case 591.5)`
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
> - decision[case 591.5][update][rule-spec-box]{ref:rule-spec-box}{supersedes:case 207}{supersedes:case 219}{supersedes:case 232}{supersedes:case 532}{supersedes:case 565}
> - decision[case 591.5][update][entity-sprint-migration]{ref:entity-sprint-migration}
> - decision[case 591.5][create][estimate-spec-box-runs-a-conserved-spec]{ref:rule-spec-box}{tags:session,workflow,git,harness}
> ```

### Case 591.6 — guppi box --check refuses a conserved Spec that cannot run now

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
> - decision[case 591.6][create][estimate-spec-box-refuses-a-stale-spec]{ref:rule-spec-box}{tags:session,workflow,git,harness}
> ```

### Case 591.7 — /work runs the Spec of the folder /box gives it

> **given:**
> `rule-work-mode` — the rule of Work Mode, taken up from the defer of case 540; its Render is the skill
> **＋** `.claude/skills/work/SKILL.md` — the skill, rendered in full from `rule-work-mode`
> **＋** `raw/<date>/<hi HHMM>/work.md` — the baseline, the marks of an expected red and the section `## Conserved Spec`
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the approved Spec of the session
> **＋** `vault/raw/<date>/<HHMM>/` — the folder of a conserved Spec, with its `spec.md` and `carry.md`
> **＋** `/box` — the skill that calls `/work` with the folder
> **＋** `vault/wiki/` — the pages, which only the librarian's run writes
> **＋** `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — its Criterion replaced whole

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, after `uv run guppi render` wrote `.claude/skills/work/SKILL.md` from `rule-work-mode`.
> **＋** Or `/box` calls `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec.

> **then:**
> `uv run guppi render --check` exits 0: `.claude/skills/work/SKILL.md` equals the Render of `rule-work-mode`.
> **＋** When a `!` substitution of `.claude/skills/work/SKILL.md` comes back empty, the agent runs its command itself — `git branch --show-current` before the check of the branch, `make test` and `make lint` before the first change — and uses that result.
> **＋** On the branch `main` the skill stops and says so, and nothing is written or changed.
> **＋** On another branch, before the first change, the agent writes `raw/<date>/<hi HHMM>/work.md`: under `## Baseline` the exit code of `make test` and of `make lint` with each failing test and each lint finding line as printed, and an empty `## Expected red`.
> **＋** When `work.md` already stands, its `## Baseline` stays as it is.
> **＋** The agent runs the tasks of `raw/<date>/<hi HHMM>/spec.md` in the order the Spec holds them, and ticks each box of code, a test, a migration or a `by hand` check in the reply that finishes the task.
> **＋** A task that changes `make lint`, one of its steps or a hook of the working tree that reads a page or a governed file the same Spec updates adds one line under `## Expected red` in the same reply: the check, and the page or file it waits for.
> **＋** With a folder from `/box`, `work.md` holds a third section, `## Conserved Spec`, naming the folder; the tasks run and ticked are those of that folder's `spec.md`; and the agent deletes that folder's `carry.md` when the last task is done, before the Work readings.
> **－** The skill writes no page of `vault/wiki/`, and it ticks no line of a page, a render, the sprint, the glossary or a reading.

> **tasks:**
> - [ ] update `rule-work-mode`
>   - old: `Work Mode runs the approved Spec of the session.`
>   - new: `` Work Mode runs the approved Spec of the session, or the conserved Spec whose folder `/box` gives it (case 591). ``
>   - old: `the person types it to resume.`
>   - new: `the person types it to resume; /box calls it with the folder of a conserved Spec.`
>   - old: `` Work Mode runs the approved Spec, `vault/raw/<date>/<hi HHMM>/spec.md`, the session's folder. ``
>   - new: `` Work Mode runs the approved Spec, `vault/raw/<date>/<hi HHMM>/spec.md`, the session's folder. When `/box` calls it with the folder of a conserved Spec, `vault/raw/<date>/<HHMM>/`, the Spec below is that folder's `spec.md`, and `work.md` still stands in the session's folder (case 591). ``
>   - old: `` write `vault/raw/<date>/<hi HHMM>/work.md` with two sections. ``
>   - new: `` write `vault/raw/<date>/<hi HHMM>/work.md` with two sections, or three with a folder from `/box`. ``
>   - old: `` `## Expected red`: empty for now. ``
>   - new: `` `## Expected red`: empty for now. With a folder from `/box`, the third, `## Conserved Spec`: the folder, on one line. ``
>   - old: `` When the last task is done, take the Work readings before `/retro`: ``
>   - new: `` When the last task is done, delete the `carry.md` of a folder from `/box`, then take the Work readings before `/retro`: ``
>   - change: `/work runs the Spec of the folder /box gives it, names that folder under Conserved Spec of work.md and deletes its carry.md after the last task (case 591.7)`
> - [ ] update `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`
>   - set: `{status: pending, purpose: "Whether /work stops on main, writes the baseline of make test and make lint into work.md before the first change — running a command itself when its substitution is empty — and keeps it on a resume, runs the tasks of the Spec of the session or of the folder /box gives it in order with their ticks, names that folder under Conserved Spec and deletes its carry.md, and marks an expected red under Expected red", method: "uv run guppi render --check; by hand, in a session after the render, the first /work the agent calls at the fork, the first /work the person types and the first /work that /box calls: the branch, work.md, the ticks of the Spec, the carry.md of the folder and each Expected red line read against the Criterion, and, where a substitution came back empty, the agent's own run of its command, recorded in the estimate line"}`
>   - change: `the Criterion replaced whole — /work runs the Spec of the folder /box gives it (case 591.7)`
> - [ ] `uv run guppi render`: `.claude/skills/work/SKILL.md`
> - [ ] read `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — by hand, in a later session, the first `/work` that `/box` calls among them

> **ratification:**
> ```
> - decision[case 591.7][update][rule-work-mode]{ref:rule-work-mode}{supersedes:case 540}
> - decision[case 591.7][update][estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline]{ref:rule-work-mode}
> ```

### Case 591.8 — /retro reviews the conserved Spec that /box ran as this session's work

> **given:**
> `rule-retro` — the rule of Retro; its Purpose holds the scope rule, its Render is the skill
> **＋** `.claude/skills/retro/SKILL.md` — the skill, rendered in full from `rule-retro`
> **＋** `raw/<date>/<hi HHMM>/work.md` — its section `## Conserved Spec`, written by `/work`
> **＋** `vault/raw/<date>/<HHMM>/spec.md` and `ledger.md` — the conserved Spec and its decision lines
> **＋** `/box` — the skill that runs the conserved Spec
> **＋** `guppi/ledger.py` — the ledger hook, which judges only this session's lines
> **＋** `estimate-retro-red-check-of-an-updated-page-is-a-handoff-note` — the expected red of the Spec's pages, which stands
> **＋** `estimate-retro-loads` — its Criterion replaced whole

> **when:**
> The agent calls `/retro` on `PreToolUse Skill` at the end of `/work`, or the person types `/retro` on `UserPromptSubmit`, and the agent takes the readings of the session's Estimates.

> **then:**
> A reading measures the Criterion the page carries at the moment of the reading — the one ratified last; its line is written only when the work that Criterion names is built — rendered, written, run.
> **＋** An Estimate that this session creates or updates — by a decision line of its slug, or by an `update` that renames a page to it — gets no reading in this session, built or not; the handoff names it as a reading of a later session.
> **＋** The `read` line of its old Criterion in an earlier Spec is not read; the reading of the new Criterion closes it in a later session, at the moment its `method` names.
> **＋** When `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec`, the Spec of this session is the `spec.md` of the folder that section names: Retro sorts its boxes, and the decision lines of that folder's `ledger.md` count as this session's for those boxes, for the scope of an edit and for the readings above.
> **－** A reading of an Estimate this session neither creates nor updates is taken as before, once its work is built.

> **tasks:**
> - [ ] update `rule-retro`
>   - old: `an edit is allowed when it finishes work a line of this session's ledger ratified, and is new scope otherwise.`
>   - new: `` an edit is allowed when it finishes work a line of this session's ledger ratified, and is new scope otherwise; in a session that `/box` runs, the lines of the conserved Spec's ledger count as this session's (case 591). ``
>   - old: `` otherwise open it with the Read tool (case 569.2). Sort the unticked boxes of the `tasks` of `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73). ``
>   - new: `` otherwise open it with the Read tool (case 569.2). When `work.md` holds `## Conserved Spec`, this session runs that conserved Spec by `/box`, and builds it: below, the Spec of this session is the `spec.md` of the folder that section names, and the decision lines of that folder's `ledger.md` count as lines of this session's ledger — for the boxes, for the scope of an edit and for the readings this session does not take; the ledger hook sees only this session's own lines, so this text is the guard (case 591). Sort the unticked boxes of the `tasks` of the Spec — `raw/<date>/<hi HHMM>/spec.md` (the session's folder, case 73), or the `spec.md` of the folder of `## Conserved Spec`. ``
>   - change: `in a session that /box runs, the conserved Spec is the Spec Retro reviews, and its decision lines count as this session's (case 591.8)`
> - [ ] update `estimate-retro-loads`
>   - set: `{status: pending, method: "one reading by hand at the first /retro, and one at the first /retro of a session that /box runs, recorded in the estimate line"}`
>   - change: `the Criterion replaced whole — in a session that /box runs, the conserved Spec counts as this session's work (case 591.8)`
> - [ ] `uv run guppi render`: `.claude/skills/retro/SKILL.md`
> - [ ] read `estimate-retro-loads` — by hand, at the first `/retro` of a session that `/box` runs

> **ratification:**
> ```
> - decision[case 591.8][update][rule-retro]{ref:rule-retro}
> - decision[case 591.8][update][estimate-retro-loads]{ref:rule-retro}
> ```

### Case 591.9 — /handoff in a box session hands back to /box

> **given:**
> `rule-handoff` — the rule of `/handoff`; its Render is the skill
> **＋** `.claude/skills/handoff/SKILL.md` — the skill, rendered in full from `rule-handoff`
> **＋** `guppi/gate.py` — the gate that reads the tree before `/handoff`
> **＋** `vault/raw/<date>/event_log.md` and `vault/raw/<date>/<hi HHMM>/` — the day's event log and the session folder
> **＋** `raw/<date>/<hi HHMM>/work.md` — its section `## Conserved Spec`, the signal of a box session
> **＋** `librarian-guppi` — the librarian the skill dispatches
> **＋** `/box` — the skill that dispatches the librarian after its merge
> **＋** `estimate-handoff-dispatches` — its Criterion replaced whole

> **when:**
> The agent calls `/handoff` on `PreToolUse Skill` after the reply that ends Retro, or the person types `/handoff` on `UserPromptSubmit`, the gate of `guppi/gate.py` reads the tree, and the agent runs the skill `.claude/skills/handoff/SKILL.md` as rendered from `rule-handoff`.

> **then:**
> The skill's context holds `git status --porcelain`. On a dirty tree the skill stops and says "commit first", and nothing is written.
> **＋** On a clean tree the day's event log `vault/raw/<date>/event_log.md` holds the `handoff` mark of the call.
> **＋** The agent writes `handoff.md` into the session's folder `vault/raw/<date>/<hi HHMM>/`: one document with no `---` and the sections that `rule-handoff` names, with no Read call on the artifacts.
> **＋** Then the agent dispatches `librarian-guppi` with one line, `Materialize <date> from <path of handoff.md>.`, the path being that of the file just written, and shows the librarian's report to the person unchanged.
> **－** In a session whose `raw/<date>/<hi HHMM>/work.md` holds `## Conserved Spec` — one that `/box` runs — the agent dispatches nothing after `handoff.md` and goes back to the step of `/box` that follows `/handoff`.
> **－** No commit follows the handoff except the librarian's own, and no reply between the call and the librarian's report carries a `LEDGER` block.

> **tasks:**
> - [ ] update `rule-handoff`
>   - old: `` Then dispatch the `librarian-guppi` agent with one line: ``
>   - new: `` Then, in a session whose `work.md` holds `## Conserved Spec` — one that `/box` runs, as you wrote it in this turn — dispatch nothing: go back to the step of `/box` that follows `/handoff`, which merges the branch and dispatches the librarian (case 591). In any other session, dispatch the `librarian-guppi` agent with one line: ``
>   - change: `in a session that /box runs, /handoff dispatches nothing and hands back to /box (case 591.9)`
> - [ ] update `estimate-handoff-dispatches`
>   - set: `{status: pending, purpose: "/handoff stops on a dirty tree, writes handoff.md from memory into the session's folder and dispatches the librarian with its path, or, in a session that /box runs, hands back to /box, with no commit after", method: "by hand at the /handoff of a later session and at the /handoff of the first session that /box runs: the event log, handoff.md, the dispatch line and git log"}`
>   - change: `the Criterion replaced whole — in a session that /box runs, /handoff hands back to /box (case 591.9)`
> - [ ] `uv run guppi render`: `.claude/skills/handoff/SKILL.md`
> - [ ] read `estimate-handoff-dispatches` — by hand, at the `/handoff` of the first session that `/box` runs

> **ratification:**
> ```
> - decision[case 591.9][update][rule-handoff]{ref:rule-handoff}
> - decision[case 591.9][update][estimate-handoff-dispatches]{ref:rule-handoff}
> ```

### Case 591.10 — /box stops where its check or a merge refuses

> **given:**
> `rule-where-to-stop` — the rule of the stops; its Purpose names who imports the file, its Render is the file
> **＋** `vault/wiki/where-to-stop.md` — the file, rendered in full from `rule-where-to-stop`
> **＋** `vault/wiki/case-schema.md` — the schema that names a task opening with `stop:`
> **＋** `.claude/skills/box/SKILL.md` — the skill of `/box`, which imports the file as `/work` does
> **＋** `/box`, `/work` and `/retro` — the skills of the run
> **＋** `uv run guppi box --check` and `git merge --ff-only` — the check and the merges of `/box` that can refuse
> **＋** `raw/<date>/<hi HHMM>/spec.md` and `raw/<date>/<hi HHMM>/handoff.md` — the Spec of the run and its report
> **＋** `estimate-where-to-stop-stops-only-on-its-conditions` — its Criterion replaced whole

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the run goes from the tasks of `raw/<date>/<hi HHMM>/spec.md` to the librarian's report.
> **＋** Or the agent calls `/box` on `PreToolUse Skill`, and the run goes from its first step to the librarian's report.

> **then:**
> The context of `/work` holds the text of `vault/wiki/where-to-stop.md`, rendered from `rule-where-to-stop`.
> **＋** The context of `/box`, from `.claude/skills/box/SKILL.md`, holds the same text.
> **＋** The agent ends a reply with a question to the person on a fork that changes a contract, on a hook refusal whose text gives no step it can follow or says that it is a stop, and before an action that git in the repository cannot undo.
> **＋** Before a task of `raw/<date>/<hi HHMM>/spec.md` whose text opens with `stop:`, the agent stops and asks; the task runs after the person's word.
> **＋** On the branch `main` the agent stops and says so: Work Mode does not start there.
> **＋** In a run of `/box`, the agent stops and asks when `uv run guppi box --check` prints a line, or when a `git merge --ff-only` of `/box` refuses.
> **＋** A reply that stops from the call of `/retro` until `raw/<date>/<hi HHMM>/handoff.md` stands opens with `STOP:`.
> **＋** After the person's answer the run goes on from where it stopped.
> **＋** `vault/wiki/case-schema.md` names a task line that opens with `stop:` as a task that waits for the person's word.
> **－** No other point stops the run: a red test, a reading that only the person can take, an observation or a doubt ends as a lesson or a line of `raw/<date>/<hi HHMM>/handoff.md`.

> **tasks:**
> - [ ] update `rule-where-to-stop`
>   - old: `` `/work` loads its text by an import of `vault/wiki/where-to-stop.md`, ``
>   - new: `` `/work` and `/box` load its text by an import of `vault/wiki/where-to-stop.md` (case 591), ``
>   - old: `` `/work`, the Work readings, `/retro` and `/handoff` run in one turn. ``
>   - new: `` `/box`, `/work`, the Work readings, `/retro` and `/handoff` run in one turn. ``
>   - old: `` 5. The branch is `main`: Work Mode does not start there; say so, and go on after the person moves to another branch. ``
>   - new:
>     ```
>     5. The branch is `main`: Work Mode does not start there; say so, and go on after the person moves to another branch.
>     6. `/box` cannot go on: its check `uv run guppi box --check` prints a reason, or one of its `git merge --ff-only` refuses; show what stopped it, and go on after the person's word.
>     ```
>   - change: `/box imports the file, and its stops — a reason of its check, a fast-forward merge that refuses — are condition 6 (case 591.10)`
> - [ ] update `estimate-where-to-stop-stops-only-on-its-conditions`
>   - set: `{status: pending, method: "by hand at the first run from /work to the librarian after the render, and at the first run of /box: the context of /work and of /box, the replies of the turn and the Spec read against the Criterion, recorded in the estimate line; a condition that does not arise is named as not exercised"}`
>   - change: `the Criterion replaced whole — /box imports the file, and its stops (case 591.10)`
> - [ ] `uv run guppi render`: `vault/wiki/where-to-stop.md`
> - [ ] read `estimate-where-to-stop-stops-only-on-its-conditions` — by hand, at the first run of `/box`

> **ratification:**
> ```
> - decision[case 591.10][update][rule-where-to-stop]{ref:rule-where-to-stop}
> - decision[case 591.10][update][estimate-where-to-stop-stops-only-on-its-conditions]{ref:rule-where-to-stop}
> ```

### Case 591.11 — The code fence of decision-case-13 is closed

> **context:**
> `make lint` prints a `fence` finding on `decision-case-13`. A code fence opens in `## When` and is still open at the end of that section, because the text was cut off when the page was written. The defer of case 565 tied this fix to the item. The fix closes the fence with one line at the end of the section, by an `update` with a `replace` pair, as earlier Cases did on Decision pages. `estimate-lint-catches-a-broken-fence` checks that lint finds such a fence, and its Criterion stands. `estimate-sprint-migration-lint-clean` checks that lint is clean at the close of the sprint; its Criterion stands, and this sub-case removes one of the lines that keep it red. Case 587 sets how `make lint` runs its steps; this sub-case changes no step.

> **given:**
> `decision-case-13` — the Decision page whose `## When` holds the open fence
> **＋** `guppi lint` — the check whose `fence` class reads the page
> **＋** `make lint` — the target that runs `guppi lint`
> **＋** `raw/2026-10-02/1202/cases/case-587.md` — the Case of this session that sets how `make lint` runs
> **＋** `estimate-lint-catches-a-broken-fence` — the check of the `fence` class, which stands
> **＋** `estimate-sprint-migration-lint-clean` — the clean lint at the close of the sprint, which stands

> **when:**
> Someone runs `make lint` after the librarian's run of this session has applied its Spec.

> **then:**
> `guppi lint` prints no `fence` line on `decision-case-13`.
> **＋** The `## When` section of `decision-case-13` ends with a closing fence line after `<!-- rule-case-protocol -->`.
> **－** The rest of the text of `decision-case-13` stays as it was; only its History gains a line.

> **tasks:**
> - [ ] update `decision-case-13`
>   - old:
>     ````
>     ```markdown
>     <!-- rule-case-protocol -->
>     ````
>   - new:
>     ````
>     ```markdown
>     <!-- rule-case-protocol -->
>     ```
>     ````
>   - change: `the code fence of When closed: the text was cut off when the page was written; no content change (case 591.11)`
> - [ ] by hand: `make lint` after the librarian's run of this session prints no `fence` line on `decision-case-13`

> **ratification:**
> ```
> - decision[case 591.11][update][decision-case-13]{ref:decision-case-13}
> ```

### Case 591.12 — The Work readings of /box leave the Estimates the conserved Spec changes

> **context:**
> The Work readings of `/work` leave a reading of an Estimate that this session creates or updates. In a box session, the Estimates that the conserved Spec creates or updates are built in this session but decided in the session that conserved the Spec, and the ledger hook sees only this session's lines. Without this sub-case `/work` could take such a reading, while `/retro` (591.8) holds it back. This sub-case extends the Work readings in the same way as 591.8. 591.7 changes other sentences of the same Render, and no pair of the two touches the same sentence.

> **given:**
> `rule-work-mode` — the rule of Work Mode; its Render holds the Work readings
> **＋** `.claude/skills/work/SKILL.md` — the skill, rendered in full from `rule-work-mode`
> **＋** `raw/<date>/<hi HHMM>/frontier.md` — the `W` lines of the readings
> **＋** `raw/<date>/<hi HHMM>/spec.md` — the approved Spec of the session
> **＋** `vault/raw/<date>/<HHMM>/` — the folder of a conserved Spec, with its `spec.md` and `ledger.md`
> **＋** `/box` and `/retro` — the skill that calls `/work`, and the skill whose reply carries the readings
> **＋** `vault/wiki/where-to-stop.md` — the stops of the run
> **＋** `estimate-work-mode-takes-the-work-readings` — its Criterion replaced whole

> **when:**
> The agent calls `/work` on `PreToolUse Skill` after the person picked it at the fork of `ExitPlanMode`, or the person types `/work` on `UserPromptSubmit`, and the last task of `raw/<date>/<hi HHMM>/spec.md` is done.
> **＋** Or `/box` called `/work` with the folder `vault/raw/<date>/<HHMM>/` of a conserved Spec, and the last task of that folder's `spec.md` is done.

> **then:**
> Before `/retro`, the agent takes, in the order of `raw/<date>/<hi HHMM>/frontier.md`, each reading of an open `W` line whose work is built and whose moment, as its `method` names it, has come.
> **＋** A moment of an earlier session, such as the librarian's run, has come.
> **＋** Every reading taken is first marked done in `raw/<date>/<hi HHMM>/frontier.md`, and its `estimate[...]` line stands in the `LEDGER` block of the one reply that ends Retro.
> **＋** The tasks, the readings and `/retro` run in one turn, and no reply ends before the reply that ends Retro, except at a stop of `vault/wiki/where-to-stop.md`.
> **－** A reading of an Estimate this session creates or updates is not taken, and its `W` line stays open.
> **－** With a folder from `/box`, a reading of an Estimate that a decision line of that folder's `ledger.md` creates or updates is not taken either, and its `W` line stays open.
> **－** A reading whose moment has not come is not taken, and its `W` line stays open.
> **－** The step ticks no `read` box of `raw/<date>/<hi HHMM>/spec.md`.

> **tasks:**
> - [ ] update `rule-work-mode`
>   - old: `Leave a reading of an Estimate this session creates or updates, and one whose moment has not come:`
>   - new: `` Leave a reading of an Estimate this session creates or updates — with a folder from `/box`, one that a decision line of that folder's `ledger.md` creates or updates too — and one whose moment has not come: ``
>   - change: `the Work readings of /box leave the Estimates that the conserved Spec creates or updates (case 591.12)`
> - [ ] update `estimate-work-mode-takes-the-work-readings`
>   - set: `{status: pending, purpose: "Whether /work, after the last task and in the same turn, takes in Frontier order each open W reading whose work is built and whose moment has come, closes its W line, leaves its line to the reply that ends Retro, and leaves open the readings this session changes, or the conserved Spec that /box gives it changes, or whose moment has not come", method: "by hand at the first /work after the render and at the first /work that /box calls: the replies after the last task, their LEDGER blocks and frontier.md read against the Criterion, recorded in the estimate line"}`
>   - change: `the Criterion replaced whole — the Work readings of /box leave the Estimates the conserved Spec changes (case 591.12)`
> - [ ] read `estimate-work-mode-takes-the-work-readings` — by hand, at the first `/work` that `/box` calls

> **ratification:**
> ```
> - decision[case 591.12][update][rule-work-mode]{ref:rule-work-mode}
> - decision[case 591.12][update][estimate-work-mode-takes-the-work-readings]{ref:rule-work-mode}
> ```
