# Handoff — 2026-11-26, the Frontier guard, the main branch setting, the split of a transcript reading

## Notes from memory

- The person took up two backlog items at the agent's discretion ("на твое усмотрение"): the name of the main branch (Case 1070) and the split of a transcript reading (Case 1071). Every recommendation of every round was accepted as given.
- Case 1069.1 refuses every shell command whose text names the Frontier file, reads and commit messages included. The person chose that knowing a commit message naming the file is refused; the reason tells the agent to name the Frontier in words.
- `/pre-spec` found that the first session of a new project on `master` would run the opening Case with `main`, since the setting lands only at the librarian's render. The person chose that `/sprint-open` and `/work` in the session of the setup Case take the name from that ratified setup Case (Case 1070.4).
- Case 1070 is large (23 decision lines). After the re-ratification, `guppi prespec --check` found one more finding: a pointer to a case outside a bracket in the new Criterion of `estimate-morph-sets-up-the-project-at-the-first-hi`. That Case was built again and ratified a third time with the same lines.
- Two lines of Case 1070.6, in its `context` and its `given`, still speak of the `purpose` alone, while the sub-case also gives `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` a new `method`. `ask-guppi` judged this harmless.

## Direct instructions to the librarian

- `entity-sprint-plugin` takes two `## Backlog` pairs, one from 1070.3 and one from 1071.1. Each removes its own line with an empty `new`, and 1070.3 also adds a line under `## Closed`. Check that both apply and that `## Backlog` keeps no blank line between items.
- The render must fill `{{main_branch}}` in the Renders of 1070.4 and 1070.5 from the new `main_branch = "main"` of the Render of `rule-guppi-config`. In this repository every rendered file should read as before.
- `insight-orchestration-frontier-closer-leaves-the-box-open` goes `actioned`, with `addressed_by` `decision-case-1069.1`.
- The `rule-hook-registry` pairs add `guppi frontierguard` to the PreToolUse entries of Bash and of PowerShell. From the next session on, a Bash or PowerShell command that names the Frontier file is refused. This holds for the librarian's own commands too, so name the session folder or use Read and Grep.

## What actually got done

- Cases ratified: 1069 (1069.1, 1069.2), 1070 (1070.1 to 1070.7) and 1071 (1071.1, 1071.2).
- Code: `.guppi/guppi/frontierguard.py` (shell calls; a closed box with no closer), `prespec.py` (`line_closer`, `closed_boxes_without_closer`, the transcript findings in `check_form`, `kept_transcript_readings` run from `judge`), `config.py` (`BRANCH_KEY`, `DEFAULT_BRANCH`, `branch_of`, `branch_in`, `main_branch`), `render.py` (`{{main_branch}}`), `box.py` (reads `main_branch` in place of `SHARED_NEVER`), `gitstate.py` (docstring), and `lint.py` (`reads_a_transcript`).
- Tests: `test_frontierguard.py`, `test_config.py`, `test_render.py`, `test_box.py`, `test_lint.py` and `test_prespec.py`.
- `uv run --project .guppi guppi test`: 2034 passed, 6 skipped, 2 deselected. `uv run --project .guppi guppi style`: clean.
- Readings, in the one Retro block: `estimate-frontier-hook-refuses-a-shell-command-on-the-frontier`, `estimate-frontier-hook-refuses-an-open-box-with-a-closer`, `estimate-spec-box-refuses-a-stale-spec`, `estimate-morph-sets-up-the-project-at-the-first-hi`, `estimate-case-protocol-splits-a-transcript-reading` and `estimate-prespec-hook-reports-a-method-that-reads-a-transcript`, all `passed`. No lesson.

## Debt

- No box of code, test or command is left unticked.
- Every other unticked box is a page, render, sprint, glossary or read line and waits for the librarian.
- `estimate-guppi-config-fills-the-main-branch` — its `method` waits for the librarian's run of this session: `guppi.toml` read for `main_branch = "main"`, and the output of `guppi render --check`. Its tests pass now (`-k main_branch`).
- `estimate-sprint-plugin-skills-name-the-main-branch-by-its-setting` — one-off on the sprint page; waits for the librarian's run of this session.
- `estimate-sprint-plugin-vault-writer-texts-name-the-main-branch` — one-off on the sprint page; waits for the librarian's run of this session.
- `estimate-sprint-plugin-setup-takes-a-main-branch-other-than-main` — one-off on the sprint page; waits for a new install in a project made by `git init -b master`, from a copy that `guppi ship --allow-draft` writes after the librarian's run of this session, taken to its own librarian's run.

## Observations

- The three updates of Case 1070.6 name a part of their pages and set no status, so Retro neither read them nor set them `failed`. `estimate-clean-branch-ships-neutral-texts` covers them.
- In this session the Frontier guard runs its new edit judgment already, since the hook runs the code of the working tree. The shell refusal waits for the render of `.claude/settings.json`.

## For the next session

- Sprint item C1, `rule-clean-branch` (the clean branch), was put off again at the close of Plan Mode.

## Ask the person
