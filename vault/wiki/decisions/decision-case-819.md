---
type: decision
case: "819"
status: current
children: ["[[decision-case-819.1]]", "[[decision-case-819.2]]", "[[decision-case-819.3]]", "[[decision-case-819.4]]"]
origin: raw/2026-10-15/0553/ledger.md#case-819
sprint: plugin
created: 2026-10-15
tags: [harness, plugin, session, workflow, render, schema, ledger, ci, git]
---

## Problem

GUPPI's code runs only where its `pyproject.toml` stands at the root of the project, so a user's project must take files at its root that it does not own, and a project with its own `pyproject.toml` cannot take GUPPI at all.

## Recommend

- **Where the code that the hooks run lives**
  - Recommended: (a) the project's own copy at its root, for this sprint.
  - Answer: (d) a copy in its own folder `.guppi/`, called as `uv run --project .guppi guppi …`; this repository moves its own code there too.
- **What the install does when `uv` is missing**
  - Recommended: (a) the install checks for `uv` first.
  - Answer: not answered; replaced by the question on what the install does about `uv` and the Python environment.
- **What the install does about `uv` and the Python environment**
  - Recommended: (a) check `uv`, then build the environment by `uv sync` after the copy.
  - Answer: agreed, (a).
- **What stays at the root of this repository**
  - Recommended: (a) a development project stays at the root.
  - Answer: (a) as a step in between, then (b), nothing at the root.
- **Which texts change to the new command**
  - Recommended: (a) the texts that run.
  - Answer: (b) every text; the Estimates that go back to pending are read later by one Case of their own.
- **Where GUPPI's own tests live**
  - Recommended: (a) they stay at the root and do not ship.
  - Answer: not answered; the person asked why not (b) and why one script cannot rewrite the paths; replaced by the question on where the tests live and whether they ship.
- **Where GUPPI's own tests live, and whether they ship**
  - Recommended: (b) move them into `.guppi/tests/` now, and leave how they ship to item C9.
  - Answer: agreed, (b).
- **Git and the Python environment of `.guppi/`**
  - Recommended: (a) a `.gitignore` of its own inside `.guppi/`.
  - Answer: agreed, (a).
- **What checks that this is done**
  - Recommended: (a) a new Estimate for each half, plus the sprint Estimate.
  - Answer: agreed, (a).
- **When the root development project goes**
  - Recommended: (a) a Case of a later session removes it.
  - Answer: agreed, (a).
- **How the pages take the new command**
  - Recommended: (a) one `reword` of the command.
  - Answer: agreed, (a).
- **Which page holds where GUPPI's code lives**
  - Recommended: (a) a new rule, `rule-guppi-package`.
  - Answer: agreed, (a).
- **How the paths of the code and the tests change in the pages**
  - Recommended: (a) `reword` learns path prefixes.
  - Answer: agreed, (a).
- **Which page carries the check of the `uv` step of the install**
  - Recommended: (a) the check stands on `rule-guppi-package`.
  - Answer: agreed, (a); Case 818 is built again too.
- **Change**
  - Asked: the person agreed to build this Case again after Case 820, which drops `make` and ships no command `ship`.
  - Taken: Case 819.3 no longer lists the `Makefile` among the files that `guppi ship` writes, in its new text of `rule-clean-branch`, its `then` and its task on `ROOT_FILES`; its `then` points to `estimate-clean-branch-ships-no-ship-command` for the module of `ship`; the Purpose of `rule-guppi-package` names the `Makefile` as the one this repository keeps for now.
- **Change**
  - Asked: the person agreed to build this Case again after Case 821, which ships the tests, the passed Estimates, the session files and `.github/workflows/checks.yml`, and builds no `prod` while a page with `core: true` is `draft`.
  - Taken: the Criterion of Case 819.3 drops its lines on the tests, `.github/` and the session files and points to the Estimates of Cases 821.1, 821.2, 821.3 and 821.5; its line on brackets leaves out the strings of a test file; its task on `guppi/ship.py` leaves the tests to Case 821.2; the method of `estimate-guppi-package-is-ready-after-the-install` waits for the first run that writes `prod`; the test of Case 819.1 builds with `--allow-draft`.
- **Change**
  - Asked: at `/pre-spec`, the person chose that each Estimate that waits for a run that writes `prod` is read from a local copy that `guppi ship --allow-draft` writes after the librarian's run of this change; and the findings of `ask-guppi` on this Case are fixed.
  - Taken: the method of `estimate-guppi-package-is-ready-after-the-install` reads such a local copy. `rule-guppi-package` takes `core: true` by a `set` of its `update`, so the field lands as a boolean that `is_core` of `guppi/pages.py` accepts. Its texts, and the Criterion of Case 819.1, name the repository of GUPPI in place of this repository. Two more pairs on `rule-estimates-schema` keep its example command and its sentence on a test path off the `reword`. The task on `TEST_PATH` reads a test path whole from its start. The Criterion of Case 819.3 says that what it writes of the tests, the environment and the module of `ship` is what Cases 820 and 821 set. A pair of Case 819.2 makes the Purpose of `rule-page-generation` name rules, entities and Estimates as what a `reword` changes.

## History

- 2026-10-15 created · raw/2026-10-15/0553/ledger.md#case-819
