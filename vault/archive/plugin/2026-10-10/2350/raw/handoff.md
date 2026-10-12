# Handoff — 2026-10-10, sprint plugin: the merge at the opening of a sprint, one supersede line

## Notes from memory

- The person found it odd that the milestone line on the opening and the close of a sprint kept the current milestone open to the end of the sprint; Case 774 removes the line rather than moving it, since the close line of the last milestone and its Done-when Estimate already hold the close.
- The person took up C1 and the two deferred skill pages of case 771 in one answer, so Cases 774 and 775 went out as a batch.
- The person left the milestone line on the repository on GitHub (`· sprint · defer`) by the words "Идём работать"; it stays the open line of the current milestone.
- Pre-spec found that a refused merge at the opening fit no stop condition; by the person's answer Case 775.3 widens condition 6 of `rule-where-to-stop`. The `recommend` sections of Cases 774 and 775 keep the wording of the answers as given, before that fix; their `context` holds the corrected facts.
- The person chose to leave the two doubled `superseded by decision-case-772.1` lines of the run of session 1913 — in `vault/wiki/log.md` and in the History of the archived `decision-case-764.1` — as the record of that run (Case 773).

## Direct instructions to the librarian

- Check first that `{supersedes:case 771}` on the lines of 775.1 and 775.2 clears `decision-case-771` from the `deferred_by` of `rule-skill-sprint-open` and `rule-skill-sprint-close`, so that `guppi backlog` drops both items.
- Cases 774 and 775 were ratified twice, the second time after the findings of pre-spec, with the same decision lines; the ledger holds each line once. 775.3 came only in the second ratification.
- The render changes `.claude/skills/sprint-open/SKILL.md`, `.claude/skills/sprint-close/SKILL.md` and `vault/wiki/where-to-stop.md`; check that each holds its new step or condition.
- `guppi sprint` writes `vault/wiki/sprint.md` with the current milestone holding the GitHub line alone.

## What actually got done

- Cases ratified: 773, 774, 775 (775.1, 775.2, 775.3).
- Code: `guppi/generate.py` — one helper, `take_superseded_by`, writes the `superseded by` History line only when it adds the name to `superseded_by`; the step for a page named in `supersedes` and the step for a sub-case call it. Test: `tests/test_generate.py`, one new test, red without the change.
- `make test`: 1495 passed, 6 skipped. `make style`: clean.
- Readings: ledger lines 9 to 12, all `passed`. Lesson: ledger line 13.

## Debt

- None.
- 16 boxes of the Spec wait for the librarian.
- `estimate-sprint-plugin-close-steps-run-from-the-line`: the end of Work Mode of the session that closes `plugin`.
- `estimate-sprint-plugin-readme-describes-the-project`: the person's answer at the `/hi` after the session whose Work Mode writes README.md under the milestone The plugin.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github`: the Retro of the session that sets up CI and a pull request from a second account, or the close of the sprint.
- `estimate-sprint-plugin-ci-writes-a-clean-branch`: the Retro of the session that builds the CI of the clean branch, or the close of the sprint.
- `estimate-sprint-plugin-installs-as-a-plugin`: the Retro of the session that installs the clean branch into an empty project, or the close of the sprint.
- `estimate-hi-writes-frontier`: the `/sprint-open` of the session after the close of `plugin`.
- `estimate-brief-written`: the `/hi` after the librarian's run of the session that closes `plugin`.

## Observations

- `make lint` was red before the work, 8 lines: `rules/rule-morph: deferred: 4 times since case 239` and `unread: pending` on `estimate-brief-written`, `estimate-hi-writes-frontier` and the five Estimates of `entity-sprint-plugin`.
- `gh` is not authenticated on this machine (`gh auth login` asked); `.github/workflows` does not exist, and the repository holds the branches `main` and `plugin` alone.
- `make style` found the new test unformatted before the commit; `ruff format` fixed it.

## For the next session

- The step of `rule-skill-hi` that makes a Cases line for an open `W` line whose reading cannot run now does not leave out an Estimate of the live sprint page whose work is not done, as `rule-brief` and `rule-retro` do since case 772: the lesson of ledger line 13.
- The milestone line "the repository on GitHub set up so that a pull request from another person is easy to review" was put off untouched; it now holds the current milestone open alone.
- The Criterion of `estimate-sprint-close-next-session-opens-the-sprint` still names "the refusals of `uv run guppi ledger` in its transcript" in its `When`; its `method` no longer does, by case 769.5.

## Ask the person
