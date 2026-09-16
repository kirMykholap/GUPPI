# Brief — 2026-09-16, after session 1955 (Slice 3d closed: case 191 taken up — generate, lint, pre-task by the Estimate model)

Written by the librarian from `raw/2026-09-16/1955/handoff.md`, the yamls of
`raw/2026-09-16/1034`, `raw/2026-09-16/1651` and `raw/2026-09-16/1955`, and the index Greps.

## Where things stand

- Cases 201–204 and 208 ratified and built in code in session 1955: `guppi/generate.py`
  (fields `purpose`/`method`/`checked` in order, `checked` from the Result's date, the old
  `criterion_block`/`remove_criterion` paths refused, the Decision page without Given and
  the Criterion list, the docstring by the five promises), `guppi/lint.py` (`unread`, the
  `method` field with the classes test / `pytest` / `make` / reading, `unmigrated` as one
  line), `guppi/pretask.py` (`check_form` by the model), `guppi/materialize.py` (`ref` on
  an Estimate item is the entry's). Tests 397 → 396 (the old-shape tests replaced), all
  green; `make style` clean; `render --check` 0.
- Rule-class by hand in the session: `decisions/schema.md` and `.yaml` (Given and Criterion
  the shape before 201.2), `index.md` §7 and §12, `case-schema.md` two sentences,
  `estimates/schema.md` and `.yaml` (201.1 and 202 instead of 191). `## How it works`
  dropped by hand on `rule-page-generation` and `rule-lint`.
- Cases 205, 206, 207 deferred under `## Deferred` of the Spec. 14 readings taken and in the
  ledger; one lesson. Commit `8fd804e` on `migration`.
- Not done in the session: the vault pages of 201–208 (this run), the three renders (this
  run), the four readings listed below, the five flags of the handoff (below).
- This run. `materialize` walked three units: 1034 extended with 0 entries (191's three
  `defer` entries and its decision record gained `superseded_by: 203.2`), 1651 with 0, 1955
  written with 41 entries — 37 in the yaml, the four readings of the created Estimates
  folded into their `create` entries (`folded`). `generate`: 42 pages written or changed
  from 1955, 0 from 1034 and 1651; stderr empty; exit 0. Counts of the 1955 yaml, all
  entries applied:
  - `create`: 4 estimates (`estimate-generate-writes-the-decision-page`,
    `estimate-generate-fails-alone`, `estimate-generate-cascades`,
    `estimate-pretask-checks-the-plan`, each with its folded reading, `passed`); 1 lesson
    (`lesson-materialize-item-ref-lifted-as-a-page-field`, `error`); 15 Decision pages
    (201.1–201.5, 202, 203.1, 203.2, 204, 205, 206, 207, 208.1–208.3); 1 placeholder rule
    from the `defer` of 207 (`rule-spec-box`, `draft`).
  - `update`: 6 entries on 5 rule pages (`rule-page-generation`, `rule-lint`, `rule-pretask`
    twice — 203.2 and 208.3 —, `rule-materialize`, `rule-case-protocol`; the five `replace`
    texts all found); 6 Estimate recuts with `sections.Criterion` and `status: pending`
    (`estimate-generate-writes`, `-generate-walks-dates`, `-lint-catches`,
    `-pretask-reconciles`, `-materialize-assembles`, `-case-protocol-case-form`); 6
    Rule-class file entries printed "a Rule-class file, applied by hand".
  - `defer`: 4 — `insight-ledger-hi-tied-to-its-session-by-position` (205),
    `rule-work-mode`, `rule-subagent-guppi` (206), all three `exists`, `deferred_by`
    appended; `rule-spec-box` (207) a placeholder.
  - `estimate`: 10 reading entries, all `passed` — the six recuts (the reading lands after
    the update, so each ends `passed`), `estimate-case-protocol-acknowledging-reply`,
    `-loaded`, `-ledger-line-form`, `estimate-permissions`.
  - Synthesis: 2 entries marked `librarian: synthesis` (below, Flags).
  - Cascade: `rule-case-protocol` and `rule-permissions` `draft` → `built`;
    `rule-page-generation`, `rule-lint`, `rule-pretask` lose `deferred_by` (203.2 supersedes
    191); `decision-case-191` `superseded`. `rule-materialize` stays `draft`
    (`estimate-materialize-marks-superseded` pending).
  - `cleanup`: 1 page moved, `decision-case-191` to
    `archive/migration/2026-09-16/1955/decisions/`. `render`: `CLAUDE.md` (208.2),
    `.claude/skills/pre-task/SKILL.md` (203.2, 208.3); `render --check` exit 0.
  - `deferred_by` now: `rule-work-mode`, `rule-subagent-guppi` by `decision-case-183` and
    `decision-case-206`; `insight-ledger-hi-tied-to-its-session-by-position` by
    `decision-case-192` and `decision-case-205`; `rule-spec-box` by `decision-case-207`.
- `sprint.md` not changed: the handoff names its Slice 3d clause as a flag, a Case of the
  next Plan Mode (Flags, item 5).

## Readings due

Four Estimates stand `pending`, none `failed`. The 1955 Spec carries no `- [ ] read` line
for any of them; the place is the page's `method`. The target Rule stands `draft` in every
case.

- `estimate-materialize-marks-superseded` — `rule-materialize` (`draft`); read: pytest in
  `tests/test_materialize.py`, the tests of the supersedes mark, plus one live reading of a
  librarian's run. Facts of this run: `materialize` marked 191's three `defer` entries in
  the 1034 yaml `superseded_by: 203.2` and its decision record `superseded_by:
  decision-case-203.2`; the entries were already `applied`, `generate` skipped nothing new;
  `decision-case-191` was set `superseded` by the record's `supersedes` and archived by
  `cleanup`.
- `estimate-end-of-work-order` — `rule-end-of-work` (`draft`); read: `make test-end-of-work`
  over `tests/test_gate.py`, and the live reading of the order by hand — the order of
  session 1955: retro, handoff, this librarian run.
- `estimate-brief-written` — `rule-brief` (`draft`); read: one reading by hand after the
  first librarian run, recorded in the estimate line — this brief.
- `estimate-carry-over-writes` — `rule-carry-over` (`draft`); read: pytest over the skill's
  render plus one live reading of a carried-over session — a live `/carry`, not this
  session.

## Deferred

1. **`insight-ledger-hi-tied-to-its-session-by-position`** — `open`, severity 1, cases 192
   and 205. Pattern: the event log ties a `hi` line to its session by the `session-start`
   lines around it, not by an id; any start missing from the window or added to it sends
   the `hi` to the wrong session and the ledger writer refuses. Proposal: Case 111 already
   writes a stamped `<stamp> hi` line from the `UserPromptSubmit` hook and reads the window
   by that stamp with the old rule as a fallback; the readings of `estimate-event-log-records`
   and `estimate-ledger-write-lifts` at the next `/hi` decide whether the binding by position
   can be retired. The defer of 205: "Retire the binding by position: `pretask.resolve_session`
   resolves the session from the stamped `hi` and walks back to the date of that `hi`,
   instead of falling back to the last `session-start` of today's event log; the ledger
   hook's window is checked against it so the two readers do not disagree at midnight.
   Closes all four children of the Insight. Needs its own Estimate and one live reading
   across midnight." In Plan Mode a Case whose `recommend` starts from that Proposal, ending
   in an `update` of the Insight (`status: actioned`, `addressed_by`), a rejection written
   the same way, or a `defer` with the Insight as its target. (stood in 4 briefs)
2. **`insight-materialize-lift-loses-a-schema-field`** — `open`, severity 1, reopened by
   this run (was `actioned` by `decision-case-144.3`); third child
   `lesson-materialize-item-ref-lifted-as-a-page-field`. Pattern: `materialize` lifts a
   ledger line or a `then` item into an entry and loses a field the page schema needs; the
   page is written without it and lint names the page, never the parser. Proposal: name,
   in one place, the fields each category's page needs and where each comes from — a brace
   of the ledger line, a key of the `then` item — and have `materialize` lift by that table
   rather than by a per-kind branch; a field the source holds and the table does not know
   is a fault of the parser, not of the page. In Plan Mode a Case whose `recommend` starts
   from that Proposal, ending in an `update` of the Insight (`status: actioned`,
   `addressed_by`), a rejection written the same way, or a `defer` with the Insight as its
   target. (stood in 1 brief)
3. **`rule-work-mode`** — cases 183 and 206, Slice 3b: "Work Mode: the Spec as tasks with
   code, the ticked boxes in spec.md, the test of each Estimate written first and turned
   green; the Plan Mode of a session of its own, after the build of cases 201–203 and
   before Slice 4." Placeholder, `draft`; lint: `deferred: 14 times since case 29`.
   (stood in 18 briefs)
4. **`rule-subagent-guppi`** — cases 183 and 206, Slice 3b: "what a subagent may do in Work
   Mode, and the fork that comes back to the main agent as a Case; with `rule-work-mode`,
   after the build of cases 201–203." Placeholder, `draft`; lint: `deferred: 14 times since
   case 29`. (stood in 18 briefs)
5. **`rule-spec-box`** — case 207, after Slice 3b: "A Spec box: a session that opens a
   conserved Spec — a `raw/<date>/<HHMM>/` folder with `carry.md` — in a git worktree on
   its own branch, and runs its Work Mode. Not `/hi`, not Plan Mode: a skill lists the
   boxes, the person picks one, the agent executes it. It writes only into that folder —
   ticks `spec.md`, readings into its `ledger.md`, `handoff.md` — and into the code; it
   never touches `wiki/` and never runs the librarian. It ends with `/retro` and `/handoff`;
   done is `handoff.md` present and `carry.md` removed. At a fork it stops and returns the
   question, as a subagent does. The branch is merged into the main branch; the librarian
   runs once there, over every unapplied unit and every handoff, and writes one brief.
   Open: the skill and its conditions; the ledger hook and `guppi gate` inside a worktree
   with its own `event_log.md`; the cut of a Spec into boxes that share no file and no
   page; a third end of a session in `rule-end-of-work`; whether the box is a subagent of
   the main session with `isolation: worktree` or a session the person starts." Placeholder,
   `draft`, `near: rule-carry-over` (the box opens a Spec `/carry` conserved). (stood in
   1 brief)

Retired from the previous brief: `rule-page-generation`, `rule-lint`, `rule-pretask` — case
191 superseded by 203.2, `decision-case-191` archived, the three pages carry no
`deferred_by`.

## Flags

- Entries: no `incomplete`, `failed` or `unparsed` in the three yamls; one `near` — the
  `defer` of `rule-spec-box` (207), `near: rule-carry-over`, checked against the 49 lines of
  the rules Grep as the handoff asked, not a duplicate. The four readings of the created
  Estimates (ledger lines 28, 29, 30, 33) have no entry of their own: folded into the
  `create` entries, `folded`.
- Synthesis, against 32 lesson lines and 13 insight lines:
  `lesson-materialize-item-ref-lifted-as-a-page-field` clustered under
  `insight-materialize-lift-loses-a-schema-field` (its first child is the same mechanism —
  every key of the item lifted into `fields`; its Proposal names the case of a field the
  source holds and the table does not know). The Insight was `actioned` (`addressed_by:
  decision-case-144.3`, "no table in code"): set `open` again, severity 0 → 1, the
  `addressed_by` field stays. The handoff expected no shared root cause.
  `lesson-materialize-file-item-matched-by-slug-only` opened and not clustered (its cause
  is `find_item` matching by slug, not the lift of fields).
- Handoff flags, each a Case of the next Plan Mode:
  1. The 13 Estimate pages born of cases 188 and 189 carry a stray `ref` field beside
     `target` (the lesson above); the code is fixed, the pages need a one-off migration.
  2. A recut `update` sets `pending` and the Criterion but not `method`, and drops neither
     `## Context` nor `## Method`: the six pages recut today stay in `unmigrated` (42). The
     rule of a recut should carry `set: {method: …}` and the two sections dropped by hand.
  3. `estimate-plan-mode-names-its-estimates`: lint `method: says by hand while
     estimate-pretask-checks-the-plan names a test file` — the MOC clause of 112.1 now
     reads the `method` field; the Estimate is a reading of Plan Mode, not a pipeline over
     the children. Either its `method` names `make test-plan-mode` or the clause changes.
  4. `estimate-permissions` read `passed` while its Criterion says "eight entries" and lists
     nine; the set holds, the count is the Criterion's own. An `update` next Plan Mode.
  5. `sprint.md`: Slice 3d closes with session 1955 — case 191 built; 3b (case 206) next;
     a line for the recut remainder counted by lint (`unmigrated`). The Slice 3d clause
     still says what remains of 3d is case 191.
- `estimate-case-protocol-loaded` read `passed` on behaviour: the Criterion asks the agent
  to state two rules at the first turn, the first turn wrote the frontier instead ("the
  rules were followed, not recited"); the person may dispute (handoff).
- The 1955 Spec carries one unticked `- [ ] read estimate-case-protocol-case-form` line;
  the reading is on ledger line 41, `passed`, applied.
- `rule-spec-box` (placeholder): lint `schema: missing field kind`, `missing field
  estimates`, `orphan: no other live page names it in its frontmatter`.
- Lint: `estimates/estimate-lint-catches: ref: body names slug, which no live or archived
  page carries` — new with its recut Criterion; the same finding on
  `estimate-generate-writes` left with its recut, as the handoff said.
- Stale defers: `rule-work-mode` and `rule-subagent-guppi`, `deferred: 14 times since case
  29` (lint), 18 briefs.
- Contradiction named by lint: `estimates/estimate-plan-mode-names-its-estimates: method:
  says by hand while estimate-pretask-checks-the-plan names a test file` (flag 3 above).
- MOC candidates: none. `entities/` holds no live page.
- Lint at the close of the run, 74 findings (77 before the librarian's run per the
  handoff):
  - 62 × `decisions/decision-case-<1–28>: schema: missing section ## Context` /
    `## Problem` (31 pages, the Cases 1–28 — the sprint's closing item).
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`,
    `orphan: no other live page names it in its frontmatter` (3).
  - `estimates/estimate-lint-catches: ref: body names slug, which no live or archived page
    carries`
  - `rules/rule-subagent-guppi: deferred: 14 times since case 29`
  - `rules/rule-work-mode: deferred: 14 times since case 29`
  - `estimates/estimate-brief-written`, `-carry-over-writes`, `-end-of-work-order`,
    `-materialize-marks-superseded`: `unread: pending` (4).
  - `estimates/estimate-plan-mode-names-its-estimates: method: says by hand while
    estimate-pretask-checks-the-plan names a test file`
  - `estimates: unmigrated: 42 pages in the shape before case 193`

## Readings at the close

- `make test`: 396 passed.
- `make lint`: 74 findings, exit 1 (the list above).
- Live pages: rules 42, estimates 59, lessons 29, insights 11, decisions 285, entities 0.
  Archived this run: 1 decision page (`decision-case-191`).
