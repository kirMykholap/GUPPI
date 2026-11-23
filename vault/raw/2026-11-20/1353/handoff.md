# Handoff — 2026-11-20, the README, the license and the gate of prod

## Notes from memory

- The session stood paused from 2026-11-20 to 2026-11-23; it went on in the same session, with no new `/hi`.
- Before the Case on the README, the person asked what to write and whether GUPPI is a "harness". The person chose one README, an honest status, the MIT license, and a first-person Why on control against cost: the project was made to steer other projects while controlling the agents, and the person finds it slow and expensive but feels that the understanding of the project and of what the agents do got better. The person did not ask for a figure of cost.
- The person put off C1, C2 and C4 of the milestone The plugin with no Case.
- At `/pre-spec`, eleven findings of `ask-guppi` sent Cases 1039, 1041, 1042 and 1043 back; all were confirmed closed. The person chose that the license text of the clean copy goes into the `## Backlog` of `entity-sprint-plugin` (Case 1043.2), not into a defer.
- Case 1043 holds `README.md` and `LICENSE` on the branch of the session only; they reach `main` by a later merge.

## Direct instructions to the librarian

- Cases 1039, 1041, 1042 and 1043 were ratified twice, the second time after `/pre-spec`; their files under `cases/` hold the texts built again, and the plan file and `spec.md` hold those texts. Take the Spec as it stands.
- `rule-case-build` is updated by both Case 1039.2 and Case 1041, in two different places of its Render; apply both, and check that the render of `.claude/agents/case-guppi.md` holds both.
- Case 1039.1 sets `insight-case-build-sibling-texts-unchecked-before-the-showing` `actioned`; two of its four children are live and `clustered`, the other two already archived.
- Case 1043.2 adds a line to the `## Backlog` of `entity-sprint-plugin` and has a `guppi sprint` line; `backlog.md` should gain that line.
- The `given` of Case 1042.1 still says "the two tests" of `test_ship.py`, while its `context`, the text for `rule-clean-branch` and the Criterion name the selections; nothing of the vault rests on that `given` line.

## What actually got done

- Cases ratified: 1039 (1039.1, 1039.2), 1040, 1041, 1042 (1042.1, 1042.2), 1043 (1043.1, 1043.2).
- Code: `.guppi/guppi/casecheck.py` (`session_case_files`, and `names_notes` takes the session folder), `.github/workflows/prod.yml` (a step that runs `-k own_style` and `-m live -k own_tests` of `test_ship.py` before the commit to `prod`), `README.md` written anew, `LICENSE` new.
- Tests: `.guppi/tests/test_casecheck.py`, two new tests of the note over the session's Case files and eight tests set to the new output.
- `uv run --project .guppi guppi test`: exit 0, 1978 passed, 6 skipped, 2 deselected. `uv run --project .guppi guppi style`: clean.
- Readings L18 to L22, all passed. Lesson L23.

## Debt

- No box of code, a test or a command is left unticked.
- 30 boxes wait for the librarian: the page, render and sprint lines and the `read` lines.
- `estimate-case-build-names-a-stale-line-of-another-case` — after the first build on the new Render of `rule-case-build` in which the note lists the Case file of another Case of the session.
- `estimate-plugin-install-asks-one-approval-in-plan-mode` — after the librarian's run of this session, three installs from an `--allow-draft` copy, one in a session that opens in Plan Mode.
- `estimate-case-build-offers-a-page-for-code-no-page-covers` — after a session whose `case-guppi.md` holds the new text and in which `case-guppi` settles a page for code that no page covers. Its first part, the Render in the Spec, reads "`context` names the page and why you chose it", which meets the Criterion.
- `estimate-clean-branch-prod-commits-only-a-tested-copy` — after a run of `prod.yml` on GitHub whose `guppi ship` exits 0. Its first part, the text of `prod.yml`, runs both selections on `ubuntu-latest` before the step that commits, and the step fails the job on a red test.
- `estimate-git-context-offers-git-init` and `estimate-morph-sets-up-the-project-at-the-first-hi` — installs by the person into new folders from an `--allow-draft` copy, after this librarian's run, as their `method` sets it; this session made no install.

## Observations

- The 7 lines of `guppi check` (three `draft` core pages, four `unread: failed`) were red before the work, as `## Baseline` of `work.md` holds.
- Whether the test suite passes on Linux is still not read: the first run of `prod.yml` after this change shows it.
- The copy on `prod` carries no license text, which the MIT license asks of each copy; it stands in the Backlog of the sprint.
- `estimate-guppi-repository-carries-the-mit-license` was read against the SPDX text and the page at opensource.org, which shows typographic quotes where `LICENSE` holds ASCII ones.

## For the next session

- C1, C2 and C4 of the milestone The plugin stay open, put off with no Case.
- The license text in the clean copy: `guppi ship` writing `LICENSE` and `/guppi:install` leaving it out, from the Backlog of the sprint.

## Ask the person

- `estimate-sprint-plugin-readme-describes-the-project` — needs the person — at the `/hi` of the next session: does `README.md` at the root of the branch `plugin` describe GUPPI as it stands, with its Why, Is it for you, how a session goes, its parts, its install and its use?
