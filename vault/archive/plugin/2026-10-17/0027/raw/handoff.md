# Handoff — 2026-10-17, sprint plugin: the clean version's texts, old defers, the top-MOC form

## Notes from memory

- The person took every recommended answer of each round (Cases 875, 876, 877) with "Согласен", and asked once for a plain explanation of C2 before taking it.
- Case 875 is one Case with one Estimate over 51 decision lines; `/pre-spec` noted its size (57 `given` lines) and the person ratified it whole. The sentences inside the `## Criterion` of shipped Estimates are left to the defer on `rule-clean-branch`.
- The person put off C1, the milestone item `rule-clean-branch` / `estimate-sprint-plugin-ci-writes-a-clean-branch`, once more; it stays the current milestone.
- One `/pre-spec` finding on the context of Case 877 was fixed after the confirmation run of `ask-guppi`, so that fix has no confirmation.

## Direct instructions to the librarian

- Case 876 stands under `## Deferred` of the Spec in the short form the main agent showed; its case file `cases/case-876.md` holds the full form. Its two `defer` lines carry `{supersedes:case 836}` and `{supersedes:case 863}`: `decision-case-836` and `decision-case-863` should go `superseded`, then `archived` by the cascade; the lesson pages and `decision-case-855` do not change.
- Case 875 updates `rule-guppi-package`, which already carries `deferred_by` decision-case-834 and decision-case-848; those defers stay.
- Case 875 updates `estimate-clean-branch-ships-neutral-texts` with `{supersedes:case 874}` and defers `rule-clean-branch` in the same Case: the Estimate leaves `backlog.md`, `rule-clean-branch` enters it.
- Case 877.1 carries `{supersedes:case 873}`: `rule-estimates-schema` leaves `backlog.md`.
- The ledger lines of Case 876 (L48, L49) were written at a `Stop` that the `ratified` hook refused, then shown again; check that the Spec holds Case 876 once.

## What actually got done

- Cases ratified: 875, 876, 877 (877.1, 877.2).
- Code: `.guppi/guppi/pages.py` (`has_no_parent`), `.guppi/guppi/glossary.py` (`group_of` imports it), `.guppi/guppi/lint.py` (`GUPPI_TEST`, `names_a_moc_form(method, top)`, `check_method`), `.guppi/guppi/prespec.py` (`plan_parent`, `form_finding`). Tests: `.guppi/tests/test_lint.py`, `.guppi/tests/test_prespec.py`.
- `uv run --project .guppi guppi test`: 1750 passed, 6 skipped, 1 deselected. `uv run --project .guppi guppi style`: clean.
- Readings: `estimate-lint-checks-the-method` passed, `estimate-prespec-catches-a-method-without-a-form` passed (Retro). Lesson: `lesson-ratified-defer-only-case-wants-its-fence-in-the-reply`.

## Debt

- None.
- 60 boxes wait for the librarian (page, render and `read` lines).
- `estimate-clean-branch-ships-neutral-texts` (pending) — after the librarian's run of this session, with a tag `prod-x.y.z` in the history of HEAD.
- `estimate-close-commits` — after the librarian's run of this session; the clause on the report needs a transcript, so the `/hi` reading cannot take it from files and commands alone.
- `estimate-clean-branch-writes-the-session-files` — an install by hand in an empty folder with no git, with a tag `prod-x.y.z`.

## Observations

- Red before the work, in `## Baseline` of `work.md`: `guppi check` exit 1 — ten draft pages with `core: true`, `estimate-clean-branch-ships-neutral-texts` `unread: failed`, `estimate-harness-make-runs-in-both-shells` `method: the Makefile has no target with`.
- A Case built by `case-guppi` whose decision lines are all `defer` clashes between two hooks: the `ratified` Stop hook reads it as a short-form Case and wants its `then` fence in the reply, while the case-file check refuses that fence in the file. Worked around by showing the Case again in the short form.
- The bash guard refused a heredoc whose body held a backslash; the tests changed by Edit instead.

## For the next session

- The clash of the `ratified` hook and the case-file check on a full Case whose lines are all `defer`: which of the two changes.
- The sentences inside the `## Criterion` of shipped Estimates true only in the repository of GUPPI, put off by Case 875 on `rule-clean-branch`, listed by the next reading of `estimate-clean-branch-ships-neutral-texts`.
- The milestone item `rule-clean-branch`, `estimate-sprint-plugin-ci-writes-a-clean-branch`, put off again; ten draft pages with `core: true` still stop every build of `prod`.

## Ask the person

- `estimate-guppi-package-is-ready-after-the-install` — needs the person — In an empty project on a machine with `uv`, after the librarian's render, does `/guppi:install` run `uv --version`, ask nothing about `uv`, build `.guppi/.venv/` by `uv sync` after the copy before it sends you to `/hi`, and do the hooks find that environment at the first `/hi`?
