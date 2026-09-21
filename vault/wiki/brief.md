# Brief — 2026-09-22, after session 1853 of 2026-09-21 (a Case superseded in its own session leaves the Spec by 299.1–299.5, which take up 298; Slice 3f — the Rule-class files into the graph — the current milestone by 301; the Insight of 1315 `actioned` by 302.1 and the synthesis births an Insight from a marked lesson by 302.2; Slice 3b deferred to 303, the seventeenth)

Written by the librarian on 2026-09-22 from `raw/2026-09-21/1853/handoff.md`, the yamls of
`raw/2026-09-21/1853`, `raw/2026-09-21/1315` and `raw/2026-09-21/0019`, and the Greps of the
indexes.

## Where things stand

- Code, commit `b3f298d` on `migration`: `guppi/prespec.py` — `superseded_in_window`,
  `check_lines` (the finding on a heading, the lines of a superseded Case freed), `check_tasks`
  (a superseded Case has no work); `guppi/materialize.py` — `mark_superseded(…, in_spec)`,
  `decision_record(…, gone_from_spec)`; `guppi/generate.py` — `decision` writes the two-line
  body for a record with `superseded_by` and no `case_text`. Tests: `test_prespec.py` +4 (68),
  `test_materialize.py` +2 (68), `test_generate.py` +1 (75); 488 in all, `make style` clean.
  By hand, committed: `vault/wiki/index.md` §7 (299.1), `vault/wiki/insights/schema.md` the
  `status` row (302.2), `vault/wiki/decisions/decision-case-298.md` `## Deferred` and a History
  line (299.4). Spec 1853: 9 task lines ticked by the session (69, 113, 114, 153, 154, 208,
  209, 210, 404).
- Closed in the session: 299.1–299.5 (298 taken up), 301, 302.1, 302.2; 303 the defer of
  Slice 3b (`rule-work-mode`, `rule-subagent-guppi`, the seventeenth). Case 300 (`replace`
  pairs written by `generate` into a Rule-class file) was formed and not ratified — in the chat
  only, no line, nothing to apply. Readings in the 1853 ledger, all `passed`: L1–L6 at `/hi`
  (`estimate-case-protocol-loaded`, `estimate-generate-cascades`,
  `estimate-generate-writes-the-decision-page`, `estimate-generate-fails-alone`,
  `estimate-generate-ticks-the-spec`, `estimate-materialize-carries-addresses`), L25–L28 after
  Work Mode (`estimate-prespec-catches-a-superseded-case`, `estimate-materialize-marks-superseded`,
  `estimate-generate-writes-the-decision-page`, `estimate-prespec-checks-the-plan`). Lesson:
  `lesson-sub-case-given-the-parents-plus-lines-has-no-form` (L29, no `{addresses:…}`).
- Not done by the session's own account: the pages and the renders — this run; the live legs
  of L25 (a later session's `/pre-spec` with a `{supersedes}` of its own Case) and L26 (the
  librarian's run of such a session) — a later session; Slice 3f — from the next session,
  theme 1 (the schemas) first; Slice 3b — defer 303.
- Three units in the walk. `raw/2026-09-21/1853`: 29 entries lifted from the ledger — 10
  readings, 1 lesson, 18 decision entries (L25 folded into the `create` of L11, so no entry
  carries `line: 25`) — and 9 Decision pages added by `generate`. Applied: all 29; no
  `failed`, no `incomplete`, no `unparsed`, no stderr from `materialize`, `generate`, `cleanup`,
  `render` or `sprint`. Decisions: 9 pages written (299.1, 299.2, 299.3, 299.4, 299.5, 301,
  302.1, 302.2, 303). Rules: none created; 5 `update` entries applied on 5 pages
  (`rule-case-protocol` 299.1, `rule-prespec` 299.2, `rule-materialize` 299.3,
  `rule-page-generation` 299.4, `rule-synthesis` 302.2 — one `replace` pair each); 2 `defer`
  entries on 2 pages, both `exists` (`rule-work-mode`, `rule-subagent-guppi` by 303).
  Estimates: 2 created (`estimate-prespec-catches-a-superseded-case`, ref `rule-prespec`,
  `passed` by L25 folded in; `estimate-sprint-migration-rule-class-files-dissolved`, ref
  `entity-sprint-migration`, `pending`); 6 `update` entries applied on 6 pages
  (`estimate-case-protocol-loaded` 299.1, `estimate-generate-writes-the-decision-page` 299.4,
  `estimate-synthesis-keeps-actioned-by-the-mark` 302.2 — the Criterion whole and `pending`;
  `estimate-materialize-marks-superseded` 299.3 — the Criterion lifted from the sub-case's
  `given`/`when`/`then`, `pending`; `estimate-prespec-checks-the-plan` 299.5 — one `replace`
  pair inside the Criterion, `pending` set by `materialize`); 10 reading lines applied on 9
  pages. Entities: 1 `update` applied (`entity-sprint-migration` 301, `Milestones` and
  `Backlog` whole). Insights: 1 `update` applied
  (`insight-materialize-estimate-update-lifts-the-criterion-whole` 302.1, `actioned`,
  `addressed_by: decision-case-296`). Lessons: 1 created (`new`). Rule-class `file` items: 2
  reported by `generate` as applied by hand (`index` 299.1, `insights-schema` 302.2). 33 pages
  written or changed. `raw/2026-09-21/1315` and `raw/2026-09-21/0019`: 0 new entries, 0 pages.
- Cleanup moved 3 pages to `archive/migration/2026-09-22/1853/`: `decision-case-298`
  (`archived`, superseded by 299.2, 299.3, 299.4 — the `{supersedes:case 298}` mark on L10,
  L12, L14) and the two `clustered` lessons of the actioned Insight,
  `lesson-estimate-update-must-carry-its-criterion-whole` and
  `lesson-estimate-purpose-update-replaced-the-signed-criterion` — the cascade the handoff
  expected.
- The checks the handoff asked first held: L8, L15, L20 carry `sections.Criterion` written
  whole and `set: {status: pending}` (L20 also `set.purpose`); L13 carries `set: {status:
  pending}` and a Criterion `materialize` lifted from 299.3's own `given`/`when`/`then` (the
  parent's two lines written out plus two); L24 carries one `replace` pair inside the Criterion
  of `estimate-prespec-checks-the-plan` and `set: {status: pending}` set by `touches_criterion`
  (296); L7, L10, L12, L14, L19 carry one `replace` pair each on a rule page, and L19's one-line
  `old` matched the five wrapped lines of `rule-synthesis`; L16 carries `sections` with
  `Milestones` and `Backlog` whole; L17 carries `ref: entity-sprint-migration`, the Criterion of
  301 and a quoted `method`; L18 carries `set: {status: actioned, addressed_by:
  decision-case-296}`.
- The order of the readings and the `update` entries on one page, as the handoff named:
  `estimate-case-protocol-loaded` — L1 `passed`, then L8 `pending`; ends `pending`.
  `estimate-generate-writes-the-decision-page` — L3 `passed`, then L15 `pending`, then L27
  `passed`; ends `passed` on the Criterion of 299.4. `estimate-prespec-catches-a-superseded-case`
  — L11 create, L25 folded in; `passed`. `estimate-materialize-marks-superseded` — L13
  `pending`, then L26 `passed`; ends `passed`. `estimate-prespec-checks-the-plan` — L24
  `pending`, then L28 `passed`; ends `passed`.
- Statuses computed by `generate`: `rule-materialize` `draft → built`
  (`estimate-materialize-carries-addresses` and `estimate-materialize-marks-superseded`
  `passed`); `rule-case-protocol` stays `draft` (`estimate-case-protocol-loaded` `pending`);
  `rule-page-generation` stays `draft` (`estimate-generate-rewords` `pending`); `rule-synthesis`
  stays `draft` (`estimate-synthesis-keeps-actioned-by-the-mark` `pending`); `rule-prespec`
  stays `built`, its `estimates` list extended with `estimate-prespec-catches-a-superseded-case`.
  `deferred_by` of `rule-prespec`, `rule-materialize` and `rule-page-generation` lost
  `decision-case-298` (the mark of 299.2–299.4); of `rule-work-mode` and `rule-subagent-guppi`
  now ends at `decision-case-303`. The `severity` of
  `insight-materialize-estimate-update-lifts-the-criterion-whole` is 0 after `actioned` (2
  before).
- In `raw/2026-09-21/1315/materialize.yaml` `materialize` marked the three `defer` entries of
  298 (lines 22–24) `superseded_by: '299.4'` and the `decisions` record of 298
  `superseded_by: [decision-case-299.2, decision-case-299.3, decision-case-299.4]`; their
  `applied` and `incomplete` marks stay as a record, as the handoff asked.
- Index check of L29 (`lesson-sub-case-given-the-parents-plus-lines-has-no-form`): the Grep
  `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 45 lines, and
  `^(pattern|deferred_by):` over `vault/wiki/insights/`, 17 lines. No line has its root cause
  (the Case schema gives a sub-case two forms of `given` and none for the parent's lines plus
  more; the agent invented a pointer the scripts do not resolve). Nearest:
  `lesson-spec-change-line-with-a-colon-breaks-the-then-block` — a form of the agent's Spec
  block that only the check sees — another cause (a YAML rule, not a gap of the schema); marked
  `near`. `lesson-supersedes-in-the-same-session-skips-the-earlier-cases-entries` (the schema
  presents one thing, the scripts do another) and `lesson-pretask-runs-before-the-check-it-adds`
  — other causes. No Insight has the pattern. Synthesis: no pair; the lesson stays `new`, as the
  handoff expected. No page opened.
- `guppi render` wrote the three files the handoff named: `vault/wiki/case-schema.md`
  (299.1), `.claude/skills/pre-spec/SKILL.md` (299.2), `.claude/agents/librarian-guppi.md`
  (302.2); no stderr. `uv run guppi render --check` after it exits 0 — the first leg of the
  reading of `estimate-case-protocol-loaded`, its line not written by this run. `guppi sprint`
  rewrote `vault/wiki/sprint.md`: Slice 3f current with its seven items — the Estimate
  `pending` and the six themes; Slices 3b, 4, 5 below it; the Backlog's two lines.
- Spec lines ticked by this run's `generate`: Spec 1853 — 18 page lines and the four `read`
  lines the handoff named (116, 155, 211, 239); the three render lines by `guppi render`, the
  sprint line by `guppi sprint`. Spec 1315 — line 194 (`estimate-case-protocol-loaded`, L1),
  lines 240–242 (the three of 295, L2–L4). Spec 0019 — line 56
  (`estimate-generate-ticks-the-spec`, L5). Open by their moment: 1853 lines 71, 318, 406; 0019
  line 158; 1315 lines 68–72 (291.1, superseded — stay for good).
- `guppi archive` moved `raw/2026-09-21/0019` and `raw/2026-09-21/1315` (all entries
  `applied`, dated the day before the run) to `archive/migration/2026-09-21/0019/raw` and
  `archive/migration/2026-09-21/1315/raw`; `raw/2026-09-21/1853` stays, the session of the run.
  No stderr. The 0019 and 1315 paths above name the Specs as they stood in `raw/` during the run.
- Tests: 488 green (`make test`), style clean.

## Readings due

No Estimate stands `failed` after `generate`.

- `estimate-case-protocol-loaded` — `rule-case-protocol` stands `draft` — read at line 71 of
  `raw/2026-09-21/1853/spec.md`: `render --check` after the render (exit 0 this run); the
  `/hi` of the next session, by hand.
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` stands
  `draft` — read at line 318 of `raw/2026-09-21/1853/spec.md`: at the close of Slice 3f, by
  its `method` (`ls vault/wiki/*/schema.md` empty and `vault/wiki/index.md` absent; the grep of
  `RULE_CLASS`, `applied by hand`, `rule_class_path`, `prose_names` over `guppi/` empty;
  `render --check`, `glossary --check` and `make lint` exit 0).
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` stands `draft` — read at
  line 406 of `raw/2026-09-21/1853/spec.md`: the librarian's run on the first marked lesson —
  under an `actioned` Insight, or the second of a new pattern; no date. Not this run: L29
  carries no mark.
- `estimate-compact-recall-reloads` — `rule-compact-recall` stands `draft` — read at line 158
  of the 0019 Spec, now `archive/migration/2026-09-21/0019/raw/spec.md`: pytest; live — the first compaction of a working session,
  by hand; no date.
- `estimate-generate-rewords` — `rule-page-generation` stands `draft` — no unticked line in a
  Spec under `raw/`; by its `method`: `pytest tests/test_generate.py` on a temp vault; live —
  the librarian's run that applies the first `reword`. No `reword` in this walk. No date.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — by its `method`:
  `make lint`, exit 0 — or only unread lines on the Estimates of `entity-sprint-migration`; at
  the close of the sprint.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — by its `method`:
  one reading of the tree by hand at the close of the sprint, each path and decision named in
  the estimate line.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — by its `method`: `make test`
  on the last commit of `migration`, then `git log` of `main` after the merge.

## Deferred

No item. The previous brief's four items are gone: 2, 3, 4 (`rule-prespec`, `rule-materialize`,
`rule-page-generation`, defer 298) — 298 superseded by 299.2, 299.3, 299.4, their `deferred_by`
cleared; 1 (`insight-materialize-estimate-update-lifts-the-criterion-whole`) — `actioned` by
302.1, `addressed_by: decision-case-296`.

Left out, the sprint page names them (case 229.4): `rule-work-mode` and `rule-subagent-guppi`
(defer 303 this walk, the seventeenth; 183, 206, 218, 231, 242, 248, 252, 254, 260, 263, 269,
276, 281, 285, 289, 293 before — Slice 3b);
`insight-workflow-code-live-before-the-page-it-reads` (`open`, `severity` 2, defer 238; in the
text of the `rule-work-mode` item); `rule-git-context`, `rule-github-issues` (in the text of
the `estimate-sprint-migration-merges` item, Slice 5); `rule-spec-box` (Slice 5); `rule-morph`
(Slice 5).

## Flags

- One `near`: the lesson entry of L29, `near:
  lesson-spec-change-line-with-a-colon-breaks-the-then-block` — the same shape (a Spec block in
  a form the scripts do not take, caught by the check alone), another root cause; not
  clustered.
- Two `exists` marks on the defers of 303 (a `defer` with a `ref` on a page on disk, as with
  293). No entry marked `incomplete`, `failed` or `unparsed`; no failed Estimate; no MOC
  candidate; no stderr from any script.
- `decision-case-298`, repaired by hand in the session (`## Deferred`, a History line), was
  set `archived` by `generate` (superseded by 299.2, 299.3, 299.4) and moved by `cleanup` to
  `archive/migration/2026-09-22/1853/decisions/`; not rewritten by this run. The `deferred_by`
  of its three targets no longer names it.
- The Spec of 1853 has no `- [ ] read` line for `estimate-generate-rewords`; its reading stands
  by the page's `method` (Readings due).
- From the handoff, no page: Case 300 formed and not ratified, in the chat only. 301: the
  criterion for a category MOC is a rule of the audit, not a decision on any page; the glossary
  from `terms` on the defining pages is the chosen shape ("a rule per term" rejected); the
  template engine is Backlog; `applies_to`/`rules` moved from the Backlog line into theme 2 of
  the Slice — all in the `context` of 301. The live legs of L25 and L26 are not taken; both
  readings are `passed` on pytest with the live leg named in the text.
- Instructions of the handoff not carried out by this run: none refused. The `render --check`
  line of `estimate-case-protocol-loaded` (1853 line 71) is not ticked and no reading is
  written — the next session's.
- Lint, gone since the previous brief: 5 `unread: pending` (`estimate-generate-cascades`,
  `estimate-generate-fails-alone`, `estimate-generate-ticks-the-spec`,
  `estimate-generate-writes-the-decision-page`, `estimate-materialize-carries-addresses`, all
  `passed`). New: 1 `unread: pending` (`estimate-sprint-migration-rule-class-files-dissolved`);
  the stale-defer count of `rule-work-mode` and `rule-subagent-guppi` 28 → 29. `unmigrated`
  stays 23.
- Standing: the defer of 238 on `insight-workflow-code-live-before-the-page-it-reads` without a
  `purpose`; `estimate-hi-no-read-calls` in the shape before case 193 by choice;
  `rule-spec-box` placeholder findings (`kind`, `estimates`, orphan); the comment in
  `pyproject.toml` lines 6–7 naming "owner's decision D3" (from the previous brief, no page).
- Stale defers by lint: `rule-work-mode` and `rule-subagent-guppi` 29 times since case 29;
  `rule-morph` 1 time since case 239.
- Lint, 77 findings: 2 `rules/rule-spec-box` schema (`kind`, `estimates`) and 1 orphan;
  62 `decisions/decision-case-<1–28>` missing `## Context` and `## Problem` (31 pages,
  Slice 5); 3 deferred (`rule-morph` 1, `rule-subagent-guppi` 29, `rule-work-mode` 29);
  8 unread pending (`estimate-case-protocol-loaded`, `estimate-compact-recall-reloads`,
  `estimate-generate-rewords`, `estimate-synthesis-keeps-actioned-by-the-mark`, the four sprint
  Estimates); `estimates: unmigrated: 23 pages in the shape before case 193`.

## Next session

Cases

- Slice 3f, theme 1 — the schemas: six Leaves `rule-<category>-schema`, `enforcement: render`,
  the Render the `schema.yaml`; `schema.md` gone; the themes of the sprint page into
  `## Cases`; from the handoff and the sprint page.
- Slice 3b — `rule-work-mode`, `rule-subagent-guppi` (defer 303, the seventeenth), with the
  sentence of `insight-workflow-code-live-before-the-page-it-reads` written into
  `rule-work-mode` and a subagent loading `CLAUDE.md` and no glossary (288.1); from the sprint
  page.

Work

- Read `estimate-case-protocol-loaded` (1853 line 71) at the next `/hi`, by hand; the first
  leg (`render --check` exit 0) is from this run.
- Read `estimate-synthesis-keeps-actioned-by-the-mark` (1853 line 406) at the first marked
  lesson under an `actioned` Insight or the second of a new pattern; no date.
- Read `estimate-sprint-migration-rule-class-files-dissolved` (1853 line 318) at the close of
  Slice 3f, by its `method`.
- Read `estimate-compact-recall-reloads` (0019 line 158, archived) at the first compaction of a working
  session, by hand; no date.
- Read `estimate-generate-rewords` at the first `reword`, by its `method`; no date.
- Read `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-leftovers-gone`,
  `estimate-sprint-migration-merges` — at the close of the sprint, by their `method`; the
  sprint page holds them under Slices 4 and 5.
- The live legs of L25 (`estimate-prespec-catches-a-superseded-case`: a later session's
  `/pre-spec` with a `{supersedes}` of its own Case) and L26
  (`estimate-materialize-marks-superseded`: the librarian's run of such a session).
- Ledger lines of the walk not applied: none. Unticked boxes: Spec 1853 lines 71, 318, 406;
  Spec 0019 line 158 and Spec 1315 lines 68–72 (291.1, stay by 298 and 299), both archived.
  The tree is clean
  after the commit of this run.

## Readings at the close

- `make test`: 488 passed.
- `make lint`: 77 findings, exit 1 (the list above).
- Pages: entities 2, rules 47, estimates 78, lessons 42, insights 15, decisions 425.
