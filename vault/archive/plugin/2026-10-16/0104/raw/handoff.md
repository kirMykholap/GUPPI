# Handoff — 2026-10-16, the clean branch: the tag prod-0.2.0 and the install readings

## Notes from memory

- The person took the readings that wait for a tag as one group (Cases 841–847) on the agent's proposal, then agreed to every recommendation of the rounds.
- At `/pre-spec` the person agreed to one stop for every install by hand. The case-guppi of Case 847 put the push into a new Case 850 instead of Case 847, and Cases 841, 843 and 846 went back a second time to name Case 850.
- The person first misread the install steps: they built one test project of their own, `C:\PROJECTS\test`, instead of the four folders the agent made in its scratchpad, and then built `C:\PROJECTS\test-claude-md`, `C:\PROJECTS\test-no-uv` and `C:\PROJECTS\test-uv-offline`. The readings rest on those four.
- The person judged the results: a `/hi` that fails without git is bad; the install with its own `CLAUDE.md` is fine; the install with no `uv` might offer to install `uv`; the offline install "worked rather strangely" and needs another discussion.
- The auto mode classifier refused `git push origin prod-0.2.0`; the person pushed it by hand. A command line that held `git ls-remote origin` beside `gh run list` was refused too; `gh run list`, `gh run view` and `gh api` alone passed.

## Direct instructions to the librarian

- Case 850 updates `estimate-sprint-plugin-ci-writes-a-clean-branch` as Case 841 does, with its Criterion unchanged: one page, two decision lines of this session.
- `{supersedes:case 831}` stands on Cases 842, 843 and 846; check that each target of case 831 is one of their three Estimates, so that no other `deferred_by` is cleared.
- The Frontier line C1 closes by Case 847, the Case that updates the sprint page; Case 850 belongs to the same item.
- After `generate`, run `uv run --project .guppi pytest .guppi/tests/test_guppi_package.py`: Case 840.1 removes the example `tests/` from `rule-page-generation` and `estimate-generate-rewords`, the only two hits of the red test.

## What actually got done

- Cases ratified: 840 (840.1, 840.2), 841, 842, 843, 844, 845, 846, 847, 850; the short defers 848 and 849.
- No code file and no test changed. Work Mode placed the local tag `prod-0.2.0` on the last commit of `plugin`; the person pushed it, and the run of `prod.yml` on it failed at "Build the clean version" on the seven draft pages with `core: true`; the branch `prod` on GitHub kept its last commit of 2026-10-14.
- `uv run --project .guppi guppi test`: 1 failed, 1714 passed, 6 skipped, 1 deselected — the same test as the Baseline. `uv run --project .guppi guppi style`: clean.
- Readings: L1 at `/hi`; at Retro the passed readings of `estimate-generate-rewords` and `estimate-plugin-install-writes-guppi-into-an-empty-project`, the failed readings of `estimate-clean-branch-ships-the-tests` and `estimate-clean-branch-writes-the-session-files`.
- Lessons: `lesson-hi-fails-outside-a-git-repository`, `lesson-case-build-opens-a-new-case-for-a-task-asked-into-its-own`, `lesson-case-build-reads-a-sibling-case-file-mid-rebuild`.

## Debt

- No box of the Spec is debt.
- The boxes of the pages, of `guppi sprint` and of the readings wait for the librarian.
- `estimate-guppi-package-runs-from-its-own-folder` — waits for the librarian's run of this session, which writes the new example of Case 840.1; then `test_guppi_package.py` and the hooks of a `/hi` in this repository.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — of the live sprint page; waits for a run of `prod.yml` that writes `prod`, before the close of `plugin`, which needs the seven draft core pages built or a later Case on them, and a tag newer than `prod-0.2.0`.
- `estimate-clean-branch-ships-neutral-texts` — its tag and its librarian's run both stand now; a reading of the clean copy against its Criterion was started at Retro and did not finish before this handoff.

## Observations

- Red before the work: `test_guppi_package.py::test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it[tests/]`, and every line of `guppi check` of the Baseline (`backlog.md` differs from its sources, the seven draft core pages, four `unread: failed` Estimates, three `method` findings).
- The clean copy carries the same red test, since it is built from the live pages before the librarian's run of Case 840.
- `claude plugin validate` passed on the clean copy with two warnings: the catalogue has no description, and `CLAUDE.md` at the root of the plugin is not loaded as context.
- At the offline install, `uv sync --project .guppi` failed on `ruff==0.16.1` (pulled in by the `dev` group), showed its output and stopped, but its last sentence still told the person to run `uv sync`, reopen Claude Code and type `/hi`; `.guppi/.venv/` was created and left unbuilt. The Criterion of `estimate-guppi-package-is-ready-after-the-install` says that it does not tell the person to type `/hi`.
- `/guppi:install` never wrote into the copy of the plugin: no file of `scratchpad/ship-plugin` changed after the installs.

## For the next session

- `/hi` in a project that is no git repository: it should go on and tell the person to run `git init`, or offer to run it (the person's word; `lesson-hi-fails-outside-a-git-repository`).
- `/guppi:install` with no `uv`: whether it offers to install `uv` (the person's word).
- `/guppi:install` when `uv sync` fails offline: the person asks to discuss it again; whether `uv sync` should take the `dev` group in a user's project at all.
- The draft core pages that stop every build of `prod`, and the next tag after `prod-0.2.0`, which the push of this session spent.
- The tag `prod-0.2.0` stands on GitHub on a commit whose run failed; whether it stays.

## Ask the person

- `estimate-clean-branch-installs-as-a-plugin` — needs the person — in session 0104 the person added `scratchpad/ship-plugin` as a catalogue and installed `guppi` from it, and said it installed; did the catalogue add and the plugin install with no error?
- `estimate-guppi-package-is-ready-after-the-install` — needs the person — in session 0104 the person reported: in `C:\PROJECTS\test-no-uv` the install said `uv` is missing and wrote nothing; in `C:\PROJECTS\test` it built `.guppi/.venv/` and the hooks ran at the first `/hi`; in `C:\PROJECTS\test-uv-offline` `uv sync` failed and it stopped, but told the person to type `/hi` after a fix. Does that pass the Criterion?
