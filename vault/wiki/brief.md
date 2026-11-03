# Brief — 2026-11-03, librarian of session 1825 (2026-11-03)

## Where things stand

- Session 1825 of the sprint `plugin`. Cases ratified: 1019 (1019.1–1019.4), 1020, 1021 (short-form defer) (handoff).
- Code and tests: `plugin/assets/icon_guppi.png` and `plugin/assets/logo_guppi.png` moved from `guppi-assets/` by `git mv`, `guppi-assets/` removed; `.guppi/tests/test_ship.py` gains three tests whose names hold `source_pictures`. `guppi test` 1946 passed, 6 skipped, 1 deselected; `guppi style` clean (handoff).
- Readings: L1, L2 at `/hi` (`estimate-skill-sprint-open-asks-the-opening-questions`, `estimate-clean-branch-refuses-a-draft-core-page`), L12–L15 at Retro (`estimate-hi-takes-its-readings`, `estimate-case-build-reads-the-readers-of-a-new-files-folder`, `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`, `estimate-clean-branch-leaves-out-the-source-pictures`), all `passed`. No lesson (handoff).
- `guppi materialize` printed `written with 15 entries` for `vault/raw/2026-11-03/1825/materialize.yaml` and `extended with 0 entries` for the yaml of 0316. The ledger has 15 lines (`grep -c`). The yaml holds entries for lines 1–13; lines 14 and 15 are folded into the `create` entries of lines 6 and 9, so every line is accounted for; `unparsed: []`.
- The yaml holds 13 entries under `entries`: 6 `update`, 2 `create` (both estimates), 1 `defer` (line 10, `entity-sprint-plugin`, marked `exists` by materialize), 4 `estimate` (lines 1, 2, 12, 13); `decisions` holds 7 items.
- Index check: the two creates are Estimates, so no Grep ran. Synthesis: the yaml holds no `lesson` entry, so no Grep ran and no entry was added.
- Marks: every entry carries `applied`; line 10 carries `exists`; no entry `failed`, `incomplete`, `near`, `librarian` or `merged`.
- `guppi generate` printed 18 pages written or changed for 1825, 0 for 0316, nothing on stderr. No unticked Spec line holds `guppi sprint-close --apply`. `guppi cleanup` printed `0 page(s) moved`. `guppi render`, `sprint`, `backlog` and `glossary` printed nothing on stderr. The render changed `.claude/skills/hi/SKILL.md` alone of its files (`git status`).
- Pages created (9), from `git status`: decisions 7 (`decision-case-1019`, `decision-case-1019.1` to `decision-case-1019.4`, `decision-case-1020`, `decision-case-1021`); estimates 2 (`estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`, `once: true`, `passed`; `estimate-clean-branch-leaves-out-the-source-pictures`, `passed`).
- Pages updated (9), from `git status`: rules 4 (`rule-skill-hi` by 1019.1; `rule-raw-archive` by 1019.1; `rule-clean-branch` by 1020, `draft` → `built` by the cascade; `rule-skill-sprint-open`, `draft` → `built` by the cascade); estimates 4 (`estimate-hi-takes-its-readings` by 1019.1, then `passed` by L12; `estimate-case-build-reads-the-readers-of-a-new-files-folder` by 1019.2, then `passed` by L13; `estimate-skill-sprint-open-asks-the-opening-questions` and `estimate-clean-branch-refuses-a-draft-core-page`, `passed` by L1 and L2); entities 1 (`entity-sprint-plugin`: Estimate added by 1019.3, `## Backlog` line by 1019.4, `deferred_by: ["[[decision-case-1021]]"]` by 1021).
- The direct instructions of the handoff, as the pages stand: before `generate`, each `old` text of the two `replace` pairs of 1019.1 on `rule-skill-hi` matched the page once (Grep counts 1 and 1); after the render, `.claude/skills/hi/SKILL.md` holds the new W step (the transcript found by the stamp of `spec.md`, read in parts) and "that you do not open that chat (as set in cases 921 and 1019.1)", and no "read no transcript of an earlier session". `rule-clean-branch` holds `plugin/assets` in `implementation_ref`; `plugin/assets/` holds `icon_guppi.png` and `logo_guppi.png`. `entity-sprint-plugin` holds both the Backlog line of 1019.4 and the defer of 1021. `rule-raw-archive` holds the new Purpose sentence of 1019.1.
- `guppi sprint`: the milestone The clean branch now stands `[x]`; The plugin stands `[ ]` with four items. `guppi backlog`: 15 items (13 before), `entity-sprint-plugin` and the Backlog line of 1019.4 added.
- `guppi archive` printed no line on stdout or stderr, exit 0, and moved nothing: it looks only at units dated before the day of the run, and both sessions of `raw/` with a ledger, 0316 and 1825, are dated 2026-11-03; `vault/raw/2026-10-14/1907/` holds no `ledger.md`, so it is no unit.

Synthesis. No Grep ran: the yaml holds no `lesson` entry.

## Readings due

27 Estimates stand `pending`, none `failed`.

- `estimate-ask-query-before-a-create` — `rule-ask` (draft) — method: by hand, after the first build of `case-guppi` whose Case proposes a create without a ref, on the Render of `rule-ask` that runs every category.
- `estimate-ask-searches-at-prespec` — `rule-ask` (draft) — `- [ ] read` line 86 of `vault/raw/2026-11-03/0316/spec.md`; method: by hand, after the first `/pre-spec` whose `ask-guppi` runs on the Render of `rule-ask` that lets the searches cover the code, its transcript.
- `estimate-case-build-goes-on-after-a-live-compaction` — `rule-case-build` (draft) — method: by hand, after the first compaction of a `case-guppi` in a working session.
- `estimate-case-build-keeps-the-old-form-until-the-writer-is-live` — `rule-case-build` (draft) — method: by hand, after the first Case built under the Render that names a test over a live file.
- `estimate-case-build-reads-each-list-of-a-new-member` — `rule-case-build` (draft) — method: by hand, after the first build in a later session whose Case adds a member to a list spelled out one by one, its transcript.
- `estimate-case-build-runs-the-vault-query-first` — `rule-case-build` (draft) — method: by hand, after the first build whose Case proposes a create without a ref, its transcript.
- `estimate-case-build-searches-the-names-of-what-it-changes` — `rule-case-build` (draft) — method: by hand, after the `/pre-spec` of the first session in which the hook of `rule-case-check` sends the note that lists the files that name what a Case changes, the transcripts of each `case-guppi` of that session and its case file.
- `estimate-git-context-offers-git-init` — `rule-git-context` (draft) — `- [ ] read` line 763 of `vault/raw/2026-11-03/0316/spec.md`; method: by hand, after the librarian's run, an install from a `--allow-draft` copy into an empty folder that is no git repository, `/hi` typed three times. This run: the render wrote `.claude/skills/hi/SKILL.md`; no install is seen.
- `estimate-hi-writes-frontier` — `rule-skill-hi` (draft) — method: by hand, after the reply that acknowledges the opening Case of `/sprint-open` in the session after the close of a sprint, the person's answer.
- `estimate-morph-sets-up-the-project-at-the-first-hi` — `rule-morph` (draft) — `- [ ] read` line 536 of `vault/raw/2026-11-03/0316/spec.md`; method: by hand, after the session whose Work Mode builds `/setup`: an install into an empty git project from a `--allow-draft` copy, `/hi` typed.
- `estimate-morph-takes-in-the-set-aside-files` — `rule-morph` (draft) — `- [ ] read` line 571 of `vault/raw/2026-11-03/0316/spec.md`; method: by hand, after the session whose Work Mode builds `/setup` and its step in `/hi`: an install into a git project with files of its own from a `--allow-draft` copy.
- `estimate-orchestration-acknowledging-reply-opens-with-stop-after-prespec` — `rule-orchestration` (draft) — method: by hand, after an acknowledging reply after `/pre-spec` that waits for the person's word, its transcript.
- `estimate-orchestration-acknowledging-reply` — `rule-orchestration` (draft), `deferred_by` Case 1014 — `- [ ] read` line 677 of `vault/raw/2026-11-03/0316/spec.md`; method: by hand, after the librarian's render of the sentence on a term of the harness into `orchestration.md`, two acknowledging replies in their transcript; by hand, after the librarian's run of the session that replaces this Criterion and a setup Case ratified in a new install. This run: the render left `vault/wiki/orchestration.md` unchanged; no setup Case in a new install is seen.
- `estimate-orchestration-signs-items-taken-together` — `rule-orchestration` (draft) — method: by hand, after the first batch taken up together in Plan Mode in which a summary carries a line Other Case naming a Case of the session.
- `estimate-plugin-install-sets-aside-the-files-of-the-project` — `rule-plugin-install` (draft), `deferred_by` Case 949 — method: by hand, after the librarian's run of the session that set this Criterion, installs from a `--allow-draft` copy. This run wrote no file of it.
- `estimate-prespec-finds-a-reader-of-a-new-files-folder` — `rule-prespec` (draft) — `- [ ] read` line 124 of `vault/raw/2026-11-03/0316/spec.md`; method: by hand, after the first `/pre-spec` on the new Render whose plan adds a file that is no page, its transcript.
- `estimate-retro-loads-on-a-red-command` — `rule-retro` (draft), `deferred_by` Case 1007 — method: by hand, after the librarian's render that writes `.claude/skills/retro/SKILL.md` with `--exit-zero`, and the first load of `/retro` after it. This run: the render left `.claude/skills/retro/SKILL.md` unchanged.
- `estimate-skill-merge-main-joins-a-conflicted-page` — `rule-skill-merge-main` (draft) — method: by hand, after the first `/merge-main` that leaves a conflicted page.
- `estimate-skill-pr-review-takes-a-pull-request-whole` — `rule-skill-pr-review` (draft) — method: by hand, after the first pull request from another account merged by `/pr-review` after the close of `plugin`.
- `estimate-sprint-plugin-close-steps-run-from-the-line` — `entity-sprint-plugin` (draft) — method: by hand, at the end of Work Mode of the session that closes `entity-sprint-plugin`.
- `estimate-sprint-plugin-installs-as-a-plugin` — `entity-sprint-plugin` (draft) — method: by hand, in a session of the sprint `plugin` before its close, an install from a `--allow-draft` copy into an empty project.
- `estimate-sprint-plugin-lesson-root-cause-holds-no-bare-link` — `entity-sprint-plugin` (draft) — method: by hand, after the librarian's run that applies the update of `lesson-ledger-reading-writes-a-bare-wikilink`. This run applied no update of that lesson.
- `estimate-sprint-plugin-link-graph-is-gone` — `entity-sprint-plugin` (draft) — method: by hand, after the librarian's run that applies the delete of `entity-link-graph`. This run applied no delete.
- `estimate-sprint-plugin-pull-requests-reviewed-on-github` — `entity-sprint-plugin` (draft) — method: by hand, a pull request from a second account read on GitHub, before the close of the sprint.
- `estimate-sprint-plugin-readme-describes-the-project` — `entity-sprint-plugin` (draft) — method: by hand, the person's answer on `README.md` at the `/hi` of the session after the one whose Work Mode writes it, before the close of the sprint.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` (draft), `deferred_by` Case 1009 — method: by hand, after a librarian's run that puts a lesson with `addressed_by` under an Insight that stands `actioned`. This run: the yaml held no `lesson` entry and the synthesis added no entry.
- `estimate-work-mode-runs-the-spec-on-a-branch-from-a-baseline` — `rule-work-mode` (draft), `deferred_by` Case 1008 — method: by hand, after the librarian's render that writes `.claude/skills/work/SKILL.md` with `--exit-zero`, and the first `/work` after it. This run: the render left `.claude/skills/work/SKILL.md` unchanged.

## Flags

- No entry `incomplete`, `failed`, `near` or `unparsed`. No failed Estimate.
- Lint (`guppi check`, 1 line): `rules/rule-morph: status: a page with core: true that is draft`. The handoff names it the baseline line that Case 1017.8 intends.
- `vault/wiki/sprint.md` now marks the milestone The clean branch `[x]`: `rule-clean-branch` went `draft` → `built` by the cascade once `estimate-clean-branch-leaves-out-the-source-pictures` passed (L15), and `estimate-sprint-plugin-ci-writes-a-clean-branch` stands `passed`. The handoff says the person put off C1, the clean branch, with the milestone The plugin (Case 1021). The line of `## For the next session` carries the clean branch.
- `rule-skill-sprint-open` went `draft` → `built` by the cascade once `estimate-skill-sprint-open-asks-the-opening-questions` passed (L1).
- `entity-sprint-plugin` carries `deferred_by: ["[[decision-case-1021]]"]` and stands first under `## Deferred` of `backlog.md`; it is still the live sprint page, and `guppi sprint` wrote `sprint.md` from it.
- The `old` text of the `replace` of 1019.1 on `rule-raw-archive` spans a line break of the page; a Grep of it on one line counted 0 before `generate`. `generate` applied it with no line on stderr, and the page holds the new sentence.
- `guppi generate` ticked the `read` boxes of `estimate-skill-sprint-open-asks-the-opening-questions` (line 618) and `estimate-clean-branch-refuses-a-draft-core-page` (line 720) in `vault/raw/2026-11-03/0316/spec.md`, and all 13 boxes of `vault/raw/2026-11-03/1825/spec.md`.
- Handoff note: `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` passed on one judgment of the agent: the root `.gitignore` is not an ignore file of a folder that holds `.guppi/guppi/frontierguard.py` or `.guppi/tests/test_frontierguard.py`; `git check-ignore` printed neither file.
- Handoff observation: `ask-guppi` at `/pre-spec`, by its own report, ran Globs and Greps over `vault/archive/` that were not by slug, and Globs and a count Grep under `~/.claude/projects/`; findings 1 and 2 rest partly on them.
- Handoff observation: the hook `guppi frontierguard` of Case 1012 refused an edit that appended the closer to C4 of `frontier.md` and left the box `[ ]`; the edit of the whole line then passed.
- No MOC candidate, no stale defer and no contradiction printed by `guppi check`, `guppi backlog` or this run.
- Read beyond the frame: a Grep for `sprint-close` over `vault/raw/2026-11-03/1825/spec.md` printed line 16, a paragraph of a Case context that is no unticked line; step 2 needed it, to look for a task line that runs `guppi sprint-close --apply`. The handoff did not ask for it.

## Next session

Cases
- The milestone The plugin and the clean branch, put off by Case 1021 and C1: the three readings by install and the install reading of the sprint can be taken in one session that prepares the copy and three folders (handoff).
- Whether the root `.gitignore` counts as an ignore file of a folder that holds the new files for `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`, which passed on the agent's judgment that it does not; the person may judge otherwise (handoff).
- Defer `estimate-morph-sets-up-the-project-at-the-first-hi` into `backlog.md`: its session did not take its reading, which waits for an install by hand from a `--allow-draft` copy (handoff Debt).
- Defer `estimate-morph-takes-in-the-set-aside-files` into `backlog.md`: its session did not take its reading, which waits for an install by hand into a git project with files of its own (handoff Debt).
- Defer `estimate-git-context-offers-git-init` into `backlog.md`: its session did not take its reading, which waits for an install by hand into an empty folder with no git (handoff Debt).

Work
- `estimate-ask-searches-at-prespec` (its `read` box, line 86 of `vault/raw/2026-11-03/0316/spec.md`)
- `estimate-prespec-finds-a-reader-of-a-new-files-folder` (its `read` box, line 124 of `vault/raw/2026-11-03/0316/spec.md`)
- `estimate-case-build-searches-the-names-of-what-it-changes`

Ask the person
- none

## Readings at the close

- `uv run --project .guppi guppi test`: exit 0, 1946 passed, 6 skipped, 1 deselected.
- `uv run --project .guppi guppi check`: exit 1, one line: `rules/rule-morph: status: a page with core: true that is draft`.
- Live pages (`ls`): decisions 557, rules 90, entities 5, estimates 358, lessons 66, insights 18; 11 files at the root of `vault/wiki/`. Files under `vault/archive/`: 3300 (`find -name "*.md"`), the same before and after `guppi archive`.
