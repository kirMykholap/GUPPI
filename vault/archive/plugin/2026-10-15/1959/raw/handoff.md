# Handoff — 2026-10-15, sprint plugin: pointers of shipped Estimates, neutral rules, setup first, tags from lessons

## Notes from memory

- The person did not see at first what C2 (Case 825) decides. They said that `/guppi:install` is the copy of the plugin and is no Case, and that only the project setup is a Case. That is where the rename "install Case" → "setup Case" comes from.
- On C13 (Case 826) the person asked why the ledger hook refuses a new tag at all. That question became a Frontier item of its own (C21, Case 827). The person wanted a plain explanation of what tags serve before choosing: a re-pitch by `/wait-what`.
- In Case 827 the person chose (b) for the check of 827.4. No Estimate reads the header of `tags.md` or the exception sentences in `rule-vault-layout`, `rule-page-generation` and `rule-documentation`. The person knew this and chose it; `/pre-spec` left the finding open on that answer.
- The person put off every other open item of the Frontier in one answer ("Откладываем остальное"): twelve short Cases, 828–839, and the sprint item C1 left as `· sprint · defer`.
- Cases 823, 824, 825 and 827 were built again on the findings of `/pre-spec` and ratified again. Case 825 gained an `update` of `rule-permissions` there.

## Direct instructions to the librarian

- Cases 824 and 825 both change `rule-morph` and `rule-permissions`. 824 writes "setup Case" in the sentences it writes; 825 renames "install Case/step/as done" by `replace` pairs built on today's text, and on `rule-permissions` changes only the words after the colon of the last Purpose sentence, which 824 leaves. Check that both apply on the page in ledger order with no pair missing its `old`.
- Case 825 changes `entity-sprint-plugin` while Case 830 defers it, and Case 827.4 changes `rule-documentation` while Case 839 defers it. Each defer stands for what the change does not fix.
- Case 826 declares `retro` and `box` for `tags.md`. The header of `tags.md` was changed by hand in Work Mode by the one-off task of Case 827.4; its table was not touched, and the rows `retro` and `box` come from this run.
- The renders this run owes: `ratification.md`, `case-schema.md`, `.claude/agents/case-guppi.md`, `.claude/agents/librarian-guppi.md`, `CLAUDE.md` and `guppi.toml` where their rules change, and `glossary.md`.

## What actually got done

- Cases ratified: 823 (823.1–823.6), 824, 825, 826, 827 (827.1–827.4), and the short defers 828–839.
- Code: `.guppi/guppi/prespec.py` (an Estimate of a core target judged for pointers: `new_criterion`, `target_slug`, `core_target`; `written_texts` reads `method`), `.guppi/guppi/materialize.py` (`parse_line` gives a lesson `new_tags` by `_new_tags`; the yaml takes them after the tags of the Cases), `.guppi/guppi/tags.py` (`lesson_tags`), `.guppi/guppi/ledger.py` (`refused_tags` takes declared tags; new `tag_message`).
- Tests: `test_prespec.py` (six `pointer` tests), `test_ledger.py` (new `unlisted_tag` tests and the new refusal words), `test_materialize.py` (four `newtag` tests), `test_ship.py` (one test marked `live`).
- Settings: the marker `live` and `addopts = '-m "not live"'` in `.guppi/pyproject.toml` and in the root `pyproject.toml`.
- `vault/wiki/tags.md`: the header, by hand (Case 827.4). `plugin/skills/install/SKILL.md`, untracked since the last librarian's run, is committed.
- `uv run --project .guppi guppi test`: 1 failed, 1714 passed, 6 skipped, 1 deselected (the `live` test). `uv run --project .guppi guppi style`: clean.
- Readings: L1–L5 at `/hi` (L5 failed); L66–L72 at Retro, all passed. Lesson: L73.

## Debt

- No box of code, a test or a command is unticked.
- 59 boxes wait for the librarian: the page, render, glossary and `read` lines.
- `estimate-clean-branch-ships-estimates-with-pointers-only-in-brackets` — waits for the librarian's run of this session, then `uv run --project .guppi pytest .guppi/tests/test_ship.py -m live`.
- `estimate-clean-branch-ships-neutral-texts` — waits for a tag `prod-x.y.z` in the history of HEAD and the librarian's run of this session.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — waits for the session whose Work Mode builds the setup step and its step in `/hi`.
- `estimate-ratification-ledger-line-form` — waits for a session whose ledger holds a lesson with the Case that closes its cause, a Case that takes up a decision with more than one Case in its `deferred_by`, and a lesson line that declares a new tag.
- `estimate-clean-branch-ships-the-tests` — waits for a tag `prod-x.y.z`: `guppi ship --allow-draft` writes nothing without it.
- `estimate-clean-branch-writes-the-session-files` — waits for a tag `prod-x.y.z` and an install in an empty project by hand.

## Observations

- Red before the work, by `## Baseline` of `work.md`: `test_guppi_package.py::test_no_live_page_names_the_old_command_or_path_where_a_reword_changes_it[tests/]` (the reading L5 failed on it; Case 837 defers it), and the 17 lines of `guppi check`: `backlog.md differs from its sources`, ten draft pages with `core: true`, three `unread: failed`, three `method` findings.
- The new `live` test of `test_ship.py` is red by design until this run: it found 20 `ship:` lines on shipped Estimates, the first `estimate-ask-finds.md:7: a reference to a case: case 782`. It is left out of every default run.
- The pytest settings that Case 823.1 named, in `.guppi/pyproject.toml`, are not read by `guppi test` from the root, which reads the root `pyproject.toml`. Work Mode set the same two lines there. In the clean version, which holds no root `pyproject.toml`, a run from the root reads neither; this is the open question of Case 834.
- `guppi prespec --check` with the widened judgment of Case 823.6 printed no finding over this session's plan.
- `ask-guppi` reported that it read an archived page by Grep against its frame; no finding rested on it.

## For the next session

- The sprint item C1 is left: the tag `prod-x.y.z` and the run of `prod.yml`. The draft pages with `core: true` still stop every build of `prod` without `--allow-draft`.
- Whether the root `pyproject.toml` keeps the pytest settings beside `.guppi/pyproject.toml` until the Case that removes it.

## Ask the person
