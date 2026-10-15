# Handoff — 2026-10-15, sprint plugin: the conserved Spec of session 0553 run by /box

## Notes from memory

- The person took the conserved Spec whole and put off every other Frontier item. The two lessons of session 0553 on the Tail have no page yet, so no defer could name them. Their lines were closed `· work` with a note: their pages come with this run of the librarian.
- At `/pre-spec`, `ask-guppi` over the Spec printed 13 findings. `/box` cannot rebuild a Case of a conserved Spec, so the person chose to run it as it stands and fix the findings in a later session. The findings are under `## For the next session`.
- `ask-guppi` did not check everything. It did not read the case files of 0553, did not compare the replaced Criteria line by line, did not open the Estimates of several updated rules, and did not verify any claim about Claude Code, uv, pytest collection or tags in CI at its source.
- The code tasks were done by five subagents in Spec order. Each made small choices the Spec does not fix:
  - **`guppi ship` and tests.** A test file is cleaned with its code masked too, not only its strings: a bracket in a comment inside a code tuple otherwise broke `test_prespec.py` in the copy. Five tests strip the pointer at the end of a message before they compare.
  - **Shipped Estimate without `checked`.** It takes the date its old Result opens with.
  - **The brief skeleton** is worded by the agent, apart from its Cases line.
  - **`ship_stands`** is `importlib.util.find_spec("guppi.ship")`.
  - **`guppi check`** runs each step as `python -P -m guppi.cli <step>`, with the same interpreter.
  - **`guppi test` / `guppi style`** split each command by `shlex`.
  - **Draft refusal.** The draft gate of `guppi ship` stands in `run`, not in the build function.
  - **Where the tag is read.** `.guppi/tests/test_guppi_package.py` builds the clean copy through the build function with a fixed version, so it does not read the tag.
  - **Version tags.** `VERSION_TAG` refuses leading zeros.
  - **CI.** The workflow step installs Claude Code by `npm install -g @anthropic-ai/claude-code`.

## Direct instructions to the librarian

- **Apply the conserved Spec.** Apply the decision lines of `raw/2026-10-15/0553/ledger.md` with the readings and lessons of this session. The two lessons at the end of that ledger, from session 0553, have no fixing Case.
- **Apply the `reword` pairs in ledger order.** First Case 819.1 (`uv run guppi`, `uv run pytest`, `guppi/`, `tests/`), then Case 820.7 (`make lint`, `make test`, `make style`).
  - The code of `reword_pattern` is new: a pair that ends with `/` now matches the start of a path, and in the link fields too. Under it, `guppi/` hits 156 pages and `tests/` hits 224.
  - The `replace` pairs of Case 819.1 on `rule-case-example`, `rule-estimates-schema` and `rule-rules-schema` must land before the `reword`, so that the examples of a person's own project keep their paths.
- **Check after the run:** `make lint` and `make test`.
  - The 9 red tests of `.guppi/tests/test_guppi_package.py` should turn green after the render of `.claude/` and the `reword`.
  - The 221 `method`/`path` findings of `guppi lint` should go after the `reword`.
- **The hooks still run the old command until the render.** The root development project keeps them working.

## What actually got done

- **Cases built:** 816 (816.1, 816.2), 818.1, 819.1–819.3, 820.1–820.7, 822.1–822.4, 822.6, 822.8, 822.9, all from the Spec of 0553. Cases 817, 818.2, 819.4, 820.8, 820.9, 822.5 and 822.7 hold no code task.
- **Moved:** `guppi/` to `.guppi/guppi/`, `tests/` to `.guppi/tests/`, and `pyproject.toml` and `uv.lock` to `.guppi/`. There is a new `.guppi/.gitignore`. The root `pyproject.toml` and `uv.lock` are now a development project that takes `guppi` from `.guppi/` as an editable path.
- **New:**
  - `plugin/plugin.json`, `plugin/marketplace.json`
  - `.guppi/guppi/check.py`, `commands.py`, `pointers.py`
  - `.guppi/tests/test_guppi_package.py`, `test_check.py`, `test_commands.py`
- **Changed:**
  - In `.guppi/guppi/`: `ship.py`, `generate.py`, `lint.py`, `prespec.py`, `pages.py`, `cli.py`, `config.py`, `ledger.py`, `onward.py`, `ratified.py`, `casecheck.py`, `bashguard.py`, and docstrings across the package.
  - Most test files under `.guppi/tests/`, where pointers in comments and docstrings now stand in brackets.
  - `Makefile`, `.github/workflows/prod.yml`, `.github/workflows/checks.yml`.
- **`make test`:** 1691 passed, 6 skipped, 9 failed. The 9 failures are all in `.guppi/tests/test_guppi_package.py` (Observations).
- **`make style`:** clean.
- **Readings:**
  - L1–L11 passed.
  - L12–L14 failed, Retro, not read: `estimate-clean-branch-installs-as-a-plugin`, `estimate-plugin-install-writes-guppi-into-an-empty-project`, `estimate-harness-pipeline`.
- **Lessons:** L15 and L16.

## Debt

- The `stop:` task of Case 816.2 is not run: the owner places the tag `prod-0.2.0` on the last commit of `plugin` and pushes it. It comes after this run (For the next session).
- 114 boxes wait for the librarian.
- **Readings waiting for the librarian's run of this change:**
  - `estimate-guppi-package-runs-from-its-own-folder`
  - `estimate-generate-rewords`
  - `estimate-guppi-package-is-ready-after-the-install`
  - `estimate-lint-runs-every-step`
  - `estimate-guppi-config-runs-the-test-and-style-commands`
  - `estimate-clean-branch-ships-the-tests`
  - `estimate-clean-branch-writes-the-session-files`
  - `estimate-claude-md-rendered`
  - `estimate-clean-branch-ships-neutral-texts`
- **Readings waiting for other moments:**
  - `estimate-morph-sets-up-the-project-at-the-first-hi`: the session whose Work Mode builds the install skill of `rule-morph` and its step in `/hi`.
  - `estimate-sprint-plugin-ci-writes-a-clean-branch`: a run of `.github/workflows/prod.yml` on a tag `prod-x.y.z` that writes `prod`, or the close of `plugin`.
  - `estimate-sprint-plugin-installs-as-a-plugin`: the Retro of the session that builds the install, or the close of `plugin`.
  - `estimate-sprint-plugin-pull-requests-reviewed-on-github`: a pull request from a second account, before the close of `plugin`.

## Observations

- **Red tests.** The 9 tests of `.guppi/tests/test_guppi_package.py` are red until the librarian's render of `.claude/settings.json` and the skills, and its `reword` of the pages. The context of Case 819 accepted this red. `rule-retro` does not, so the commit went in red (lesson L15).
- **Expected red, as `work.md` names it:**
  - `guppi lint` `method`/`path` findings on old root paths, until the `reword`.
  - `guppi test` and `guppi style` exit 1 with `no key test` / `no key style`, and so do the jobs `test` and `style` of `checks.yml`, until the render of `guppi.toml`.
  - A `guppi lint` `status` finding on each draft page with `core: true`: `entity-sprint`, `rule-morph`, `rule-skill-hi`, `rule-skill-merge-main`, `rule-skill-pr-review`, `rule-work-mode`. More will appear for each core page this run sets `draft`.
- **Backlog check.** `guppi backlog --check` exits 1 because `/work` deleted `carry.md` of `raw/2026-10-15/0553/`. It clears at the librarian's `guppi backlog`. No line of `work.md` names it.
- **`guppi ship` from this repository exits 1** for three reasons:
  - there is no tag `prod-x.y.z`;
  - six core pages are draft;
  - a build with the real vault prints 20 `ship:` lines in 16 shipped `passed` Estimates whose Criterion, `method` or `purpose` holds a pointer outside a bracket.
- **Plugin check.** `claude plugin validate` on a local build passed with two warnings: the catalogue has no top-level `description`, and a root `CLAUDE.md` is not loaded as plugin context.
- **Method of `estimate-clean-branch-ships-the-tests`.** It selects `-k tests`, which matches every test of `test_ship.py`, because pytest also matches the folder name.
- **Long lines.** About 26 docstring lines now run past 100 characters after the path change. Ruff does not enforce that limit.

## For the next session

- **The 13 `/pre-spec` findings on the Spec of 0553 need Cases:**
  - Case 817 and Case 822.3 both put their Case first at the first `/hi` of a new project, with no order between them.
  - Case 822.7's reading fails on `in English` in `rule-language`, `rule-case-build`, `rule-case-protocol` and `rule-spec-write`, and on the `this repository` sentences that Case 817 writes into `rule-morph`.
  - `rule-rules-schema` still says a core page ships without its Estimates. `estimate-rules-schema-checked` and `estimate-clean-branch-pages-hold-pointers-only-in-brackets` speak of what Case 822.1 changed.
  - The `reword` of Case 820.7 leaves `estimate-guppi-tests-green` and `estimate-page-schemas-one-file-per-rule` with a method that does not fit a MOC.
  - The milestone line of `entity-sprint-plugin` still names `prod-2`.
  - Pointers outside a bracket in shipped Estimates stop every build of `prod` (Observations).
  - The readings of Cases 816.1, 818.1 and 819.4 need a tag `prod-x.y.z`, or the librarian's render, before they can run.
  - The `when` of Case 819.4 names `prod`.
  - Case 822.5 and Case 820.9 read texts that only the librarian's run writes, and their methods name no such moment.
  - Not confirmed: whether pytest collects `.guppi/tests/` from the root in a project with no root `pyproject.toml`.
  - Stale counts and facts in the contexts of Cases 816, 817, 818, 820 and 822.
- **The tag `prod-0.2.0`.** The `stop:` task of Case 816.2 asks the owner to place and push it. While the pointers in the shipped Estimates stand, a run on it fails. The recommendation at `/pre-spec` was to hold the tag until that is fixed.
- **New tags.** Lessons L15 and L16 wanted the tags `retro`, `box` and `pre-spec`. They were written with tags of `tags.md`. A Case may add `retro` and `box`.
- **Two lessons of session 0553 have no fixing Case:** `lesson-ledger-window-stops-at-a-resume-on-the-next-day` and `lesson-case-build-agent-context-grows-on-every-resume`.

## Ask the person
