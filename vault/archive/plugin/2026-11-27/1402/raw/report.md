Librarian report for 2026-11-27, session 1402. Commit def97898 `docs(vault): librarian, 2026-11-27`. The tree is clean after the commit.

**Pages created, by category** (`git status`, `log.md`)
- decisions: 13 — `decision-case-1082`, `1084`, `1085`, `1085.1` to `1085.9`, `1086`. `guppi cleanup` then moved `decision-case-1082`, which is superseded, to `vault/archive/plugin/2026-11-27/1402/decisions/`.
- estimates: 5
  - `passed`: `estimate-spec-write-rebuilds-the-maps-of-the-spec`, `estimate-spec-write-map-follows-the-ticks-of-the-scripts`, `estimate-sprint-plugin-edit-takes-a-file-a-hook-changed`, `estimate-sprint-plugin-first-sketch-picture-is-small`.
  - `pending`: `estimate-spec-write-shows-the-boxes-in-the-plan-file`.
- lessons: 2 — `lesson-code-mode-not-taken-up` and `lesson-work-mode-style-check-skipped-at-a-repeated-stop`, both `new`.

**Pages updated, by category**
- entities: 2 — `entity-guppi-repository` (the cascade set it draft → built) and `entity-sprint-plugin`.
- estimates: 7 — `estimate-work-mode-runs-the-style-check-before-a-stop`, `estimate-guppi-repository-readme-shows-the-first-sketch`, `estimate-spec-write-writes-the-map`, `estimate-generate-ticks-the-spec`, `estimate-render-harness-ticks-the-spec`, `estimate-sprint-ticks-the-spec`, `estimate-glossary-ticks-the-spec`.
- rules: 7
  - by their entries: `rule-work-mode`, `rule-spec-write`, `rule-hook-registry`, `rule-spec-capture`.
  - by the cascade, built → draft: `rule-glossary`, `rule-render-harness`, `rule-sprint`.

**Entries marked incomplete or failed**
- `incomplete`: ledger line 3, the `create` of `estimate-sprint-plugin-first-sketch-picture-is-small` by Case 1082, lacks `criterion`. It carries `superseded_by: ['1086']` and was not applied.
- `failed`: none. `unparsed: []`.

**Pages archived**
- `guppi cleanup` moved 1 page, `decision-case-1082`.
- `guppi archive` printed no line on stdout or stderr and exited 0. It moved no unit and kept none with a reason. The code looks only at units dated before the day of the run, so `raw/2026-11-27/0947` (dated today) was not looked at. `raw/2026-11-27/1402` is the session of the run.

**Flags raised**
- `near`: the entry of `lesson-work-mode-style-check-skipped-at-a-repeated-stop` now carries `near: lesson-plugin-copy-shipped-before-the-style-check`. They are not clustered.
- The handoff does not match the disk on one point. Its last librarian instruction says the first tick of `vault/raw/2026-11-27/0947/spec.md` rewrites its map into the new form. That Spec holds no map: a grep for `Map of the Cases` printed nothing. This run changed only its line 73, a `read` line ticked.
- Handoff observation 38 asks the librarian to judge the return of Case 1085 with 1085.9 against `estimate-orchestration-leaves-the-number-to-case-guppi`. That is a reading, not a step of this run, so I did not do it. The brief puts that Estimate under Next session, Work, with that event and the replacement of 1082 by 1086.
- The brief also lists handoff observations: the pillow uninstall in the root environment, the Edit-after-rewrite note, and the readme reading that stands.
- Reads beyond the frame, each a flag in the brief:
  - a grep for `Map of the Cases|✅` and `^# ` over the 0947 Spec, and `^# ` over the 1402 Spec, for the handoff's last instruction (the handoff asked for this check);
  - a grep for `sprint-close` over the 1402 Spec, for step 2;
  - a grep over both Specs for task lines opening with a code span holding `guppi sprint`, `guppi glossary` or `guppi render`, for the Readings due facts of the three ticks-the-spec Estimates.
- No hook refused a call. No stderr line from generate, cleanup, render, sprint, backlog, glossary or archive. No MOC candidate, stale defer or contradiction.

**Lint total**
- `guppi check` exited 0 with no line, both before the brief and at the close.

**Other parts the frame sends to the report**
- Handoff instructions:
  - (1) Only the line of 1086 applied for the first-sketch Estimate; the 1082 line is `superseded_by`.
  - (2) Before `generate`, a Grep of the 1085.2 `old` text over `vault/wiki/rules/rule-hook-registry.md` counted 1 hit. `guppi render` then wrote the `guppi ratified --boxes` `PostToolUse` entry into `.claude/settings.json`.
  - (3) `rule-spec-write` keeps `deferred_by: decision-case-1081`.
  - (4) The lesson was compared as asked; see below.
  - (5) is the flag above.
  - No instruction asked to repair an entry.
- Index check and synthesis. I ran two Greps; they served both steps:
  - `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 73 lines. The output was too long to show, so the harness saved it to a file, and I read that file.
  - `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 19 lines.
  - Every `create` was an Estimate, so there was nothing to compare across creates. No merge.
  - `lesson-code-mode-not-taken-up`: no pair; no lesson or Insight speaks of Code Mode.
  - `lesson-work-mode-style-check-skipped-at-a-repeated-stop`: no pair. I added `near` (above).
- Page opened: `vault/wiki/lessons/lesson-plugin-copy-shipped-before-the-style-check.md`, for the synthesis and the handoff's instruction to compare.
  - A Grep for `1061|guppi style` over `vault/wiki/lessons/` printed only this page.
  - Outcome: not clustered. Its cause is that Work Mode ran no style check before a stop. The new lesson's cause is that the agent read the existing step as due once per `stop:` task.
  - It is near, so the yaml entry carries `near` and the brief reports it.
- Ledger read: `vault/raw/2026-11-27/1402/ledger.md` has 26 lines (`wc -l`). The yaml holds 22 entries for lines 1–20, 23 and 26; lines 21, 22, 24 and 25 are folded. So every line is accounted for, and only line 3 was not applied (superseded by 1086). `guppi materialize` printed "written with 26 entries".
- Scripts' own file read: `.guppi/guppi/archive.py`, for the reason the archive printed nothing.

Files:
- c:\PROJECTS\GUPPI\vault\wiki\brief.md
- c:\PROJECTS\GUPPI\vault\raw\2026-11-27\1402\materialize.yaml
