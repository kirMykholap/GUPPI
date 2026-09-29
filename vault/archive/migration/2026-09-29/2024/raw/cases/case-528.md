## Case 528 — The remote leaves the repository and `/hi`, and git tracks no raw date folder without a session

> **context:**
> The migration sprint closes when the leftovers of the old repository are gone, or are kept by a decision (`estimate-sprint-migration-leftovers-gone`). Case 510 deleted `vault/parked/` and the August documents under `docs/`. Case 102.1 deleted the old August archive root, with the line `delete: [old-archive]`. A Glob of `vault/archive/2026-*/**` finds nothing, and `vault/archive/` holds only `migration/`. Three things were left: the raw date folders, `git pull` and `gh`.
> At every session start `/hi` runs `git pull --ff-only` (`rule-git-context`) and `gh issue list --limit 5` (`rule-github-issues`). Both fail. The only remote, `origin`, is `c:/PROJECTS/job hunt ai`. That is the product repository this vault was split from. `migration` has no upstream. At the `/hi` of this session the pull printed "There is no tracking information for the current branch", and `gh` printed "To get started with GitHub CLI, please run: gh auth login". A note in the Closed section of `entity-sprint-migration` keeps both off the Frontier (case 268.2). Decisions 11.1 and 11.2 kept the two lines as they were, and cases 220 and 243 put the choice off to the close. `main` tracks `origin/main`, so after the merge of the sprint `/hi` on `main` would pull from the other project. Nothing in `guppi/` or `.claude/` reads the remote.
> Each past date folder under `vault/raw/` holds only `event_log.md`. `.gitignore` excludes it with `vault/raw/*/event_log.md`, and `rule-raw-archive` keeps it there on purpose. So git tracks no such folder, but the Criterion says "`vault/raw/` has no date folder without a session".
> In two rounds the person accepted every recommendation. After the first round they wrote "I agree with the recommendations", and after the second, "I agree".
> - The repository has no remote. `origin` is removed, the `Pull:` and `Open issues:` lines leave `/hi`, and `rule-github-issues` leaves the harness.
> - `rule-git-context` keeps the render, branch and status lines. Its promise that no pull runs mid-session goes with the pull.
> - The date folders stay on disk. The promise reads them by what git tracks.
>
> What `case-guppi` found in the frame:
> - The Criteria of `estimate-hi-no-read-calls` and `estimate-hi-writes-frontier` name `Pull:` and `Open issues:`. 528.3 replaces the first whole. Case 531.11 replaces the second.
> - The Frontier sentence of `rule-skill-hi` on a failed pull reads the sprint note. Case 531.11 removes the sentence, and 528.5 removes the note.
> - `rule-skill-hi` names both commands in `allowed-tools` and in its `description`.
> - `rule-session-start` explains the split into two Leaves by how `git pull` and `gh` fail, and it lists open issues among the sources of the Frontier.
> - `rule-ledger-tail` places its line after `rule-github-issues`.
> - The glossary row Issue points at `rule-github-issues`.
> - Each of these four texts is changed.
> - `cleanup` takes an archived slug out of the `children` and `estimates` lists of live pages (`rule-cleanup`).
>
> These texts stand as they are:
> - `rule-retro` says "`gh` is not available: name a deferred bug in the handoff". That stays true.
> - `rule-rules-schema` shows `rule-github-issues` in an example of an older sprint. It is an example.
> - `vault/wiki/tags.md` gives the tag `git` the meaning "branch, status, pull". The tag still fits `rule-git-context`, and `tags.md` is not a page.
> - `docs/migration/migration-plan.md` names `git pull`. The closing Case deletes it.
> - `rule-render-harness` names "the Render line of /hi after the pull" only in its History.
>
> Sub-case 528.4 changed the Frontier sentence of `rule-skill-hi` and the Criterion of `estimate-hi-writes-frontier`. Case 531.11 of this session superseded it and carries both changes, so 528.4 has left the Spec.
> `rule-git-context` and `rule-github-issues` are backlog items, deferred by cases 220 and 243. The lines of 528.1 and 528.2 that name them carry `{supersedes:case 220}{supersedes:case 243}`, and both pages leave the backlog (case 429).
> The check of the answer notes that some lines of the old Criteria are not carried. Each is left out on purpose:
> - In 528.1, the old lines of `estimate-git-context-current` named "the four commands", the `Pull:` line, a failing pull, and no `git pull` later in the session. The person chose to take the pull out with the remote and to drop the promise on a pull mid-session. The lines on `Render:`, `Branch:` and `Status:` are carried word for word.
> - In 528.3, the old first line of `estimate-hi-no-read-calls` listed `Pull:` and `Open issues:`. The new line is the same without them. The `－` line on read-tool calls is carried word for word.
> - In 528.5, the old archive and raw line of `estimate-sprint-migration-leftovers-gone` becomes two lines: the archive root with its decision named, and the tracked files of `vault/raw/`. "A decision stands on `git pull` … keep as is, or repair" becomes the decision taken: no remote, and neither command in `/hi`. The `－` line "What to do with … those are the Cases of Slice 5" goes, because this Case decides those things. The lines on `vault/parked/`, on `docs/` and on the migration plan are carried word for word.
>
> The check also notes that the first `then` line of 528.3 shares words with 528.1 and 528.2. The three sub-cases hold different promises. 528.3 is the order of the blocks of the first turn. 528.1 is the git lines and the absence of a remote. 528.2 is the archive of the rule and the place of the tail.
> No hook changes, and no reader in code refuses anything between the edit and the render. The Case creates no page, so no vault query was run. The readings of the two `/hi` Estimates of this Case wait for a session after the render. The reading of the leftovers Estimate waits for the close (case 428.1).
> Not done: a remote for backup, the deletion of the migration plan, and the merge of `migration` into `main`.

> **problem:**
> `/hi` runs two commands against a remote that is not this project, and both fail at every session start. The note that keeps them off the Frontier goes away with the sprint. After the merge, `main` would pull from the product repository. The promise on the raw date folders asks that folders git does not track be gone, but `rule-raw-archive` keeps their logs on purpose.

> **recommend:**
> Remove `origin`. Take the pull and the issues out of `/hi`, and archive `rule-github-issues`. Read the date folders by what git tracks. A GitHub remote was rejected: it needs an account outside the repository, and issues are notes outside the vault, which the one rule of `case-schema.md` forbids. Deleting the date logs was rejected: they are the only record of hook refusals, and git holds none of them.

### Case 528.1 — `/hi` runs no `git pull`, and the repository has no remote

> **given:**
> `rule-git-context` — the rule of the git lines of `/hi`
> **＋** `estimate-git-context-current` — its promise, whose Criterion is replaced whole
> **＋** `.claude/skills/hi/SKILL.md` — the skill file the rule renders into
> **＋** `.git/config` — the remote `origin` and the upstream of `main`

> **when:**
> The person invokes `/hi`, and `.claude/skills/hi/SKILL.md` runs the commands of `rule-git-context`.

> **then:**
> The context holds `Render:` with the output of `uv run guppi render --sync` (a diff for each governed file that differed and was written, or nothing), then `Branch:` with the current branch and `Status:` with `git status --short`.
> **＋** `git remote` prints no remote: `.git/config` holds no `origin`, and `main` has no upstream.
> **－** The skill runs no `git pull`, and the context holds no `Pull:` line.

> **tasks:**
> - [ ] update `rule-git-context`
>   - set: `{purpose: Prevents a session from starting on a branch it does not know}`
>   - sections.Purpose:
>     ```
>     Prevents a session from starting on a branch it does not know.
>
>     **Branch tells us what kind of start this is.** On `main` or a working branch, no plan is
>     open. On a plan branch, unfinished work exists and becomes the first Frontier item. This is
>     never restated in `brief.md` — git already knows, and a second source of truth eventually
>     disagrees with the first.
>     ```
>   - sections.Render:
>     ```
>     <!-- rule-git-context -->
>     Render: !`uv run guppi render --sync`
>     Branch: !`git branch --show-current`
>     Status: !`git status --short`
>     <!-- /rule-git-context -->
>     ```
>   - sections.How it works:
>     ```
>     The `Render:` line runs `uv run guppi render --sync` once more inside `/hi`, after the `SessionStart` hook has run it; a diff on that line is a Frontier item like the one of the session start (case 115). The repository has no remote since case 528: `origin` was the product repository this vault was split from and `migration` had no upstream, so the pull that stood first in this block failed at every session start. `/hi` runs no `git pull`; a Case that adds a remote writes its pull line and its rule again.
>     ```
>   - change: `taken up: the pull leaves /hi with the remote; the rule keeps the render, the branch and the status; the defers of cases 220 and 243 retired (case 528.1)`
> - [ ] update `estimate-git-context-current`
>   - set: `{status: pending, purpose: "At /hi the context holds the render sync, the branch and the status, and the skill runs no git pull", method: "by hand at the /hi of a session after the render, the first turn's context and the output of git remote, written into the estimate line"}`
>   - change: `the Criterion replaced whole — no Pull line, no git pull, no remote; the promise on a pull mid-session gone with the pull (case 528.1)`
> - [ ] by hand: `git remote remove origin`, then `git remote` prints nothing
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] read `estimate-git-context-current` — by hand at the /hi of a session after the render

> **ratification:**
> ```
> - decision[case 528.1][update][rule-git-context]{ref:rule-git-context}{supersedes:case 220}{supersedes:case 243}
> - decision[case 528.1][update][estimate-git-context-current]{ref:estimate-git-context-current}
> ```

### Case 528.2 — `rule-github-issues` leaves the harness

> **given:**
> `rule-github-issues` — the rule of the `Open issues:` line of `/hi`, deleted
> **＋** `estimate-github-issues-listed` — its promise, deleted with it
> **＋** `rule-cleanup` — moves a deleted page to the archive and takes its slug out of `children` and `estimates`
> **＋** `vault/archive/` — where `cleanup` puts the deleted pages
> **＋** `entity-glossary` — the table whose row Issue points at the rule
> **＋** `vault/wiki/glossary.md` — the render of that table
> **＋** `rule-ledger-tail` — its How it works places the `Tail:` line after the rule
> **＋** `rule-git-context` — the block that the `Tail:` line follows after the change

> **when:**
> `uv run guppi cleanup` runs at the librarian's run after the Case is applied, and then `uv run guppi glossary` runs.

> **then:**
> `rule-github-issues` and `estimate-github-issues-listed` stand under `vault/archive/`, and no live page lists them in `children` or `estimates`.
> **＋** The table of `entity-glossary` and `vault/wiki/glossary.md` hold no row Issue.
> **＋** `rule-ledger-tail` places the `Tail:` line after `rule-git-context`.
> **－** The other rows of the table of `entity-glossary` do not change.

> **tasks:**
> - [ ] delete `rule-github-issues`
>   - impact: `The Open issues line leaves /hi with the remote; cleanup moves the page to the archive and takes it out of the children of rule-skill-hi; the defers of cases 220 and 243 retired (case 528.2)`
> - [ ] delete `estimate-github-issues-listed`
>   - impact: `Its rule is gone; no gh command runs at /hi to read (case 528.2)`
> - [ ] update `entity-glossary`
>   - old: `` | Issue | Tracked on GitHub; never a page, a `ref` only | [[rule-github-issues]] | | Work Mode | ``
>   - new: `| Work Mode |`
>   - change: `the row Issue removed: rule-github-issues left the harness with the remote (case 528.2)`
> - [ ] update `rule-ledger-tail`
>   - old: `` after `rule-github-issues`; ``
>   - new: `` after `rule-git-context`; ``
>   - change: `the Tail line follows the git lines: rule-github-issues left the harness (case 528.2)`
> - [ ] `uv run guppi glossary`

> **ratification:**
> ```
> - decision[case 528.2][delete][rule-github-issues]{ref:rule-github-issues}{supersedes:case 220}{supersedes:case 243}
> - decision[case 528.2][delete][estimate-github-issues-listed]{ref:estimate-github-issues-listed}
> - decision[case 528.2][update][entity-glossary]{ref:entity-glossary}
> - decision[case 528.2][update][rule-ledger-tail]{ref:rule-ledger-tail}
> ```

### Case 528.3 — The frame of `/hi` holds no pull and no issues

> **given:**
> `rule-skill-hi` — the rule that renders the frame of `/hi`, its `description` and its `allowed-tools`
> **＋** `estimate-hi-no-read-calls` — its promise on the blocks of the first turn, whose Criterion is replaced whole
> **＋** `rule-session-start` — the parent that explains the Leaves of `/hi` and the sources of the Frontier
> **＋** `.claude/skills/hi/SKILL.md` — the skill file
> **＋** `rule-internal-context` — the block of the loaded files
> **＋** `rule-git-context` — the block of the git lines
> **＋** `rule-ledger-tail` — the block of the tail

> **when:**
> The person invokes `/hi`, and Claude Code expands `.claude/skills/hi/SKILL.md` before the agent's first turn.

> **then:**
> The context of the first turn holds the output of each block of the skill, in the order of the children of `rule-skill-hi`: the text of the files `rule-internal-context` loads, the lines `Render:`, `Branch:` and `Status:` of `rule-git-context`, and the line `Tail:` of `rule-ledger-tail`.
> **＋** The `allowed-tools` of the skill names `uv run guppi render --sync`, `git branch --show-current`, `git status --short` and `uv run guppi tail`, and neither `git pull` nor `gh`.
> **－** The agent makes no read-tool call to get any of them.

> **tasks:**
> - [ ] update `rule-skill-hi`
>   - old: `description: Open a working session — sprint, brief, git state, open issues, then the Frontier.`
>   - new: `description: Open a working session — sprint, brief, git state, then the Frontier.`
>   - old: `allowed-tools: Bash(git pull --ff-only:*), Bash(uv run guppi render --sync), Bash(git branch --show-current), Bash(git status --short), Bash(gh issue list:*), Bash(uv run guppi tail)`
>   - new: `allowed-tools: Bash(uv run guppi render --sync), Bash(git branch --show-current), Bash(git status --short), Bash(uv run guppi tail)`
>   - old: `<!-- rule-git-context --> <!-- rule-github-issues -->`
>   - new: `<!-- rule-git-context -->`
>   - old: `the four children splice into the markers below`
>   - new: `the three children splice into the markers below`
>   - old: `` `allowed-tools` names the six `!` commands of the skill ``
>   - new: `` `allowed-tools` names the four `!` commands of the skill ``
>   - change: `the frame without the pull and the issues: description, allowed-tools and the marker of rule-github-issues (case 528.3)`
> - [ ] update `estimate-hi-no-read-calls`
>   - set: `{status: pending}`
>   - change: `the Criterion replaced whole — no Pull and no Open issues line; allowed-tools names neither git pull nor gh (case 528.3)`
> - [ ] update `rule-session-start`
>   - old: `` `git pull` and `gh issue list` fail differently, on merge conflicts versus authentication, so they are separate. ``
>   - new: `The git commands fail apart from the imports, so they are a Leaf of their own.`
>   - old: `` `brief.md` + `sprint.md` + open issues, plus ``
>   - new: `` `brief.md` + `sprint.md` + the git state and the tail, plus ``
>   - change: `no pull and no issues at /hi: the git Leaf and the sources of the Frontier (case 528.3)`
> - [ ] `uv run guppi render`: `.claude/skills/hi/SKILL.md`
> - [ ] read `estimate-hi-no-read-calls` — by hand at the /hi of a session after the render

> **ratification:**
> ```
> - decision[case 528.3][update][rule-skill-hi]{ref:rule-skill-hi}
> - decision[case 528.3][update][estimate-hi-no-read-calls]{ref:estimate-hi-no-read-calls}
> - decision[case 528.3][update][rule-session-start]{ref:rule-session-start}
> ```

### Case 528.5 — The leftovers promise reads what git tracks and names the remote decision

> **given:**
> `estimate-sprint-migration-leftovers-gone` — the promise, whose Criterion is replaced whole
> **＋** `entity-sprint-migration` — the sprint page, its Slice 5 items and its Closed note; `vault/wiki/sprint.md` renders it
> **＋** `rule-raw-archive` — keeps `event_log.md` in `vault/raw/<date>/`
> **＋** `vault/parked/` — the parked pages, deleted by case 510
> **＋** `docs/` — the documents of 2026-08, the rule documents of `docs/migration/`, and `docs/migration/migration-plan.md`
> **＋** `vault/archive/` — the archive and its roots
> **＋** `vault/raw/` — the date folders `vault/raw/<date>/` and their session folders `vault/raw/<date>/<HHMM>/`
> **＋** `.claude/skills/hi/SKILL.md` — the skill file that ran `git pull` and `gh`

> **when:**
> Someone reads the tree of the repository at the close of the sprint.

> **then:**
> `vault/parked/` is absent: its pages were deleted by a decision named in the reading, and git history keeps them.
> **＋** Under `docs/` no 2026-08 document remains, and no rule document of `docs/migration/`; each became a page, was archived, or was deleted by a decision named in the reading.
> **＋** `vault/archive/` has no root outside the folders of its sprints, and the decision that deleted the old root is named in the reading.
> **＋** Every file under `vault/raw/` that git tracks lies in a session folder `vault/raw/<date>/<HHMM>/`.
> **＋** The repository has no remote, and `.claude/skills/hi/SKILL.md` runs neither `git pull` nor `gh`; the decision is named in the reading.
> **－** `docs/migration/migration-plan.md` is outside this promise: the Case that closes the sprint deletes it.
> **－** The `event_log.md` of a past date stays in `vault/raw/<date>/`, as `rule-raw-archive` keeps it, and does not fail this promise.

> **tasks:**
> - [ ] update `estimate-sprint-migration-leftovers-gone`
>   - set: `{status: pending, purpose: "vault/parked/, the 2026-08 documents and the old archive root are gone, git tracks no raw date folder without a session, and the repository has no remote, each by a decision named at the close of the sprint"}`
>   - change: `the Criterion replaced whole — the raw date folders read by what git tracks, the remote removed and git pull and gh out of /hi, the old archive root deleted by case 102.1 (case 528.5)`
> - [ ] update `entity-sprint-migration`
>   - old: `` `vault/parked/` and the documents of 2026-08 under `docs/` deleted (case 510); the old archive root, the empty raw date folders, `git pull` and `gh`, and the reading, at the close ``
>   - new: `` `vault/parked/` and the documents of 2026-08 under `docs/` deleted (case 510), the old archive root (case 102.1); the raw date folders read by what git tracks, the remote and `git pull` and `gh` out of `/hi` (case 528); the reading at the close ``
>   - old: `` `make test` green, `migration` merged into `main`; at the close [[rule-git-context]] and [[rule-github-issues]] — the upstream of the branch and the GitHub remote, decisions 11.1, 11.2, defers 220, 243 — read by [[estimate-sprint-migration-leftovers-gone]] ``
>   - new: `` `make test` green, `migration` merged into `main` ``
>   - old: `` Kept without a page: `git pull` in `/hi` without an upstream (decision 11.1); `gh` not logged in, no GitHub remote (11.2) — both decided again at the close (`estimate-sprint-migration-leftovers-gone`). ``
>   - new: `` `git pull` and `gh` left `/hi` with the remote of the product repository, kept since decisions 11.1 and 11.2 (case 528). ``
>   - change: `Slice 5: the raw date folders, git pull and gh decided; the remote removed; the merge item no longer names the two rules (case 528.5)`
> - [ ] `uv run guppi sprint`
> - [ ] read `estimate-sprint-migration-leftovers-gone` — by hand on the tree at the close of the sprint

> **ratification:**
> ```
> - decision[case 528.5][update][estimate-sprint-migration-leftovers-gone]{ref:estimate-sprint-migration-leftovers-gone}
> - decision[case 528.5][update][entity-sprint-migration]{ref:entity-sprint-migration}
> ```
