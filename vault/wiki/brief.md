# Brief — 2026-11-25, librarian of session 0816

## Where things stand

- Session 0816 of the sprint `plugin`, 2026-11-25. Cases ratified: 1053.1, 1053.2, 1054.1, 1054.2, 1055.1–1055.5, 1057.1–1057.5; Cases 1053 and 1057 each ratified twice after `/pre-spec`, the second form standing (handoff).
- Code: `.guppi/guppi/ratified.py` (`held_number` refuses a first write of a case file whose number has a decision line in the session's ledger), `.guppi/guppi/prespec.py` (`check_stop_before_render`, over `lint.CODE_SPAN`), `.guppi/guppi/sprint.py` (ticks only a `passed` Estimate), `.guppi/guppi/sprint_close.py` (settles an Estimate of the sprint page only by `--archive-unread`), `.guppi/guppi/ledger.py` (a docstring). Tests: `test_ratified.py` 5 new, `test_prespec.py` 6 new, `test_sprint.py` and `test_sprint_close.py` 1 renamed each. `guppi test` 1994 passed, 6 skipped, 2 deselected; `guppi style` clean (handoff).
- Readings: L1 at `/hi`; L23–L31 at Retro, the five install Estimates read at the install stop of Work Mode in five test projects under `C:/tmp/guppi-1055/`; lessons L32 (`knowledge`) and L33 (`error`) (handoff, ledger).
- `guppi materialize` printed `written with 33 entries` for `vault/raw/2026-11-25/0816/materialize.yaml` and `extended with 0 entries` for `vault/raw/2026-11-25/0605/materialize.yaml`. The ledger has 33 lines (`wc -l`). The yaml holds 32 entries under `entries`, for lines 1 to 23 and 25 to 33; line 24 is folded into the `create` entry of line 4, and `log.md` shows it applied with `#L24` as origin. Every line is accounted for; `unparsed: []`.
- Entries by kind: 1 `create` (an Estimate), 20 `update`, 9 `estimate`, 2 `lesson`; 18 entries under `decisions`. After `generate`, every entry carries `applied`. One entry carries `incomplete: [source]`; no entry carries `failed` or `exists`.
- Index check: the one `create` entry is an Estimate, so no Grep ran for it. The two `lesson` entries: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 71 lines; `lesson-plugin-copy-shipped-before-the-style-check` marked `near: lesson-ship-leaves-an-empty-comment-after-a-removed-pointer`; `lesson-plugin-install-writes-a-project-settings-file` neither same nor near.
- `guppi generate` printed 49 pages written or changed for 0816 and 0 for 0605, nothing on stderr. It ticked 33 lines of `vault/raw/2026-11-25/0816/spec.md` and line 436 of `vault/raw/2026-11-25/0605/spec.md` (`git diff`). 5 `read` lines stand unticked (200, 244, 551, 671, 714). No unticked Spec line holds `guppi sprint-close --apply`.
- `guppi cleanup` printed `2 page(s) moved`, into `vault/archive/plugin/2026-11-25/0816/`: `decision-case-949` (superseded by 1055.5) and `lesson-case-build-puts-a-reading-before-the-render-it-tests`, archived by the cascade of `insight-workflow-code-live-before-the-page-it-reads`, set `actioned`.
- Pages created (`git status`, `log.md`): decisions 18 (`decision-case-1053`, `-1053.1`, `-1053.2`, `-1054`, `-1054.1`, `-1054.2`, `-1055`, `-1055.1` to `-1055.5`, `-1057`, `-1057.1` to `-1057.5`); estimates 1 (`estimate-prespec-hook-reports-a-stop-before-the-render-it-tests`, `passed`); lessons 2 (`lesson-plugin-install-writes-a-project-settings-file`, `lesson-plugin-copy-shipped-before-the-style-check`, both `new`).
- Pages updated (`git status`, `log.md`): rules 10 (`rule-spec-reconcile`, `rule-orchestration`, `rule-case-build`, `rule-sprint`, `rule-skill-sprint-close` by their Cases; `rule-prespec-hook` gained its new Estimate; `rule-git-context`, `rule-morph`, `rule-plugin-install` `draft` → `built` and `rule-sprint-close` `built` → `draft` by the cascade); estimates 14 (`passed`: `estimate-case-build-reads-each-list-of-a-new-member`, `estimate-spec-reconcile-refuses-a-case-file-another-agent-holds`, `estimate-plugin-install-asks-one-approval-in-plan-mode`, `estimate-morph-sets-up-the-project-at-the-first-hi`, `estimate-git-context-offers-git-init`, `estimate-plugin-install-writes-guppi-into-an-empty-project`, `estimate-plugin-install-sets-aside-the-files-of-the-project`, `estimate-sprint-ticks-a-read-one-off-estimate`, `estimate-sprint-close-settles-unread-estimates`; `pending`: `estimate-orchestration-dispatches-case-guppi-at-a-level`, `estimate-case-build-settles-form-by-itself`, `estimate-sprint-plugin-done-counts-a-one-off-reading`, `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`, `estimate-sprint-close-takes-the-readings-in-groups`); entities 1 (`entity-sprint-plugin`: its Purpose and a `## Backlog` line by 1057.1); insights 1 (`insight-workflow-code-live-before-the-page-it-reads`, `open` → `actioned`, `addressed_by` `decision-case-1053.2`, severity 0); decisions 1 (`decision-case-949`, superseded, archived); lessons 1 (`lesson-case-build-puts-a-reading-before-the-render-it-tests`, archived).
- The five install Estimates: `log.md` shows the `method` update of each before its `pending → passed` line, as the handoff asked. The defer of `estimate-plugin-install-sets-aside-the-files-of-the-project` by `decision-case-949` stands superseded in `log.md`, not applied.
- `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr. The render changed `.claude/agents/case-guppi.md`, `.claude/skills/sprint-close/SKILL.md` and `vault/wiki/orchestration.md` (`git status`).
- `guppi sprint`: under Done when of `sprint.md`, 11 lines, 3 `- [x]`; the line of `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` went `- [x] … · failed` → `- [ ] … · pending`, as the handoff asked; the Purpose line took the text of Case 1057.1. `guppi backlog`: 10 items. Out: `estimate-plugin-install-sets-aside-the-files-of-the-project`, `insight-workflow-code-live-before-the-page-it-reads`. In: the Backlog line of Case 1057.1 on whether a passed one-off Estimate is never read again.
- `guppi archive` printed nothing on stdout or stderr, exit 0; it moved no unit. `raw/2026-11-25/0605` is dated the day of the run, which the archive does not look at; `raw/2026-11-25/0816` is the session of the run.

Synthesis. Greps: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 71 lines; `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 19 lines. 0 entries added.
- `lesson-plugin-install-writes-a-project-settings-file` — none: its cause is a `.claude/settings.json` written into the project by Claude Code's `/plugin install`; the other `plugin-install` lessons name hooks of the copy that run at once and an untracked `__pycache__/`, and no Insight names a file that Claude Code writes. It stays `new`.
- `lesson-plugin-copy-shipped-before-the-style-check` — none: its cause is a copy written at a stop of Work Mode before any `guppi style` over the new code; `lesson-ship-leaves-an-empty-comment-after-a-removed-pointer` names a defect that the cleaning of `ship` makes, with no style run over the copy; `insight-workflow-code-live-before-the-page-it-reads` names a page that lands after its code. It stays `new`, marked `near` the first.

## Readings due

25 Estimates: 0 `failed`, 25 `pending`. The session's `spec.md` holds 5 unticked `read` lines (200, 244, 551, 671, 714); `vault/raw/2026-11-25/0605/spec.md` holds 1 (124).

- `estimate-orchestration-dispatches-case-guppi-at-a-level` — `rule-orchestration` (draft) — `read` line 200 — method: by hand, at the Retro of the session that sets this Criterion, the new Render in the Spec; by hand, after a session whose `orchestration.md` holds that Render, each Agent call of `case-guppi` in its transcript. The render of this run wrote `vault/wiki/orchestration.md`.
- `estimate-case-build-settles-form-by-itself` — `rule-case-build` (draft) — `read` line 244 — method: by hand, at the Retro of the session that sets this Criterion, the new Render in the Spec; by hand, after a session whose `case-guppi.md` holds that Render, each round in its transcript. The render of this run wrote `.claude/agents/case-guppi.md`.
- `estimate-sprint-plugin-done-counts-a-one-off-reading` — `entity-sprint-plugin` (draft), `once: true` — `read` line 551, and line 124 of the 0605 Spec — method: by hand, after the librarian's run of session 0816, the Purpose of `vault/wiki/entities/entity-sprint-plugin.md`. This run: the Purpose holds `Done when every Estimate of this page passes, a one-off Estimate, which carries `once: true`, by one reading that passes, a failed one worked on until a reading passes:`.
- `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` — `entity-sprint-plugin` (draft), `once: true` — `read` line 671 — method: by hand, after a `case-guppi` build of the sprint `plugin` whose Case adds a file outside `vault/wiki/`, its agent transcript and case file.
- `estimate-sprint-close-takes-the-readings-in-groups` — `rule-sprint-close` (draft) — `read` line 714 — method: by hand, after the Work Mode of a session that closed a sprint, its closing Case and ledger.
- `estimate-ask-query-before-a-create` — `rule-ask` (draft) — method: by hand, after the first build of `case-guppi` whose Case proposes a create without a ref, on the Render of `rule-ask` that runs every category.
- `estimate-case-build-goes-on-after-a-live-compaction` — `rule-case-build` (draft) — method: by hand, after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `rule-case-build` (draft) — method: by hand, after the first Case built under the Render that names a test over a live file.
- `estimate-case-build-names-a-stale-line-of-another-case` — `rule-case-build` (draft) — method: by hand, after the first build on the new Render in which the note of `rule-case-check` lists the Case file of another Case of the session.
- `estimate-case-build-offers-a-page-for-code-no-page-covers` — `rule-case-build` (draft) — method: by hand, at the Retro of the session whose Render asks `context` for why the page was chosen; by hand, after a session in which `case-guppi` settles a page for code that no page covers.
- `estimate-case-build-runs-the-vault-query-first` — `rule-case-build` (draft) — method: by hand, after the first build whose Case proposes a create without a ref.
- `estimate-clean-branch-prod-commits-only-a-tested-copy` — `rule-clean-branch` (draft) — method: by hand, `.github/workflows/prod.yml` read against the Criterion; by hand, after a run of `prod.yml` on GitHub whose step `guppi ship` exits 0, `gh run view --log`. The last commit of `origin/prod` is of 2026-11-03 (`git log`).
- `estimate-hi-writes-frontier` — `rule-skill-hi` (draft) — method: by hand, after the reply that acknowledges the opening Case of `/sprint-open` in the session after the close of a sprint, the person's answer.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` — `rule-orchestration` (draft) — method: by hand, after an acknowledging reply after `/pre-spec` that waits for the person's word, its transcript. The handoff says Cases 1053 and 1057 were ratified again after `/pre-spec` in session 0816.
- `estimate-orchestration-signs-items-taken-together` — `rule-orchestration` (draft) — method: by hand, after the first batch taken up together in Plan Mode in which a summary carries a line Other Case naming a Case of the session.
- `estimate-retro-loads-on-a-red-command` — `rule-retro` (draft), `deferred_by` Case 1007 — method: by hand, after the librarian's render that writes `.claude/skills/retro/SKILL.md` with `--exit-zero`, and the first load of `/retro` after it. This run: the render left `.claude/skills/retro/SKILL.md` unchanged.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `rule-skill-merge-main` (draft) — method: by hand, after the first `/merge-main` that leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `rule-skill-pr-review` (draft) — method: by hand, after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-sprint-plugin-case-guppi-level-trial-decided` — `entity-sprint-plugin` (draft), `once: true` — method: by hand, in the session that closes the sprint `plugin`, the output of `guppi agents` and the findings of `ask-guppi`, the person's answer.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `entity-sprint-plugin` (draft) — method: by hand, at the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link` — `entity-sprint-plugin` (draft), `once: true` — method: by hand, after the librarian's run that applies the update of `lesson-ledger-reading-writes-a-bare-wikilink`. This run applied no update of that lesson.
- `estimate-sprint-plugin-link-graph-is-gone` — `entity-sprint-plugin` (draft), `once: true` — method: by hand, after the librarian's run that applies the delete of `entity-link-graph`. This run applied no delete.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `entity-sprint-plugin` (draft) — method: by hand, a pull request from a second account read on GitHub, before the close of the sprint.
- `estimate-sprint-plugin-readme-describes-the-project` — `entity-sprint-plugin` (draft) — method: by hand, the person's answer on `README.md` at the `/hi` of the session after the one whose Work Mode writes it, before the close of the sprint.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` (draft), `deferred_by` Case 1009 — method: by hand, after a librarian's run that puts a lesson with `addressed_by` under an Insight that stands `actioned`, the yaml and the brief. This run: the yaml held 2 `lesson` entries, neither with `addressed_by`; the synthesis put neither under an Insight and added no entry.

## Flags

- `incomplete`: `lesson-plugin-install-writes-a-project-settings-file` (line 32), `incomplete: [source]`; the page was written with no `source`, and `guppi check` prints `schema: missing field source` for it.
- `near`: `lesson-plugin-copy-shipped-before-the-style-check` (line 33), `near: lesson-ship-leaves-an-empty-comment-after-a-removed-pointer`.
- No entry `failed` or `unparsed`. No failed Estimate.
- Lint (`guppi check`, exit 1, 1 line): `lessons/lesson-plugin-install-writes-a-project-settings-file: schema: missing field source (given {'kind': 'knowledge'})`. The baseline lines of the handoff (`core: true that is draft` of `rule-case-build`, `rule-morph`, `rule-orchestration`; `unread: failed` of three Estimates) no longer print, and the expected red of `guppi sprint --check` does not print after `guppi sprint`.
- `vault/archive/plugin/2026-11-20/1353/raw/spec.md` holds the unticked line 224 `read` of `estimate-plugin-install-asks-one-approval-in-plan-mode`, which this run read `passed`; `generate` ticked no line of that archived Spec.
- `guppi materialize` printed 33 entries for 0816; the yaml holds 32 under `entries` and line 24 folded into the entry of line 4.
- Handoff observation: in p1 and p2 the Claude Code CLI could not approve the long plan at `ExitPlanMode`; `/approve-spec` approved it.
- Handoff observation: `uv sync` in each test project warned that `build_system.requires = ["uv-build>=0.11,<0.12"]` of `.guppi/pyproject.toml` does not hold uv 0.13.10; the build passed.
- Handoff observation: the setup Case of p2 first proposed the transcripts folder with a lower-case `c--`; a Glob found `C--`, and the Case used it.
- Handoff note: `plugin` is ahead of `origin/plugin` again (`git rev-list` counts 2 commits before this run's commit).
- Read outside the frame: a Grep of the unticked lines of `vault/archive/plugin/2026-11-20/1353/raw/spec.md`, a file under `vault/archive/`, for Readings due (where each `read` line stands); the handoff did not ask for it.
- No MOC candidate, no stale defer and no contradiction printed by `guppi check`, `guppi backlog` or this run.

## Next session

Cases
- Whether the copy for an install stop is written only after `uv run --project .guppi guppi style` is clean, or Work Mode runs the style check before a stop that hands over a copy; `lesson-plugin-copy-shipped-before-the-style-check` records the cause (handoff).
- Whether `.guppi/pyproject.toml` should widen its `uv-build` bound past 0.12 (handoff).
- The Backlog line of Case 1057.1: whether a passed one-off Estimate is never read again (handoff).
- `lesson-plugin-install-writes-a-project-settings-file` has no `source`, a field its `knowledge` kind needs; `guppi check` exits 1 on it (yaml `incomplete: [source]`, `guppi check`).

Work
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec`: the handoff says Cases 1053 and 1057 were ratified again after `/pre-spec` in session 0816.

Ask the person
- `estimate-sprint-plugin-readme-describes-the-project` — needs the person — does `README.md` at the root of the branch `plugin` describe GUPPI as it stands, with its Why, Is it for you, how a session goes, its parts, its install and its use?

## Readings at the close

- `uv run --project .guppi guppi test`: exit 0, 1994 passed, 6 skipped, 2 deselected.
- `uv run --project .guppi guppi check`: exit 1, 1 line, as under Flags.
- Live pages (`find vault/wiki/<category> -name "*.md"`): decisions 631, rules 90, entities 5, estimates 376, lessons 72, insights 19; 11 files at the root of `vault/wiki/`. Files under `vault/archive/` (`find -name "*.md"`): 3395 after `guppi archive`.
