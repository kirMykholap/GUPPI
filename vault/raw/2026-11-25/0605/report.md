I applied the 2026-11-25 materialize of session 0605 and committed it as 333a758e, `docs(vault): librarian, 2026-11-25`. No entry is `incomplete` or `failed`. `guppi check` exits 1 with 6 lines, the same total as before the session (the Baseline of the handoff); three of the lines name different pages, listed under Lint. The tree is clean after the commit.

**Pages created**
- decisions 10: `decision-case-1045`, `-1046`, `-1047`, `-1048`, `-1049`, `-1049.1`, `-1049.2`, `-1050`, `-1051`, `-1052`. `-1049.2` was archived in the same run.
- estimates 4:
  - `estimate-event-log-keeps-the-whole-path`, `estimate-clean-branch-ships-the-license` and `estimate-sprint-ticks-a-read-one-off-estimate` are `passed`; each had its reading folded in from ledger lines 21, 22 and 23.
  - `estimate-sprint-plugin-done-counts-a-one-off-reading` is `pending`.
- lessons 3: `lesson-case-build-numbers-a-new-case-from-the-case-files-alone` stays `new`. `lesson-case-build-puts-a-reading-before-the-render-it-tests` is `clustered`. `lesson-event-log-cuts-the-path-of-the-plan-file` was archived.
- insights 1: `insight-event-log-cuts-the-plan-path`, born `actioned` with `addressed_by: decision-case-1045`.

**Pages updated**
- rules 4: `rule-clean-branch`, `rule-event-log`, `rule-plugin-install`, `rule-sprint`.
- estimates 6: `estimate-orchestration-dispatches-case-guppi-at-a-level`, `estimate-case-build-writes-the-case`, `estimate-case-build-settles-form-by-itself`, `estimate-case-build-searches-the-names-of-what-it-changes`, `estimate-ask-searches-at-prespec`, `estimate-plugin-install-writes-guppi-into-an-empty-project`.
- entities 1: `entity-sprint-plugin`.
- insights 1: `insight-workflow-code-live-before-the-page-it-reads`, `actioned` → `open`.
- lessons 1: `lesson-gate-plan-path-cut-by-the-event-log-detail-limit`, archived.
- decisions 2: `decision-case-1037` and `decision-case-1038`, superseded and archived.

**Entries the scripts did not apply.** Yaml lines 12, 13 and 14 (Case 1049.2) carry `superseded_by: ['1052']`. This matches the handoff's instruction to apply nothing of 1049.2.

**Pages archived**
- `guppi cleanup` moved 5 pages into `vault/archive/plugin/2026-11-25/0605/`: `decision-case-1037`, `decision-case-1038`, `decision-case-1049.2`, `lesson-event-log-cuts-the-path-of-the-plan-file` and `lesson-gate-plan-path-cut-by-the-event-log-detail-limit`.
- `guppi archive` moved one unit, `raw/2026-11-20/1353 → archive/plugin/2026-11-20/1353/raw`.
- It kept `raw/2026-11-25/0605`, the session of this run. `vault/raw/2026-10-14/1907/` holds no `ledger.md`, so it is no unit.
- No script printed anything on stderr.

**Index check.** All four `create` entries are Estimates, so no category Grep ran for them.

**Synthesis**
- My two Greps: `^(root_cause|deferred_by):` over `vault/wiki/lessons/` printed 70 lines, and `^(pattern|deferred_by):` over `vault/wiki/insights/` printed 18. The lessons output was long, so the harness saved it to a file, and I read that file.
- I added 6 entries, each marked `librarian: synthesis`.
- Pages I opened to decide the synthesis:
  - `vault/wiki/lessons/lesson-gate-plan-path-cut-by-the-event-log-detail-limit.md`: to check that it shares the root cause (the 80-character cut of the event log) and is live (`new`). Outcome: clustered with `lesson-event-log-cuts-the-path-of-the-plan-file` under the new Insight. That lesson carries `addressed_by: decision-case-1045`, so the Insight was born `actioned`, and the cascade archived both lessons.
  - `vault/wiki/insights/insight-workflow-code-live-before-the-page-it-reads.md`, its Pattern and History: it already has the child `lesson-case-reading-moment-before-the-render-it-reads`. Outcome: `lesson-case-build-puts-a-reading-before-the-render-it-tests` clustered under it, and the Insight set `open`, since the lesson has no `addressed_by`.
  - `vault/wiki/lessons/lesson-case-build-leans-on-a-precedent-it-did-not-read.md`, its Trigger and Root cause. Outcome: not clustered; its cause is a History line copied from a precedent.
- `lesson-case-build-numbers-a-new-case-from-the-case-files-alone` has no pair and stays `new`.

**Ledger read.** One read of `ledger.md`, by `wc -l`: 27 lines. The yaml covers lines 1–20 and 24–27, and lines 21, 22 and 23 are folded into create entries. Every line is accounted for, and `unparsed` is empty.

**What the handoff asked**
- Instructions 15, 16 and 19 are done:
  - 1046, 1052 and 1050 were applied to `entity-sprint-plugin`.
  - Nothing of 1049.2 was applied.
  - The two Estimates left `backlog.md`, which now has 11 items, down from 13.
- Instruction 18 is done: the frontierguard line of `sprint.md` stands `- [x] … · failed`.
- Instruction 17 did not happen as written: `rule-sprint` stands `built`, not `draft`, because its new Estimate was created and read `passed` in the same run.
- The handoff asked for no repair, and no hook refused a call.

**Flags**
- Contradiction: the `context` of Case 1045 says the knowledge lesson `lesson-gate-plan-path-cut-by-the-event-log-detail-limit` "is not changed". The synthesis clustered it and the cascade archived it.
- `rule-sprint` stands `built`, against handoff instruction 17 (above).
- `rule-ask` stands `draft` but no longer prints a lint line.
- The handoff expected `guppi sprint --check` to print red; it does not.
- The handoff's own notes are carried into the brief:
  - The method of Case 1048 reads in two ways.
  - `cases/case-1050.md` stands empty.
  - The `case-guppi` of Case 1052 got the same note of `rule-case-check` twice.
  - A subagent's plan file, named with `-agent-<id>`, could be taken for the session's plan now that paths stay whole.
  - The reading of `estimate-case-build-searches-the-names-of-what-it-changes` judged the 600-odd listed files by group.
- Under Next session, Cases proposes deferring three Estimates into `backlog.md`, because session 0605 did not take their readings (handoff Debt): `estimate-plugin-install-asks-one-approval-in-plan-mode`, `estimate-morph-sets-up-the-project-at-the-first-hi` and `estimate-git-context-offers-git-init`.
- I made no read that this frame says the job does not need.

**Lint** (`guppi check`, exit 1, 6 lines):
- `status: a page with core: true that is draft` on `rule-case-build`, `rule-morph` and `rule-orchestration`.
- `unread: failed` on `estimate-case-build-settles-form-by-itself`, `estimate-orchestration-dispatches-case-guppi-at-a-level` and `estimate-sprint-plugin-frontierguard-build-read-its-folders-readers`.

Files are in c:\PROJECTS\GUPPI\vault:
- wiki\brief.md
- raw\2026-11-25\0605\materialize.yaml
