# Handoff — 2026-11-04, the install readings of the setup and the hook guppi codewrite

## Notes from memory

- The person took the three trial installs through whole sessions and judged the result a failure of speed and clarity, not of the install: each trial session took 45 to 55 minutes, about 40 of them agent time, for three settings and the opening of a sprint, and the person's own words were the description and the sprint goal; the rest were "ok" and "ratify".
- The person found the questions on the keys `test` and `style` of the setup Case unclear and proposed to remove them, or to ask them only where the project holds code of its own; the change of `rule-skill-setup` and `rule-morph` was left for the next Plan Mode.
- The person asked whether the slowness comes from the concept of GUPPI or from the model: the trials ran on `opus[1m]` with `effortLevel: high`, subagents included, and every main model call read about 140k tokens; the routine setup and opening Cases went through the full `case-guppi` build and the `ask-guppi` audit, whose 6 to 11 findings per session were all of the kind "the context does not name Estimate X" and changed no ratified decision line. The person wants to understand which part costs what.
- Earlier in the session the person asked why a whole Case was built only to put off a reading, and why the work was put off rather than taken: that led to Case 1026 and the installs.

## Direct instructions to the librarian

- Cases 1022, 1023 and 1024 are superseded by 1026.1, 1026.2 and 1026.3, and Case 1027 by 1028.1; the decision of 1014 is superseded by 1026.5 for `estimate-orchestration-acknowledging-reply`.
- `rule-clean-branch` is updated by both 1028.1 and 1028.2; apply both replace sets to the one page.
- The render of `.claude/settings.json` registers `guppi codewrite` on `PostToolUse` of `Edit|Write|MultiEdit`; the module `.guppi/guppi/codewrite.py` and its command in `cli.py` already stand.
- The four lessons below under Observations were held twice by the ledger hook and may be missing from the ledger: check the ledger for them first.

## What actually got done

- Cases ratified: 1025 (1025.1, 1025.2), 1026 (1026.1 to 1026.5), 1028 (1028.1, 1028.2).
- Code: `.guppi/guppi/ship.py` (`live_code`, `without_code_write`, `CODE_WRITE_ENTRY`, `codewrite.py` in `LEFT_OUT`), the new `.guppi/guppi/codewrite.py`, `.guppi/guppi/cli.py` (the command `codewrite` under `ship_stands`), `.guppi/tests/test_ship.py` (10 new tests, `live_code_lines` by `ship.live_code`).
- `guppi test`: 1956 passed, 6 skipped, 1 deselected; `guppi style`: clean.
- The copy of `guppi ship --allow-draft` and three trial folders under `C:/PROJECTS/guppi-trial-0358/`, installed by the person.
- Readings: ledger lines 4 to 8 of the Retro block, five of Case 1026 (two failed: `estimate-morph-sets-up-the-project-at-the-first-hi`, `estimate-git-context-offers-git-init`), and the readings of `estimate-case-build-reads-the-readers-of-a-new-files-folder`, `estimate-clean-branch-names-a-pointer-at-the-write` and `estimate-clean-branch-ships-no-code-write-hook`, all passed; the three readings at `/hi` stand at lines 1 to 3.

## Debt

- No box is debt.
- 16 boxes wait for the librarian.

## Observations

- Four lessons were written in the `LEDGER` block of the reply that ends Retro and held twice by the ledger hook with its question on `{addressed_by:...}`, though its docstring says a lesson is held once; the same double hold happened in the trial in `empty-git`. If the ledger does not hold them, the next session writes them:
  - `lesson-hooks-relative-project-path-fails-after-a-cd` (hooks, plugin): a `cd` in a Bash call moves the working folder of every later hook, `uv run --project .guppi` then fails with exit 2, and every tool call and reply is refused; it froze the trial in `no-git` until Esc, and a Bash call of this session moved the shell into `vault/wiki/estimates` too.
  - `lesson-ship-leaves-an-empty-comment-after-a-removed-pointer` (plugin, ci): the copy fails its own style (51 PLR2044 empty comments, 5 files to reformat) and two tests, since the cleaning leaves a `#` and a space at the end of a line where it removed a bracket.
  - `lesson-plugin-install-leaves-pycache-untracked` (git, plugin): no ignore file of the copy covers `__pycache__/`, and the gate refused `/handoff` on it.
  - `lesson-git-context-plan-mode-blocks-git-init` (git, plugin): `"defaultMode": "plan"` of the copy's `.claude/settings.json` keeps the agent from running `git init -b main` on the person's yes.
- In every trial, Work Mode stopped on `main`: `/sprint-open` writes no branch task when the branch is `main`, so the first sprint of a new project always stops there.
- Every setup Case asked, beside the values the Criterion lists, how the Case is split and how it is checked: the frame of `case-guppi` asks those of every Case.
- In each trial the person ratified the setup and opening Cases twice: once in the build, once after `/pre-spec` rebuilt their `context`.
- The `/guppi:install` of each trial asked the person to approve a plan, since the session opened in Plan Mode.

## For the next session

- Fix the hook commands so that a `cd` in a Bash call cannot break them, such as `--project "$CLAUDE_PROJECT_DIR/.guppi"`; this risk stands in this repository too.
- Fix the cleaning of `guppi ship` so that the copy passes its own style and tests, and add a test that runs them over the copy.
- The opening Case of the first sprint on `main` gets a task `git switch -c <id>`.
- The copy ignores `__pycache__/`.
- The step of `rule-git-context` in a session that opens in Plan Mode: the default mode of the copy, or how the step runs `git init`.
- The setup Case asks only the values of the Criterion: drop the questions on the split and the check, and remove the questions on `test` and `style` or ask them only where the project holds code of its own.
- The cost of a routine Case: whether the setup Case and the opening Case need the full `case-guppi` build and the `ask-guppi` audit, and whether the subagents run on a smaller model or a lower effort; a trial session with effort medium or Sonnet, measured against this session's numbers.
- The ledger hook holds a lesson twice where its docstring says once.

## Ask the person
