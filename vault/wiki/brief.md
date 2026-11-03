# Brief — 2026-11-03, librarian of session 0316 (2026-11-03)

## Where things stand

- Session 0316 of the sprint `plugin`. Cases ratified: 1014 (short-form defer), 1015 (1015.1, 1015.2), 1016, 1017 (1017.1–1017.9), 1018 (1018.1, 1018.2) (handoff).
- Code: `.guppi/guppi/config.py` (`SETUP_KEY`, `setup_pending`), `.guppi/guppi/ship.py` (`setup_not_done`), `.guppi/guppi/ledger.py` (`refused_without_sprint` passes every line while the setup is pending), `.guppi/guppi/sprint.py` (`hi_hook` prints the `/setup` line first); `plugin/plugin.json` gains `"icon": "./.guppi/icon.png"`; new `.guppi/icon.png` (512×512 PNG, transparent background); `guppi-assets/` holds both source pictures. Tests: `test_config.py`, `test_ship.py`, `test_ledger.py`, `test_sprint.py`. `guppi test` 1943 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- Readings: L27–L31 passed (`estimate-clean-branch-ships-the-plugin-icon`, `estimate-clean-branch-ships-the-setup-not-done`, `estimate-ledger-write-passes-every-line-before-the-setup`, `estimate-skill-setup-starts-at-hi`, `estimate-skill-sprint-open-asks-the-goal-as-an-open-question`). Lessons: L32, L33 (error) (handoff).
- `guppi materialize` printed `written with 33 entries` for `vault/raw/2026-11-03/0316/materialize.yaml` and `extended with 0 entries` for the yaml of 2155. The ledger has 33 lines (`wc -l`). The yaml holds entries for lines 1–26 and 31–33; lines 27–30 are folded into the `create` entries of their Estimates (lines 6, 9, 11, 14), so every line is accounted for; `unparsed: []`.
- The yaml holds 29 entries under `entries` before the synthesis: 20 `update`, 5 `create` (4 estimates, 1 rule), 1 `defer` (line 1, marked `exists` by materialize), 1 `estimate` (line 31), 2 `lesson` (lines 32, 33); `decisions` holds 18 items.
- Index check: the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/` printed 90 lines; `rule-skill-setup` got `near: rule-morph`. The four Estimate creates have no index check.
- The synthesis added 2 entries marked `librarian: synthesis`: 1 `update` in `insights`, 1 `update` in `lessons`.
- Marks: every entry carries `applied`; one entry carries `near` (line 12); line 1 carries `exists`; no entry `failed`, `incomplete` or `merged`.
- `guppi generate` printed 46 pages written or changed for 0316, 0 for 2155, nothing on stderr. No unticked Spec line holds `guppi sprint-close --apply`. `guppi cleanup` printed `0 page(s) moved`. `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr. After the render `guppi.toml` holds `setup_done = true`.
- Pages created (25), from `git status`: decisions 18 (`decision-case-1014`, `decision-case-1015`, `decision-case-1015.1`, `decision-case-1015.2`, `decision-case-1016`, `decision-case-1017`, `decision-case-1017.1` to `decision-case-1017.9`, `decision-case-1018`, `decision-case-1018.1`, `decision-case-1018.2`); rules 1 (`rule-skill-setup`, `core: true`, `draft` → `built` by the cascade, child of `rule-session-start`); estimates 4 (`estimate-clean-branch-ships-the-plugin-icon`, `estimate-clean-branch-ships-the-setup-not-done`, `estimate-ledger-write-passes-every-line-before-the-setup`, `estimate-skill-setup-starts-at-hi`, each `passed`); lessons 2 (`lesson-case-build-crop-spec-ignores-the-alpha-channel`, `new`; `lesson-orchestration-batch-asks-one-fork-twice-with-opposite-answers`, `clustered` by the synthesis).
- Pages updated (21), from `git status`: rules 10 (`rule-ask` by 1015.1; `rule-clean-branch` by 1016 and 1017.1, `built` → `draft` by the cascade; `rule-guppi-config` by 1017.1; `rule-ledger-write` by 1017.2; `rule-skill-hi` by 1017.3; `rule-session-start`, child `rule-skill-setup` added; `rule-morph` by 1017.4; `rule-skill-sprint-open` by 1017.6 then 1018.1, `built` → `draft` by the cascade; `rule-orchestration` by 1017.7; `rule-git-context`, `built` → `draft` by the cascade); estimates 9 (`estimate-ask-searches-at-prespec` by 1015.1; `estimate-prespec-finds-a-reader-of-a-new-files-folder` by 1015.2; `estimate-morph-sets-up-the-project-at-the-first-hi` by 1017.4; `estimate-morph-takes-in-the-set-aside-files` by 1017.5; `estimate-skill-sprint-open-asks-the-opening-questions` by 1017.6; `estimate-orchestration-acknowledging-reply` deferred by 1014 and updated by 1017.7; `estimate-clean-branch-refuses-a-draft-core-page` by 1017.8; `estimate-skill-sprint-open-asks-the-goal-as-an-open-question` by 1018.2, then `passed` by L31; `estimate-git-context-offers-git-init` by 1017.9); entities 1 (`entity-sprint-plugin` by 1017.4); insights 1 (`insight-case-build-sibling-texts-unchecked-before-the-showing`, child added and `actioned` → `open` by the synthesis).
- The direct instructions of the handoff, as the pages stand: `estimate-orchestration-acknowledging-reply` holds the new Criterion and `method` of 1017.7 and `deferred_by: ["[[decision-case-1014]]"]`; `rule-skill-sprint-open` holds the text of 1017.6 (the setup Case before the opening Case) and of 1018.1 (step 2 and step 5); `rule-clean-branch` holds the text of 1016 (the icon) and of 1017.1 (`setup_done = false`); `rule-morph` and `rule-skill-setup` carry `core: true`.
- `guppi archive`: see the report of this run.

Synthesis. The Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 64 lines; the Grep `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 18 lines.
- `lesson-case-build-crop-spec-ignores-the-alpha-channel` — none: no lesson or Insight names a Case built without reading a property of its input file; `insight-case-build-rests-on-an-unchecked-fact-of-a-tool` names how an outside tool behaves. It stays `new`.
- `lesson-orchestration-batch-asks-one-fork-twice-with-opposite-answers` — joined `insight-case-build-sibling-texts-unchecked-before-the-showing` (Cases built at once, not checked against each other before the showing). The Insight stood `actioned` (`addressed_by: [[decision-case-872.1]]`) and the lesson carries no `addressed_by`, so the Insight is set `open`; its `addressed_by` stands.

## Readings due

28 Estimates stand `pending`, none `failed`.

- `estimate-ask-query-before-a-create` — `rule-ask` (draft) — method: by hand, after the first build of `case-guppi` whose Case proposes a create without a ref, on the Render of `rule-ask` that runs every category.
- `estimate-ask-searches-at-prespec` — `rule-ask` (draft) — `- [ ] read` line 86 of `vault/raw/2026-11-03/0316/spec.md`; method: by hand, after the first `/pre-spec` whose `ask-guppi` runs on the new Render of `rule-ask`, its transcript.
- `estimate-case-build-goes-on-after-a-live-compaction` — `rule-case-build` (draft) — method: by hand, after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `rule-case-build` (draft) — method: by hand, after the first Case built under the Render that names a test over a live file.
- `estimate-case-build-reads-each-list-of-a-new-member` — `rule-case-build` (draft) — method: by hand, after the first build in a later session whose Case adds a member to a list spelled out one by one.
- `estimate-case-build-reads-the-readers-of-a-new-files-folder` — `rule-case-build` (draft) — method: by hand, after the `/pre-spec` of the first session on the Render of `rule-case-build` in which a Case adds a file that is no page, its `case-guppi` transcript.
- `estimate-case-build-runs-the-vault-query-first` — `rule-case-build` (draft) — method: by hand, after the first build whose Case proposes a create without a ref.
- `estimate-case-build-searches-the-names-of-what-it-changes` — `rule-case-build` (draft) — `- [ ] read` line 130 of `vault/raw/2026-11-02/2155/spec.md`; method: by hand, after the `/pre-spec` of the first session in which the hook of `rule-case-check` sends the note that lists the files that name what a Case changes.
- `estimate-clean-branch-refuses-a-draft-core-page` — `rule-clean-branch` (draft) — `- [ ] read` line 720 of the session's `spec.md`; method: `uv run --project .guppi pytest .guppi/tests/test_ship.py .guppi/tests/test_lint.py -k draft_core`, then by hand, after the librarian's run that applies the updates of `rule-morph` and the create of `rule-skill-setup`, a Grep for `^core:` in four rule pages and for `--allow-draft` in `.github/workflows/prod.yml`. This run: `guppi generate` applied the update of `rule-morph` (1017.4) and the create of `rule-skill-setup` (1017.3); both pages hold `core: true`; `rule-morph` stands `draft`, `rule-skill-setup` stands `built` (cascade); `guppi check` printed `rules/rule-morph: status: a page with core: true that is draft`; this run wrote no line of `rule-skill-merge-main`, `rule-skill-pr-review` or `.github/workflows/prod.yml`.
- `estimate-git-context-offers-git-init` — `rule-git-context` (draft) — `- [ ] read` line 763 of the session's `spec.md`; method: by hand, after the librarian's run, an install from a `--allow-draft` copy into an empty folder that is no git repository, `/hi` typed three times. This run: the render wrote `.claude/skills/hi/SKILL.md` and `.claude/skills/setup/SKILL.md`, and `guppi.toml` with `setup_done = true`.
- `estimate-hi-writes-frontier` — `rule-skill-hi` (draft) — method: by hand, after the reply that acknowledges the opening Case of `/sprint-open` in the session after the close of a sprint, the person's answer.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `rule-morph` (draft) — `- [ ] read` line 536 of the session's `spec.md`; method: by hand, after the session whose Work Mode builds `/setup`, its step in `/hi` and in `/sprint-open` and the pass of the ledger hook: an install into an empty git project from a `--allow-draft` copy, `/hi` typed.
- `estimate-morph-takes-in-the-set-aside-files` — `rule-morph` (draft) — `- [ ] read` line 571 of the session's `spec.md`; method: by hand, after the session whose Work Mode builds `/setup` and its step in `/hi`: an install into a git project with files of its own from a `--allow-draft` copy.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` — `rule-orchestration` (draft) — method: by hand, after an acknowledging reply after `/pre-spec` that waits for the person's word, its transcript.
- `estimate-orchestration-acknowledging-reply` — `rule-orchestration` (draft), `deferred_by` Case 1014 — `- [ ] read` line 677 of the session's `spec.md` and line 452 of the 2155 `spec.md`; method: by hand, after the librarian's render of the sentence of Case 1013 into `orchestration.md`, two acknowledging replies in their transcript; by hand, after the librarian's run of the session that replaces this Criterion and a setup Case ratified in a new install from a `--allow-draft` copy. This run: the Criterion was replaced by 1017.7 and the render wrote `vault/wiki/orchestration.md`; no setup Case in a new install is seen.
- `estimate-orchestration-signs-items-taken-together` — `rule-orchestration` (draft) — method: by hand, after the first batch taken up together in Plan Mode in which a summary carries a line Other Case naming a Case of the session.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — `rule-plugin-install` (draft), `deferred_by` Case 949 — method: by hand, after the librarian's run of the session that set this Criterion, three installs from a `--allow-draft` copy. This run wrote no file of it.
- `estimate-prespec-finds-a-reader-of-a-new-files-folder` — `rule-prespec` (draft) — `- [ ] read` line 124 of the session's `spec.md`; method: by hand, after the first `/pre-spec` on the new Render whose plan adds a file that is no page, its transcript.
- `estimate-retro-loads-on-a-red-command` — `rule-retro` (draft), `deferred_by` Case 1007 — method: by hand, after the librarian's render that writes `.claude/skills/retro/SKILL.md` with `--exit-zero`, and the first load of `/retro` after it. This run: the render left `.claude/skills/retro/SKILL.md` unchanged.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `rule-skill-merge-main` (draft) — method: by hand, after the first `/merge-main` that leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `rule-skill-pr-review` (draft) — method: by hand, after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-skill-sprint-open-asks-the-opening-questions` — `rule-skill-sprint-open` (draft) — `- [ ] read` line 618 of the session's `spec.md`; method: by hand, after the librarian's run of the session that replaces this Criterion, the Renders in `.claude/skills/sprint-open/SKILL.md` and `.claude/skills/setup/SKILL.md` and the sentence on the reply that acknowledges the setup Case in `vault/wiki/orchestration.md`. This run: the Criterion was replaced by 1017.6; the render wrote `.claude/skills/sprint-open/SKILL.md` (from the texts of 1017.6 and 1018.1), `.claude/skills/setup/SKILL.md` (new) and `vault/wiki/orchestration.md` (1017.7).
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `entity-sprint-plugin` (draft) — method: by hand, at the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` — `entity-sprint-plugin` (draft) — method: by hand, in a session of the sprint `plugin` before its close, an install from a `--allow-draft` copy into an empty project.
- `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link` — `entity-sprint-plugin` (draft) — method: by hand, after the librarian's run that applies the update of `lesson-ledger-reading-writes-a-bare-wikilink`. This run applied no update of that lesson.
- `estimate-sprint-plugin-link-graph-is-gone` — `entity-sprint-plugin` (draft) — method: by hand, after the librarian's run that applies the delete of `entity-link-graph`. This run applied no delete.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `entity-sprint-plugin` (draft) — method: by hand, a pull request from a second account read on GitHub, before the close of the sprint.
- `estimate-sprint-plugin-readme-describes-the-project` — `entity-sprint-plugin` (draft) — method: by hand, the person's answer on `README.md` at the `/hi` of the session after the one whose Work Mode writes it, before the close of the sprint.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` (draft), `deferred_by` Case 1009 — method: by hand, after a librarian's run that puts a lesson with `addressed_by` under an Insight that stands `actioned`. This run: the synthesis put `lesson-orchestration-batch-asks-one-fork-twice-with-opposite-answers`, which carries no `addressed_by`, under the `actioned` `insight-case-build-sibling-texts-unchecked-before-the-showing`, with `set: {status: open}`.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` (draft), `deferred_by` Case 1008 — method: by hand, after the librarian's render that writes `.claude/skills/work/SKILL.md` with `--exit-zero`, and the first `/work` after it. This run: the render left `.claude/skills/work/SKILL.md` unchanged.

## Flags

- `near`: line 12, `create` of `rule-skill-setup`, `near: rule-morph` — `rule-morph` sets the setup Case, `rule-skill-setup` governs the skill `/setup` that builds it.
- No entry `incomplete`, `failed` or `unparsed`. No failed Estimate.
- Lint (`guppi check`, 1 line): `rules/rule-morph: status: a page with core: true that is draft`. The handoff names it intended by 1017.8: `guppi ship` refuses to write `prod` while it stands.
- `rule-skill-setup` stands `built`, not `draft`: the cascade set it `built` when its one Estimate, `estimate-skill-setup-starts-at-hi`, passed (L30). The handoff wrote that both `rule-morph` and `rule-skill-setup` gain `core: true` while `draft`; of the two, only `rule-morph` blocks the clean build.
- The synthesis reopened `insight-case-build-sibling-texts-unchecked-before-the-showing`: `actioned` (by `decision-case-872.1`) → `open`, severity 0 → 1, with `lesson-orchestration-batch-asks-one-fork-twice-with-opposite-answers` as its third child.
- No MOC candidate, no stale defer and no contradiction printed by `guppi check`, `guppi backlog` or this run.
- Handoff observation: the task text of Case 1016 says the icon is padded with white; `.guppi/icon.png` has a transparent background, as the person chose at the stop of Work Mode, with no new Case; the Criterion names no background.
- Handoff observation: whether the field `icon` clears `ICON_MISSING` of `claude plugin validate` is not checked; it shows at the next run of `prod.yml`, which writes nothing while `rule-morph` is `draft`.
- Handoff observation: `ask-guppi` at `/pre-spec` reported two searches of code beyond its frame, the third session running; Case 1015 lifts that limit, and this run's render wrote `.claude/agents/ask-guppi.md` from it. `ask-guppi`, confirming its findings, took the facts of code of findings 3, 5, 6 and 12 from the contexts and ran no search.
- Handoff note: `guppi ship` does not take `guppi-assets/` (not in `TREES` or `ROOT_FILES`).
- Reads beyond the frame: none.

## Next session

Cases
- Defer `estimate-case-build-reads-the-readers-of-a-new-files-folder` into the backlog, or give it a `method` that reads a later session, since its event was session 2155 and that transcript cannot be read (handoff).
- Where the source pictures in `guppi-assets/` live for good: the person put them there for now (handoff).
- The milestone The plugin: C1 (the clean version installed by hand), C3 (the README) and C4 (the close of `plugin`) were left for later; C1's reading by hand now also covers the setup of Case 1017 (handoff).

Work
- `estimate-morph-sets-up-the-project-at-the-first-hi`
- `estimate-morph-takes-in-the-set-aside-files`
- `estimate-skill-sprint-open-asks-the-opening-questions`
- `estimate-clean-branch-refuses-a-draft-core-page`
- `estimate-git-context-offers-git-init`

Ask the person
- none

## Readings at the close

- `uv run --project .guppi guppi test`: exit 0, 1943 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: exit 1, one line: `rules/rule-morph: status: a page with core: true that is draft`.
- Live pages (`ls`): decisions 550, rules 90, entities 5, estimates 356, lessons 66, insights 18; 11 files at the root of `vault/wiki/`. Files under `vault/archive/`: 3288 (`find -name "*.md"`).
