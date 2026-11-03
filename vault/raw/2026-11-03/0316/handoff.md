# Handoff — 2026-11-03, the sprint plugin: the setup of a new project, the opening of a sprint, the plugin icon

## Notes from memory

- Case 1017 was ratified, then changed on the person's word while Case 1018 was built: the person wants every sprint to open with an open question on what to build, and the id proposed after it, not asked first. 1017 and 1018 were rebuilt as a batch and ratified again; the person agreed in one message to two opposite recommendations on who proposes the id (1017.Q12 and 1018.Q4), so the fork was asked a third time and settled as the main agent proposing the id in one plain question.
- On Case 1016 the person chose the icon in rounds without seeing it; at the stop of Work Mode they asked for a transparent background in place of the white padding the task named. The Criterion names no background, so the change was taken at that stop with no new Case; the task text of the Spec still says "padded with white".
- The person chose to keep the two source pictures in `guppi-assets/` at the root of the repository, not outside it as the tasks of Case 1016 offered, "until we decide where to move them". `guppi ship` does not take that folder (not in `TREES` or `ROOT_FILES`).
- The person asked what C1, C2 and W hold before choosing; C1, C3 and C4 were left for a later session.
- At `/pre-spec`, `ask-guppi` reported two searches of code beyond its frame again, the third session running; Case 1015 lifts that limit, but its Render lands only at this run.

## Direct instructions to the librarian

- Case 1014 defers `estimate-orchestration-acknowledging-reply`, and Case 1017.7 updates the same Estimate (its Criterion and `method`); both are meant to stand: the page keeps the new Criterion and `deferred_by` Case 1014.
- `rule-skill-sprint-open` takes replace pairs from both 1017.6 and 1018.1, anchored in different sentences; apply 1017.6 then 1018.1 and check that both new texts stand.
- `rule-clean-branch` takes replace pairs from 1016 and 1017.1, on different sentences.
- `estimate-git-context-offers-git-init` is updated by 1017.9, a sub-case added in the loop after `/pre-spec`; its line stands later in the ledger than the other lines of 1017.
- The render lines of `guppi.toml` (1017.1), `.claude/skills/setup/SKILL.md` and `.claude/skills/hi/SKILL.md` (1017.3), `.claude/skills/sprint-open/SKILL.md` (1017.6, 1018.1), `.claude/agents/ask-guppi.md` (1015.1) and `vault/wiki/orchestration.md` (1017.7) are this run's; after the render `guppi.toml` holds `setup_done = true`.
- `rule-morph` and `rule-skill-setup` gain `core: true` while `draft`: `guppi ship` will refuse to write `prod` until they are `built`; that is intended (1017.8).

## What actually got done

- Cases ratified: 1014 (short-form defer), 1015 (1015.1, 1015.2), 1016, 1017 (1017.1–1017.9), 1018 (1018.1, 1018.2).
- Code: `.guppi/guppi/config.py` (`SETUP_KEY`, `setup_pending`), `.guppi/guppi/ship.py` (`setup_not_done`, docstring on the icon and on a file that is no text), `.guppi/guppi/ledger.py` (`refused_without_sprint` passes every line while the setup is pending), `.guppi/guppi/sprint.py` (`hi_hook` prints the `/setup` line first). `plugin/plugin.json` gains `"icon": "./.guppi/icon.png"`. New `.guppi/icon.png` (512×512 PNG, transparent background), made from `guppi-assets/icon_guppi.png`; `guppi-assets/` holds both source pictures.
- Tests: `.guppi/tests/test_config.py`, `test_ship.py`, `test_ledger.py`, `test_sprint.py`, by the names `icon` and `setup`. `guppi test`: 1943 passed, 6 skipped, 1 deselected. `guppi style`: clean.
- Readings: L27–L31 passed (`estimate-clean-branch-ships-the-plugin-icon`, `estimate-clean-branch-ships-the-setup-not-done`, `estimate-ledger-write-passes-every-line-before-the-setup`, `estimate-skill-setup-starts-at-hi`, `estimate-skill-sprint-open-asks-the-goal-as-an-open-question`). Lessons: L32 and L33 (error).

## Debt

- No box of code, test or command is debt.
- 37 boxes wait for the librarian (page, render and read lines); the 8 `read` lines of the Estimates below wait for their events.
- `estimate-ask-searches-at-prespec` — waits for the first `/pre-spec` whose `ask-guppi` runs on the new Render of `rule-ask`.
- `estimate-prespec-finds-a-reader-of-a-new-files-folder` — waits for the first `/pre-spec` on that Render whose plan adds a file that is no page.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — waits for an install by hand in an empty git project from a `--allow-draft` copy, after this run.
- `estimate-morph-takes-in-the-set-aside-files` — waits for an install by hand in a project with files of its own, after this run.
- `estimate-skill-sprint-open-asks-the-opening-questions` — waits for this librarian's run; then the three Renders are read against the Criterion.
- `estimate-orchestration-acknowledging-reply` — deferred by Case 1014; its second reading waits for a setup Case ratified in a new install after this run.
- `estimate-clean-branch-refuses-a-draft-core-page` — its Grep waits for this run, which writes `core: true` on `rule-morph` and `rule-skill-setup`.
- `estimate-git-context-offers-git-init` — waits for an install by hand in a folder with no git, after this run.
- `estimate-case-build-reads-the-readers-of-a-new-files-folder` (W1) — its method reads the transcript of the `case-guppi` of session 2155, an earlier session, which no session may read; it cannot be taken as it stands.

## Observations

- The task text of Case 1016 says the icon is padded with white; the file is transparent, as the person chose at the stop. The Criterion holds either way.
- Whether the field `icon` clears `ICON_MISSING` of `claude plugin validate` is not checked; it shows at the next run of `prod.yml`, which writes nothing while `rule-morph` and `rule-skill-setup` are `draft`.
- `ask-guppi`, confirming its findings, took the facts of code of findings 3, 5, 6 and 12 from the contexts and ran no search.

## For the next session

- Defer `estimate-case-build-reads-the-readers-of-a-new-files-folder` into the backlog, or give it a `method` that reads a later session, since its event was session 2155 and that transcript cannot be read.
- Where the source pictures in `guppi-assets/` live for good: the person put them there for now.
- The milestone The plugin: C1 (the clean version installed by hand), C3 (the README) and C4 (the close of `plugin`) were left for later; C1's reading by hand now also covers the setup of Case 1017.

## Ask the person
