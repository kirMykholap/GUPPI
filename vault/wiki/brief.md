# Brief — 2026-10-16, librarian of session 0342

## Where things stand

- Session 0342 of the sprint `plugin`. Cases ratified: 851 (851.1, 851.2, 851.3), 852 (852.1, 852.2), 853, and the short defer 855 (handoff).
- Code: `.guppi/guppi/gitstate.py` (new, `guppi gitstate`) and `.guppi/guppi/cli.py`; test `.guppi/tests/test_gitstate.py` (new, 4 tests). The `stop:` box of the tag `prod-0.2.0` in `vault/archive/plugin/2026-10-15/0553/raw/spec.md` is ticked. The two installer commands of the new step 1 of `rule-plugin-install` were read against the installation page of `uv` and match. `guppi test` 1719 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- The session's readings: at `/hi` L1, L2, L3, L4, L14, L16; at Retro L19. Lessons L20, L21.
- `guppi materialize` printed `written with 21 entries` for `vault/raw/2026-10-16/0342/materialize.yaml` and `extended with 0 entries` for the yaml of `0104`. The yaml holds 20 entries for the 21 lines of the ledger (L19 folded into the create of L18) and 3 of the synthesis, 23 in all, each marked `applied`: 6 `estimate`, 2 `lesson`, 5 `create`, 9 `update`, 1 `defer` (marked `exists`). One entry is marked `near`; none `failed`, `incomplete` or `merged`; `unparsed: []`.
- The ledger has 21 lines; the yaml accounts for each of them.
- Pages created (16): decisions 9 (851, 851.1, 851.2, 851.3, 852, 852.1, 852.2, 853, 855), estimates 4, lessons 2, insights 1. Pages updated (14): estimates 8, rules 5 (`rule-git-context`, `rule-skill-hi` and `rule-default-mode` by Case 851.1; `rule-plugin-install` by Case 852.1, then 853; `rule-harness` `draft` → `built` by the cascade), lessons 1. The cascade set `rule-git-context` and `rule-plugin-install` `built` → `draft`. `guppi generate` printed 30 pages for `0342` and 0 for `0104`.
- `generate` ticked 15 boxes of `vault/raw/2026-10-16/0342/spec.md` and the `read` boxes of `estimate-guppi-package-runs-from-its-own-folder`, `estimate-clean-branch-installs-as-a-plugin` and `estimate-guppi-package-is-ready-after-the-install` in `vault/raw/2026-10-16/0104/spec.md`.
- The handoff's instructions: the yaml applies Case 852.1 (line 9) before 853 (line 12), and the `failed` reading L4 of `estimate-guppi-package-is-ready-after-the-install` (line 4) before the update of Case 852.2 (line 11), which set it `pending`. After the render, `.claude/skills/hi/SKILL.md` runs `uv run --project .guppi guppi gitstate` on its `Branch:` line, and its `allowed-tools` names that command and no `git init`.
- `guppi cleanup` moved 0 pages. `guppi render` changed `.claude/skills/hi/SKILL.md` and `plugin/skills/install/SKILL.md`. `guppi sprint` and `guppi glossary` changed nothing. `guppi backlog`: `backlog.md` from 15 to 17 items (`estimate-clean-branch-writes-the-session-files`, `insight-case-build-opens-a-new-case-where-one-was-named`).
- `guppi archive` printed nothing and moved no unit. It does not walk `raw/2026-10-16/0342`, the session of this run, or `raw/2026-10-16/0104`, dated today; `raw/2026-10-14/1907` holds no `ledger.md`.
- Index check: the two `create` entries of lessons were compared by the Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 52 lines; the four `create` entries of estimates have no index. `lesson-case-build-rebuilds-a-ratified-case-under-a-new-number-in-plan-mode` is marked `near: lesson-case-build-opens-a-new-case-for-a-task-asked-into-its-own`.
- Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/`: 52 lines. `^(pattern|deferred_by):` over `vault/wiki/insights/`: 7 lines.
  - `lesson-case-build-rebuilds-a-ratified-case-under-a-new-number-in-plan-mode` joined `lesson-case-build-opens-a-new-case-for-a-task-asked-into-its-own` under the new `insight-case-build-opens-a-new-case-where-one-was-named` (status `open`, severity 2): in both, case-guppi put a new Case number where the main agent had named the Case to change.
  - `lesson-case-build-claims-a-page-stands-without-reading-the-path-it-changes`: none; its cause is a check of the readers on the old path only, and the nearest line, `insight-case-build-claims-what-code-does-without-reading-it`, names a claim on code made without reading the function.

## Readings due

- `estimate-clean-branch-ships-neutral-texts` (failed) — `rule-clean-branch` (draft) — by its `method`: after a tag `prod-x.y.z` and the librarian's run of the session that set the `method`, `guppi ship --allow-draft` into an empty folder, read against the Criterion. Result: `/hi` of session 0342 (L2), it fails on three sentences true only in the repository of GUPPI — the `core` field of the Render of `rule-rules-schema` and of `rule-entities-schema`, and a sentence of `rule-ratification` — and on four shipped Estimates. This run: no step ran `guppi ship`.
- `estimate-clean-branch-writes-the-session-files` (failed, `deferred_by` case 855) — `rule-clean-branch` (draft) — by its `method`: `test_ship.py -k skeleton`, then after a tag `prod-x.y.z` an install in an empty project, `/hi`, and the three `--check` commands over the copy. Result: Retro of session 0104, the three checks exit 0, and the first `/hi` in `C:\PROJECTS\test`, no git repository, stopped on `fatal: not a git repository`.
- `estimate-git-context-offers-git-init` (pending) — `rule-git-context` (draft) — by `read` at line 124 of `vault/raw/2026-10-16/0342/spec.md`; by hand after the librarian's run: an install into an empty folder with no git, `/hi` answered no, then yes, then `/hi` again. This run: the render wrote `.claude/skills/hi/SKILL.md`, whose `Branch:` line runs `uv run --project .guppi guppi gitstate` and is followed by the step for `none: this folder is no git repository`; its `allowed-tools` does not name `git init`.
- `estimate-hi-no-read-calls` (pending) — `rule-skill-hi` (draft) — by `read` at line 156 of `vault/raw/2026-10-16/0342/spec.md`; by hand at the first `/hi` after this run, its transcript. This run: the `allowed-tools` of `.claude/skills/hi/SKILL.md` after the render names `uv run --project .guppi guppi render --sync`, `uv run --project .guppi guppi gitstate` and `uv run --project .guppi guppi tail`, and no `git pull`, `git init` or `gh`.
- `estimate-plugin-install-offers-to-install-uv` (pending) — `rule-plugin-install` (draft) — by `read` at line 279 of `vault/raw/2026-10-16/0342/spec.md`; by hand after the librarian's run with a tag `prod-x.y.z` in the history of HEAD: an install from a terminal with no `uv`, answered no, then yes. This run: the render wrote step 1 of `plugin/skills/install/SKILL.md` with the offer and the two installer commands; `git tag --merged HEAD` prints `prod-0.2.0`.
- `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` (pending) — `rule-plugin-install` (draft) — by `read` at line 378 of `vault/raw/2026-10-16/0342/spec.md`; by hand after the librarian's run with a tag `prod-x.y.z` in the history of HEAD: an install offline with an empty cache of `uv`. This run: the render wrote step 6 of `plugin/skills/install/SKILL.md`, which deletes what step 4 copied when `uv sync` fails; `git tag --merged HEAD` prints `prod-0.2.0`.
- `estimate-guppi-package-is-ready-after-the-install` (pending) — `rule-guppi-package` (draft) — by `read` at line 314 of `vault/raw/2026-10-16/0342/spec.md`; by hand after a tag `prod-x.y.z`: an install in an empty project with `uv`, `/hi`, and the person's answer.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` (pending) — `entity-sprint-plugin` (draft) — by its `method`: `test_ship.py`, then a run of `prod.yml` on a tag `prod-x.y.z` that writes `prod`, before the close of `plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` (pending) — `entity-sprint-plugin` (draft) — by its `method`: in a session of the sprint before its close.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` (pending) — `entity-sprint-plugin` (draft) — by its `method`: a pull request from a second account, before the close.
- `estimate-sprint-plugin-close-steps-run-from-the-line` (pending) — `entity-sprint-plugin` (draft) — by its `method`: at the end of Work Mode of the session that closes the sprint.
- `estimate-sprint-plugin-readme-describes-the-project` (pending) — `entity-sprint-plugin` (draft) — by its `method`: the person's answer at the `/hi` after the session that writes `README.md`, before the close.
- `estimate-hi-writes-frontier` (pending) — `rule-skill-hi` (draft) — by its `method`: the person's answer in the session after the close of a sprint.
- `estimate-skill-pr-review-takes-a-pull-request-whole` (pending) — `rule-skill-pr-review` (draft) — by its `method`: after the first pull request from another account merged by `/pr-review` after the close of `plugin`; not seen.
- `estimate-morph-sets-up-the-project-at-the-first-hi` (pending) — `rule-morph` (draft) — by its `method`: after the session whose Work Mode builds the setup skill of `rule-morph`; not seen.
- `estimate-ratification-ledger-line-form` (pending) — `rule-ratification` (draft) — by its `method`: after a session whose ledger holds a lesson with the Case that closes its cause, a Case that takes up a decision with more than one Case in its `deferred_by`, and a lesson line that declares a new tag; not seen: the ledger of 0342 holds two lessons and no Case that closes their cause.
- `estimate-skill-merge-main-joins-a-conflicted-page` (pending) — `rule-skill-merge-main` (draft) — by its `method`: after the first `/merge-main` whose merge leaves a conflicted page; not seen in `git log`.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (pending) — `rule-work-mode` (draft) — by its `method`: after the first `/work` on the rendered `.claude/skills/work/SKILL.md` in which a Case is ratified in Work Mode; not seen in the handoff of 0342.

## Flags

- `near`: `lesson-case-build-rebuilds-a-ratified-case-under-a-new-number-in-plan-mode` → `lesson-case-build-opens-a-new-case-for-a-task-asked-into-its-own` (both now clustered under `insight-case-build-opens-a-new-case-where-one-was-named`).
- Lint (`guppi check`, exit 1, 12 lines): draft pages with `core: true` — `entity-sprint`, `rule-git-context`, `rule-guppi-package`, `rule-morph`, `rule-ratification`, `rule-skill-hi`, `rule-work-mode`.
- Lint: `unread: failed` — `estimate-clean-branch-ships-neutral-texts`, `estimate-clean-branch-writes-the-session-files`.
- Lint: `method` — `estimate-guppi-tests-green` (a MOC's Estimate names no `make <target>` or `pytest` with test files), `estimate-harness-make-runs-in-both-shells` (the Makefile has no target with), `estimate-page-schemas-one-file-per-rule` (says by hand while `estimate-entities-schema-checked` names a test file).
- Failed Estimates: `estimate-clean-branch-ships-neutral-texts` (L2 of this session), `estimate-clean-branch-writes-the-session-files` (Retro of session 0104; deferred by case 855).
- `estimate-harness-pipeline` and `estimate-guppi-tests-green` are `passed` and keep `deferred_by` (cases 833 and 849; case 829), so `backlog.md` still lists them.
- Contradiction: the context of `decision-case-855` says that Case 851 makes `/hi` "go on to `/sprint-open`"; after /pre-spec, the `/hi` that runs `git init` ends, and the next `/hi` starts `/sprint-open` (handoff, Notes).
- The render wrote `plugin/skills/install/SKILL.md`, which lies outside the four paths of the close commit (`vault`, `CLAUDE.md`, `.claude`, `guppi.toml`); it stays modified after this run's commit.
- The reading L2 was a keyword grep, not a read of every sentence (handoff, Observations).
- `guppi caseid --session` takes the session id of the `hi:` line, not its HHMM; a first call with `0342` printed no id (handoff, Observations).
- `cases/case-856.md` is empty; no ledger line names case 856; the id 854 was printed for C6 and not used (handoff).
- One thing rests on no checked source: that Claude Code asks the person before a Bash call that `allowed-tools` does not name; the hand reading of `estimate-git-context-offers-git-init` checks it (handoff, Notes).

## Next session

### Cases

- Failed `estimate-clean-branch-ships-neutral-texts`: rewrite the three sentences named in Observations, and the Estimates listed in its reading, so that the clean version holds no sentence true only in the repository of GUPPI (handoff).
- The milestone item `rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch` was left for later: the seven draft pages with `core: true` stop every build of `prod`, and the next tag after `prod-0.2.0` is open (handoff).
- The four hand readings under `## Debt` wait for one install session: an empty folder with no git, a terminal with no `uv`, and an offline install, all from a copy built after the librarian's render (handoff).
- Failed Estimate `estimate-clean-branch-writes-the-session-files`: the first `/hi` stopped outside a git repository at Retro of session 0104; deferred by case 855 to after the render of Case 851, which this run made.
- Contradiction: the context of `decision-case-855` says that Case 851 makes `/hi` go on to `/sprint-open`, while the ratified Case 851 ends that `/hi` (handoff, Notes).
- Defect: the close commit of the librarian takes `vault`, `CLAUDE.md`, `.claude` and `guppi.toml` only, and the render writes `plugin/skills/install/SKILL.md`, so that file stays uncommitted after the run (this run, `git status`).

### Work

- `estimate-hi-no-read-calls` (its `read` box at line 156 of `vault/raw/2026-10-16/0342/spec.md`), at the first `/hi`.
- `estimate-git-context-offers-git-init` (its `read` box at line 124 of `vault/raw/2026-10-16/0342/spec.md`).
- `estimate-plugin-install-offers-to-install-uv` (its `read` box at line 279 of `vault/raw/2026-10-16/0342/spec.md`).
- `estimate-plugin-install-undoes-the-copy-when-uv-sync-fails` (its `read` box at line 378 of `vault/raw/2026-10-16/0342/spec.md`).
- Dirty tree: `plugin/skills/install/SKILL.md`, written by the render of this run and not in its commit.

### Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — this reading follows the new Criterion of Case 852.2. In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?

## Readings at the close

- `uv run --project .guppi guppi test`: 1719 passed, 6 skipped, 1 deselected (exit 0).
- `uv run --project .guppi guppi check`: 12 lines (exit 1), as in Flags.
- Pages (`.md`) under `vault/wiki/`: decisions 204, estimates 300, rules 86, lessons 54, insights 7, entities 5.
