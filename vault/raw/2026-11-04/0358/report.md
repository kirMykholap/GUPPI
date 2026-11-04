Librarian report: 2026-11-04, session 0358

The run is done and committed as `82eede72` ("docs(vault): librarian, 2026-11-04"). After the commit `git status` is clean, so no file the render wrote is left modified or untracked. `guppi check` exits 1 with 9 lint lines, listed under Lint below.

**Pages created (22)**
- decisions: 16. `decision-case-1022`, `-1023`, `-1024`, `-1025`, `-1025.1`, `-1025.2`, `-1026`, `-1026.1` to `-1026.5`, `-1027`, `-1028`, `-1028.1`, `-1028.2`. Four of them (1022, 1023, 1024, 1027) were superseded and went to the archive in the same run.
- estimates: 2. `estimate-clean-branch-names-a-pointer-at-the-write` and `estimate-clean-branch-ships-no-code-write-hook`, both `passed`.
- lessons: 4, all `new`. `lesson-hooks-relative-project-path-fails-after-a-cd`, `lesson-ship-leaves-an-empty-comment-after-a-removed-pointer`, `lesson-plugin-install-leaves-pycache-untracked`, `lesson-git-context-plan-mode-blocks-git-init`.

**Pages updated (16)**
- estimates: 10.
  - Now `failed`: `estimate-ask-searches-at-prespec`, `estimate-case-build-searches-the-names-of-what-it-changes`, `estimate-morph-sets-up-the-project-at-the-first-hi`, `estimate-git-context-offers-git-init`, and `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers` (failed by case 1025.1).
  - Now `passed`: `estimate-prespec-finds-a-reader-of-a-new-files-folder`, `estimate-case-build-reads-the-readers-of-a-new-files-folder`, `estimate-morph-takes-in-the-set-aside-files`, `estimate-sprint-plugin-installs-as-a-plugin`, `estimate-orchestration-acknowledging-reply`.
- rules: 4. `rule-case-build`, `rule-clean-branch` (both 1028.1 and 1028.2 applied, as the handoff asked), `rule-hook-registry`, and `rule-prespec`, which went `draft` → `built` by the cascade.
- insights: 1. `insight-ship-live-code-writes-a-case-number-outside-a-bracket` is now `actioned` by `decision-case-1028.1`.
- decisions: 1. `decision-case-1014` was superseded by 1026.5, then archived.

**Entries marked incomplete or failed**
- Incomplete: line 15 of the yaml, the `create` of `estimate-clean-branch-names-a-pointer-at-the-write` by case 1027, lacks `criterion`. It is superseded by 1028.1 and was not applied. The page stands from the `create` of 1028.1.
- Failed: none.

**Pages archived**
- `guppi cleanup` moved 7 pages into `vault/archive/plugin/2026-11-04/0358/`: `decision-case-1014`, `-1022`, `-1023`, `-1024`, `-1027` (superseded), and `lesson-ship-docstring-sample-writes-a-real-case-number` and `lesson-ship-test-comment-writes-a-bare-case-reference` (their Insight was actioned).
- `guppi archive` moved two units and printed nothing on stderr:
  - `raw/2026-11-03/0316 → archive/plugin/2026-11-03/0316/raw`
  - `raw/2026-11-03/1825 → archive/plugin/2026-11-03/1825/raw`
- It kept `raw/2026-11-04/0358`, the session of this run. `vault/raw/2026-10-14/1907/` holds no `ledger.md`, so it is no unit.

**Index check and synthesis**
- Index check: the three `create` entries are all Estimates, so no Grep ran for them.
- Synthesis, two Greps:
  - `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 66 lines. The harness saved the output to a file because it was too long, and I read that file. Three lines were too long to show; their file names are not related to the four new lessons.
  - `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 19 lines.
- None of the four lessons shares a root cause with a lesson or an Insight, so no entry was added and no yaml edit was made.
- No page was opened for the index check, the synthesis or a script error.

**Handoff instructions**
- The handoff asked me to check the ledger for the four lessons, which the ledger hook had held twice. They stand at lines 33 to 36. Those four lines were in the working tree but not in the session commit; this run's commit carries them.
- No repair of an entry was asked.

**Ledger read (the one read for the Work line)**
- `wc -l` and a print of `vault/raw/2026-11-04/0358/ledger.md`: 36 lines.
- The yaml holds 34 entries (lines 1 to 30 and 33 to 36). Lines 31 and 32 are folded into the `create` entries of lines 19 and 23.
- 27 entries are `applied`. 7 are superseded and not applied: lines 4 to 6 (the defers of 1022 to 1024) and lines 15 to 18 (case 1027).
- No ledger line is left to apply. `unparsed: []`.

**Flags raised**
- No script printed a line on stderr: materialize, generate, cleanup, render, sprint, backlog, glossary and archive.
- No unticked Spec line holds `guppi sprint-close --apply`.
- 5 failed Estimates. Three are in the brief's Cases: `estimate-git-context-offers-git-init` and `estimate-morph-sets-up-the-project-at-the-first-hi`, each with the handoff line that carries it, and `estimate-ask-searches-at-prespec`. The fourth Cases line is `estimate-case-build-searches-the-names-of-what-it-changes`. The fifth, the `once: true` sprint Estimate of the frontierguard build, stands in Readings due only.
- The handoff observations are flagged in the brief: the ledger hook holds a lesson twice; Work Mode stops on `main`; the setup Case asks about the split and the check; Cases were ratified twice after `/pre-spec`; `/guppi:install` asks for plan approval in Plan Mode; the trials cost 45 to 55 minutes.
- No MOC candidate, stale defer or contradiction.
- Two reads the frame says my job does not need:
  - `git diff -- vault/raw/2026-11-04/0358/ledger.md`, a second read of the ledger, for Where things stand (which lines were not in the session commit). The handoff did not ask for it.
  - `git diff -- vault/raw/2026-11-03/0316/materialize.yaml`, an earlier yaml, for Where things stand (what materialize changed there: `superseded_by` 1026.5). The handoff did not ask for it.

**Lint**
9 lines:
- `status: a page with core: true that is draft` on `rule-ask`, `rule-case-build`, `rule-git-context` and `rule-morph`.
- `unread: failed` on the five failed Estimates.

The brief is rewritten in full at `C:\PROJECTS\GUPPI\vault\wiki\brief.md`. The yaml of this run is `C:\PROJECTS\GUPPI\vault\raw\2026-11-04\0358\materialize.yaml`.
