# Handoff — 2026-11-04 (Work Mode 2026-11-20), the speed of a Case and fixes from the trial installs

## Notes from memory

- The person asked to make GUPPI faster. The first idea, effort raised during a Case with no question, cannot be built: the docs name no way to change the effort of a running agent, and changing `output_config.effort` invalidates the message cache. The person agreed to effort chosen at the dispatch, with no model passed and no raise (Case 1029). The main agent first told the person that the agent files held no `effort` or `model`; that was false (L59).
- The person wants questions of form (how a Case splits, which Estimate, which page) settled by `case-guppi` without a question. Case 1031 sets it; it reaches `case-guppi` only at the librarian's render, so this session still asked such questions.
- On Q2 of Case 1031 the person first leaned to never asking about the project's tests, then chose (b): ask only where the project holds code of its own, worded as how the project's tests run beside GUPPI's.
- Case 1032 was built before Case 1035 found that Claude Code 2.1.317 writes `[command hook <number>]` in the bracket of Stop feedback; 1032 was shown again with 1035 and once more after the `/pre-spec` findings (L60).
- The Claude Code process ended twice while a background agent ran; each was resumed by a message (L58). Plan Mode spanned 2026-11-04 to 2026-11-20 with pauses.

## Direct instructions to the librarian

- Case 1029.2 and Case 1031.1 change `estimate-case-build-writes-the-case` and create `estimate-case-build-settles-form-by-itself`; the promises on a new Case beside a ratified one moved from the first to the second on purpose. Check that no line stands in both.
- Case 1032.1 renders `.claude/settings.json` and the frontmatter of `.claude/agents/librarian-guppi.md` with `uv run --project "${CLAUDE_PROJECT_DIR}/.guppi"`. The code already takes both forms; check that `guppi render --check` and `test_every_hook_command_runs_the_code_from_the_project_folder` pass after the render.
- Case 1034.2 carries `{supersedes:case 1008}` on `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline`; its defer should leave `backlog.md`.
- Case 1036 also sets only the `method` of `estimate-clean-branch-writes-the-session-files`; its Criterion and status stay.
- `vault/raw/2026-11-04/0807/agents-baseline.md` holds the output of `guppi agents` over this session and the three trial installs of session 0358, the numbers the trial of Case 1029 starts from.

## What actually got done

- Cases ratified: 1029 (1029.1–1029.4), 1030 (1030.1, 1030.2), 1031 (1031.1–1031.3), 1032 (1032.1–1032.4), 1033, 1034 (1034.1–1034.3), 1035 (1035.1–1035.3), 1036; short-form defers 1037 and 1038.
- Code: `.guppi/guppi/ledger.py` (a refusal found by the name of its hook after the bracket, `own_text`, `hook_name`; `PROJECT_RUN` with the project folder, `command_forms` keeping the form with `--project .guppi`), `.guppi/guppi/onward.py` (every line of the `--plan` run opens with `onward --plan:`), `.guppi/guppi/casecheck.py` (comment), `.guppi/guppi/agents.py` (new, `guppi agents`), `.guppi/guppi/cli.py`, `.guppi/guppi/ship.py` (`without_empty_comments`, `FORMAT` with its cache outside the copy, `CODE_WRITE_ENTRY` in each form), `.guppi/guppi/pointers.py` (`BRACKET` takes a bracket alone on its line), `.guppi/guppi/sprint.py` (the setup line literals), `.guppi/.gitignore` (`__pycache__/`).
- Tests: `test_agents.py` (new), `test_ledger.py`, `test_onward.py`, `test_casecheck.py`, `test_ratified.py`, `test_guppi_package.py`, `test_ship.py` (`own_style` tests, `test_own_tests_pass_over_the_copy` marked `live`, a `no_code_write_hook` test of the new form), `test_lint.py`.
- `uv run --project .guppi guppi test`: exit 0, 1976 passed, 6 skipped, 2 deselected. `uv run --project .guppi guppi style`: clean. The `live` test over the copy: 1 passed.
- Readings L45–L57: twelve passed, `estimate-case-build-offers-a-page-for-code-no-page-covers` failed (L57). Lessons L58–L60. The ledger hook held the two error lessons once under `[command hook 1]` and wrote them on the repeat, with the new code.

## Debt

- No box of code, a test or a command is unticked.
- 73 boxes wait for the librarian: page, render and `read` lines.
- `estimate-orchestration-dispatches-case-guppi-at-a-level` — after a session whose `orchestration.md` holds the text of Case 1029.1.
- `estimate-case-build-writes-the-case` — after a session whose `orchestration.md` sets the effort of each dispatch of `case-guppi`.
- `estimate-case-build-settles-form-by-itself` — after a session whose `case-guppi.md` holds the text of Case 1031.1.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — after the librarian's run of this session: two installs from an `--allow-draft` copy, an empty git project and one with code of its own.
- `estimate-guppi-package-runs-from-its-own-folder` — after the librarian's render of the harness: a session with a `cd` in a Bash call and later tool calls.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — after the librarian's render of `.claude/skills/work/SKILL.md` and the first `/work` after it.
- `estimate-git-context-offers-git-init` — after the librarian's run of this session: an install into a folder that is no git repository.
- `estimate-sprint-plugin-case-guppi-level-trial-decided` — the session that closes the sprint `plugin`.

## Observations

- `guppi agents` counts `seconds` of the main agent from the first record to the last, pauses included: 1402372 for this session, which spans 2026-11-04 to 2026-11-20. A run cut off by the end of the process has no notice and is not counted, and a librarian run in the foreground shows `runs -`.
- The `claude-code-guide` agent ran on `claude-haiku-5-5`; every `case-guppi` and `ask-guppi` on `claude-opus-5-5`.
- Rounds that asked only a question of form cost a full run: after the person's "Ок" on Case 1030 the run took 274 s and returned a form question; on Case 1029 a 113 s run did the same.
- The two Stop feedback records of this session before the change read `[command hook 6]: onward: …`, so the bracket no longer holds the command in Claude Code 2.1.317.
- The `estimate-retro-onward-sends-the-agent-to-the-handoff` reading took the tests only; the by-hand part at the end of Retro came after the reply.

## For the next session

- `estimate-case-build-offers-a-page-for-code-no-page-covers` failed (L57): the Render of Case 1031.2 says "`context` names the page" and sets no reason, while its Criterion asks for the reason too. Either the Render or the Criterion changes.
- L60: a later Case can leave a ratified Case's text stale; it joins `insight-case-build-sibling-texts-unchecked-before-the-showing` in kind. Whether a step searches the ratified Cases for lines that rest on what a later Case changes, before the showing.
- `.github/workflows/prod.yml` runs neither style nor tests over the copy, so a copy whose tests fail can still reach `prod`; whether the suite passes on Linux is not read.
- The plan approval that `/guppi:install` asks in Plan Mode stays as it was (Case 1036 left it out).

## Ask the person
