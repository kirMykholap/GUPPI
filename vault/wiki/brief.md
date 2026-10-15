# Brief — 2026-10-15, librarian of session 1959

## Where things stand

- Session 1959 of the sprint `plugin`. Cases ratified: 823 (823.1–823.6), 824, 825, 826, 827 (827.1–827.4), and the short defers 828–839.
- Code: `.guppi/guppi/prespec.py` (an Estimate of a core target judged for pointers), `.guppi/guppi/materialize.py` (a lesson's `newtag` block reaches `new_tags`), `.guppi/guppi/tags.py` (`lesson_tags`), `.guppi/guppi/ledger.py` (`refused_tags` takes declared tags; `tag_message`). Tests in `test_prespec.py`, `test_ledger.py`, `test_materialize.py`, and one test of `test_ship.py` marked `live`. The marker `live` and `addopts = '-m "not live"'` stand in `.guppi/pyproject.toml` and in the root `pyproject.toml`.
- By hand: the header of `vault/wiki/tags.md` (Case 827.4). `plugin/skills/install/SKILL.md` is committed.
- The session's readings: L1–L5 at `/hi` (L5 failed), L66–L72 at Retro, all passed; L72 is folded into the `create` of `estimate-materialize-lifts-a-tag-of-a-lesson`. Lesson L73.
- This run applied `vault/raw/2026-10-15/1959/materialize.yaml`: 75 entries — 72 from the ledger, 3 of the synthesis — all marked `applied`: 11 `estimate`, 1 `lesson`, 3 `create`, 44 `update`, 16 `defer` (all 16 marked `exists`). The yamls of `0553` and `1739` were extended with 0 entries.
- Pages created: decisions 27, estimates 2 (`estimate-clean-branch-ships-estimates-with-pointers-only-in-brackets`, `estimate-materialize-lifts-a-tag-of-a-lesson`), lessons 1, insights 1. Pages updated: estimates 32, rules 18, entities 2, lessons 5, insights 1.
- `tags.md` gained the rows `retro` and `box`, from the `new_tags` of the yaml (Case 826).
- `guppi cleanup` moved 0 pages. The render changed `.claude/agents/librarian-guppi.md` and `vault/wiki/ratification.md`; `vault/wiki/case-schema.md`, `.claude/agents/case-guppi.md`, `CLAUDE.md` and `guppi.toml` stand unchanged on disk. `guppi glossary` changed 3 rows of `glossary.md`. `guppi backlog`: `backlog.md` from 6 to 19 items.
- `guppi archive` printed nothing and moved no unit: `raw/2026-10-15/0553`, `1739` and `1959` are of the run day; `raw/2026-10-14/1907` holds no ledger.
- Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/`: 48 lines. `^(pattern|deferred_by):` over `vault/wiki/insights/`: 4 lines.
  - `lesson-case-build-names-a-pytest-config-the-root-run-does-not-read` joined `lesson-case-build-recommended-an-unchecked-github-fact` under the new `insight-case-build-rests-on-an-unchecked-fact-of-a-tool` (status `open`): both Cases rested on a fact of an outside tool (GitHub, pytest) that nothing checked before ratification.

## Readings due

- `estimate-guppi-package-runs-from-its-own-folder` (failed) — `rule-guppi-package` (draft) — by its `method`: `test_guppi_package.py` and, by hand after the librarian's run of the session whose Work Mode moves the code, the hooks of `/hi`. Result: L5, the `/hi` of session 1959: 1 failed, 11 passed, `test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it[tests/]` on `rules/rule-page-generation` and `estimates/estimate-generate-rewords`. Deferred by case 837. This run: `guppi test` printed 1 failed (the same test), 1714 passed, 6 skipped, 1 deselected.
- `estimate-clean-branch-installs-as-a-plugin` (failed) — `rule-clean-branch` (draft) — by its `method`: `test_ship.py` and, by hand after the Work Mode, `guppi ship --allow-draft` into an empty folder and an install. Result: Retro of session 1739, not read; `guppi ship --allow-draft` exits 1 with no tag `prod-x.y.z`. Deferred by case 831.
- `estimate-plugin-install-writes-guppi-into-an-empty-project` (failed) — `rule-plugin-install` (draft) — by its `method`: `test_ship.py -k plugin_skill` and, by hand after the Work Mode, a local copy and `/guppi:install` in two empty projects. Result: Retro of session 1739, not read; no local copy with no tag `prod-x.y.z`. Deferred by case 831.
- `estimate-harness-pipeline` (failed) — `rule-harness` (draft) — by its `method`: `make test-harness` and `guppi check` by hand. Result: Retro of session 1739, not read; `guppi backlog --check` exited 1 then. Deferred by case 833.
- `estimate-clean-branch-ships-estimates-with-pointers-only-in-brackets` (pending) — `rule-clean-branch` (draft) — read box at line 177 of `vault/raw/2026-10-15/1959/spec.md`; by hand after the librarian's run of this session: `pytest .guppi/tests/test_ship.py -m live`. This run: `generate` wrote the `method` of the 12 Estimates of Case 823.1 and the Criteria of Cases 823.2–823.6; `pytest -m live` is no step of this run and was not run; `guppi test` deselected 1 test.
- `estimate-clean-branch-ships-neutral-texts` (pending) — `rule-clean-branch` (draft) — read box at line 1663 of `vault/raw/2026-10-15/0553/spec.md`; its `method` waits for a tag `prod-x.y.z` in the history of HEAD — `git tag` holds `prod-1` and `prod-2` only — and the librarian's run of the session of case 824, which is this run. This run ran no `guppi ship`.
- `estimate-clean-branch-ships-the-tests` (pending) — `rule-clean-branch` (draft) — read box at line 1446 of `vault/raw/2026-10-15/0553/spec.md`; by hand after the librarian's run of its change, `guppi ship --allow-draft`. This run ran no `guppi ship`; `guppi test` ran `.guppi/tests/test_ship.py` with no failure, its `live` test deselected.
- `estimate-clean-branch-writes-the-session-files` (pending) — `rule-clean-branch` (draft) — read box at line 1501 of `vault/raw/2026-10-15/0553/spec.md`; by hand after the librarian's run of its change, an install from a copy of `guppi ship --allow-draft`. This run ran no `guppi ship`.
- `estimate-guppi-package-is-ready-after-the-install` (pending) — `rule-guppi-package` (draft) — read box at line 774 of `vault/raw/2026-10-15/0553/spec.md`; deferred by cases 831 and 832. This run ran no `guppi ship`.
- `estimate-morph-sets-up-the-project-at-the-first-hi` (pending) — `rule-morph` (draft) — read box at line 610 of `vault/raw/2026-10-15/1959/spec.md`; its `method` waits for the session whose Work Mode builds the setup skill of `rule-morph`; not seen.
- `estimate-ratification-ledger-line-form` (pending) — `rule-ratification` (draft) — read box at line 859 of `vault/raw/2026-10-15/1959/spec.md`; its `method` waits for a session whose ledger holds a lesson with the Case that closes its cause, a Case that takes up a decision with more than one Case in its `deferred_by`, and a lesson line that declares a new tag; not seen.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` (pending) — `entity-sprint-plugin` (draft) — read box at line 166 of `vault/raw/2026-10-15/0553/spec.md`; a run of `prod.yml` on a tag `prod-x.y.z`, before the close of `plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` (pending) — `entity-sprint-plugin` (draft) — read box at line 409 of `vault/raw/2026-10-15/0553/spec.md`; a session of `plugin` before its close.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` (pending) — `entity-sprint-plugin` (draft) — read box at line 1238 of `vault/raw/2026-10-15/0553/spec.md`; a pull request from a second account, before the close of `plugin`.
- `estimate-sprint-plugin-close-steps-run-from-the-line` (pending) — `entity-sprint-plugin` (draft) — by its `method`: the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-readme-describes-the-project` (pending) — `entity-sprint-plugin` (draft) — by its `method`: the person's answer at the `/hi` of the session after the one whose Work Mode writes `README.md`.
- `estimate-hi-writes-frontier` (pending) — `rule-skill-hi` (draft) — by its `method`: the person's answer in the session after the close of a sprint.
- `estimate-skill-merge-main-joins-a-conflicted-page` (pending) — `rule-skill-merge-main` (draft) — by its `method`: after the first `/merge-main` whose merge of main leaves a conflicted page; no merge commit in `git log`.
- `estimate-skill-pr-review-takes-a-pull-request-whole` (pending) — `rule-skill-pr-review` (draft) — by its `method`: after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (pending) — `rule-work-mode` (draft) — by its `method`: after the first `/work` on the rendered `.claude/skills/work/SKILL.md` in which a Case is ratified in Work Mode; not seen.

## Flags

- `incomplete`, `failed`, `near`, `unparsed`: none in the yaml of 1959; `unparsed: []`.
- Failed Estimates: `estimate-guppi-package-runs-from-its-own-folder` (failed at L5 of this session), `estimate-clean-branch-installs-as-a-plugin`, `estimate-plugin-install-writes-guppi-into-an-empty-project`, `estimate-harness-pipeline`; each carries a `deferred_by` of this session.
- Contradiction: the Criterion of `estimate-guppi-package-runs-from-its-own-folder` (no live page names a path of the tests outside `.guppi/`) against the text of Case 819.2 in `rule-page-generation` and `estimate-generate-rewords`, which names `tests/` as the example of a pair; its test stays red. Case 837 defers the Estimate.
- The handoff's check of Cases 824 and 825 on `rule-morph` and `rule-permissions`: each `old` of the `replace` pairs of both Cases stood once on its page before `generate`; `generate` printed nothing on stderr and marked no entry `failed`. On `rule-morph`, Case 825 does not rename by `replace` pairs, as the handoff says: it sets `purpose` and replaces the section `Purpose` whole; its new text holds the two changes of Case 824 ("the repository of GUPPI"). On `rule-permissions`, the `old` of Case 825 (`whose initiation at install sets the folder name`) stands after the colon of the sentence whose start Case 824 changes.
- `guppi check`: exit 1, 14 lines:
  - `status: a page with core: true that is draft` on `entity-sprint`, `rule-guppi-package`, `rule-harness`, `rule-morph`, `rule-ratification`, `rule-skill-hi`, `rule-work-mode`;
  - `unread: failed` on the 4 failed Estimates;
  - `method` on `estimate-guppi-tests-green` and `estimate-page-schemas-one-file-per-rule` (deferred by case 829);
  - `method` on `estimate-harness-make-runs-in-both-shells`: "the Makefile has no target with" (`rule-lint` deferred by case 838).
- `guppi check` printed no MOC candidate and no stale defer line.
- The `live` test of `.guppi/tests/test_ship.py`, red by design until this run per the handoff, was not run by this run.

## Next session

### Cases

- The sprint item C1 is left: the tag `prod-x.y.z` and the run of `prod.yml` (the `stop:` task at line 165 of `vault/raw/2026-10-15/0553/spec.md`, unticked); the draft pages with `core: true` still stop every build of `prod` without `--allow-draft`.
- Whether the root `pyproject.toml` keeps the pytest settings beside `.guppi/pyproject.toml` until the Case that removes it.
- Failed Estimate `estimate-guppi-package-runs-from-its-own-folder`: L5 failed on the `[tests/]` test; deferred by case 837.
- Failed Estimate `estimate-clean-branch-installs-as-a-plugin`: not read, no tag `prod-x.y.z`; deferred by case 831.
- Failed Estimate `estimate-plugin-install-writes-guppi-into-an-empty-project`: not read, no tag `prod-x.y.z`; deferred by case 831.
- Failed Estimate `estimate-harness-pipeline`: not read at Retro of session 1739; deferred by case 833.
- Contradiction: `estimate-guppi-package-runs-from-its-own-folder` against the text of Case 819.2 in `rule-page-generation` and `estimate-generate-rewords` (Flags).
- `estimate-clean-branch-ships-the-tests`: its reading waits for a tag `prod-x.y.z` (handoff `## Debt`); defer it into `backlog.md`.
- `estimate-clean-branch-writes-the-session-files`: its reading waits for a tag `prod-x.y.z` and an install in an empty project by hand (handoff `## Debt`); defer it into `backlog.md`.

### Work

- `estimate-clean-branch-ships-estimates-with-pointers-only-in-brackets`

### Ask the person

- none

## Readings at the close

- `uv run --project .guppi guppi test`: 1 failed, 1714 passed, 6 skipped, 1 deselected (exit 1); the failure is `test_guppi_package.py::test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it[tests/]`.
- `uv run --project .guppi guppi check`: exit 1, 14 lines (Flags).
- Live pages: rules 86, entities 5, estimates 296, decisions 186, lessons 49, insights 5.
