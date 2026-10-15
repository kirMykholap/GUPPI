# Brief — 2026-10-15, librarian of session 1739 (the conserved Spec of session 0553)

## Where things stand

- Session 1739 of the sprint `plugin` ran the conserved Spec `vault/raw/2026-10-15/0553/spec.md` by `/box` and `/work`. Cases built: 816 (816.1, 816.2), 818.1, 819.1–819.3, 820.1–820.7, 822.1–822.4, 822.6, 822.8, 822.9; Cases 817, 818.2, 819.4, 820.8, 820.9, 822.5 and 822.7 hold no code task.
- The code of GUPPI moved: `guppi/` to `.guppi/guppi/`, `tests/` to `.guppi/tests/`, `pyproject.toml` and `uv.lock` to `.guppi/`. The root keeps a development project that takes `guppi` from `.guppi/`. New: `plugin/plugin.json`, `plugin/marketplace.json`, `.guppi/guppi/check.py`, `commands.py`, `pointers.py` and three test files.
- The session's readings: L1–L11 passed; L12–L14 failed at Retro, not read. Lessons L15 and L16.
- This run applied two yamls. `vault/raw/2026-10-15/0553/materialize.yaml`: 90 entries, 67 applied, 23 marked `superseded_by` 822.1 (the entries of Case 821), none failed. `vault/raw/2026-10-15/1739/materialize.yaml`: 16 entries and 2 of the synthesis, all applied.
- Pages created: decisions 40 (8 of them, `decision-case-821` and its sub-cases, archived by this run's cleanup), estimates 13, rules 2 (`rule-plugin-install`, `rule-guppi-package`), lessons 4. Pages updated: rules 64, estimates 233, entities 3, insights 1, decisions 1 (`decision-case-805`, superseded by 822.1). 293 of the updated pages were touched by a `reword`.
- The `reword` pairs ran in ledger order: Case 819.1 (`uv run guppi` 195 pages, `uv run pytest` 116, `guppi/` 156, `tests/` 223), then Case 820.7 (`make lint` 36, `make test` 22, `make style` 12). The `replace` pairs of Case 819.1 on `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema` stand before the `reword` in the yaml.
- `guppi cleanup` moved 9 pages: `decision-case-805`, `decision-case-821`, `decision-case-821.1`–`821.7`. The render wrote 2 agents, 9 skills and `settings.json` under `.claude/`, `CLAUDE.md`, `guppi.toml`, `plugin/skills/install/SKILL.md` and 7 files under `vault/wiki/`.
- `guppi archive` moved `raw/2026-10-14/0101`, `0232` and `1536` to `archive/plugin/2026-10-14/<HHMM>/raw`. `raw/2026-10-15/0553` and `1739` are of the run day and were not looked at; `raw/2026-10-14/1907` holds no ledger.
- Synthesis. `^(root_cause|deferred_by):` over `vault/wiki/lessons/`: 44 lines. `^(pattern|deferred_by):` over `vault/wiki/insights/`: 4 lines.
  - `lesson-retro-red-test-that-a-case-ratified-to-wait-for-the-librarian` joined `insight-workflow-code-live-before-the-page-it-reads` (status `open`, kept).
  - `lesson-box-cannot-act-on-the-prespec-findings-of-a-conserved-spec`: none; no index line speaks of `/pre-spec` findings on a conserved Spec that `/box` cannot rebuild.
  - `lesson-ledger-window-stops-at-a-resume-on-the-next-day`: none; no index line speaks of the walk of the event logs stopping at a resume.
  - `lesson-case-build-agent-context-grows-on-every-resume`: none; no index line speaks of a resumed agent's context that only grows.

## Readings due

- `estimate-clean-branch-installs-as-a-plugin` (failed) — `rule-clean-branch` (draft) — by its `method`: `test_ship.py` and, by hand after the Work Mode, `guppi ship --allow-draft` into an empty folder and an install. Result: Retro, not read; `guppi ship --allow-draft` exits 1 with no tag `prod-x.y.z`; the install in an empty project was not run.
- `estimate-plugin-install-writes-guppi-into-an-empty-project` (failed) — `rule-plugin-install` (draft) — by its `method`: `test_ship.py -k plugin_skill` and, by hand after the Work Mode, a local copy and `/guppi:install` in two empty projects. Result: Retro, not read; `plugin/skills/install/SKILL.md` stood only after the librarian's render, and `guppi ship --allow-draft` exits 1 with no tag.
- `estimate-harness-pipeline` (failed) — `rule-harness` (draft) — by its `method`: `make test-harness` and `guppi check` by hand. Result: Retro, not read; `guppi backlog --check` exited 1 after `/work` deleted `carry.md` of `raw/2026-10-15/0553/`.
- `estimate-claude-md-rendered` (pending) — `rule-claude-md` (draft) — read box at line 1557 of `vault/raw/2026-10-15/0553/spec.md`. This run: the render rewrote `CLAUDE.md`; the 16 lines that `make lint` (`guppi check`) printed are all of `guppi lint`, none of `render --check`.
- `estimate-clean-branch-ships-neutral-texts` (pending) — `rule-clean-branch` (draft) — read box at line 1663 of `vault/raw/2026-10-15/0553/spec.md`. This run ran no `guppi ship`.
- `estimate-clean-branch-ships-the-tests` (pending) — `rule-clean-branch` (draft) — read box at line 1446 of `vault/raw/2026-10-15/0553/spec.md`. This run ran no `guppi ship`; `make test` ran `.guppi/tests/test_ship.py` with no failure.
- `estimate-clean-branch-writes-the-session-files` (pending) — `rule-clean-branch` (draft) — read box at line 1501 of `vault/raw/2026-10-15/0553/spec.md`. This run ran no `guppi ship`.
- `estimate-generate-rewords` (pending) — `rule-page-generation` (draft) — read box at line 649 of `vault/raw/2026-10-15/0553/spec.md`. This run: `guppi generate` printed 760 `reword` lines, one per page and pair (`uv run guppi` 195, `uv run pytest` 116, `guppi/` 156, `tests/` 223, `make lint` 36, `make test` 22, `make style` 12), an empty stderr, and no entry marked `failed`.
- `estimate-guppi-config-runs-the-test-and-style-commands` (pending) — `rule-guppi-config` (draft) — read box at line 958 of `vault/raw/2026-10-15/0553/spec.md`. This run: the render wrote `guppi.toml` with `test = ["uv run --project .guppi pytest -q"]` and `style = ["uv run --project .guppi ruff check .", "uv run --project .guppi ruff format --check ."]`; a search for `make test` and `make style` as whole words outside History and Result found 0 live rules, entities and Estimates and 0 files of `.claude/`.
- `estimate-guppi-package-is-ready-after-the-install` (pending) — `rule-guppi-package` (draft) — read box at line 774 of `vault/raw/2026-10-15/0553/spec.md`. This run: the render wrote `plugin/skills/install/SKILL.md`; no `guppi ship` was run.
- `estimate-guppi-package-runs-from-its-own-folder` (pending) — `rule-guppi-package` (draft) — read box at line 600 of `vault/raw/2026-10-15/0553/spec.md`. This run: `make test` printed 1 failed, 1699 passed, 6 skipped; the one failure is `test_guppi_package.py::test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it[tests/]`, on `rules/rule-page-generation` and `estimates/estimate-generate-rewords`; the render rewrote `.claude/settings.json`, 9 skills and 2 agents.
- `estimate-lint-runs-every-step` (pending) — `rule-lint` (draft) — read box at line 889 of `vault/raw/2026-10-15/0553/spec.md`. This run: `make lint` ran `uv run --project .guppi guppi check`, exit 2, 16 lines; a search for `make lint` as whole words outside History and Result found 0 live rules, entities and Estimates and 0 files of `.claude/`.
- `estimate-morph-sets-up-the-project-at-the-first-hi` (pending) — `rule-morph` (draft) — read box at line 250 of `vault/raw/2026-10-15/0553/spec.md`; its `method` waits for the session whose Work Mode builds the install skill of `rule-morph` and its step in `/hi`.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` (pending) — `entity-sprint-plugin` (draft) — read box at line 166 of `vault/raw/2026-10-15/0553/spec.md`; a run of `prod.yml` on a tag `prod-x.y.z`, before the close of `plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` (pending) — `entity-sprint-plugin` (draft) — read box at line 409 of `vault/raw/2026-10-15/0553/spec.md`; a session of `plugin` before its close.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` (pending) — `entity-sprint-plugin` (draft) — read box at line 1238 of `vault/raw/2026-10-15/0553/spec.md`; a pull request from a second account, before the close of `plugin`.
- `estimate-sprint-plugin-close-steps-run-from-the-line` (pending) — `entity-sprint-plugin` (draft) — by its `method`: the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-readme-describes-the-project` (pending) — `entity-sprint-plugin` (draft) — by its `method`: the person's answer at the `/hi` of the session after the one whose Work Mode writes `README.md`.
- `estimate-hi-writes-frontier` (pending) — `rule-skill-hi` (draft) — by its `method`: the person's answer in the session after the close of a sprint.
- `estimate-skill-merge-main-joins-a-conflicted-page` (pending) — `rule-skill-merge-main` (draft) — by its `method`: after the first `/merge-main` whose merge of main leaves a conflicted page; not seen in `git log`.
- `estimate-skill-pr-review-takes-a-pull-request-whole` (pending) — `rule-skill-pr-review` (draft) — by its `method`: after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` (pending) — `rule-work-mode` (draft) — by its `method`: after the first `/work` on the rendered `.claude/skills/work/SKILL.md` in which a Case is ratified in Work Mode; not seen.

## Flags

- `incomplete`: the 7 `create` entries of Cases 821.1–821.7 in the 0553 yaml carry `incomplete: [criterion]` (`estimate-clean-branch-ships-the-passed-estimates`, `-ships-the-tests`, `-writes-the-session-files`, `-ships-a-blank-project-description`, `-ships-the-checks-workflow`, `-ships-neutral-texts`, `-refuses-a-draft-core-page`). All 7 are `superseded_by` 822.1; their pages were written from the creates of Case 822.
- `failed`, `near`, `unparsed`: none in either yaml.
- Failed Estimates: `estimate-clean-branch-installs-as-a-plugin`, `estimate-plugin-install-writes-guppi-into-an-empty-project`, `estimate-harness-pipeline`.
- `make test`: 1 failed, 1699 passed, 6 skipped. The handoff expected the 9 red tests of `.guppi/tests/test_guppi_package.py` to turn green after the render and the `reword`; 8 did. The red one finds `tests/` in `rules/rule-page-generation` and `estimates/estimate-generate-rewords`, in the text of Case 819.2 that names the pair `tests/` → `.guppi/tests/` as an example. Case 819.2's entries stand after the `reword` of Case 819.1 in ledger order.
- Contradiction: the Criterion of `estimate-guppi-package-runs-from-its-own-folder` (no live rule, entity or Estimate names a path of the tests outside `.guppi/`) against the text that Case 819.2 wrote into `rule-page-generation` and `estimate-generate-rewords`, which names `tests/` as the example of a pair.
- The `reword` of `tests/` hit 223 pages; the handoff counted 224.
- The 221 `method`/`path` findings the handoff named are gone. `make lint` exit 2, 16 lines:
  - `status: a page with core: true that is draft` on `entity-sprint`, `rule-claude-md`, `rule-guppi-config`, `rule-guppi-package`, `rule-harness`, `rule-lint`, `rule-morph`, `rule-page-generation`, `rule-skill-hi`, `rule-work-mode`;
  - `unread: failed` on the 3 failed Estimates;
  - `method` on `estimate-guppi-tests-green` (a MOC's Estimate names no `make <target>` or `pytest` with test files) and `estimate-page-schemas-one-file-per-rule` (says by hand while `estimate-entities-schema-checked` names a test file), both named by the `/pre-spec` findings;
  - `method` on `estimate-harness-make-runs-in-both-shells`: "the Makefile has no target with".
- Defect: `guppi lint` reads the words "make with the targets help, style, test and lint" of the `method` of `estimate-harness-make-runs-in-both-shells` as the target `with` (`.guppi/guppi/lint.py`, the `MAKE_TARGET` match at lines 847–849 and 868–870).
- Defect: the render wrote `plugin/skills/install/SKILL.md`; the close commits only `vault`, `CLAUDE.md`, `.claude` and `guppi.toml`, so the file stands untracked after the librarian's commit.
- `guppi backlog --check`, red at Retro after `/work` deleted `carry.md` of `raw/2026-10-15/0553/`, printed no line in `make lint` after this run's `guppi backlog`.
- Read beyond the frame: the first 3 lines of `vault/raw/2026-10-15/1739/spec.md`, to find which Spec holds the unticked lines that Readings due and Next session take (the session's own `spec.md` holds no box); the handoff did not ask for it.
- Read beyond the frame: the line counts of two ledgers, `vault/raw/2026-10-15/1739/ledger.md` (16) and `vault/raw/2026-10-15/0553/ledger.md` (90), since this run applied the yamls of both; the frame names one read of `ledger.md`.

## Next session

### Cases

- A `/pre-spec` finding: Case 817 and Case 822.3 both put their Case first at the first `/hi` of a new project, with no order between them.
- A `/pre-spec` finding: the reading of Case 822.7 fails on `in English` in `rule-language`, `rule-case-build`, `rule-case-protocol` and `rule-spec-write`, and on the `this repository` sentences that Case 817 wrote into `rule-morph`.
- A `/pre-spec` finding: `rule-rules-schema` still says a core page ships without its Estimates; `estimate-rules-schema-checked` and `estimate-clean-branch-pages-hold-pointers-only-in-brackets` speak of what Case 822.1 changed.
- A `/pre-spec` finding: the `reword` of Case 820.7 leaves `estimate-guppi-tests-green` and `estimate-page-schemas-one-file-per-rule` with a `method` that does not fit a MOC (both in `make lint`).
- A `/pre-spec` finding: the milestone line of `entity-sprint-plugin` still names `prod-2`.
- A `/pre-spec` finding: pointers outside a bracket in shipped Estimates stop every build of `prod`.
- A `/pre-spec` finding: the readings of Cases 816.1, 818.1 and 819.4 need a tag `prod-x.y.z`, or the librarian's render, before they can run.
- A `/pre-spec` finding: the `when` of Case 819.4 names `prod`.
- A `/pre-spec` finding: Case 822.5 and Case 820.9 read texts that only the librarian's run writes, and their methods name no such moment.
- A `/pre-spec` finding, not confirmed: whether pytest collects `.guppi/tests/` from the root in a project with no root `pyproject.toml`.
- A `/pre-spec` finding: stale counts and facts in the contexts of Cases 816, 817, 818, 820 and 822.
- The tag `prod-0.2.0`: the `stop:` task of Case 816.2 (line 165 of `vault/raw/2026-10-15/0553/spec.md`, unticked) asks the owner to place and push it; while the pointers in the shipped Estimates stand, a run on it fails, and `/pre-spec` recommended holding the tag until that is fixed.
- New tags: lessons L15 and L16 wanted `retro`, `box` and `pre-spec`; a Case may add `retro` and `box` to `tags.md`.
- Two lessons of session 0553 have no fixing Case: `lesson-ledger-window-stops-at-a-resume-on-the-next-day` and `lesson-case-build-agent-context-grows-on-every-resume`.
- Failed Estimate `estimate-clean-branch-installs-as-a-plugin`: not read, `guppi ship --allow-draft` exits 1 with no tag `prod-x.y.z`.
- Failed Estimate `estimate-plugin-install-writes-guppi-into-an-empty-project`: not read, no local copy could be built with no tag `prod-x.y.z`.
- Failed Estimate `estimate-harness-pipeline`: not read, `guppi backlog --check` was red at Retro and the new Purpose of `rule-harness` landed only at this run.
- Contradiction: `estimate-guppi-package-runs-from-its-own-folder` and its test `test_guppi_package.py` (`[tests/]`, red) against the text of Case 819.2 in `rule-page-generation` and `estimate-generate-rewords`, which names `tests/` as an example (Flags).
- Defect: `guppi lint` reads "make with the targets …" in a `method` as the Makefile target `with` (`.guppi/guppi/lint.py`, Flags).
- Defect: the close of the librarian commits `vault`, `CLAUDE.md`, `.claude` and `guppi.toml` only, while the render now writes `plugin/skills/install/SKILL.md` (Flags).

### Work

- `estimate-claude-md-rendered`
- `estimate-clean-branch-ships-neutral-texts`
- `estimate-clean-branch-ships-the-tests`
- `estimate-clean-branch-writes-the-session-files`
- `estimate-generate-rewords`
- `estimate-guppi-config-runs-the-test-and-style-commands`
- `estimate-guppi-package-is-ready-after-the-install`
- `estimate-guppi-package-runs-from-its-own-folder`
- `estimate-lint-runs-every-step`
- Dirty tree: `plugin/skills/install/SKILL.md`, written by this run's render, stands untracked after the librarian's commit.

### Ask the person

- none

## Readings at the close

- `make test`: 1 failed, 1699 passed, 6 skipped (exit 2).
- `make lint`: exit 2, 16 findings (Flags).
- Live pages: rules 86, entities 5, estimates 294, decisions 159, lessons 48, insights 4.
