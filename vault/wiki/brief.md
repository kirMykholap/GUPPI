# Brief — 2026-10-16, librarian of session 0104

## Where things stand

- Session 0104 of the sprint `plugin`. Cases ratified: 840 (840.1, 840.2), 841, 842, 843, 844, 845, 846, 847, 850, and the short defers 848 and 849.
- No code file and no test changed (handoff). Work Mode placed the local tag `prod-0.2.0` on the last commit of `plugin`; the person pushed it, and the run of `prod.yml` on it failed at "Build the clean version" on the seven draft pages with `core: true`; the branch `prod` on GitHub kept its last commit of 2026-10-14 (handoff).
- The session's readings: L1 at `/hi` (passed); at Retro L15 and L16 passed, L17 and L18 failed. Lessons L19, L20, L21.
- This run applied `vault/raw/2026-10-16/0104/materialize.yaml`: 24 entries — 21 from the 21 lines of the ledger, 3 of the synthesis — all marked `applied`: 5 `estimate`, 3 `lesson`, 1 `create`, 13 `update`, 2 `defer` (both marked `exists`). No entry is marked `failed`, `incomplete`, `near` or `merged`. The yamls of `2026-10-15/0553`, `1739` and `1959` were extended with 0 entries; `generate` wrote `superseded_by` marks into the yaml of `1959`.
- Pages created: decisions 13 (840, 840.1, 840.2, 841–850), lessons 3, insights 1. Pages updated: estimates 10, rules 3 (`rule-page-generation` by Case 840.1, `rule-guppi-package` deferred by Case 848, `rule-plugin-install` `draft` → `built` by the cascade), entities 1 (`entity-sprint-plugin`), lessons 1 (`lesson-subagents-parallel-on-one-tree-red-mid-flight`).
- Superseded and moved by `guppi cleanup` (4 pages): `decision-case-830`, `decision-case-831`, `decision-case-832`, `decision-case-837`, into `vault/archive/plugin/2026-10-16/0104/decisions/`. The `deferred_by` of case 831 stood on three live pages, `estimate-clean-branch-installs-as-a-plugin`, `estimate-plugin-install-writes-guppi-into-an-empty-project` and `estimate-guppi-package-is-ready-after-the-install`, the Estimates of Cases 842, 843 and 846; no other page carried it.
- After `generate`: `uv run --project .guppi pytest .guppi/tests/test_guppi_package.py`: 12 passed (the handoff asked for it).
- `guppi render` changed no file. `guppi sprint` changed one milestone line of `sprint.md`. `guppi backlog`: `backlog.md` from 19 to 15 items. `guppi glossary` changed nothing.
- `guppi archive` moved 3 units: `raw/2026-10-15/0553`, `1739` and `1959`, to `archive/plugin/2026-10-15/<hhmm>/raw`. Kept: `raw/2026-10-16/0104`, the session of this run; `raw/2026-10-14/1907`, which holds `cases` and `frontier.md` and no ledger.
- Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/`: 49 lines. `^(pattern|deferred_by):` over `vault/wiki/insights/`: 6 lines.
  - `lesson-case-build-reads-a-sibling-case-file-mid-rebuild` joined `lesson-subagents-parallel-on-one-tree-red-mid-flight` under the new `insight-subagents-read-a-sibling-mid-flight` (status `open`, severity 2): in both, an agent read what a sibling agent of the same run was still writing.
  - `lesson-hi-fails-outside-a-git-repository`: none; no index line names a skill that needs a git repository the install does not make.
  - `lesson-case-build-opens-a-new-case-for-a-task-asked-into-its-own`: none; its cause is case-guppi opening a new Case where the main agent named an existing one, and no index line names that.

## Readings due

- `estimate-clean-branch-ships-the-tests` (failed) — `rule-clean-branch` (draft) — by its `method`: `test_ship.py -k tests`, then after a tag `prod-x.y.z` a `guppi ship --allow-draft` and `pytest .guppi/tests` in that folder. Result: Retro of session 0104, 1 failed, 1655 passed, 15 skipped in the copy — the `[tests/]` test of `test_guppi_package.py` on `rule-page-generation` and `estimate-generate-rewords`.
- `estimate-clean-branch-writes-the-session-files` (failed) — `rule-clean-branch` (draft) — by its `method`: `test_ship.py -k skeleton`, then an install in an empty project and `/hi`. Result: Retro of session 0104, the first `/hi` in `C:\PROJECTS\test`, no git repository, stopped on `fatal: not a git repository` and did not start `/sprint-open`.
- `estimate-harness-pipeline` (failed) — `rule-harness` (draft) — by its `method`: `make test-harness` and `guppi check` by hand. Result: Retro of session 1739, not read; `guppi backlog --check` exited 1 then. Deferred by cases 833 and 849.
- `estimate-guppi-package-runs-from-its-own-folder` (pending) — `rule-guppi-package` (draft) — by `read` at line 118 of `vault/raw/2026-10-16/0104/spec.md`; after this librarian's run: `test_guppi_package.py`, then `/hi` in this repository and its hooks. This run: `pytest .guppi/tests/test_guppi_package.py` 12 passed after `generate` and after `render`; `guppi test` 1715 passed, 6 skipped, 1 deselected; no `/hi` ran in this run.
- `estimate-clean-branch-ships-neutral-texts` (pending) — `rule-clean-branch` (draft) — by `read` at line 1663 of `vault/archive/plugin/2026-10-15/0553/raw/spec.md`; after a tag `prod-x.y.z` and the librarian's run of the session that set the `method`: `guppi ship --allow-draft` into an empty folder, read against the Criterion. This run: no step ran `guppi ship`.
- `estimate-clean-branch-installs-as-a-plugin` (pending) — `rule-clean-branch` (draft) — by `read` at line 247 of `vault/raw/2026-10-16/0104/spec.md`; after a tag `prod-x.y.z`: `test_ship.py`, `guppi ship --allow-draft`, `claude plugin validate`, then the person's answer on the install.
- `estimate-guppi-package-is-ready-after-the-install` (pending) — `rule-guppi-package` (draft) — by `read` at line 508 of `vault/raw/2026-10-16/0104/spec.md` and line 774 of `vault/archive/plugin/2026-10-15/0553/raw/spec.md`; the three installs by hand and the person's answer.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` (pending) — `entity-sprint-plugin` (draft) — by `read` at line 166 of `vault/archive/plugin/2026-10-15/0553/raw/spec.md`; after a run of `prod.yml` on a tag `prod-x.y.z` that writes `prod`, before the close of `plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` (pending) — `entity-sprint-plugin` (draft) — by `read` at line 409 of `vault/archive/plugin/2026-10-15/0553/raw/spec.md`; in a session of the sprint before its close.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` (pending) — `entity-sprint-plugin` (draft) — by `read` at line 1238 of `vault/archive/plugin/2026-10-15/0553/raw/spec.md`; a pull request from a second account, before the close.
- `estimate-sprint-plugin-close-steps-run-from-the-line` (pending) — `entity-sprint-plugin` (draft) — by its `method`: at the end of Work Mode of the session that closes the sprint.
- `estimate-sprint-plugin-readme-describes-the-project` (pending) — `entity-sprint-plugin` (draft) — by its `method`: the person's answer at the `/hi` after the session that writes `README.md`, before the close.
- `estimate-hi-writes-frontier` (pending) — `rule-skill-hi` (draft) — by its `method`: the person's answer in the session after the close of a sprint.
- `estimate-skill-pr-review-takes-a-pull-request-whole` (pending) — `rule-skill-pr-review` (draft) — by its `method`: after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-morph-sets-up-the-project-at-the-first-hi` (pending) — `rule-morph` (draft) — by `read` at line 250 of `vault/archive/plugin/2026-10-15/0553/raw/spec.md` and line 610 of `vault/archive/plugin/2026-10-15/1959/raw/spec.md`; after the session whose Work Mode builds the setup skill of `rule-morph`; not seen.
- `estimate-ratification-ledger-line-form` (pending) — `rule-ratification` (draft) — by `read` at line 859 of `vault/archive/plugin/2026-10-15/1959/raw/spec.md`; after a session whose ledger holds a lesson with the Case that closes its cause, a Case that takes up a decision with more than one Case in its `deferred_by`, and a lesson line that declares a new tag; not seen in one session.
- `estimate-skill-merge-main-joins-a-conflicted-page` (pending) — `rule-skill-merge-main` (draft) — by its `method`: after the first `/merge-main` whose merge leaves a conflicted page; not seen.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (pending) — `rule-work-mode` (draft) — by its `method`: after the first `/work` on the rendered `.claude/skills/work/SKILL.md` in which a Case is ratified in Work Mode; not seen.

## Flags

- Lint (`guppi check`, exit 1, 13 lines): draft pages with `core: true` — `entity-sprint`, `rule-guppi-package`, `rule-harness`, `rule-morph`, `rule-ratification`, `rule-skill-hi`, `rule-work-mode`.
- Lint: `unread: failed` — `estimate-clean-branch-ships-the-tests`, `estimate-clean-branch-writes-the-session-files`, `estimate-harness-pipeline`.
- Lint: `method` — `estimate-guppi-tests-green` (a MOC's Estimate names no `make <target>` or `pytest` with test files), `estimate-harness-make-runs-in-both-shells` (the Makefile has no target with), `estimate-page-schemas-one-file-per-rule` (says by hand while `estimate-entities-schema-checked` names a test file).
- Failed Estimates: `estimate-clean-branch-ships-the-tests` (L17 of this session), `estimate-clean-branch-writes-the-session-files` (L18 of this session), `estimate-harness-pipeline` (deferred by cases 833 and 849).
- The run of `prod.yml` on the tag `prod-0.2.0` failed and wrote nothing to `prod` (handoff).
- At the offline install, `uv sync --project .guppi` failed on `ruff==0.16.1` of the `dev` group, and the last sentence still told the person to type `/hi`; `.guppi/.venv/` was left unbuilt (handoff, Observations).
- The auto mode classifier refused `git push origin prod-0.2.0` and a command line with `git ls-remote origin` beside `gh run list` (handoff).
- `claude plugin validate` passed on the clean copy with two warnings: the catalogue has no description; `CLAUDE.md` at the root of the plugin is not loaded as context (handoff).
- The `stop:` box at line 165 of `vault/archive/plugin/2026-10-15/0553/raw/spec.md` (the tag `prod-0.2.0`) stays unticked, while Case 841 took it up and the tag stands and was pushed (handoff).

## Next session

### Cases

- `/hi` in a project that is no git repository: it should go on and tell the person to run `git init`, or offer to run it (the person's word; `lesson-hi-fails-outside-a-git-repository`).
- `/guppi:install` with no `uv`: whether it offers to install `uv` (the person's word).
- `/guppi:install` when `uv sync` fails offline: the person asks to discuss it again; whether `uv sync` should take the `dev` group in a user's project at all.
- The draft core pages that stop every build of `prod`, and the next tag after `prod-0.2.0`, which the push of this session spent.
- The tag `prod-0.2.0` stands on GitHub on a commit whose run failed; whether it stays.
- Failed Estimate `estimate-clean-branch-ships-the-tests`: L17 failed in the copy on the `[tests/]` test of `test_guppi_package.py`; after this run that test passes in the repository.
- Failed Estimate `estimate-clean-branch-writes-the-session-files`: L18 failed, the first `/hi` stopped outside a git repository.
- Failed Estimate `estimate-harness-pipeline`: not read at Retro of session 1739; deferred by cases 833 and 849.

### Work

- `estimate-guppi-package-runs-from-its-own-folder`
- `estimate-clean-branch-ships-neutral-texts`
- The `stop:` box at line 165 of `vault/archive/plugin/2026-10-15/0553/raw/spec.md`, unticked.

### Ask the person

- `estimate-clean-branch-installs-as-a-plugin` — needs the person — in session 0104 the person added `scratchpad/ship-plugin` as a catalogue and installed `guppi` from it, and said it installed; did the catalogue add and the plugin install with no error?
- `estimate-guppi-package-is-ready-after-the-install` — needs the person — in session 0104 the person reported: in `C:\PROJECTS\test-no-uv` the install said `uv` is missing and wrote nothing; in `C:\PROJECTS\test` it built `.guppi/.venv/` and the hooks ran at the first `/hi`; in `C:\PROJECTS\test-uv-offline` `uv sync` failed and it stopped, but told the person to type `/hi` after a fix. Does that pass the Criterion?

## Readings at the close

- `uv run --project .guppi guppi test`: 1715 passed, 6 skipped, 1 deselected (exit 0).
- `uv run --project .guppi guppi check`: 13 lines (exit 1), as in Flags.
- Pages (`.md`) under `vault/wiki/`: decisions 195, estimates 296, rules 86, lessons 52, insights 6, entities 5.
