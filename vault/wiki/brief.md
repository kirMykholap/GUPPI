# Brief — 2026-11-23, librarian of session 1353 (2026-11-20)

## Where things stand

- Session 1353 of the sprint `plugin`, 2026-11-20 to 2026-11-23, paused from 2026-11-20 to 2026-11-23 with no new `/hi`. Cases ratified: 1039 (1039.1, 1039.2), 1040, 1041, 1042 (1042.1, 1042.2), 1043 (1043.1, 1043.2); 1039, 1041, 1042 and 1043 ratified a second time after `/pre-spec` (handoff).
- Code: `.guppi/guppi/casecheck.py` (`session_case_files`; `names_notes` takes the session folder), `.github/workflows/prod.yml` (a step that runs `-k own_style` and `-m live -k own_tests` of `test_ship.py` before the commit to `prod`), `README.md` written anew, `LICENSE` new. Tests: `.guppi/tests/test_casecheck.py`, two new tests and eight set to the new output. `guppi test` exit 0, 1978 passed, 6 skipped, 2 deselected; `guppi style` clean (handoff).
- Readings L18 to L22, all passed. Lesson L23 (handoff, ledger).
- `guppi materialize` printed `written with 23 entries` for `vault/raw/2026-11-20/1353/materialize.yaml` and `extended with 0 entries` for `vault/raw/2026-11-04/0807/materialize.yaml`. The ledger has 23 lines (`wc -l`). The yaml holds 22 entries under `entries`, for lines 1 to 21 and 23; line 22, the reading of `estimate-guppi-repository-carries-the-mit-license`, is folded into its `create` entry (line 15), and `log.md` shows it applied with `#L22` as origin. Every line is accounted for; `unparsed: []`.
- Entries by kind: 4 `create` (all Estimates), 13 `update`, 4 `estimate`, 1 `lesson`; 11 entries under `decisions`. All 33 carry `applied` after `generate`. No entry carries `failed`, `incomplete` or `exists`; the synthesis added no entry.
- Index check: the four `create` entries are Estimates, so no Grep of a category ran for them. For the `lesson` entry, `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 70 lines; `lesson-case-build-context-claims-a-run-it-did-not-make` got `near: lesson-case-build-states-what-a-past-decision-did-from-its-effect-on-one-page`.
- `guppi generate` printed 34 pages written or changed for 1353 and 0 for 0807, nothing on stderr. It ticked 25 boxes of `vault/raw/2026-11-20/1353/spec.md` and 2 `read` boxes of `vault/raw/2026-11-04/0807/spec.md` (lines 747, 1079) (`git diff`). 5 `read` boxes of the 1353 Spec stand unticked. No unticked Spec line holds `guppi sprint-close --apply`.
- `guppi cleanup` printed `2 page(s) moved`: `lesson-case-build-a-later-case-leaves-a-ratified-text-stale` and `lesson-orchestration-batch-asks-one-fork-twice-with-opposite-answers`, archived by the cascade of `insight-case-build-sibling-texts-unchecked-before-the-showing` set `actioned` by 1039.1, into `vault/archive/plugin/2026-11-23/1353/lessons/`.
- `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr. The render changed `.claude/agents/case-guppi.md`, `plugin/skills/install/SKILL.md` and `vault/wiki/orchestration.md` (`git status`). `.claude/agents/case-guppi.md` holds both changes of its Render: `as set in case 1039.2` (1 line) and `and why you chose it (as set in case 1041)` (1 line) (`grep -c`), as the handoff asked.
- Pages created (16, `git status`): decisions 11 (`decision-case-1039`, `-1039.1`, `-1039.2`, `-1040`, `-1041`, `-1042`, `-1042.1`, `-1042.2`, `-1043`, `-1043.1`, `-1043.2`); estimates 4 (`estimate-case-build-names-a-stale-line-of-another-case`, `estimate-plugin-install-asks-one-approval-in-plan-mode`, `estimate-clean-branch-prod-commits-only-a-tested-copy` pending; `estimate-guppi-repository-carries-the-mit-license` passed); lessons 1 (`lesson-case-build-context-claims-a-run-it-did-not-make`, `new`).
- Pages updated (18, `git status`): rules 7 (`rule-case-build`, `rule-case-check`, `rule-clean-branch`, `rule-guppi-package`, `rule-orchestration`, `rule-plugin-install`, `rule-work-mode`), estimates 6, entities 2 (`entity-guppi-repository`, `entity-sprint-plugin`), insights 1 (`insight-case-build-sibling-texts-unchecked-before-the-showing`, `open` → `actioned`, `addressed_by` `decision-case-1039.1`, severity 2 → 0), lessons 2 (the two archived above). By the cascade: `rule-clean-branch` `built` → `draft`; `rule-guppi-package` and `rule-work-mode` `draft` → `built` (`log.md`).
- `guppi sprint`: the milestone The clean branch went `[x]` → `[ ]`, its line `rule-clean-branch` open; The plugin shows as one line of 4 items. `guppi backlog`: 13 items (14 before). In: the Backlog line of `entity-sprint-plugin` on the MIT license text of the clean copy (case 1043.2), as the handoff asked. Out: `insight-case-build-sibling-texts-unchecked-before-the-showing`, `rule-work-mode`.
- `guppi archive` printed one line on stdout, exit 0, nothing on stderr: `raw/2026-11-04/0807 → archive/plugin/2026-11-04/0807/raw`. It kept `raw/2026-11-20/1353`, the session of the run; `vault/raw/2026-10-14/1907/` holds no `ledger.md`, so it is no unit.

Synthesis. Greps: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 70 lines, 3 of them too long to show (`lesson-case-build-subagent-compaction-fires-below-its-window`, `lesson-hooks-subagentstop-fires-before-and-after-the-handback`, `lesson-hooks-subagentstop-reads-the-last-text-not-the-handback`); `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 18 lines. No entry added.
- `lesson-case-build-context-claims-a-run-it-did-not-make` — none: its cause is a count or a run stated in `context` from names and lists, without the run, the mark or the status. `lesson-case-build-states-what-a-past-decision-did-from-its-effect-on-one-page` names the reach of a Decision stated without reading the History of its rule (near, not the same); `lesson-librarian-writes-a-total-no-count-printed` names a total of the librarian's brief; `insight-case-build-claims-what-code-does-without-reading-it` names a claim about a function not read in the code. It stays `new`.

## Readings due

31 Estimates: 3 `failed`, 28 `pending`. The session's `spec.md` holds 5 unticked `read` lines (145, 224, 275, 341, 457).

- `estimate-ask-searches-at-prespec` — `failed` — `rule-ask` (draft), `deferred_by` Case 1037 — 2026-11-04, `/hi` of session 0358: the `ask-guppi` transcript of the pre-spec of session 1825 read against the Criterion, not met; method: by hand, after the first `/pre-spec` whose `ask-guppi` runs on the Render of `rule-ask` that lets the searches cover the code, its transcript.
- `estimate-case-build-searches-the-names-of-what-it-changes` — `failed` — `rule-case-build` (draft), `deferred_by` Case 1038 — 2026-11-04, `/hi` of session 0358: the build of Case 1015 of session 0316 did not meet the Criterion after the note of 47 files; method: by hand, after the `/pre-spec` of the first session in which the hook of `rule-case-check` sends the note, the transcripts and the case files.
- `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` — `failed` — `entity-sprint-plugin` (draft) — 2026-11-03, Work Mode of session 1825: the transcript of the build of Case 1012 and its case file, not met; method: by hand, in the Work Mode of the session that creates this Estimate.
- `estimate-case-build-names-a-stale-line-of-another-case` — `rule-case-build` (draft) — `read` line 145 — method: by hand, after the first build on the new Render of `rule-case-build` in which the note of `rule-case-check` lists the Case file of another Case of the session, its transcript, case file and summary.
- `estimate-plugin-install-asks-one-approval-in-plan-mode` — `rule-plugin-install` (draft) — `read` line 224 — method: by hand, after the librarian's run of the session that sets this Criterion, three installs from an `--allow-draft` copy in Plan Mode, one with no `uv` on PATH, one with the plan not approved. This run is that librarian's run: the render wrote `plugin/skills/install/SKILL.md`; it made no install.
- `estimate-case-build-offers-a-page-for-code-no-page-covers` — `rule-case-build` (draft) — `read` line 275 — method: by hand, at the Retro of the session whose Render asks `context` for why the page was chosen, that Render in the Spec; by hand, after a session whose `case-guppi.md` holds this text in which `case-guppi` settles a page for code that no page covers, its transcript and case file.
- `estimate-clean-branch-prod-commits-only-a-tested-copy` — `rule-clean-branch` (draft) — `read` line 341 — method: by hand, `.github/workflows/prod.yml` read against the Criterion; by hand, after a run of `prod.yml` on GitHub whose step `guppi ship` exits 0, the output of `gh run view --log`.
- `estimate-sprint-plugin-readme-describes-the-project` — `entity-sprint-plugin` (draft) — `read` line 457 — method: by hand, the person's answer on `README.md` at the `/hi` of the session after the one whose Work Mode writes it, before the close of the sprint.
- `estimate-orchestration-dispatches-case-guppi-at-a-level` — `rule-orchestration` (draft) — method: by hand, at the Retro of the session that creates this Estimate, the new Render in the Spec; by hand, after a session whose `orchestration.md` holds this text, each Agent call of `case-guppi` in its transcript. Its `read` box stands unticked at line 92 of the 0807 Spec, which `guppi archive` moved to `vault/archive/plugin/2026-11-04/0807/raw/spec.md`.
- `estimate-case-build-writes-the-case` — `rule-case-build` (draft) — method: by hand, the text of `.claude/agents/case-guppi.md` as rendered, or the new Render at the Retro; by hand, after a session whose `orchestration.md` sets the effort of each dispatch of `case-guppi`, the effort of each call in its transcript. `read` box at line 164 of the 0807 Spec.
- `estimate-case-build-settles-form-by-itself` — `rule-case-build` (draft) — method: by hand, at the Retro of the session that creates this Estimate, the new Render in the Spec; by hand, after a session whose `case-guppi.md` holds this text, each round in its transcript. `read` box at line 472 of the 0807 Spec.
- `estimate-sprint-plugin-case-guppi-level-trial-decided` — `entity-sprint-plugin` (draft) — method: by hand, in the session that closes the sprint `plugin`, the output of `guppi agents` and the findings of `ask-guppi`, the person's answer. `read` box at line 263 of the 0807 Spec.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `rule-morph` (draft) — method: by hand, after the librarian's run of the session that ratifies this Criterion, installs from an `--allow-draft` copy into an empty git project and one with code of its own, `/hi` typed. `read` box at line 598 of the 0807 Spec. This run made no install.
- `estimate-git-context-offers-git-init` — `rule-git-context` (draft) — method: by hand, after the librarian's run of the session that ratifies this Criterion, an install from an `--allow-draft` copy into an empty folder that is no git repository, `/hi`, `! git init -b main`, `/hi` again. `read` box at line 1411 of the 0807 Spec. This run made no install.
- `estimate-ask-query-before-a-create` — `rule-ask` (draft) — method: by hand, after the first build of `case-guppi` whose Case proposes a create without a ref, on the Render of `rule-ask` that runs every category.
- `estimate-case-build-goes-on-after-a-live-compaction` — `rule-case-build` (draft) — method: by hand, after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `rule-case-build` (draft) — method: by hand, after the first Case built under the Render that names a test over a live file.
- `estimate-case-build-reads-each-list-of-a-new-member` — `rule-case-build` (draft) — method: by hand, after the first build in a later session whose Case adds a member to a list spelled out one by one.
- `estimate-case-build-runs-the-vault-query-first` — `rule-case-build` (draft) — method: by hand, after the first build whose Case proposes a create without a ref.
- `estimate-hi-writes-frontier` — `rule-skill-hi` (draft) — method: by hand, after the reply that acknowledges the opening Case of `/sprint-open` in the session after the close of a sprint, the person's answer.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` — `rule-orchestration` (draft) — method: by hand, after an acknowledging reply after `/pre-spec` that waits for the person's word, its transcript.
- `estimate-orchestration-signs-items-taken-together` — `rule-orchestration` (draft) — method: by hand, after the first batch taken up together in Plan Mode in which a summary carries a line Other Case naming a Case of the session.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — `rule-plugin-install` (draft), `deferred_by` Case 949 — method: by hand, after the librarian's run of the session that set this Criterion, with a tag `prod-x.y.z` in the history of HEAD, three installs from an `--allow-draft` copy. This run made no install.
- `estimate-retro-loads-on-a-red-command` — `rule-retro` (draft), `deferred_by` Case 1007 — method: by hand, after the librarian's render that writes `.claude/skills/retro/SKILL.md` with `--exit-zero`, and the first load of `/retro` after it. This run: the render left `.claude/skills/retro/SKILL.md` unchanged.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `rule-skill-merge-main` (draft) — method: by hand, after the first `/merge-main` that leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `rule-skill-pr-review` (draft) — method: by hand, after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `entity-sprint-plugin` (draft) — method: by hand, at the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link` — `entity-sprint-plugin` (draft) — method: by hand, after the librarian's run that applies the update of `lesson-ledger-reading-writes-a-bare-wikilink`. This run applied no update of that lesson.
- `estimate-sprint-plugin-link-graph-is-gone` — `entity-sprint-plugin` (draft) — method: by hand, after the librarian's run that applies the delete of `entity-link-graph`. This run applied no delete.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `entity-sprint-plugin` (draft) — method: by hand, a pull request from a second account read on GitHub, before the close of the sprint.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` (draft), `deferred_by` Case 1009 — method: by hand, after a librarian's run that puts a lesson with `addressed_by` under an Insight that stands `actioned`. This run: the yaml held 1 `lesson` entry, with no `addressed_by`; the synthesis put it under no Insight.

## Flags

- `near`: `lesson-case-build-context-claims-a-run-it-did-not-make` carries `near: lesson-case-build-states-what-a-past-decision-did-from-its-effect-on-one-page`. No entry `incomplete`, `failed` or `unparsed`.
- Failed Estimates: 3, listed first under Readings due. `estimate-ask-searches-at-prespec` and `estimate-case-build-searches-the-names-of-what-it-changes` carry `deferred_by` Cases 1037 and 1038 and stand in `backlog.md`. `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` targets the live sprint page.
- Lint (`guppi check`, exit 1, 6 lines): `rules/rule-ask`, `rules/rule-case-build`, `rules/rule-morph`: `status: a page with core: true that is draft`; `estimates/estimate-ask-searches-at-prespec`, `estimates/estimate-case-build-searches-the-names-of-what-it-changes`, `estimates/estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`: `unread: failed`.
- `rule-clean-branch` went `built` → `draft` by the cascade, since 1042.1 created `estimate-clean-branch-prod-commits-only-a-tested-copy` `pending`; `sprint.md` shows the milestone The clean branch open again.
- `estimate-case-build-offers-a-page-for-code-no-page-covers`: the handoff's Debt says the first part of its method, the Render in the Spec, meets the Criterion; no line of the ledger records that reading, and the Estimate stands `pending`.
- `estimate-clean-branch-prod-commits-only-a-tested-copy`: the handoff's Debt says the first part of its method, the text of `prod.yml`, meets the Criterion; no line of the ledger records that reading.
- Contradiction (handoff): the `given` of Case 1042.1 says "the two tests" of `test_ship.py`, while its `context`, the text for `rule-clean-branch` and the Criterion name the selections `-k own_style` and `-m live -k own_tests`; the handoff says nothing of the vault rests on that `given` line.
- Handoff observation: whether the test suite passes on Linux is not read; the first run of `prod.yml` after this change shows it.
- Handoff observation: the copy on `prod` carries no license text, which the MIT license asks of each copy; it stands in the Backlog of the sprint.
- Handoff observation: `estimate-guppi-repository-carries-the-mit-license` was read against the SPDX text and the page at opensource.org, which shows typographic quotes where `LICENSE` holds ASCII ones.
- Handoff note: Case 1043 holds `README.md` and `LICENSE` on the branch `plugin` only; they reach `main` by a later merge.
- No MOC candidate, no stale defer and no other contradiction printed by `guppi check`, `guppi backlog` or this run.

## Next session

Cases
- C1, C2 and C4 of the milestone The plugin stay open, put off with no Case (handoff).
- The license text in the clean copy: `guppi ship` writing `LICENSE` and `/guppi:install` leaving it out, from the Backlog of the sprint (handoff).
- `estimate-ask-searches-at-prespec` failed; `deferred_by` Case 1037, in `backlog.md`.
- `estimate-case-build-searches-the-names-of-what-it-changes` failed; `deferred_by` Case 1038, in `backlog.md`.
- `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` failed; its target is the live sprint page.
- The `given` of Case 1042.1 says "the two tests" of `test_ship.py` where its `context`, `rule-clean-branch` and the Criterion name the two selections (handoff).

Work
- `estimate-plugin-install-asks-one-approval-in-plan-mode` (`read` line 224 of `vault/raw/2026-11-20/1353/spec.md`): its librarian's run is this run.
- `estimate-orchestration-dispatches-case-guppi-at-a-level` (`read` line 92 of the 0807 Spec, now `vault/archive/plugin/2026-11-04/0807/raw/spec.md`): session 1353 ran on the `orchestration.md` that holds its text.
- `estimate-case-build-writes-the-case` (`read` line 164 of the 0807 Spec): session 1353 ran on the `orchestration.md` that sets the effort of each dispatch.
- `estimate-case-build-settles-form-by-itself` (`read` line 472 of the 0807 Spec): session 1353 ran on the `case-guppi.md` that holds its text.
- `estimate-morph-sets-up-the-project-at-the-first-hi` (`read` line 598 of the 0807 Spec).
- `estimate-git-context-offers-git-init` (`read` line 1411 of the 0807 Spec).
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec`: the handoff names Cases ratified again after the `/pre-spec` of session 1353.

Ask the person
- `estimate-sprint-plugin-readme-describes-the-project` — needs the person — at the `/hi` of the next session: does `README.md` at the root of the branch `plugin` describe GUPPI as it stands, with its Why, Is it for you, how a session goes, its parts, its install and its use?

## Readings at the close

- `uv run --project .guppi guppi test`: exit 0, 1978 passed, 6 skipped, 2 deselected.
- `uv run --project .guppi guppi check`: exit 1, 6 lines, as under Flags.
- Live pages (`ls`): decisions 608, rules 91, entities 6, estimates 372, lessons 71, insights 19; 11 files at the root of `vault/wiki/`. Files under `vault/archive/` (`find -name "*.md"`): 3372 after `guppi archive`.
