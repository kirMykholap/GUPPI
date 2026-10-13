# Handoff — 2026-10-13, sprint plugin: the causes of three lessons, lint's red lines, the orphan rule

## Notes from memory

- Case 795: the person turned down every grouping rule page as the parent of `rule-github-repository`. The rules of the GUPPI repository can differ from those of a repository of someone who uses GUPPI, so the repository became an entity of its own. The rule links to it by `applies_to` and has no `parent`, as `rule-sprint-close` has none.
- Case 796: the person asked for a plain explanation of what a heredoc is before answering, then chose a check in both shells, against the recommendation of Bash only.
- Case 799: the person asked how a waiting event is found later once lint stops marking it red. The answer they accepted: the brief's Readings due and Work lists find it, and lint never did. They also chose that one waiting part of a `method` is enough. Lint therefore leaves out `estimate-ask-finds` and `estimate-hi-writes-frontier` too, although part of each could be read now.
- The person added the red lines of `make lint` as an item of their own (Case 799), and `rule-morph` as a separate item. They then put off the rest of the Frontier: the milestone The clean branch stays in the sprint, and `rule-morph` stays in the backlog as it stood.

## Direct instructions to the librarian

- Case 795.1 creates `entity-guppi-repository` under `entity-guppi` and gives `rule-github-repository` `applies_to: entity-guppi-repository`. Check that the cascade writes the rule into the `rules` of the new entity, created in the same run, and that `make lint` then prints no `orphan` line for `rule-github-repository`.
- Case 796.1: the section `## How it works` of `rule-bash-guard` was removed by hand in Work Mode, by the Case's task. The `update` of the page sets only `purpose` and `## Purpose`. Do not bring the section back.
- Cases 797.1, 798.1 and 798.2 all update `rule-case-build`, with three `replace` entries on different sentences. Check that each one carries `applied`, and render `.claude/agents/case-guppi.md` once after all three.
- Case 796.2 adds a `PowerShell` entry to the Render of `rule-hook-registry`. Render `.claude/settings.json`, and check that the entry stands after the `Bash` entry of `guppi bashguard`.
- Case 798.1 sets `insight-case-build-recommends-without-reading-the-governing-rule` `actioned`, with `addressed_by: decision-case-798.1`. Its two lessons should be archived by the cascade.

## What actually got done

- Ratified: Cases 795 (795.1, 795.2), 796 (796.1, 796.2), 797 (797.1, 797.2), 798 (798.1, 798.2) and 799. Cases 796–799 were built again on the findings of `/pre-spec` and ratified again with the same decision lines.
- Code: `guppi/materialize.py` (`create_lacks` judges the parent of a Leaf rule, with its `ref` or `applies_to`; `_lift_item` marks by it alone); `guppi/prespec.py` (`check_required` passes the `ref` of the item or of its decision line); `guppi/bashguard.py` (`interpreter`, the one judgment of an interpreter fed inline, and the third reason, `it feeds <interpreter>`); new `guppi/powershellguard.py`; `guppi/cli.py` (the command `powershellguard`); `guppi/lint.py` (`waits_for_a_later_moment`; `check_unread` leaves out a pending Estimate whose method waits).
- Tests: `tests/test_prespec.py`, `tests/test_bashguard.py`, new `tests/test_powershellguard.py`, `tests/test_lint.py`.
- Page by hand: `vault/wiki/rules/rule-bash-guard.md`, `## How it works` removed (Case 796.1).
- `make test`: 1587 passed, 6 skipped. `make style`: clean, after `ruff format` of `tests/test_powershellguard.py`.
- Readings: ledger lines 22–28, six `passed` and one `failed` (line 28, `estimate-case-build-reads-the-last-output-of-a-check`). Lessons: lines 29 and 30.

## Debt

- No box of code, a test or a by-hand check is left unticked.
- 33 boxes wait for the librarian: page, render and read lines.
- `estimate-powershell-guard-refuses-a-here-string-piped-into-an-interpreter`: waits for the librarian's run of this session that renders `rule-hook-registry`. Its test part passed at Retro (11 passed).
- `estimate-case-build-judges-by-the-state-at-the-moment`: waits for the event its method names, a Case built by `case-guppi`, as rendered by Case 797.1, whose form or reading depends on another Case of the same session. The Cases of this session were built before that render.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live`: waits for the first Case `case-guppi` builds that changes a reader in code and the text or the writer it reads. No Case of this session did.
- `estimate-hi-writes-frontier`, `estimate-skill-merge-main-joins-a-conflicted-page` and `estimate-skill-pr-review-takes-a-pull-request-whole`: wait for the moments their methods name, unchanged.
- The five Estimates of `entity-sprint-plugin`: each waits for the Retro of the session that finishes its work, or for the close of the sprint.

## Observations

- Red before the work, held by `## Baseline` of `work.md`: `make lint` printed `backlog: vault/wiki/backlog.md differs from its sources`, `rules/rule-github-repository: orphan` and `rules/rule-morph: deferred: 4 times since case 239`. All three still printed after the work. The ten `unread: pending` lines of the Baseline are gone with Case 799.
- `estimate-ask-finds` was read in Work Mode on the ask-guppi run of this session's own `/pre-spec`, which also runs on the render of case 782. At `/hi` it had been left open, because the transcript of session 2349 may not be read.
- The `failed` reading of `estimate-case-build-reads-the-last-output-of-a-check`: the new sentence of Case 798.2 says that `context` names the last output of a check, but its Criterion asks that `context` quotes the output with its source.
- The Bash guard of the working tree refused a live `python - <<'EOF'` call at Retro, as Case 796.1 sets. Since Work Mode, an agent that feeds a heredoc to Python is refused in this repository.
- At the exit of Plan Mode, the auto mode of Claude Code advised in its own text to make small file changes with sed, heredocs or short scripts through Bash. That is the habit Case 796 refuses. The guards hold against it, but the advice comes back at every exit of Plan Mode in auto mode.

## For the next session

- The `failed` reading of `estimate-case-build-reads-the-last-output-of-a-check`: change the sentence of `rule-case-build` so that `context` quotes the output with its source, or change the Criterion to "names".
- The milestone The clean branch (CI that writes `prod`) is still the current one. It was put off in this session.
- `rule-morph` is still a placeholder, put off 4 times. The person wanted it taken up, then left it in the backlog as it stood.
- The cause of `lesson-case-build-gave-a-sub-case-no-estimate`, and the cause of `lesson-ask-guppi-read-a-decision-page-without-a-reason`.

## Ask the person
