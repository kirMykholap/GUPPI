The librarian's run for session 2003 (2026-11-25) is finished and committed as ab917b63 `docs(vault): librarian, 2026-11-25`. Every script exited 0 and printed no error line. `guppi check` exits 0 with no finding, and the tree is clean after the commit. One thing came out other than the handoff expected: `backlog.md` still holds 10 items, not 9.

**Pages created per category**
- decisions: 8 (`decision-case-1058`, `-1059`, `-1060`, `-1061`, `-1063`, `-1063.1`, `-1063.2`, `-1063.3`). `decision-case-1060` is superseded by 1063.1 and was archived, so 7 are live.
- estimates: 3.
  - `estimate-sprint-plugin-uv-build-range-holds-the-uv-of-the-machine` is `passed`.
  - `estimate-work-mode-runs-the-style-check-before-a-stop` is `pending`.
  - `estimate-sprint-plugin-passed-one-off-estimate-is-not-read-again` is `pending`.
- lessons: 1 (`lesson-orchestration-case-built-again-in-another-shape-under-its-old-number`, `new`).

**Pages updated per category**
- rules: 6.
  - `rule-work-mode` (case 1061), which the cascade then set `built` → `draft`.
  - `rule-case-protocol`, `rule-case-build`, `rule-prespec`, `rule-estimates-schema` (case 1063.1).
  - `rule-skill-merge-main` (case 1063.3).
- estimates: 2.
  - `estimate-case-protocol-case-form`: Criterion replaced whole, then `pending → passed` by ledger line L21.
  - `estimate-skill-merge-main-joins-a-conflicted-page`: Criterion replaced whole, stays `pending`.
- entities: 1 (`entity-sprint-plugin`).
- lessons: 1 (`lesson-plugin-install-writes-a-project-settings-file`, `source` set).

**Entries marked incomplete or failed**
- Ledger line 8 is the case 1060 `create` of `estimate-sprint-plugin-passed-one-off-estimate-is-not-read-again`. It carries `incomplete: [criterion]`. It is superseded and was not applied; the page was written from line 16, Criterion included.
- No entry is marked `failed`, `exists`, `near` or `unparsed`.

**Pages archived**
- `guppi cleanup` moved `decision-case-1060` to `vault/archive/plugin/2026-11-26/2003/decisions/`.
- `guppi archive` moved these units:
  - `raw/2026-11-25/0605` → `archive/plugin/2026-11-25/0605/raw`.
  - `raw/2026-11-25/0816` → `archive/plugin/2026-11-25/0816/raw`.
- It kept `raw/2026-11-25/2003`, the session of the run.
- `raw/2026-10-14/1907` stays because it has no `ledger.md`, so it is not a unit (docstring of `.guppi/guppi/archive.py`).

**Index check and synthesis**
- No Grep ran for the four `create` entries: all are Estimates.
- For the lesson entry:
  - `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 72 lines. The harness saved that output to a file and I read it.
  - `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 19 lines.
- I opened `vault/wiki/insights/insight-case-build-opens-a-new-case-where-one-was-named.md`, because its index line did not settle whether it shares the lesson's root cause (the handoff asked me to check the lesson against Cases built again).
  - Outcome: not clustered.
  - The Insight names `case-guppi` putting a new number where the main agent named a Case.
  - The lesson names `orchestration.md` lacking the new-number rule of `case-schema.md`, so the main agent sent a correct rebuild back. That is another agent and the other direction.
- No yaml edit and no synthesis entry.

**Ledger read**
- I read `vault/raw/2026-11-25/2003/ledger.md` once for the `Work` line: 22 lines.
- The yaml holds 21 entries for lines 1–19, 21 and 22. Line 20 is folded into the entry of line 2 and shows in `log.md` as applied, so every line is accounted for.

**Handoff instructions**
- Case 1060's decision lines (L3–L8) were not applied, and `decision-case-1060` stands superseded by 1063.1.
- Line C4 of `frontier.md` closes `· case 1063`.
- The `guppi check` line on the settings lesson no longer prints.
- The 1063.2 update was applied before the L21 `passed` reading.
- The render wrote the six files the handoff named.
- The lesson was checked against the lessons and Insights on rebuilt Cases.
- The expected one-item drop in `guppi backlog` did not happen (first flag below).

**Flags raised**
- **Backlog count:** `guppi backlog` holds 10 items before and after.
  - The Backlog line of case 1057.1 left, but `rule-work-mode` came in as `put off in 31 sessions`.
  - The cascade set `rule-work-mode` to `draft` for its new `pending` Estimate. The `## Backlog` of the archived `entity-sprint-migration` names it, and `guppi backlog` drops such a line of a closed sprint only when its page is finished (`finished` in `.guppi/guppi/backlog.py`, case 743.4).
  - This is also a line under Cases of Next session.
- **Materialize count:** `guppi materialize` printed `22 entries`, but the yaml holds 21 under `entries`.
- **Double log line:** `log.md` holds two `decision-case-1060 archived` lines, one from `generate` and one from `cleanup`.
- **Handoff observations carried into the brief:**
  - The `guppi prespec --check` notes on two Criterion lines.
  - The `ask-guppi` run had no web tool for the uv docs claims of Case 1059.
  - `cases/case-1062.md` stands empty.
- **Reads outside the frame:**
  - `spec.md` read whole, for Readings due and Next session. The handoff did not ask for it.
  - A `grep -l` of `rule-work-mode` over archived `entity-sprint-*.md`, to explain the backlog count the handoff expected. The handoff did not ask for the read.
- No hook refused a call.
- No MOC candidate, no stale defer and no contradiction.

**Lint total:** `guppi check` exits 0 with 0 lines.

The rewritten brief is at `c:\PROJECTS\GUPPI\vault\wiki\brief.md`, and the yaml is at `c:\PROJECTS\GUPPI\vault\raw\2026-11-25\2003\materialize.yaml`.
