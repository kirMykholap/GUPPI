# Handoff — 2026-10-12, sprint plugin: the repository on GitHub, Case ids with a sprint, the merge of main

## Notes from memory

- The person took the GitHub item only after a long discussion and split it into four Cases (787 setup, 788 Case ids, 789 pull requests into main, 790 the vault at a merge). The flow of a pull request was rebuilt several times: first the owner settled conflicts at review, then the author by `/merge-main` before the pull request, then `/merge-main` moved before the close, and a merge with no conflict got a short Case after all. The person said twice that they no longer followed Case 790; the explanation with branches X and Y settled it. The final roles in the person's own words: the author settles the conflicts of their branch; whether a pull request is taken is the owner's decision, by a separate Case.
- The person asked whether another user of GUPPI gets these GitHub rules; the answer stood that rulesets are settings of this repository, not files, and that whether `prod` leaves out `.github/` and `rule-github-repository` belongs to the item The clean branch.
- In Work Mode the person chose to cut the history at the commit that removed the former product (Case 794, superseding 787.1): the product history and the scraped HTML fixtures holding a third-party Google API key are not on GitHub, and the old commits were removed from the local repository too, the backup branch and the tag `vault-v1` included. Commit ids quoted in pages before the cut now open nowhere; the person accepted that.
- The person chose `style` and `test` as the only required checks on `main`; `lint` runs and shows its result without blocking.
- Case 792 (an `update` that drops a section) was put off by Case 793, so `rule-git-context` keeps `## How it works` with one sentence changed.

## Direct instructions to the librarian

- Case 794 supersedes 787.1 by `{supersedes:case 787.1}` on its create of `rule-github-repository`; 787.1 and 794 both name `rule-github-repository`, `estimate-sprint-plugin-pull-requests-reviewed-on-github` and `entity-sprint-plugin`. Apply 794's text; check that the page of `rule-github-repository` is created once, from 794, and that the sprint page moves the milestone The sprint turn and GitHub to `## Closed` once.
- `rule-skill-sprint-open` is updated by 788.1, 788.3 and 789.1 on different anchors; `rule-page-generation` and `entity-glossary` by 786.1 and 790; `rule-orchestration` by 786.2 and 788.2. Check that each `replace` pair finds its `old` text once after the earlier pairs of the same page applied.
- Case 793 is a short-form defer of `rule-page-generation`, which also takes updates from 786.1 and 790 in this session.
- `guppi/caseid.py` is new and registered as `guppi caseid`; `rule-ratification` names it in `implementation_ref` (788.2).

## What actually got done

- Ratified: Cases 785, 786 (786.1, 786.2), 787.2, 788 (788.1–788.7), 789 (789.1–789.3), 790, 791, 793 (a defer), 794. Case 787.1 is superseded by 794. C4 needed no decision: `lesson-case-build-sub-cases-contradicted-each-other` is right, Case 781 had eight sub-cases when the lesson's events happened and nine after its rebuild.
- Code: `guppi/materialize.py` (`PLACEHOLDER_CATEGORIES`, `defer_writes_no_page`), `guppi/generate.py`, `guppi/prespec.py`, `guppi/lint.py` (786); new `guppi/caseid.py` with `guppi caseid --next`, and `guppi/casecheck.py`, `guppi/ratified.py`, `guppi/lint.py`, `guppi/gate.py`, `guppi/box.py`, `guppi/ledger.py` (`refused_taken_sprint`), `guppi/cli.py` (788); `.gitattributes` with `merge=union` for `vault/wiki/log.md` and `vault/wiki/tags.md` (790); `.github/workflows/checks.yml` and the history sentence of `README.md` (787, 794).
- Tests: `tests/test_generate.py`, `tests/test_prespec.py`, `tests/test_ledger.py`, `tests/test_casecheck.py`, `tests/test_ratified.py`, `tests/test_box.py`, new `tests/test_caseid.py`.
- GitHub: public repository `kirMykholap/GUPPI`; history cut at the commit that removed the product (new root without parent, files of every commit unchanged, the key and the token absent); `main` and `plugin` pushed; ruleset `main` (no deletion, no force push, changes by pull request, `style` and `test` required, admin bypass); ruleset `prod` (no creation, update, deletion or force push, admin bypass); approval of runs for first-time contributors. The first CI run on `plugin`: `style` and `test` passed, `lint` failed on the same 8 lines as the local Baseline.
- `make test`: 1563 passed, 6 skipped. `make style`: clean.
- Readings: ledger lines 44–56, all `passed`. Lessons: lines 57–59.

## Debt

- No box of code, test, command or migration is left unticked.
- 72 boxes wait for the librarian (page, render, sprint, glossary and read lines).
- `estimate-sprint-plugin-pull-requests-reviewed-on-github`: target the live sprint page; waits for a pull request from a second account against `main`, in a session of the sprint before its close.
- `estimate-git-context-current`: waits for the first `/hi` after the first push to GitHub, which is the next session.
- `estimate-skill-pr-review-takes-a-pull-request-whole`: waits for the first pull request from another account merged into `main` by `/pr-review` after the close of `plugin`.
- `estimate-skill-merge-main-joins-a-conflicted-page`: waits for the first `/merge-main` whose merge of `main` leaves a conflicted page.

## Observations

- `make lint` was red before the work with 8 lines (7 `unread: pending`, `rules/rule-morph: deferred: 4 times since case 239`), the same 8 after it; nothing in `## Expected red`.
- The workflow installs `make` by `choco` on `windows-latest`; it worked on the first run.
- `make lint` is red on GitHub for the same reason as locally; it will stay red while any Estimate is unread, which is why it is not a required check.
- During Plan Mode, Case 785's sentence was not yet in the Render of `case-guppi`; the `ask-guppi` run found two judgments that two sides would answer differently (the next free id, the taken sprint id), both fixed in Case 788 before ratification.
- Case 789.1's own merge of the owner's pull request waits for `gh pr checks --watch`; GitHub may show the required checks only after the first run of the workflow on that branch.

## For the next session

- The cause of `lesson-case-build-made-an-always-red-check-required`: `case-guppi` recommended a required check without reading what `make lint` prints at the Baseline or `rule-lint`.
- The cause of `lesson-case-build-chose-a-key-its-own-session-adds`: a Case may not use a form of an update that only its own session's Work Mode makes valid; it clusters with `insight-workflow-code-live-before-the-page-it-reads`.
- The cause of `lesson-work-mode-edited-a-source-file-through-the-shell`.
- The milestone The clean branch is now the current one: CI that writes `prod`, and whether `prod` leaves out `.github/` and `rule-github-repository`; the CI writer goes into the bypass list of the ruleset on `prod`.
- The test pull request from a second account against `main`, to read `estimate-sprint-plugin-pull-requests-reviewed-on-github`.

## Ask the person
