# Brief — 2026-10-29, librarian of session 2341

## Where things stand

- Session 2341 of the sprint `plugin`. Cases ratified: 913; 914; 915 (915.1–915.3); 916 (916.1, 916.2); 917 (917.1, 917.2); 918 (918.1–918.4). Cases 913, 915, 916, 917 and 918 were built again on twelve findings of `/pre-spec` and ratified again with the same lines. C1 (`rule-clean-branch`, the CI run on a tag `prod-x.y.z`) was put off with no Case (handoff).
- Code: `.guppi/guppi/render.py` (`--paths` sets `newline="\n"` on its stdout), `.guppi/guppi/ledger.py` (the reminder of a lesson with no mark removed; `unmarked_lessons` leaves out a `knowledge` lesson unless a marked line of its slug stands), `.guppi/guppi/materialize.py` (`unlinked_lessons` removed), docstrings of `.guppi/guppi/onward.py` and `.guppi/guppi/sprint_close.py`. Tests: `.guppi/tests/test_render.py` gains a child-process test of `--paths`; `.guppi/tests/test_ledger.py` replaces the reminder tests. `guppi test` 1786 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- Readings: L1, L2, L5 at `/hi`; L3 and L8 `failed`; L30–L39 at Retro, all `passed`. Lessons: L4, L40, L41 (handoff).
- `guppi materialize` printed `written with 41 entries` for `vault/raw/2026-10-29/2341/materialize.yaml` and `extended with 0 entries` for the yamls of `0327` and `1930`. The yaml holds 38 entries (lines 1–30, 32, 35–41) and the readings of lines 31, 33 and 34 folded into the `create` entries of lines 15, 19 and 23; `unparsed: []`. The ledger has 41 lines (`wc -l`), so every line is accounted for. Kinds: 20 `update`, 3 `create` (estimates), 12 `estimate`, 3 `lesson`; 13 decision units in the `decisions` block.
- Marks: every entry `applied`; no entry `failed`, `incomplete`, `exists` or `merged`; 1 entry `near` (L4).
- `guppi generate` printed 44 pages written or changed for `2341` and 0 for `0327` and `1930`. `guppi cleanup` printed 0 pages moved. `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr. No unticked Spec line holds `guppi sprint-close --apply`.
- Pages created (23), from `git status`: decisions 17 (`decision-case-913`, `914`, `915`, `915.1`–`915.3`, `916`, `916.1`, `916.2`, `917`, `917.1`, `917.2`, `918`, `918.1`–`918.4`); estimates 3 (`estimate-case-build-marks-the-lesson-its-case-fixes`, `estimate-orchestration-passes-a-change-to-an-item-not-built`, `estimate-case-build-names-an-item-not-built-on-the-other-case-line`, all `passed`); lessons 3 (`lesson-librarian-writes-a-total-no-count-printed`, `lesson-hi-reads-the-end-state-of-a-command-that-failed-first`, `lesson-hi-asks-a-reading-of-a-text-it-names-no-place-of`).
- Pages updated (20), from `git status`: estimates 13 (12 modified, and `estimate-close-reports-in-twenty-lines` renamed to `estimate-close-reports-the-run`); rules 6 (`rule-case-build`, `rule-close`, `rule-ledger-write`, `rule-orchestration`, `rule-permissions`, `rule-prespec-onward`); decisions 1 (`decision-case-903.2`). 23 created plus 20 updated plus the removed old path of the rename make the 44 paths `generate` printed.
- Cascade: `rule-permissions` `draft → built` (log).
- The handoff's instructions, checked in `git diff -- vault/wiki/log.md`: `estimate-close-reports-the-run` took L3 `failed`, L5 `passed`, then the `update` of Case 913, the rename and `pending`; the `estimates` ref of `rule-close` followed the rename. `estimate-close-commits` took L1 `passed`, L8 `failed`, then the `update` of Case 914, and stands `pending`. `rule-orchestration`, `rule-case-build` and `rule-ledger-write` each took both of their updates.
- This run ticked 38 boxes of `vault/raw/2026-10-29/2341/spec.md` (33 by `generate`, 5 render boxes by `render`) and 3 `read` boxes of `vault/raw/2026-10-29/1930/spec.md` (`estimate-close-commits`, `estimate-close-reports-in-twenty-lines`, `estimate-permissions`). Three `read` boxes of the 2341 Spec stay unticked.
- Index check: the 3 `create` entries are Estimates and have no index; the 3 `lesson` entries were checked by `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 56 lines. L4 is close to `lesson-orchestration-claimed-a-reading-before-taking-it` (a fact stated without the output that holds it) and carries `near:`; L40 and L41 match no line.
- Synthesis: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 56 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 12 lines.
  - `lesson-librarian-writes-a-total-no-count-printed` — none: `insight-orchestration-writes-from-its-own-reading` names the main agent copying a line of a source of record, this cause is the librarian's total in the brief; the near lesson is the main agent's.
  - `lesson-hi-reads-the-end-state-of-a-command-that-failed-first` — none: no index line names a method that reads only the end state of a command.
  - `lesson-hi-asks-a-reading-of-a-text-it-names-no-place-of` — none: no index line names an Ask question that gives no place of the text it asks about.

## Readings due

- `estimate-close-commits` — `pending`; target `rule-close` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-29/2341/spec.md` (Case 914): `test_render.py -k paths`, then after a librarian's run whose `librarian-guppi.md` holds the Render of `rule-close`, `git log` and `git status`. This run: `guppi render --paths` printed 32 paths, `plugin/skills/install/SKILL.md` on line 16; `grep -c $'\r'` over its output printed 0; the close command runs as `rule-close` writes it, after this brief.
- `estimate-close-reports-the-run` — `pending`; target `rule-close` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-29/2341/spec.md` (Case 913): the person's answer on the report after a librarian's run whose `librarian-guppi.md` holds the Render of `rule-close` with no limit of lines. This run: its `librarian-guppi.md` held the old Render at its start; `guppi render` of this run wrote `.claude/agents/librarian-guppi.md` (modified in `git status`).
- `estimate-guppi-package-is-ready-after-the-install` — `pending`; target `rule-guppi-package` (`draft`); read by its unticked `read` box in `vault/raw/2026-10-29/2341/spec.md` (Case 918.4): after this session's librarian run with a tag `prod-x.y.z` in the history of HEAD, a clean copy by `guppi ship --allow-draft`, an install by the person at a stop of Work Mode, and the person's answer. This run: `git tag --merged HEAD` printed `prod-0.2.0`, `prod-1`, `prod-2`.
- `estimate-plugin-install-runs-no-hook-before-uv-sync` — `pending`; target `rule-plugin-install` (`draft`); method: after the librarian's run of the session that sets its Criterion, with a tag `prod-x.y.z` in the history of HEAD, two installs by hand from a clean copy, one normal and one with `UV_OFFLINE=1` and an empty `UV_CACHE_DIR`. This run: `git tag --merged HEAD` printed `prod-0.2.0`, `prod-1`, `prod-2`.
- `estimate-orchestration-shows-the-built-case` — `pending`; target `rule-orchestration` (`draft`); method: after the first summary of `case-guppi` in Plan Mode with a line `Other Case` naming a Case of the session under the new Render.
- `estimate-orchestration-signs-items-taken-together` — `pending`; target `rule-orchestration` (`draft`); method: after the first batch taken up together under the new Render in which a summary carries a line `Other Case` naming a Case of the session.
- `estimate-case-build-goes-on-after-a-live-compaction` — `pending`; target `rule-case-build` (`draft`); method: after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `pending`; target `rule-case-build` (`draft`); method: after the first Case built under the Render that names a test over a live file and changes both.
- `estimate-ratification-ledger-line-form` — `pending`; target `rule-ratification` (`draft`); method: after a session whose ledger holds a lesson with the Case that closes its cause, a Case taking up a decision with more than one Case in `deferred_by`, and a lesson line declaring a new tag.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `pending`; target `rule-morph` (`draft`); method: after the session whose Work Mode builds the setup skill of `rule-morph`.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `pending`; target `rule-skill-merge-main` (`draft`); method: after the first `/merge-main` that leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `pending`; target `rule-skill-pr-review` (`draft`); method: after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `pending`; target `rule-work-mode` (`draft`); method: after the first `/work` on the rendered skill in which a Case is ratified in Work Mode.
- `estimate-hi-writes-frontier` — `pending`; target `rule-skill-hi` (`draft`); method: the person's answer in the session after the close of a sprint.
- `estimate-sprint-plugin-ci-writes-a-clean-branch` — `pending`; target `entity-sprint-plugin` (`draft`); method: `test_ship.py`, and a run of `.github/workflows/prod.yml` on a tag `prod-x.y.z` before the close of `plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` — `pending`; target `entity-sprint-plugin` (`draft`); method: an install from a clean copy in a session of `plugin` before its close.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `pending`; target `entity-sprint-plugin` (`draft`); method: a pull request from a second account, before the close of `plugin`.
- `estimate-sprint-plugin-readme-describes-the-project` — `pending`; target `entity-sprint-plugin` (`draft`); method: the person's answer at the `/hi` after the session that writes `README.md`.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `pending`; target `entity-sprint-plugin` (`draft`); method: at the end of Work Mode of the session that closes `entity-sprint-plugin`.

## Flags

- `near`: L4 `lesson-librarian-writes-a-total-no-count-printed` — `near: lesson-orchestration-claimed-a-reading-before-taking-it`.
- No entry `incomplete`, `failed` or `unparsed`. No `failed` Estimate.
- MOC candidates: none named by any step of this run.
- Stale defer: `rule-clean-branch` stands `built` and keeps `deferred_by: decision-case-893.1`; `backlog.md` lists it, put off in 13 sessions.
- Contradictions: none found by this run.
- Lint (`guppi check`, exit 1, 11 lines): 9 pages with `core: true` stand `draft` — `entity-sprint`, `rule-case-build`, `rule-close`, `rule-guppi-package`, `rule-morph`, `rule-orchestration`, `rule-ratification`, `rule-skill-hi`, `rule-work-mode`; `estimates/estimate-harness-make-runs-in-both-shells: method: the Makefile has no target with`; `ship: .guppi/tests/test_render.py:500: a reference to a case: Case 914`.
- Handoff, Observations: `.guppi/tests/test_onward.py` keeps two test names and docstrings that speak of the reminder of the ledger hook; Case 917 has no `**Change**` item for its fix of a `/pre-spec` finding; `guppi ship` writes `vault/.gitignore`.

## Next session

### Cases

- Five shipped Estimates hold Criterion sentences true only in the repository of GUPPI: `estimate-permissions`, `estimate-orchestration-forwards-a-discussion-question`, `estimate-case-check-sends-back-a-faulty-case`, `estimate-case-example-passes-the-check`, `estimate-ratification-case-id-carries-the-sprint`; Case 918 left their rewrite to a later Case (handoff, For the next session).
- An `A` line of `/hi` that asks the person to judge a text the main agent cannot open names no place to find it and quotes none of it (lesson L41; handoff, For the next session).
- `rule-clean-branch` stands `built` and keeps `deferred_by: decision-case-893.1`; that defer still holds four Estimates whose rewrite waits: `estimate-synthesis-keeps-actioned-by-the-mark`, `estimate-synthesis-clusters`, `estimate-ask-query-before-a-create`, `estimate-compact-recall-reloads` (handoff, For the next session).
- `guppi check` prints `ship: .guppi/tests/test_render.py:500: a reference to a case: Case 914`: a test this session added names a Case where the clean version takes no reference to a case (lint).

### Work

- `estimate-close-commits`: `git log` and `git status` on the commit of this run, and whether the close command passed at its first run (the librarian's report), against its Criterion; its pytest part passed at Retro (handoff).

### Ask the person

- `estimate-plugin-install-runs-no-hook-before-uv-sync` — needs the person — Have you made the two installs by hand from a clean copy written by `guppi ship --allow-draft`, one normal and one with `UV_OFFLINE=1` and an empty `UV_CACHE_DIR`? If so, did the project hold no `.claude/settings.json` until `uv sync` passed, and did no hook error show after the rollback of the offline one?
- `estimate-guppi-package-is-ready-after-the-install` — needs the person — After the agent writes a clean copy by `guppi ship --allow-draft` in the repository of GUPPI, and you, at a stop of Work Mode, add it as a catalogue, install `guppi`, type `/guppi:install` in an empty project, reopen Claude Code and type `/hi`: did the output of the install, the order of its steps, the files of the project and its `.guppi/.venv/` match the Criterion?

## Readings at the close

- `uv run --project .guppi guppi test`: 1786 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: exit 1, 11 lines (Flags).
- Pages under `vault/wiki/`: rules 86, estimates 318, entities 5, lessons 59, insights 12, decisions 366. Files `*.md` under `vault/archive/`: 2935.
