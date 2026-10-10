## Case 756 — The sprint plugin opens

> **context:**
> A sprint is one page, `entity-sprint-<id>`, a Leaf under `entity-sprint`. Its `estimates` are its Definition of done and its `## Milestones` are the work in order. `guppi sprint` renders `vault/wiki/sprint.md` from it. Since the close of `migration` no live sprint page stands, and `vault/wiki/sprint.md` reads that no sprint is open. The ledger hook refuses each decision line but a `defer` until a `create` of an `entity-sprint-` page stands, so this opening Case, run under `/sprint-open` (`rule-skill-sprint-open`), is the first Case the session ratifies. The person set the id `plugin` and a goal of five lines of work: the opening and the close of a sprint fixed, a final README, the repository on GitHub ready for pull requests from others, CI that writes a clean version of the project to a branch of its own, and that clean version made into a Claude Code plugin. Each line becomes one condition of the Definition of done, one Estimate each, in Case 756.2 to Case 756.6; Case 756.1 creates the page. `vault/wiki/backlog.md` holds 3 items, and the person took none of them. A Glob `vault/**/*plugin*` printed only `vault/.obsidian/core-plugins.json`, so the new slugs are free. Case 756.1 adds no Estimate: `estimate-sprint-renders-the-backlog` already checks the render of a live sprint page, and the pending `estimate-sprint-close-next-session-opens-the-sprint` checks that the pages written from this session's ledger carry the new sprint id; their Criteria speak of any sprint page and stand. `estimate-skill-sprint-open-asks-the-opening-questions` checks the questions of the opening, which this Case asked, and stands. `case-schema.md` says that a `method` holds only what runs in the Case's own session. The methods of Case 756.2 to Case 756.6 are read in a later session of the sprint, before its close, since `rule-sprint` and `entity-sprint` set that the Estimates of a sprint page are read before its close. Neither page states an exception to case 670.4; the exception for a sprint page stands on their words that its Estimates are read before its close, and on the precedent of `entity-sprint-migration`, whose Estimate `estimate-sprint-migration-merges` was read in Work Mode of session 1555, the session that closed it. The read lines of these Estimates stay open at the Retro of this session and are carried until their moment. The sprint-turn condition is read at the end of Work Mode of the closing session, since the move to the archive runs later, in the librarian's run (Q7). No separate reading of that run comes at the close of `plugin`: `estimate-sprint-close-runs-in-the-librarian-run` was read `passed` at the `/hi` of this session over the close of `migration`, line 1 of this session's ledger, and the move of the sprint page and its Estimates is held by the tests of `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`. Case 756.2 signs only what is new, no step done or fixed by hand; the steps of the skill stand in the Criteria of `estimate-skill-sprint-close-leads-the-closing-session` and `estimate-sprint-close-takes-the-readings-in-groups`, which are not signed again. `README.md` exists at the root of the repository with the heading `# Vault harness`; a Grep for `README` over `vault/wiki/`, `log.md` left out, printed nothing, so no page governs it yet. The person added that the form of the sprint opening may be discussed later, and asked no change for it now.

> **problem:**
> No sprint is open, and the session can ratify no other Case until a sprint page stands. The next sprint needs its id, its goal, its Definition of done, its milestones and an answer on the backlog.

> **recommend:**
> - **What is the goal of the sprint?**
>   - Recommended: (a) your own goal; failing one, (b) settle what `migration` left.
>   - Answer: (a), the sprint's own goals: make sure the opening and the close of a sprint work correctly and fix every flaw; write the final README on the main parts of the project, why it is needed and how to use it; connect GitHub and set it up so that pull requests from other people are easy to review; set up CI/CD so that a branch of its own holds a clean version of the project, with no case references in its texts and a clean Frontier, sprint and the like; that clean version becomes the Claude plugin. The rest comes as the work goes.
> - **Do you take any backlog item into the sprint?**
>   - Recommended: (a) take none now.
>   - Answer: (a), nothing now; to be thought about later.
> - **What is the id of the sprint?**
>   - Recommended: (a) `plugin`.
>   - Answer: agreed, (a).
> - **How is the goal written in one sentence?**
>   - Recommended: (a) the whole list in one sentence.
>   - Answer: agreed, (a).
> - **Which conditions make the Definition of done?**
>   - Recommended: (a) five conditions, one per line of the list.
>   - Answer: agreed, (a).
> - **How are the milestones cut?**
>   - Recommended: (b) three milestones in the order of the work.
>   - Answer: agreed, (b).
> - **When is the condition on the sprint turn read?**
>   - Recommended: (a) read the steps up to Work Mode; the archive run stays with the check of the close rule.
>   - Answer: agreed, (a).
> - **Change**
>   - Asked: pre-spec found that the methods of Case 756.2 to Case 756.6 wait for a later session against case 670.4; the person agreed to name in `context` where the exception for a sprint page stands and its precedent.
>   - Taken: `context` names `rule-sprint`, `entity-sprint` and the reading of `estimate-sprint-migration-merges` in session 1555.
> - **Change**
>   - Asked: pre-spec found that the `then` of Case 756.2 signs again the steps that `estimate-skill-sprint-close-leads-the-closing-session` and `estimate-sprint-close-takes-the-readings-in-groups` hold; the person agreed to keep only what is new.
>   - Taken: the `then` of Case 756.2 holds only that no step is done or fixed by hand, and names the two Estimates for the rest.
> - **Change**
>   - Asked: pre-spec found that the alias of the new tag `ci` would also point at the tag `case-build`; the person agreed to another alias.
>   - Taken: the aliases of `ci` are CI, CI/CD and continuous integration in Russian.
> - **Change**
>   - Asked: pre-spec found that `context` and Case 756.2 say a reading of `estimate-sprint-close-runs-in-the-librarian-run` comes at the close of `plugin`, and none is due; the person chose (a), keep that Estimate as it stands and correct the text.
>   - Taken: `context` and the `－` line of Case 756.2 say that the run was read `passed` at the close of `migration` and that `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` holds the move of the pages.

### Case 756.1 — The sprint page plugin

> **given:**
> `entity-sprint-plugin`: the new page of the sprint.
> **＋** `entity-sprint`: the sprint as a kind, the parent of the page.
> **＋** `guppi/sprint.py`: the script that renders the sprint page.
> **＋** `vault/wiki/sprint.md`: the file the script writes.
> **＋** `vault/wiki/backlog.md`: the items put off.
> **＋** `rule-sprint`: the guard of the sprint page and its render.

> **when:**
> `uv run guppi sprint` of `guppi/sprint.py` runs in the librarian's run of this session with the live page `entity-sprint-plugin`.

> **then:**
> `vault/wiki/sprint.md` names the sprint `plugin`, with its Purpose and its Done when.
> **＋** The milestone `The sprint turn and GitHub` stands whole as the current one.
> **＋** The milestones `The clean branch` and `The plugin` stand one line each, and the close line is the last item of `The plugin`.
> **＋** Each page written from the ledger of this session carries `sprint: plugin`.
> **－** No item of `vault/wiki/backlog.md` enters `entity-sprint-plugin`.

> **tasks:**
> - [ ] create `entity-sprint-plugin`
>   - type: `entity`
>   - kind: `Leaf`
>   - ref: `entity-sprint`
>   - purpose: `GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the opening and close of a sprint work with no fix by hand`
>   - tags: `[sprint, workflow]`
>   - sections.Purpose: `GUPPI ships as a Claude Code plugin: a clean version built by CI on a branch of its own, on GitHub with a README and ready for pull requests from others, and the opening and close of a sprint work with no fix by hand. Done when every Estimate of this page passes: the close steps run from the close line, the README describes the project, a pull request from another account is checked and reviewed on GitHub, CI writes the clean branch, and the clean branch installs as a plugin. Each Estimate of this page is read before the close of the sprint; one that has not passed by then goes to the archive with this page, its status kept in the record of the close (rule-sprint-close).`
>   - sections.Milestones:
>     ````
>     ### The sprint turn and GitHub
>
>     - the opening and the close of a sprint run with no fix by hand and each flaw found in them is fixed
>     - the repository on GitHub set up so that a pull request from another person is easy to review
>
>     ### The clean branch
>
>     - CI that writes a clean version of the project to a branch of its own with no case references in its texts and no session data such as the Frontier or the sprint
>
>     ### The plugin
>
>     - the clean version made into a Claude Code plugin
>     - the README on what the project is and what it is for and on its main parts and its use
>     - the close of `plugin` — `/sprint-close`, a session of its own
>     ````
> - [ ] `uv run guppi sprint`

> **ratification:**
> ```
> - decision[case 756.1][create][entity-sprint-plugin]{ref:entity-sprint}{tags:sprint,workflow}
> ```

### Case 756.2 — The close steps run from the close line

> **given:**
> `estimate-sprint-plugin-close-steps-run-from-the-line`: the new check of the steps of the close.
> **＋** `entity-sprint-plugin`: the sprint page that holds the close line.
> **＋** `.claude/skills/sprint-close/SKILL.md`: the skill the close line starts.
> **＋** `estimate-skill-sprint-close-leads-the-closing-session`: the check of the steps of the skill.
> **＋** `estimate-sprint-close-takes-the-readings-in-groups`: the check of the readings of the closing session.
> **＋** `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest`: the check of the move of the sprint page to the archive.

> **when:**
> In the session that closes `entity-sprint-plugin`, the person takes up the line ``the close of `plugin` — `/sprint-close`, a session of its own`` of its `## Milestones`; at the end of Work Mode someone reads that session's `frontier.md`, ledger, `spec.md` and transcript.

> **then:**
> From that line to the end of Work Mode, no step of `/sprint-close` of `.claude/skills/sprint-close/SKILL.md` is done or fixed by hand outside what the skill sets.
> **－** The steps the skill sets are not part of this promise: `estimate-skill-sprint-close-leads-the-closing-session` and `estimate-sprint-close-takes-the-readings-in-groups` hold them.
> **－** The move of the pages to the archive in the librarian's run is not part of this promise: `estimate-sprint-close-archives-the-sprint-page-and-keeps-the-rest` holds it.

> **tasks:**
> - [ ] create `estimate-sprint-plugin-close-steps-run-from-the-line`
>   - ref: `entity-sprint-plugin`
>   - kind: `QA`
>   - purpose: `Whether the session that closes sprint plugin runs /sprint-close from the close line up to the end of Work Mode with no step done or fixed by hand`
>   - method: `by hand, at the end of Work Mode of the session that closes entity-sprint-plugin: its frontier.md, ledger, spec.md and transcript`
>   - tags: `[sprint, workflow]`
> - [ ] read `estimate-sprint-plugin-close-steps-run-from-the-line`

> **ratification:**
> ```
> - decision[case 756.2][create][estimate-sprint-plugin-close-steps-run-from-the-line]{ref:entity-sprint-plugin}{tags:sprint,workflow}
> ```

### Case 756.3 — The README describes the project

> **given:**
> `estimate-sprint-plugin-readme-describes-the-project`: the new check of the README.
> **＋** `entity-sprint-plugin`: the sprint page.
> **＋** `README.md`: the description of the project at the root of the repository.

> **when:**
> In a session of the sprint `plugin` before its close, the person reads `README.md`.

> **then:**
> `README.md` says what GUPPI is and what it is for.
> **＋** It names the main parts of the project and what each one does.
> **＋** It says how to install GUPPI and how to use it.
> **＋** The person says that it describes the project as it stands.

> **tasks:**
> - [ ] tag `readme`
>   - meaning: `the README of the repository: what the project is, its parts and how to use it`
>   - aliases: `ридми, описание проекта`
> - [ ] create `estimate-sprint-plugin-readme-describes-the-project`
>   - ref: `entity-sprint-plugin`
>   - kind: `QA`
>   - purpose: `Whether README.md says what GUPPI is and what it is for, its main parts and how to install and use it, as the person confirms`
>   - method: `by hand, the person's answer on README.md, in a session of the sprint plugin before its close`
>   - tags: `[sprint, readme]`
> - [ ] read `estimate-sprint-plugin-readme-describes-the-project`

> **ratification:**
> ```
> - decision[case 756.3][create][estimate-sprint-plugin-readme-describes-the-project]{ref:entity-sprint-plugin}{tags:sprint,readme}
> ```

### Case 756.4 — A pull request is checked and reviewed on GitHub

> **given:**
> `estimate-sprint-plugin-pull-requests-reviewed-on-github`: the new check of pull requests.
> **＋** `entity-sprint-plugin`: the sprint page.
> **＋** the repository of the project on GitHub, with its branch `main`.

> **when:**
> In a session of the sprint `plugin` before its close, someone opens a pull request against `main` of the repository of the project on GitHub from an account other than the owner's.

> **then:**
> The checks of CI run on the pull request and show their result on it.
> **＋** The owner reviews the pull request on GitHub and can merge it into `main`.

> **tasks:**
> - [ ] create `estimate-sprint-plugin-pull-requests-reviewed-on-github`
>   - ref: `entity-sprint-plugin`
>   - kind: `QA`
>   - purpose: `Whether a pull request from another account runs the checks of CI on GitHub and can be reviewed and merged into main`
>   - method: `by hand, a pull request from a second account read on GitHub, in a session of the sprint plugin before its close`
>   - tags: `[sprint, github, git]`
> - [ ] read `estimate-sprint-plugin-pull-requests-reviewed-on-github`

> **ratification:**
> ```
> - decision[case 756.4][create][estimate-sprint-plugin-pull-requests-reviewed-on-github]{ref:entity-sprint-plugin}{tags:sprint,github,git}
> ```

### Case 756.5 — CI writes the clean branch

> **given:**
> `estimate-sprint-plugin-ci-writes-a-clean-branch`: the new check of the clean version.
> **＋** `entity-sprint-plugin`: the sprint page.
> **＋** the repository of the project on GitHub, with its branch `main` and its CI.

> **when:**
> In a session of the sprint `plugin` before its close, a commit lands on `main` of the repository of the project on GitHub, and CI runs on it.

> **then:**
> CI writes a clean version of the project to a branch of its own.
> **＋** No text of the clean version holds a reference to a case or a decision.
> **＋** The clean version holds no data of the sessions of this repository, such as its Frontier and its sprint.
> **＋** A check of CI fails the run when a case reference or session data remains in the clean version.

> **tasks:**
> - [ ] tag `ci`
>   - meaning: `the continuous integration of the repository on GitHub: its runs, its checks and the branches it writes`
>   - aliases: `CI, CI/CD, непрерывная интеграция`
> - [ ] create `estimate-sprint-plugin-ci-writes-a-clean-branch`
>   - ref: `entity-sprint-plugin`
>   - kind: `QA`
>   - purpose: `Whether CI writes a clean version of the project to a branch of its own, with no case reference and no session data, and fails when one remains`
>   - method: `by hand, a CI run on GitHub and the clean branch it wrote, read in a session of the sprint plugin before its close`
>   - tags: `[sprint, ci, git]`
> - [ ] read `estimate-sprint-plugin-ci-writes-a-clean-branch`

> **ratification:**
> ```
> - decision[case 756.5][create][estimate-sprint-plugin-ci-writes-a-clean-branch]{ref:entity-sprint-plugin}{tags:sprint,ci,git}
> ```

### Case 756.6 — The clean branch installs as a plugin

> **given:**
> `estimate-sprint-plugin-installs-as-a-plugin`: the new check of the plugin.
> **＋** `entity-sprint-plugin`: the sprint page.
> **＋** the clean branch that CI writes in the repository of the project on GitHub.
> **＋** `/hi`: the command that opens a working session, run in the project the plugin goes into.

> **when:**
> In a session of the sprint `plugin` before its close, someone installs the clean branch as a Claude Code plugin into an empty project, opens Claude Code there and types `/hi`.

> **then:**
> The plugin installs with no error.
> **＋** `/hi` opens a working session in that project.

> **tasks:**
> - [ ] tag `plugin`
>   - meaning: `GUPPI as a Claude Code plugin: its clean version, its install and its use in another project`
>   - aliases: `плагин`
> - [ ] create `estimate-sprint-plugin-installs-as-a-plugin`
>   - ref: `entity-sprint-plugin`
>   - kind: `QA`
>   - purpose: `Whether the clean branch installs as a Claude Code plugin into an empty project and /hi runs there`
>   - method: `by hand, an install of the clean branch into an empty project, in a session of the sprint plugin before its close`
>   - tags: `[sprint, plugin]`
> - [ ] read `estimate-sprint-plugin-installs-as-a-plugin`

> **ratification:**
> ```
> - decision[case 756.6][create][estimate-sprint-plugin-installs-as-a-plugin]{ref:entity-sprint-plugin}{tags:sprint,plugin}
> ```
