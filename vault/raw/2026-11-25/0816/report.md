The librarian's run for session 0816 (2026-11-25) is committed as 034128dc, `docs(vault): librarian, 2026-11-25`. The tree is clean after the commit. `guppi check` still exits 1 on one line: `lesson-plugin-install-writes-a-project-settings-file` has no `source` field.

**Pages created**
- decisions: 18 (`decision-case-1053`, `-1053.1`, `-1053.2`, `-1054`, `-1054.1`, `-1054.2`, `-1055`, `-1055.1` to `-1055.5`, `-1057`, `-1057.1` to `-1057.5`)
- estimates: 1 (`estimate-prespec-hook-reports-a-stop-before-the-render-it-tests`, `passed`)
- lessons: 2 (`lesson-plugin-install-writes-a-project-settings-file` and `lesson-plugin-copy-shipped-before-the-style-check`, both `new`)

**Pages updated**
- rules: 10
  - Changed by their Cases: `rule-spec-reconcile`, `rule-orchestration`, `rule-case-build`, `rule-sprint`, `rule-skill-sprint-close`.
  - `rule-prespec-hook` gained its new Estimate.
  - The cascade set `rule-git-context`, `rule-morph` and `rule-plugin-install` from `draft` to `built`, and `rule-sprint-close` from `built` to `draft`.
- estimates: 14. Nine are now `passed`. Five stay `pending`: orchestration-dispatches, case-build-settles, sprint-plugin-done-counts, frontierguard and sprint-close-takes.
- entities: 1 (`entity-sprint-plugin`: its Purpose and one Backlog line, by Case 1057.1)
- insights: 1 (`insight-workflow-code-live-before-the-page-it-reads`, from `open` to `actioned`, `addressed_by` `decision-case-1053.2`)
- decisions: 1 (`decision-case-949`, superseded by 1055.5)
- lessons: 1 (`lesson-case-build-puts-a-reading-before-the-render-it-tests`, archived by the cascade of that Insight)

**Marked entries**
- incomplete: line 32, `lesson-plugin-install-writes-a-project-settings-file`, `incomplete: [source]`.
- failed: none. unparsed: none.
- near: line 33, `lesson-plugin-copy-shipped-before-the-style-check`, `near: lesson-ship-leaves-an-empty-comment-after-a-removed-pointer`.

**Pages archived**
- `guppi cleanup` moved 2 pages into `vault/archive/plugin/2026-11-25/0816/`: `decisions/decision-case-949.md` and `lessons/lesson-case-build-puts-a-reading-before-the-render-it-tests.md`.
- `guppi archive` printed nothing and exited 0. It moved no unit and printed no "kept" line.
  - `raw/2026-11-25/0605` was not looked at, because it is dated the day of the run.
  - `raw/2026-11-25/0816` is the session of the run.

**Index check and synthesis**
- The one `create` entry is an Estimate, so no Grep ran for it.
- For the two lesson entries:
  - `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 71 lines. The harness saved them to a file, which I read.
  - `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 19 lines.
- Results:
  - `lesson-plugin-install-writes-a-project-settings-file`: no same or near page, not clustered.
  - `lesson-plugin-copy-shipped-before-the-style-check`: marked `near` (see Pages opened), not clustered.
  - The synthesis added 0 entries.

**Pages opened**
- `vault/wiki/lessons/lesson-ship-leaves-an-empty-comment-after-a-removed-pointer.md`, because its index line did not settle same, near or shared cause for `lesson-plugin-copy-shipped-before-the-style-check`.
  - Outcome: near, not the same and not clustered.
  - That page's defect comes from the cleaning that `ship` does. The new lesson's defect comes from source code that no `guppi style` run checked before the copy was written at a Work Mode stop. The two share only the missing style run over the copy.

**Ledger read**
- I read `vault/raw/2026-11-25/0816/ledger.md` with `wc -l` (33 lines) and a print of line 24.
- The yaml covers every line: 32 entries plus line 24, folded into the entry of line 4.

**Flags**
- `guppi check` exits 1 with that one line: `lessons/lesson-plugin-install-writes-a-project-settings-file: schema: missing field source (given {'kind': 'knowledge'})`.
- `guppi materialize` printed 33 entries for 0816. The yaml holds 32 under `entries`, plus line 24 folded into the entry of line 4.
- The archived Spec `vault/archive/plugin/2026-11-20/1353/raw/spec.md` still has an unticked `read` box at line 224 for `estimate-plugin-install-asks-one-approval-in-plan-mode`, which this run read `passed`.
- Read outside the frame: a Grep of the unticked lines of `vault/archive/plugin/2026-11-20/1353/raw/spec.md` for Readings due. The handoff did not ask for it.
- `generate`, `cleanup`, `render`, `sprint`, `backlog`, `glossary` and `archive` printed nothing on stderr.

**Handoff instructions**
- Case 1055.5 retires Case 949: done. `log.md` shows the defer by `decision-case-949` superseded and not applied, and cleanup archived that decision.
- The second form of Cases 1053 and 1057 stands: the yaml carries one form of each.
- For the five install Estimates, `log.md` shows each `method` update before its reading.
- `sprint.md` was rendered after `entity-sprint-plugin` changed. The frontierguard line is now `- [ ] … · pending`.
- The handoff asked for no repair and no read that needs a flag.
- No hook refused a call.

**Lint total:** 1 line (`guppi check`, exit 1).

The brief is in `c:\PROJECTS\GUPPI\vault\wiki\brief.md`; the yaml with the `near` mark is `c:\PROJECTS\GUPPI\vault\raw\2026-11-25\0816\materialize.yaml`.
