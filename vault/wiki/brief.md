# Brief — 2026-11-26, librarian of session 1336

## Where things stand

- Session 1336 of the sprint `plugin`, 2026-11-26. Cases ratified: 1064, 1065, 1066, 1067, and the defer Case 1068 (handoff).
- Code: `.guppi/guppi/pages.py` (`HISTORY_DATE`, `STATUS_SET`, `status_lines`; `is_draft_core` judges by `status_lines`, `SET_BUILT` gone), `.guppi/guppi/box.py` (imports `HISTORY_DATE`), `.guppi/guppi/backlog.py` (`closed_on`, `stood_finished`, `finished` with the day of the close); six new tests in `.guppi/tests/test_backlog.py`. `guppi test` 2000 passed, 6 skipped, 2 deselected; `guppi style` clean (handoff).
- Readings: L1 `estimate-orchestration-dispatches-case-guppi-at-a-level` failed, L2 `estimate-case-build-settles-form-by-itself` failed, L3 `estimate-sprint-plugin-readme-describes-the-project` passed, L12 `estimate-backlog-renders` passed, L13 `estimate-case-build-settles-form-by-itself` passed. Lesson: L14 `lesson-frontier-line-closed-in-two-changes-through-bash` (handoff).
- `guppi materialize` printed `written with 14 entries` for `vault/raw/2026-11-26/1336/materialize.yaml` and `extended with 0 entries` for the yaml of 2003. The ledger has 14 lines (`wc -l`); the yaml holds 14 entries for lines 1 to 14, so every line is accounted for; `unparsed: []`.
- Entries by kind, after the synthesis: 5 `estimate`, 8 `update` (6 of the Cases, 2 of the synthesis), 1 `create` (an Estimate), 1 `defer`, 1 `lesson`; 5 entries under `decisions`. All 16 carry `applied`; none carries `failed`, `incomplete` or `near`. The `defer` entry of line 11 carries `exists: true`.
- Index check: the one `create` entry is an Estimate, so no Grep of its category ran. No yaml edit by the index check.
- `guppi generate` printed 15 pages written or changed for 1336 and 0 for 2003, and no error line. With the render, 11 lines of `vault/raw/2026-11-26/1336/spec.md` are ticked (`git diff --numstat`: 11); 2 `read` lines stand unticked (56, 158). No unticked Spec line holds `guppi sprint-close --apply`.
- `guppi cleanup` printed `0 page(s) moved`.
- Pages created (`git status`, `log.md`): decisions 5 (`decision-case-1064` to `decision-case-1068`); estimates 1 (`estimate-orchestration-leaves-the-number-to-case-guppi`, `pending`); lessons 1 (`lesson-frontier-line-closed-in-two-changes-through-bash`, `clustered` by the synthesis).
- Pages updated (`git status`, `log.md`): rules 2 (`rule-orchestration` by 1064 and 1066, `draft`; `rule-backlog` by 1067, `built`); estimates 4 (`estimate-orchestration-dispatches-case-guppi-at-a-level`: `pending → failed` by L1, then Criterion replaced and `pending` by 1064; `estimate-case-build-settles-form-by-itself`: `failed` by L2, Criterion replaced and `pending` by 1065, `passed` by L13; `estimate-backlog-renders`: Criterion replaced by 1067, `passed` by L12; `estimate-sprint-plugin-readme-describes-the-project`: `passed` by L3); entities 1 (`entity-guppi-repository`: `deferred_by` `decision-case-1068`, status `built`); insights 1 (`insight-orchestration-frontier-closer-leaves-the-box-open`, by the synthesis).
- Handoff instructions: (1) the three anchors of 1064 and 1066 in `rule-orchestration` each hit once (Grep `-o` over the page printed one line each, lines 39, 43, 43); `log.md` shows the update of 1064 before the one of 1066, and the render rewrote `vault/wiki/orchestration.md`. (2) `log.md` shows the lines in ledger order: L1 failed, the update of 1064, L2 failed, the update of 1065, L13 passed; the pages stand `pending` and `passed`. (3) `guppi backlog` no longer lists `rule-work-mode` and lists `entity-guppi-repository`; it also lists `insight-orchestration-frontier-closer-leaves-the-box-open`, which the synthesis reopened, so the count went from 10 to 11 items, not to 10 (Flags). (4) The `defer` of 1068 set `deferred_by` on `entity-guppi-repository`.
- `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr. The render changed `vault/wiki/orchestration.md` alone (`git status`). `guppi sprint`: the Done-when line of `estimate-sprint-plugin-readme-describes-the-project` is now `- [x] · passed`. `guppi glossary` left `glossary.md` unchanged.

Synthesis. Greps: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 73 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 19 lines. 2 entries added.
- `lesson-frontier-line-closed-in-two-changes-through-bash` — joined `insight-orchestration-frontier-closer-leaves-the-box-open`: the box and the closer of one Frontier line written in two changes, the box left open by the first. The Insight stood `actioned` by `decision-case-1012` (a guard that refuses an Edit leaving an open box beside a closer); this lesson got past that guard by Bash, so the `update` set it `open`, its `addressed_by` standing; severity 1; the lesson is `clustered`.

## Readings due

26 Estimates: 0 `failed`, 26 `pending`. The session's `spec.md` holds 2 unticked `read` lines (56, 158); the `spec.md` of 2003 holds 3 (158, 260, 351).

- `estimate-orchestration-dispatches-case-guppi-at-a-level` — `rule-orchestration` (draft) — `read` line 56 — method: by hand, at the Retro of the session that sets this Criterion, the new Render in the Spec; by hand, after a session whose `orchestration.md` holds that Render, each Agent call of `case-guppi` in its transcript. The handoff Debt says the new Render in the Spec holds every line of the new Criterion; the ledger holds no reading of it at Retro. This run's render wrote that Render into `orchestration.md`.
- `estimate-orchestration-leaves-the-number-to-case-guppi` — `rule-orchestration` (draft) — `read` line 158 — method: by hand, at the Retro of this session, the new Render in the Spec; by hand, after a session in which a ratified Case comes back in another shape, its transcript. The handoff Debt says the new Render in the Spec holds the two sentences of Case 1066; the ledger holds no reading of it at Retro.
- `estimate-work-mode-runs-the-style-check-before-a-stop` — `rule-work-mode` (draft) — `read` line 158 of the 2003 Spec — method: by hand, after the first `/work` that loads after the librarian's render of `.claude/skills/work/SKILL.md` and reaches a task that opens with `stop:`, its transcript. This run: the render left `.claude/skills/work/SKILL.md` unchanged; the 1336 Spec holds no `stop:`.
- `estimate-sprint-plugin-passed-one-off-estimate-is-not-read-again` — `entity-sprint-plugin` (draft), `once: true` — `read` line 260 of the 2003 Spec — method: by hand, after the librarian's run of session 2003, `vault/wiki/case-schema.md`, `.claude/agents/case-guppi.md`, `.claude/skills/pre-spec/SKILL.md` and `vault/wiki/estimates/schema.yaml`. This run: the render left the four files unchanged; each holds one line with `case 1063.1` (`grep -c`).
- `estimate-skill-merge-main-joins-a-conflicted-page` — `rule-skill-merge-main` (draft) — `read` line 351 of the 2003 Spec — method: by hand, after the first `/merge-main` whose merge of `main` leaves a conflicted page. `git log --merges` printed no merge commit.
- `estimate-ask-query-before-a-create` — `rule-ask` (draft) — method: by hand, after the first build of `case-guppi` whose Case proposes a create without a ref, on the Render of `rule-ask` that runs every category.
- `estimate-case-build-goes-on-after-a-live-compaction` — `rule-case-build` (draft) — method: by hand, after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `rule-case-build` (draft) — method: by hand, after the first Case built under the Render that names a test over a live file.
- `estimate-case-build-names-a-stale-line-of-another-case` — `rule-case-build` (draft) — method: by hand, after the first build on the new Render in which the note of `rule-case-check` lists the Case file of another Case of the session.
- `estimate-case-build-offers-a-page-for-code-no-page-covers` — `rule-case-build` (draft) — method: by hand, at the Retro of the session whose Render asks `context` for why the page was chosen; by hand, after a session in which `case-guppi` settles a page for code that no page covers.
- `estimate-case-build-runs-the-vault-query-first` — `rule-case-build` (draft) — method: by hand, after the first build whose Case proposes a create without a ref.
- `estimate-clean-branch-prod-commits-only-a-tested-copy` — `rule-clean-branch` (draft) — method: by hand, `.github/workflows/prod.yml` read against the Criterion; by hand, after a run of `prod.yml` on GitHub whose step `guppi ship` exits 0, `gh run view --log`. The last commit of `origin/prod` is of 2026-11-03 (`git log`).
- `estimate-hi-writes-frontier` — `rule-skill-hi` (draft) — method: by hand, after the reply that acknowledges the opening Case of `/sprint-open` in the session after the close of a sprint, the person's answer.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` — `rule-orchestration` (draft) — method: by hand, after an acknowledging reply after `/pre-spec` that waits for the person's word, its transcript.
- `estimate-orchestration-signs-items-taken-together` — `rule-orchestration` (draft) — method: by hand, after the first batch taken up together in Plan Mode in which a summary carries a line Other Case naming a Case of the session.
- `estimate-retro-loads-on-a-red-command` — `rule-retro` (draft), `deferred_by` Case 1007 — method: by hand, after the librarian's render that writes `.claude/skills/retro/SKILL.md` with `--exit-zero`, and the first load of `/retro` after it. This run: the render left `.claude/skills/retro/SKILL.md` unchanged.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `rule-skill-pr-review` (draft) — method: by hand, after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-sprint-close-takes-the-readings-in-groups` — `rule-sprint-close` (draft) — method: by hand, after the Work Mode of a session that closed a sprint, its closing Case and ledger.
- `estimate-sprint-plugin-case-guppi-level-trial-decided` — `entity-sprint-plugin` (draft), `once: true` — method: by hand, in the session that closes the sprint `plugin`, the output of `guppi agents` and the findings of `ask-guppi`, the person's answer.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `entity-sprint-plugin` (draft) — method: by hand, at the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-done-counts-a-one-off-reading` — `entity-sprint-plugin` (draft), `once: true` — method: by hand, after the librarian's run of session 0816, the Purpose of `vault/wiki/entities/entity-sprint-plugin.md`. This run left `entity-sprint-plugin.md` unchanged (`git status`).
- `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` — `entity-sprint-plugin` (draft), `once: true` — method: by hand, after a `case-guppi` build of the sprint `plugin` whose Case adds a file outside `vault/wiki/`, its agent transcript and case file.
- `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link` — `entity-sprint-plugin` (draft), `once: true` — method: by hand, after the librarian's run that applies the update of `lesson-ledger-reading-writes-a-bare-wikilink`. This run applied no update of that lesson.
- `estimate-sprint-plugin-link-graph-is-gone` — `entity-sprint-plugin` (draft), `once: true` — method: by hand, after the librarian's run that applies the delete of `entity-link-graph`. This run applied no delete.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `entity-sprint-plugin` (draft) — method: by hand, a pull request from a second account read on GitHub, before the close of the sprint.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` (draft), `deferred_by` Case 1009 — method: by hand, after a librarian's run that puts a lesson with `addressed_by` under an Insight that stands `actioned`, the yaml and the brief. This run: the yaml held 1 `lesson` entry, with no `addressed_by`; the synthesis put it under `insight-orchestration-frontier-closer-leaves-the-box-open`, which stood `actioned`, and set that Insight `open`.

## Flags

- No entry `incomplete`, `failed`, `near` or `unparsed`. No failed Estimate.
- The `defer` entry of line 11 (`entity-guppi-repository`) carries `exists: true`, set by `guppi materialize`.
- The synthesis set `insight-orchestration-frontier-closer-leaves-the-box-open` from `actioned` to `open`, with `addressed_by` `decision-case-1012` standing; it now stands in `backlog.md`, severity 1.
- `guppi backlog` counts 11 items, not the 10 that the handoff's two moves give: `rule-work-mode` left, `entity-guppi-repository` came in, and the reopened Insight came in too.
- Lint (`guppi check`, exit 0): no line. The expected red of the handoff, `guppi backlog --check` on `vault/wiki/backlog.md`, no longer prints after this run wrote the file.
- Handoff note: `/pre-spec` found that Case 1064 gives no `update` to `estimate-sprint-plugin-case-guppi-level-trial-decided`; the main agent left it with the reason in the `context` of 1064, and `ask-guppi` accepted it.
- Handoff observation: the number 1062 of session 2003 stands as an empty `cases/case-1062.md` in that session's folder.
- No MOC candidate, no stale defer and no contradiction printed by `guppi check`, `guppi backlog` or this run.

## Next session

Cases
- Whether frontierguard should also judge a Bash command that changes `frontier.md`, or a guard should refuse such a command, so that the box and the closer of a line always change in one edit; `lesson-frontier-line-closed-in-two-changes-through-bash` records the cause, and `insight-orchestration-frontier-closer-leaves-the-box-open` stands `open` again (handoff, synthesis).
- The sprint item C1, `rule-clean-branch` (the clean branch), put off by the person at the close of Plan Mode with no Case (handoff).

Work
- none

Ask the person
- none

## Readings at the close

- `uv run --project .guppi guppi test`: exit 0, 2000 passed, 6 skipped, 2 deselected.
- `uv run --project .guppi guppi check`: exit 0, no line.
- Live pages (`find vault/wiki/<category> -name "*.md"`): decisions 643, rules 90, entities 5, estimates 380, lessons 74, insights 19; 11 files at the root of `vault/wiki/`. Files under `vault/archive/` (`find -name "*.md"`): 3434 before `guppi archive`, 3450 after it.
- `guppi archive` printed `raw/2026-11-25/2003 → archive/plugin/2026-11-25/2003/raw`; `raw/2026-11-26/1336` is the session of the run. The three unticked `read` lines of the 2003 Spec named under Readings due now stand in `vault/archive/plugin/2026-11-25/2003/raw/spec.md`.
