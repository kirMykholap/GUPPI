# Brief — 2026-09-21, after session 1315 of 2026-09-21 (`lift_criterion`: a part named changes alone, a part inside the Criterion sets `pending` by 296, which supersedes 291.1 in the same session; the Criteria of 286 and 288.1 restored by 291.2; the Case schema, three `given` lines, `estimates/schema.md` and `index.md` §7 name the field-only update by 294, 295, 297; Slice 3b deferred to 293; a same-session supersede leaves the Spec, deferred to 298)

Written by the librarian from `raw/2026-09-21/1315/handoff.md`, the yamls of
`raw/2026-09-21/1315` and `raw/2026-09-21/0019`, and the Greps of the indexes.

## Where things stand

- Code, commit `716f850` on `migration`: `guppi/materialize.py` — `names_a_part`,
  `touches_criterion`, `lift_criterion` takes `project_dir`, the module docstring;
  `tests/test_materialize.py` +6 (66 in the file, 481 in all). By hand, committed (297):
  `vault/wiki/estimates/schema.md` (the row `## Criterion`) and `vault/wiki/index.md` §7.
  `make style` clean, LF. Spec 1315: 5 task lines ticked by the session (239, 309, 310, 345,
  346).
- Closed in the session: 291.2, 294, 295, 296 (supersedes 291.1), 297; 293 the defer of Slice
  3b (`rule-work-mode`, `rule-subagent-guppi`, the sixteenth); 298 the defer of `rule-prespec`,
  `rule-materialize`, `rule-page-generation`. Readings in the 1315 ledger, `passed`:
  `estimate-case-protocol-loaded` (L1, at `/hi`), `estimate-claude-md-rendered` (L2),
  `estimate-materialize-assembles` (L19, pytest and `--show`), `estimate-internal-context-loaded`
  (L20, at `/hi`). Lessons: `lesson-estimate-purpose-update-replaced-the-signed-criterion` (L3,
  `addressed_by: decision-case-296`), `lesson-retro-answered-in-the-skills-language` (L21).
- Not done by the session's own account: the pages and the render — this run; the readings
  of `estimate-case-protocol-loaded` (294), `estimate-generate-cascades`,
  `estimate-generate-writes-the-decision-page`, `estimate-generate-fails-alone` (295) — the
  next session; Slice 3b — defer 293.
- Two units in the walk. `raw/2026-09-21/1315`: 24 entries lifted from the ledger, as the
  handoff expected — 4 readings, 2 lessons, 18 decision entries — plus 3 entries of the
  librarian's synthesis and 8 Decision pages added by `generate`. Applied: 25 of the 27
  entries; the 2 entries of 291.1 (lines 4, 5) carry `superseded_by: '296'` and are not
  applied. No stderr, `unparsed` empty. Decisions: 8 pages written (291.1, 291.2, 293, 294,
  295, 296, 297, 298); `decision-case-291.1` set `archived` by `generate` (superseded) and moved
  by `cleanup` to `archive/migration/2026-09-21/1315/decisions/`. Rules: none created; 2
  `update` entries applied on 2 pages (`rule-case-protocol` 294, `rule-materialize` 296); 5
  `defer` entries on 5 pages, all marked `exists` (`rule-work-mode`, `rule-subagent-guppi` by
  293; `rule-prespec`, `rule-materialize`, `rule-page-generation` by 298). Estimates: none
  created; 7 `update` entries applied on 7 pages (`estimate-generate-ticks-the-spec` and
  `estimate-internal-context-loaded` by 291.2, the Criterion whole and `pending`;
  `estimate-case-protocol-loaded` by 294, the Criterion whole and `pending`;
  `estimate-generate-cascades`, `estimate-generate-writes-the-decision-page`,
  `estimate-generate-fails-alone` by 295, one `replace` pair each and `pending`;
  `estimate-materialize-assembles` by 296, the Criterion whole and `pending`); 4 reading lines
  applied on 4 pages. Lessons: 2 created, 2 `update` entries (the synthesis) applied.
  Insights: 1 created (`insight-materialize-estimate-update-lifts-the-criterion-whole`, `open`,
  `severity` 2). Rule-class `file` items: 2 reported by `generate` as applied by hand
  (`estimates-schema`, `index`, 297). 28 pages written or changed. `raw/2026-09-21/0019`: 0
  new entries, 0 pages. Cleanup moved 1 page.
- The checks the handoff asked first held: the three entries of 295 (lines 12–14) carry
  `replace`, `set: {status: pending}` and no `sections`; 291.2 (lines 6, 7), 294 (line 11)
  and 296 (line 16) carry `sections.Criterion` written whole and `set: {status: pending}`;
  `superseded_by: '296'` on both entries of 291.1; `addressed_by: decision-case-296` on the
  lesson entry of L3 (L4 and L15 both carry `{addresses:…}`, the last mark stands).
- The order of the readings and the `update` entries on one page, as the handoff named:
  `estimate-case-protocol-loaded` — L1 `passed`, then 294 `pending`; the page ends `pending`.
  `estimate-materialize-assembles` — 296 `pending`, then L19 `passed`; the page ends `passed`
  on the Criterion of 296. `estimate-internal-context-loaded` — 291.2 `pending`, then L20
  `passed`; ends `passed` on the Criterion of 288.1 restored. `estimate-claude-md-rendered` —
  L2 `passed`. `estimate-generate-ticks-the-spec` — 291.2, `pending` on the Criterion of 286
  restored.
- Statuses computed by `generate`: `rule-internal-context` `draft → built`; `rule-claude-md`
  `draft → built`; `rule-case-protocol` stays `draft` (`estimate-case-protocol-loaded`
  `pending`); `rule-page-generation` stays `draft` (`estimate-generate-rewords`,
  `estimate-generate-ticks-the-spec`, the three of 295 `pending`); `rule-materialize` stays
  `draft` (`estimate-materialize-carries-addresses` `pending`); `rule-prespec` stays `built`.
  `deferred_by` of `rule-work-mode` and `rule-subagent-guppi` now ends at `decision-case-293`;
  of `rule-prespec`, `rule-materialize`, `rule-page-generation` at `decision-case-298`.
- Synthesis: `lesson-estimate-purpose-update-replaced-the-signed-criterion` (L3) shares its
  root cause with `lesson-estimate-update-must-carry-its-criterion-whole` (0958, `new`) — the
  Grep `^(root_cause|deferred_by):` over `vault/wiki/lessons/`, 43 lines, and
  `^(pattern|deferred_by):` over `vault/wiki/insights/`, 16 lines; no Insight had the pattern.
  Appended, marked `librarian: synthesis`: a `create` of
  `insight-materialize-estimate-update-lifts-the-criterion-whole` (children: both lessons;
  tags `harness, workflow, librarian`; `Pattern`, `Proposal`) and an `update` of each lesson
  (`status: clustered`, `insight`). The pair of the mark: the lesson entry carries
  `addressed_by: decision-case-296`, and the Insight is new, `open`, 296 named in its
  Proposal — no `actioned` Insight of the pattern existed, so no `set` of `addressed_by` on an
  Insight this run. `lesson-retro-answered-in-the-skills-language` (L21): no lesson and no
  Insight with its cause; stays `new`.
- `guppi render` wrote `vault/wiki/case-schema.md` (294) — the one file the handoff named,
  no stderr; `uv run guppi render --check` after it exits 0. `guppi sprint` rewrote
  `vault/wiki/sprint.md`: Slice 3b current, both items `draft`, their defers ending at 293
  (the sixteenth). 298 is not a Slice item.
- The `read` lines ticked by this run's `generate`, the four the handoff named: 0019 line 214
  (`estimate-internal-context-loaded`, L20), 0019 line 251 (`estimate-case-protocol-loaded`,
  L1), 0019 line 299 (`estimate-claude-md-rendered`, L2), 1315 line 311
  (`estimate-materialize-assembles`, L19, under 296). 1315 line 72 — the `read` of the same
  slug under the superseded 291.1 — stays `[ ]`. Spec 1315: 9 page lines ticked by
  `generate` (139, 140, 191, 192, 236, 237, 238, 307, 308), the render line 193 by
  `guppi render`. Spec 0019 lines 56 and 158 stay `[ ]`.
- `guppi archive` moved nothing and printed nothing: both units are dated the day of the
  run, and `archive` looks only at units dated before it (`guppi/archive.py`);
  `raw/2026-09-21/1315` is the session of the run. `raw/2026-09-21/0019` (all 30 entries
  `applied`) stays in `raw/` until a run on a later day.
- Tests: 481 green (`make test`), style clean.

## Readings due

No Estimate stands `failed` after `generate`.

- `estimate-case-protocol-loaded` — `rule-case-protocol` stands `draft` — read at line 194
  of `raw/2026-09-21/1315/spec.md`: `render --check` after the render (exit 0 this run); the
  `/hi` of the next session, by hand.
- `estimate-generate-cascades` — `rule-page-generation` stands `draft` — read at line 240 of
  `raw/2026-09-21/1315/spec.md`: `pytest tests/test_generate.py` at the librarian's run of
  this session or the next `/hi`. `generate` applied the pair this run; the pytest reading is
  not taken by this run.
- `estimate-generate-writes-the-decision-page` — `rule-page-generation` — read at line 241
  of the same Spec: the same run.
- `estimate-generate-fails-alone` — `rule-page-generation` — read at line 242 of the same
  Spec: the same run.
- `estimate-generate-ticks-the-spec` — `rule-page-generation` stands `draft` — read at line 56
  of `raw/2026-09-21/0019/spec.md`: pytest now; live —
  the first librarian's run whose ledger holds a `{supersedes:case N}` and a reading of a
  slug with a `read` line under the superseded Case. That run is this one: the 1315 ledger
  holds `{supersedes:case 291.1}` (L15) and the reading of `estimate-materialize-assembles`
  (L19); after `generate`, 1315 line 311 (under 296) is `[x]` and line 72 (under 291.1) is
  `[ ]`. The reading is written by the next session from these two lines.
- `estimate-compact-recall-reloads` — `rule-compact-recall` stands `draft` — read at line 158
  of `raw/2026-09-21/0019/spec.md`: pytest; live — the first compaction of a working session, by hand.
  No date.
- `estimate-materialize-carries-addresses` — `rule-materialize` stands `draft` — read at line
  158 of the 2106 Spec, `archive/migration/2026-09-20/2106/raw/spec.md`: pytest; live — the
  librarian's run on the first marked lesson. That run is this one: in
  `raw/2026-09-21/1315/materialize.yaml` the decision entries of 291.1 (line 4) and 296 (line
  15) carry `addresses: [lesson-estimate-purpose-update-replaced-the-signed-criterion]`, the
  lesson entry (yaml line 3, `addressed_by` at line 75 of the file) carries
  `addressed_by: decision-case-296` at the entry's level and not under `fields`; the lesson
  page carries no such field. The page's Criterion promises exactly that. The reading is
  written by the next session.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` stands `draft` — read at
  line 210 of the same archived 2106 Spec: the librarian's run on the first marked lesson
  under an actioned Insight, by hand. Not this run: the Insight of the marked lesson is new
  and `open`. No date.
- `estimate-generate-rewords` — `rule-page-generation` stands `draft` — read at line 745 of
  the 1308 Spec, `archive/migration/2026-09-20/1308/raw/spec.md`: pytest now; live — the first
  `reword` applied (case 277.4). No `reword` in this walk. No date.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` stands `draft` — by its
  `method`: `make lint`, exit 0 — or only unread lines on the Estimates of
  `entity-sprint-migration`; at the close of the sprint.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — by its `method`:
  one reading of the tree by hand at the close of the sprint, each path and decision named in
  the estimate line.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — by its `method`: `make test`
  on the last commit of `migration`, then `git log` of `main` after the merge.

## Deferred

Four items. The previous brief's list was empty.

1. `insight-materialize-estimate-update-lifts-the-criterion-whole` — `open`, `severity` 2,
   first brief. Pattern: `lift_criterion` in `guppi/materialize.py` knows one kind of update
   of an Estimate, the change of the promise: it lifts the Case's given/when/then into every
   update of an Estimate and sets `pending`, a correction of one word or a field alone
   included, so the Criterion the person signed is replaced by the Case's text and nothing
   before the librarian's run reads the `then` of the Case against the mechanism. Proposal:
   296 built the cure in the mechanism (a part named changes alone; a pair inside the
   Criterion or a written `sections.Criterion` sets `pending`); what remains is a check —
   pre-spec reads the `then` of an Estimate `update` against what `materialize` will assemble,
   and the librarian flags an `update` whose `sections.Criterion` replaces a Criterion that
   stood `passed`. In Plan Mode a Case whose `recommend` starts there, ending in an `update`
   of the Insight (`status: actioned`, `addressed_by`), a rejection, or a `defer` with the
   Insight as its target.
2. `rule-prespec` — defer 298, first brief, no Insight, no `purpose` reached the page (the
   entry is `incomplete`, see Flags). From the Decision page's Context and Problem: a Case
   superseded in its own session is removed from the Spec by the agent and the superseding Case
   written whole; pre-spec catches a superseded Case still in the plan.
3. `rule-materialize` — defer 298, first brief, as above: `materialize` copes with a
   superseded entry whose Case is not in the Spec (today it would mark the entry
   `incomplete: [then]`).
4. `rule-page-generation` — defer 298, first brief, as above: `generate` writes the Decision
   page of the superseded Case from the text the Spec no longer holds.

Left out, the sprint page names them (case 229.4): `rule-work-mode` and `rule-subagent-guppi`
(defer 293 this walk, the sixteenth; 183, 206, 218, 231, 242, 248, 252, 254, 260, 263, 269,
276, 281, 285, 289 before — Slice 3b, the current milestone);
`insight-workflow-code-live-before-the-page-it-reads` (`open`, `severity` 2, defer 238; in the
text of the `rule-work-mode` item); `rule-git-context`, `rule-github-issues` (in the text of
the `estimate-sprint-migration-merges` item, Slice 5); `rule-spec-box` (Slice 5); `rule-morph`
(Slice 5).

## Flags

- Three entries marked `incomplete` — the `defer` entries of 298 (yaml lines 22, 23, 24:
  `rule-prespec`, `rule-materialize`, `rule-page-generation`): "then block is not YAML: mapping
  values are not allowed here … line 7, column 136: `… by the mark alone — no incomplete:
  [then], no case_text; the repl …`" — a colon in a plain scalar of the `then` block of Case
  298 in Spec 1315, the form of `lesson-spec-change-line-with-a-colon-breaks-the-then-block`.
  The three entries applied all the same: `deferred_by` extended on the three pages, the
  Decision page written with Context and Problem; no `purpose` reached the pages and
  `decision-case-298` has no `## Deferred` section. The `decisions` record of 298 carries the
  same `incomplete`. The handoff expected no `incomplete` ("`--show` over the unit was clean at
  Retro"); the yaml of this run does not agree. Not repaired.
- One `near`: the lesson entry of L3, `near: lesson-estimate-update-must-carry-its-criterion-whole`
  — the same root cause, a different trigger (the second case); the two are clustered by the
  synthesis above. Index check of L3 and L21 against the Grep `^(root_cause|deferred_by):` over
  `vault/wiki/lessons/`, 43 lines; L21 (the Retro in English) matches no line — the nearest,
  `lesson-plan-mode-frontier-refused-on-the-client-text` (the client's text put above the
  project's rule), is another mechanism; not near. No page opened for the index check.
- Five `exists` marks on the defers of 293 and 298 (a `defer` with a `ref` on a page on
  disk, as with 289). No entry marked `failed` or `unparsed`; no failed Estimate; no MOC
  candidate.
- The two entries of 291.1 (yaml lines 4, 5) carry `superseded_by: '296'` and were not
  applied; `decision-case-291.1` stands `archived`, `superseded_by: decision-case-296`, in the
  archive. Spec 1315 lines 68–72 (291.1's five task lines) stay `[ ]` for good — Case 298.
- From the handoff, no page: the comment in `pyproject.toml` lines 6–7 still names "owner's
  decision D3, 2026-09-09" ("Add no new dependencies"), a condition the owner dropped in the
  chat of 1315 — no Rule, no page, the frontier line closed `· work`; the comment goes at the
  next touch of the file. Untested corner: `touches_criterion` reads
  `vault/wiki/estimates/<slug>.md` only — an `update` of an archived Estimate carries
  `set.status` anyway and takes the whole-replacement branch. `estimate-materialize-assembles`
  has no `purpose` field; 296 set none. Caveats the owner accepted: `method` is not a touched
  Criterion in 296; 294 sets `estimate-case-protocol-loaded` `pending` again after L1.
- From the handoff, the tools: `materialize --show` piped into Python on Windows arrives as
  surrogate escapes (`#xdc8d` at the `＋` operand) — a redirect to a file read with
  `encoding="utf-8"` works; `bashguard` refused two heredocs (a path into the plan folder; a
  backslash) — known.
- Instructions of the handoff not carried out by this run: the readings the handoff offered
  to the librarian ("or by you, `passed`/`failed` on those two lines"; "by you if you take
  readings" — `pytest tests/test_generate.py` for the three of 295) — the librarian writes no
  ledger line and ticks no Spec line by hand; the facts stand in Readings due for the next
  session. No instruction refused.
- The lesson page of L3 carries no `addressed_by` field — the lessons schema has none; the
  mark lives on the yaml entry and on the Decision page, as `estimate-materialize-carries-addresses`
  promises.
- Rule-class `file` items of 297 (`estimates-schema`, `index`): `generate` reported "a
  Rule-class file, applied by hand" on stdout; ticked in Spec 1315 lines 345, 346 by the
  session.
- Lint, gone since the previous brief: 2 `unread: pending` (`estimate-internal-context-loaded`,
  `estimate-claude-md-rendered`, `passed`). New: 3 `unread: pending`
  (`estimate-generate-cascades`, `estimate-generate-writes-the-decision-page`,
  `estimate-generate-fails-alone`); the stale-defer count of `rule-work-mode` and
  `rule-subagent-guppi` 27 → 28. `unmigrated` stays 23.
- Standing: the defer of 238 on `insight-workflow-code-live-before-the-page-it-reads` without a
  `purpose`; `estimate-hi-no-read-calls` in the shape before case 193 by choice;
  `rule-spec-box` placeholder findings (`kind`, `estimates`, orphan).
- Stale defers by lint: `rule-work-mode` and `rule-subagent-guppi` 28 times since case 29;
  `rule-morph` 1 time since case 239.
- Lint, 81 findings: 2 `rules/rule-spec-box` schema (`kind`, `estimates`) and 1 orphan;
  62 `decisions/decision-case-<1–28>` missing `## Context` and `## Problem` (31 pages,
  Slice 5); 3 deferred (`rule-morph` 1, `rule-subagent-guppi` 28, `rule-work-mode` 28);
  12 unread pending (`estimate-case-protocol-loaded`, `estimate-compact-recall-reloads`,
  `estimate-generate-cascades`, `estimate-generate-fails-alone`, `estimate-generate-rewords`,
  `estimate-generate-ticks-the-spec`, `estimate-generate-writes-the-decision-page`,
  `estimate-materialize-carries-addresses`, `estimate-synthesis-keeps-actioned-by-the-mark`,
  the three sprint Estimates); `estimates: unmigrated: 23 pages in the shape before case 193`.

## Next session

Cases

- Slice 3b — `rule-work-mode`, `rule-subagent-guppi` (defer 293, the sixteenth), with the
  sentence of `insight-workflow-code-live-before-the-page-it-reads` written into
  `rule-work-mode` and, by 293's `purpose`, a subagent loads `CLAUDE.md` and no glossary
  (288.1); from the handoff and the sprint page.
- Case 298 — a Case superseded in its own session leaves the Spec: pre-spec catches it,
  `materialize` and `generate` cope with a superseded entry without a Case (defer 298 on
  `rule-prespec`, `rule-materialize`, `rule-page-generation`); and the defect of this run: the
  `then` block of 298 in Spec 1315 is not YAML (a colon in a plain scalar), so its three
  entries are `incomplete` and `decision-case-298` has no `## Deferred` — from the yaml.
- The owner's topic: `index.md`, `glossary.md` and the category schemas — Rule-class files
  applied by hand today — applied by the script from a decision (`replace` pairs, no History)
  instead of "applied by hand"; from the handoff.

Work

- Read `estimate-case-protocol-loaded` (1315 line 194) at the next `/hi`, by hand.
- Read `estimate-generate-cascades`, `estimate-generate-writes-the-decision-page`,
  `estimate-generate-fails-alone` (1315 lines 240–242): `pytest tests/test_generate.py`.
- Read `estimate-generate-ticks-the-spec` (0019 line 56) from this run: 1315 line
  311 `[x]`, line 72 `[ ]`.
- Read `estimate-materialize-carries-addresses` (2106 line 158, archived) from this run: the
  lesson entry of L3 carries `addressed_by: decision-case-296` at the entry's level.
- Read `estimate-compact-recall-reloads` (0019 line 158) at the first compaction of
  a working session, by hand; no date.
- Read `estimate-generate-rewords` at the first `reword` (1308 line 745, archived); no date.
- Read `estimate-synthesis-keeps-actioned-by-the-mark` (2106 line 210, archived) at the first
  marked lesson under an actioned Insight; no date.
- Read `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-leftovers-gone`,
  `estimate-sprint-migration-merges` — at the close of the sprint, by their `method`; the
  sprint page holds them under Slices 4 and 5.
- Ledger lines of the walk not applied: 1315 L4 and L5 (291.1, superseded by 296 — by rule,
  not by error). Unticked boxes: Spec 1315 lines 68–72 (291.1, stay by Case 298), 194,
  240–242; Spec 0019 lines 56, 158. The tree is clean after the commit of this run.

## Readings at the close

- `make test`: 481 passed.
- `make lint`: 81 findings, exit 1 (the list above).
- Pages: entities 2, rules 47, estimates 76, lessons 43, insights 15, decisions 417.
