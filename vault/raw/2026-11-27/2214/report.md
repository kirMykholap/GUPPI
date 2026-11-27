Librarian report: session 2214, 2026-11-27 (run on 2026-11-28). Commit d4537e12 `docs(vault): librarian, 2026-11-27`. The tree is clean after the commit.

**Pages created** (`git status`, `log.md`)
- decisions: 16 (`decision-case-1087`, `1087.1` to `1087.14`, `1088`)
- estimates: 1 (`estimate-spec-write-readers-take-the-cases-file`, `pending`)

**Pages updated**
- estimates: 18
  - 16 moved to `passed` by readings: ledger lines 1–5 and 30–40.
  - `estimate-spec-capture-appends` and `estimate-compact-recall-reloads` moved to `pending`, each with a new Criterion.
- rules: 11
  - 7 by their entries: `rule-spec-write`, `rule-skill-approve-spec`, `rule-orchestration` (pairs of 1087.3 and then 1088, in ledger order), `rule-case-protocol`, `rule-spec-capture`, `rule-prespec-hook`, `rule-prespec`.
  - 4 by the cascade alone:
    - `rule-compact-recall` went `built → draft`.
    - `rule-glossary`, `rule-render-harness` and `rule-sprint` went `draft → built`.
    - `rule-spec-capture`, one of the 7 above, also went `built → draft`.
- entities: 1 (`entity-glossary`)
- insights: 1 (`insight-orchestration-frontier-closer-leaves-the-box-open`): now `actioned`, `addressed_by: [[decision-case-1088]]`, `severity` 1 → 0.

**Entries marked incomplete or failed:** none.
- 40 entries plus 16 decision records, all `applied`, which is 56 marks.
- `unparsed: []`. No `exists`, `near`, `librarian` or `merged` marks.

**Pages archived**
- `guppi cleanup` moved 2 pages to `vault/archive/plugin/2026-11-28/2214/`:
  - `decision-case-1081`, superseded by `decision-case-1087.1`. This cleared the `deferred_by` of `rule-spec-write`, and the page left `backlog.md`.
  - `lesson-frontier-line-closed-in-two-edits`, because its Insight is now actioned.
- `guppi archive` moved 2 units and kept 1:
  - Moved `raw/2026-11-27/0947` to `archive/plugin/2026-11-27/0947/raw`.
  - Moved `raw/2026-11-27/1402` to `archive/plugin/2026-11-27/1402/raw`.
  - Kept `raw/2026-11-27/2214`, because it is the session of the run.
  - No line on stderr. No `pending` Estimate's `method` names the archive step.

**Index check:** no Grep was run. The only `create`, `estimate-spec-write-readers-take-the-cases-file`, is an Estimate and has no index. Nothing was merged and nothing was marked near.

**Synthesis:** the yaml has no `lesson` entry, so I added no entries. For the brief:
- `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 76 lines.
- `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 19 lines.

**Pages opened** to judge a duplicate, a shared root cause or a script error: none.

**The one ledger read:** `wc -l` gives 40 lines for `vault/raw/2026-11-27/2214/ledger.md`, plus one view of the first 110 characters of each line. Every line has its own entry (lines 1–40), so none is unaccounted for.

**Handoff instructions:**
- All five were carried out by the scripts and checked against `log.md` and `git diff`.
- None asked for a repair, so none was refused. No hook refused a call.

**Flags raised**
- No line on stderr from any of: materialize, generate, cleanup, render, sprint, backlog, glossary, archive.
- No unticked Spec line holds `guppi sprint-close --apply`, so no close ran.
- Four handoff observations went into the brief's Flags:
  - `is_plan_file` treats the Cases file as a plan file. A `tool Write:` line in the event log would make `plan_path` name it as the plan. This has not happened.
  - An empty Cases file is never removed.
  - The map of this session's plan file names a Cases file that does not exist for this session.
  - `frontierguard` refused the first edit of the C2 line. Case 1088 addresses this.
- Reads beyond the frame:
  - A `grep` for `- \[ \]` over the three Specs also printed lines of Case text that hold `- [ ]` (2214: 2 lines; 1402: 5; 0947: 7). Needed for Readings due and Next session.
  - A `grep` for `stop:` over the 2214 Spec, filtered to task lines, printed nothing. Needed for Readings due: whether the event of `estimate-work-mode-runs-the-style-check-before-a-stop` happened in this session.
- Brief:
  - 30 Estimates are `pending` and 0 are `failed`.
  - Next session has one Cases line, from For the next session: the live check of Case 1087 and `estimate-spec-write-shows-the-boxes-in-the-plan-file`.
  - It has one Work line: `estimate-spec-write-readers-take-the-cases-file`, whose event is this run's render of `.claude/skills/pre-spec/SKILL.md`.
  - Ask the person: none.
  - No Debt line led to a proposal to defer. `estimate-spec-capture-appends` and `estimate-compact-recall-reloads` both wait for events that have not happened yet.

**Lint total:** `guppi check` exit 0, 0 lines, both before and after the brief.

The brief is at c:\PROJECTS\GUPPI\vault\wiki\brief.md and the yaml at c:\PROJECTS\GUPPI\vault\raw\2026-11-27\2214\materialize.yaml.
