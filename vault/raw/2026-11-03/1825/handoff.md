# Handoff — 2026-11-03, the sprint plugin: transcripts at /hi, the source pictures of the icon

## Notes from memory

- The person found it absurd that `/hi` could not read a transcript a method names, and asked for a fix rather than a defer of the one Estimate. The person then asked how such an Estimate reaches the clean version, and asked for a one-off reading of the past build beside a lasting Estimate. That is the split of Case 1019.2 and 1019.3. The person kept the split to this one Estimate. Whether it becomes a rule is the backlog line of Case 1019.4, which the person asked for as a separate item.
- At `/pre-spec` the person chose that Case 1019.1 also updates the Purpose of `rule-raw-archive`, because the new `/hi` reads the first line of an archived `spec.md`.
- The person put off the milestone The plugin (Case 1021) and C1, the clean branch, together with the readings W1, W2 and W5. Each of them needs the same install by hand from a `--allow-draft` copy in a separate Claude Code window. The person first asked whether those readings had already been taken: W5 passed in session 0327 on an older Criterion, and W1 and W2 were never read, since `/setup` stood only from session 0316 on.
- `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` passed on one judgment of mine. The build of Case 1012 read `.guppi/.gitignore` and not the root `.gitignore`. I read "each ignore file of git in a folder that holds those files" as the folders `.guppi/`, `.guppi/guppi/` and `.guppi/tests/`. `git check-ignore` printed neither new file. The person may judge otherwise.

## Direct instructions to the librarian

- Case 1019.4 and Case 1021 both name `entity-sprint-plugin`: 1019.4 adds a line to its `## Backlog`, and 1021 defers the page for the milestone The plugin. `guppi prespec --check` printed the pair as a note.
- Case 1019.1 holds two `replace` pairs on `rule-skill-hi`. The second changes "that you cannot open that chat (as set in case 921)" to "that you do not open that chat (as set in cases 921 and 1019.1)". Check that both match the page once, and that `.claude/skills/hi/SKILL.md` renders the new step.
- Case 1020 adds `plugin/assets` to the `implementation_ref` of `rule-clean-branch`. The folder exists since Work Mode.
- The decision line of Case 1019.1 on `rule-raw-archive` stands at L11, after the lines of Case 1020 and 1021, because it came in the re-ratification after `/pre-spec`.

## What actually got done

- Cases ratified: 1019 (1019.1–1019.4), 1020, 1021 (short-form defer).
- Code and tests: `plugin/assets/icon_guppi.png` and `plugin/assets/logo_guppi.png` moved from `guppi-assets/` by `git mv`, and `guppi-assets/` removed. `.guppi/tests/test_ship.py` gains three tests whose names hold `source_pictures`, and its module docstring names them and the new Estimate.
- `uv run --project .guppi guppi test`: 1946 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: L1 and L2 at `/hi` (`estimate-skill-sprint-open-asks-the-opening-questions`, `estimate-clean-branch-refuses-a-draft-core-page`, both passed). The four readings of Retro follow L11: `estimate-hi-takes-its-readings`, `estimate-case-build-reads-the-readers-of-a-new-files-folder`, `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` and `estimate-clean-branch-leaves-out-the-source-pictures`, all passed. No lesson.

## Debt

- No box of the Spec is debt.
- 13 boxes wait for the librarian: the page, render and read lines of Cases 1019 and 1020.
- `estimate-morph-sets-up-the-project-at-the-first-hi`: waits for an install by hand from a `guppi ship --allow-draft` copy into an empty git project, with `/hi` typed there.
- `estimate-morph-takes-in-the-set-aside-files`: waits for an install by hand into a git project with its own `CLAUDE.md`, `.claude/settings.json` with a hook, `.gitattributes` and a tag `prod-x.y.z`.
- `estimate-git-context-offers-git-init`: waits for an install by hand into an empty folder with no git, with `/hi` typed three times.
- `estimate-sprint-plugin-installs-as-a-plugin`: waits for the same install by hand, in a session of the sprint before its close.

## Observations

- `guppi check` printed `rules/rule-morph: status: a page with core: true that is draft` before the work. It is the baseline line, and Case 1017.8 intends it.
- `ask-guppi` at `/pre-spec`, by its own report, broke its frame: it ran Globs and Greps over `vault/archive/` that were not by slug, and Globs and a count Grep under `~/.claude/projects/`. Findings 1 and 2 rest partly on them.
- When I closed C4 of `frontier.md`, the hook `guppi frontierguard` of Case 1012 refused an edit that appended the closer and left the box `[ ]`. The edit of the whole line then passed.

## For the next session

- The milestone The plugin and the clean branch, put off by Case 1021 and C1: the three readings by install and the install reading of the sprint can be taken in one session that prepares the copy and three folders.

## Ask the person
