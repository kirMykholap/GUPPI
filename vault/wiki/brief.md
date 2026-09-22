# Brief — 2026-09-22, after session 1121 of 2026-09-22 (Slice 3f themes 4–6: `rule-vault-layout` by 315, `rule-session` by 316, `rule-atomicity` by 317, `index.md` and its pointers gone by 318, the `file` route out of the scripts by 320, "Rule-class" retired by 321, the Slice closed by 321; Slice 3b deferred by 322, the nineteenth)

Written by the librarian on 2026-09-22 from `raw/2026-09-22/1121/handoff.md`, the yamls of
`raw/2026-09-22/1121` and `raw/2026-09-22/0014`, `tags.md` and the Greps of the indexes.

## Where things stand

- Ratified by the session: 21 Cases, 308.1 through 323, plus the defer 322. Cases 310.1 and
  310.4 were superseded in the session by 313 and 320 and left the Spec.
- Code, commit `bfe18d9` on `migration`: `guppi/lint.py` gained `check_layout` (315);
  `guppi/sprint.py` takes every wikilink before the first " — " as the pages of an item and
  renders a note without a tick (313); `guppi/prespec.py` accepts the closer `sprint`, binds a
  sprint line to an `update` of the sprint page and refuses any item carrying `file` (310.6,
  314.2, 320); `guppi/materialize.py` lifts a create whole when the unit changes that category's
  schema rule, moves a folded reading on a supersede, and lost `RULE_CLASS`, `rule_class_path`
  and the `category: file` route (308.2, 309, 320); `guppi/generate.py` ticks every `read` line
  of a slug in the first Spec that holds one and lost the Rule-class branch (312, 320).
  `vault/wiki/index.md` was deleted by hand in Work Mode; it is absent.
- Not done by the session's own account: the pages — this run; eight readings whose moment had
  not come; the by-hand check of 308.1; Slice 3b, deferred by 322.
- Two units in the walk. `raw/2026-09-22/1121`: 92 entries lifted, 3 added by the librarian
  (synthesis), 95 in all — 11 readings, 2 lessons, 2 defers, 1 delete of an Estimate, 1 delete
  of `index.md`, 12 creates, 66 updates — and 23 Decision records. `unparsed: []`. Applied: 91;
  3 skipped as `superseded_by` (2 of 310.1, 1 of 310.4); 1 `incomplete` applied (below). 82
  pages written or changed. `raw/2026-09-22/0014`: `materialize` extended it with 0 entries, 0
  pages written or changed.
- Decisions: 23 pages written — 21 live (308.1, 308.2, 309, 310.2, 310.3, 310.5, 310.6, 311,
  312, 313, 314.1, 314.2, 315, 316, 317, 318, 319, 320, 321, 322, 323) and 2 moved by `cleanup`
  (310.1, 310.4, the superseded ones).
- Rules: 3 created — `rule-vault-layout` (Leaf under `rule-harness`, `enforcement: check`, born
  `built`), `rule-session` (MOC over the five phases, `draft`), `rule-atomicity` (Leaf under
  `rule-case-protocol`, `enforcement: render`, `render_mode: partial`, `draft`). 20 pages
  updated: `rule-ask`, `rule-case-protocol`, `rule-claude-md`, `rule-decisions-schema`,
  `rule-documentation`, `rule-end-of-work`, `rule-entities-schema`, `rule-glossary`,
  `rule-harness`, `rule-lint`, `rule-materialize`, `rule-page-generation`, `rule-plan-mode`,
  `rule-prespec`, `rule-rules-schema`, `rule-session-start`, `rule-skill-hi`, `rule-sprint`,
  `rule-subagent-guppi`, `rule-work-mode` (the last two by the defer 322, both `exists`). Every
  `replace` `old` hit; no `failed`.
- Entities: none created; 2 updated — `entity-glossary` (317, 318, 321, 323) and
  `entity-sprint-migration` (310.2, 318, 319, 320, 321, 323). The edge of 308.1 landed:
  `rule-glossary` carries `applies_to: ["[[entity-glossary]]"]` and `entity-glossary` carries
  `rules: ["[[rule-glossary]]"]`.
- Estimates: 8 created (`estimate-materialize-lifts-unfiltered-on-a-schema-change`,
  `estimate-materialize-refolds-a-reading-on-a-supersede`,
  `estimate-sprint-migration-index-dissolved`, `estimate-prespec-binds-a-sprint-line`,
  `estimate-vault-layout-holds`, `estimate-session-phases-in-order`,
  `estimate-atomicity-rendered`, `estimate-sprint-migration-file-route-gone`); 16 pages updated;
  1 deleted (`estimate-materialize-finds-a-rule-class-item`, by 320); 11 readings applied — 10
  `passed`, 1 `failed` (`estimate-documentation-completes`). The two readings the previous brief
  reported lost to a supersede, `estimate-rules-schema-checked` and
  `estimate-entities-schema-checked`, were written again this session and both landed `passed`.
- Lessons: 2 created, both clustered by the librarian. Insights: 1 created,
  `insight-workflow-edit-pair-signed-from-a-grep-fragment`, `open`, `severity` 2.
- The handoff's order check, done before `generate`: every `replace` pair of the Spec was
  simulated in entry order against the pages on disk, whitespace collapsed as `generate`
  collapses it. All 71 anchors hit exactly once. 314.2's `old` is produced by 310.6's `new` and
  follows it (entries 12 and 21); the pairs of 310.2, 318, 319 and 320 on `## Milestones` all
  precede 321's whole-section write (entries 7, 48, 54, 65 before 69), and 323's Purpose write
  is last (72). `generate` then applied them with no stderr, which confirms the simulation.
- Index check: the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/`, 61 lines, for the
  three rule creates (the five estimate creates have no index). No line names the same thing.
  `rule-vault-layout` stands beside `rule-lint` (the checker of pages, not the place of files)
  and `rule-index-check` (a page born twice, not a file misplaced) — other things, not near.
  `rule-session` stands beside `rule-session-start` — its own child, a phase, not the chain.
  `rule-atomicity` stands beside `rule-case-protocol` and `rule-prespec` — its parent and its
  one mechanical guard. One page opened: `vault/wiki/rules/rule-case-protocol.md`, because the
  index line could not say whether `rule-atomicity` repeats the `## Splitting` section that
  stays there; it does not — `## Splitting` is the sub-case machinery on a follow-up question,
  `rule-atomicity` is the test of when a unit splits at all. No `near` mark, no entry merged.
- Synthesis: the Greps `^(root_cause|deferred_by):` over `vault/wiki/lessons/` (44 lines) and
  `^(pattern|deferred_by):` over `vault/wiki/insights/` (16 lines). One page opened:
  `vault/wiki/lessons/lesson-reword-pairs-signed-before-the-places-were-read.md` (Trigger and
  Root cause), because its index line is cut before the cause is stated; clustered. Both lessons
  name an edit pair signed from a grep fragment without reading the place. No Insight held that
  pattern, so three entries were appended:
  `create insights insight-workflow-edit-pair-signed-from-a-grep-fragment` with both lessons as
  `children`, and an `update` of each lesson with `set: {status: clustered, insight: …}`. Neither
  lesson entry carried `addressed_by`, so the Insight is born `open`.
  `lesson-tests-coupled-to-a-signature-or-a-whole-finding-list` found no pair and stays `new`.
- `cleanup` moved 3 pages to `archive/migration/2026-09-22/1121/`: `decision-case-310.1`,
  `decision-case-310.4` (superseded) and `estimate-materialize-finds-a-rule-class-item` (deleted
  by 320). No stderr.
- `guppi render` exited 1 and wrote nothing (Flags). `guppi sprint` rewrote
  `vault/wiki/sprint.md`: Slice 3f out of Milestones and into Closed, the sixth `Done when` line
  ticked. `guppi glossary` rewrote `vault/wiki/glossary.md`. Neither had stderr. `tags.md`
  registers no new tag.
- Tests: 548 passed, 2 skipped (`make test`).

## Readings due

`estimate-documentation-completes` stands `failed` after `generate`.

- `estimate-documentation-completes` — `rule-documentation` stands `draft` — read by its
  `method`: `make test-documentation`, then the live reading by hand. The reading of 2026-09-22
  failed on one clause: the 0014 librarian read lines 52–64 of `raw/2026-09-22/0014/ledger.md`
  while counting entries and the Criterion says no ledger; step 6, the commit and
  `make test-documentation` were all green.
- `estimate-atomicity-rendered` — `rule-atomicity` stands `draft` — read at line 694 of
  `raw/2026-09-22/1121/spec.md`: `make lint` — `render --check` exit 0; the text between the
  markers of `case-schema.md` read by hand.
- `estimate-case-protocol-case-form` — `rule-case-protocol` stands `draft` — read at line 959 of
  the 1121 Spec: with `estimate-generate-fails-alone` and `estimate-generate-ticks-the-spec`,
  their Criteria changed.
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` stands `draft` — read at line
  814 of the 1121 Spec: by hand at a session start — `case-schema.md` alone now.
- `estimate-generate-fails-alone` — `rule-page-generation` stands `draft` — read at line 959 of
  the 1121 Spec, with the two above.
- `estimate-harness-pipeline` — `rule-harness` stands `draft` — read at line 304 of the 1121
  Spec: `make test-harness`, then `make lint` — the three checks silent, `guppi lint` its own
  count.
- `estimate-hi-writes-frontier` — `rule-skill-hi` stands `draft` — read at line 236 of the 1121
  Spec: by hand at the first `/hi` of the next session.
- `estimate-session-phases-in-order` — `rule-session` stands `draft` — read at line 599 of the
  1121 Spec: by hand at the close of this session — the six marks in order.
- `estimate-sprint-migration-index-dissolved` — `entity-sprint-migration` stands `draft` — read
  at line 813 of the 1121 Spec: `test -e vault/wiki/index.md` false; `rg` over `vault/wiki`,
  `.claude`, `guppi`, `CLAUDE.md` — empty but for the archive and `raw/`.
- `estimate-sprint-migration-rule-class-files-dissolved` — `entity-sprint-migration` stands
  `draft` — read at line 1054 of the 1121 Spec: `ls vault/wiki/*/schema.md` empty,
  `vault/wiki/index.md` absent, the `rg` over `guppi/` empty, `render --check`,
  `glossary --check`, `make lint` exit 0.
- `estimate-synthesis-keeps-actioned-by-the-mark` — `rule-synthesis` stands `draft` — no
  unticked line under `raw/`; by its `method`: one reading by hand of the yaml and the brief
  after the librarian's run on the first marked lesson clustered under an `actioned` Insight. Not
  this run: neither lesson carried `addressed_by`, and the Insight was born `open`.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — no unticked line; by its
  `method`: `make lint`, exit 0 — or only unread lines on the Estimates of
  `entity-sprint-migration`; at the close of the sprint.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — no unticked line; by
  its `method`: one reading of the tree by hand at the close of the sprint, each path and
  decision named in the estimate line.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — no unticked line; by its
  `method`: `make test` on the last commit of `migration`, then `git log` of `main` after the
  merge.

## Deferred

One item. The previous brief's list was empty. The two `defer` targets of this walk —
`rule-work-mode` and `rule-subagent-guppi` (defer 322, the nineteenth) — and
`insight-workflow-code-live-before-the-page-it-reads` (`open`, `severity` 2, defer 238) are
named by the sprint page under Slice 3b, and so are `rule-spec-box`, `rule-morph`,
`estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-merges` and
`estimate-sprint-migration-leftovers-gone`; the sprint is their window (case 229.4).

1. `insight-workflow-edit-pair-signed-from-a-grep-fragment` — `severity` 2, standing in 1 brief.
   Pattern: an edit pair — a `reword` or a `replace` — is signed from a grep fragment: the
   matched words are copied out as the anchor, and neither the sentence they sit in nor what an
   earlier Case of the same Spec leaves of it is read before the Case is ratified. Proposal: bind
   the pair to a read of its place in two halves — the procedure that already governs a `reword`
   widened to a `replace`, and a mechanical check that simulates the pairs of a Spec in entry
   order against the pages on disk, reporting an anchor that misses or is not unique with its
   Case, so the anchor is judged against the page as the Spec leaves it and not as it stands
   today.

## Flags

- `guppi render` exited 1: `render: rule-atomicity: ## Render is not wrapped in
  <!-- rule-atomicity --> … <!-- /rule-atomicity -->`. `own_text` in `guppi/render.py` requires
  the `## Render` section of every rendering page to open and close with its own marker lines;
  the `sections.Render` of the `create` of case 317 begins at `## Atomicity — when a unit
  splits`, with no markers. Case 317 put the marker pair into the body of `rule-case-protocol`,
  the source of `case-schema.md` — the receiving side — and not around the text of
  `rule-atomicity` itself. The entry stays as it is; the page is on disk as it was written.
- Because `plan()` raises before any file is written, `render` wrote **no** governed file this
  run. Every file it renders is stale. The Spec's five unticked `uv run guppi render` lines (235,
  433, 692, 810, 956) name: `.claude/skills/hi/SKILL.md`, `.claude/skills/pre-spec/SKILL.md`,
  `.claude/agents/ask-guppi.md`, `CLAUDE.md`, `vault/wiki/case-schema.md`,
  `vault/wiki/entities/schema.yaml`, `vault/wiki/decisions/schema.yaml`. They are left to the
  next session start. `make lint` stops at its first step for the same reason.
- `delete` of `index.md` marked `incomplete: [category]` and applied: the entry has
  `category: unknown` because a slug with no page prefix has no folder since case 320.
  `generate` printed `index: outside the vault, nothing to archive` and the file is absent. The
  Case's intent held; the entry shape did not.
- Three entries skipped as `superseded_by` and not applied, as the handoff said: `update
  rule-sprint` and `update estimate-sprint-renders-the-backlog` of 310.1 (superseded by 313),
  `create estimate-sprint-migration-file-route-gone` of 310.4 (superseded by 320). Two of them
  also carry `incomplete: [criterion]` from `materialize`; no page was written from either, so
  the marks describe entries that never landed. The live create of 320 wrote the Estimate.
- The handoff asked whether the extra lint finding `rules/rule-case-protocol: ref: body names
  index` survives. It does not: `guppi lint` has no `ref` finding at all. 318's pair hit.
- One Estimate with two `read` lines in two Specs, still: `estimate-lint-catches` was read
  `passed` this session and line 1134 of the 1121 Spec is ticked, while line 1105 of the 0014
  Spec stays unticked. `generate` ticks the first Spec that holds a line for the slug. The same
  defect the previous brief reported.
- New lint findings since the previous brief: `rules/rule-materialize: status: draft while every
  Estimate is passed` (308.2, 309 and 320 left its eleven Estimates all `passed`), and
  `estimates/estimate-sprint-migration-index-dissolved: method: names no tests/ file, pytest or
  make target and is not a reading`.
- Lint, gone since the previous brief: 5 `unread: pending`
  (`estimate-page-schemas-one-file-per-rule`, `estimate-rules-schema-checked`,
  `estimate-entities-schema-checked`, `estimate-glossary-terms-defined`,
  `estimate-case-protocol-loaded` — all read this session). New: 7 `unread`
  (`estimate-atomicity-rendered`, `estimate-case-protocol-case-form`,
  `estimate-case-protocol-ledger-line-form`, `estimate-generate-fails-alone`,
  `estimate-hi-writes-frontier`, `estimate-session-phases-in-order`,
  `estimate-sprint-migration-index-dissolved`); `estimate-documentation-completes` moved
  `pending → failed`. The stale-defer count of `rule-work-mode` and `rule-subagent-guppi`
  30 → 31. `unmigrated` stays 23.
- Stale defers by lint: `rule-work-mode` and `rule-subagent-guppi` 31 times since case 29;
  `rule-morph` 1 time since case 239.
- No MOC candidate. No entry marked `near`, `merged` or `unparsed`. No contradiction found
  between the entries of the walk and the pages.
- `rule-case-protocol` is now a MOC with one child, `rule-atomicity`. The handoff names the
  precedent (`rule-claude-md`, cases 272.2–272.3) and the risk: if pre-spec or lint ever judges a
  MOC by a count of children, this is the page that shows it.
- Standing: the defer of 238 on `insight-workflow-code-live-before-the-page-it-reads` without a
  `purpose`; `estimate-hi-no-read-calls` in the shape before case 193 by choice; `rule-spec-box`
  placeholder findings (`kind`, `estimates`, orphan); the comment in `pyproject.toml` lines 6–7
  naming "owner's decision D3" (no page).
- From the handoff, no page: the `## Work` lines of the Frontier were closed `· work` before
  their work was done, because `/pre-spec` refuses an open line and the readings happen in Work
  Mode after it; the form allows it, the two moments have come apart. Three Backlog notes of
  case 319 (the reuse edge, the question, the hook) wait to be cut into Cases; the third note
  records that a new module written beside an existing one in another file is caught by the vault
  query alone, never by a script.
- Lint, 85 findings, exit 1: 62 `decisions/decision-case-<1–28>` missing `## Context` and
  `## Problem` (31 pages, Slice 5); 2 `rules/rule-spec-box` schema (`kind`, `estimates`) and 1
  orphan; 14 unread (13 `pending`, 1 `failed` — the fourteen of Readings due); 3 deferred
  (`rule-morph` 1, `rule-subagent-guppi` 31, `rule-work-mode` 31); 1 status (`rule-materialize`);
  1 method (`estimate-sprint-migration-index-dissolved`); 1 `estimates: unmigrated: 23 pages in
  the shape before case 193`. `render --check`, `sprint --check` and `glossary --check` are not
  in the count: `render --check` fails on `rule-atomicity` as `render` does, the other two exit 0.

## Next session

Cases

- `rule-atomicity`'s `## Render` has no `<!-- rule-atomicity --> … <!-- /rule-atomicity -->`
  wrapper, so `guppi render` and `make lint` exit 1 and every governed file is stale. Whether the
  wrapper is added to the page by an `update`, or `render` is to place a partial's own markers
  itself; from this run.
- `estimate-documentation-completes` stands `failed`: the 0014 librarian read the ledger while
  counting entries. Whether the frame's wording is wrong or the run was; from the handoff and
  this run.
- The three Backlog notes of case 319 — the reuse edge `uses` / `used_by` between Entities, the
  second question of the vault query before a `create`, the lint finding on two Entities naming
  one path in `code_ref` — cut into Cases; from the handoff and the sprint page.
- The `## Work` lines of the Frontier close `· work` before their work is done, because
  `/pre-spec` refuses an open line and the readings happen after it; from the handoff's Retro.
- `rules/rule-materialize: status: draft while every Estimate is passed` — the page moves to
  `built` or an Estimate is added; from this run.
- `estimate-sprint-migration-index-dissolved`'s `method` names no `tests/` file, pytest or make
  target and is not a reading; from this run.
- One Estimate with two `read` lines in two Specs (`estimate-lint-catches`, 0014 line 1105):
  whether the second line is a form to refuse or a tick to add; standing from the previous brief
  and this run.
- Slice 3b — `rule-work-mode`, `rule-subagent-guppi` (defer 322, the nineteenth), with the
  sentence of `insight-workflow-code-live-before-the-page-it-reads` written into
  `rule-work-mode`; from the sprint page.
- `insight-workflow-edit-pair-signed-from-a-grep-fragment` (`open`, `severity` 2): its Proposal
  ratified, rejected or deferred; from Deferred above.

Work

- Read `estimate-documentation-completes` (`failed`) by its `method`: `make test-documentation`,
  then the live reading by hand.
- Read `estimate-atomicity-rendered` (1121 line 694), `estimate-case-protocol-case-form` and
  `estimate-generate-fails-alone` (line 959), `estimate-case-protocol-ledger-line-form` (line
  814), `estimate-harness-pipeline` (line 304), `estimate-hi-writes-frontier` (line 236),
  `estimate-session-phases-in-order` (line 599), `estimate-sprint-migration-index-dissolved`
  (line 813), `estimate-sprint-migration-rule-class-files-dissolved` (line 1054).
- Read `estimate-synthesis-keeps-actioned-by-the-mark`, `estimate-sprint-migration-lint-clean`,
  `estimate-sprint-migration-leftovers-gone` and `estimate-sprint-migration-merges` by their
  `method`; no date for the first, the close of the sprint for the other three.
- Run `uv run guppi render` once `rule-atomicity` renders, and tick the five `uv run guppi
  render` lines of the 1121 Spec (235, 433, 692, 810, 956) it stands for; then `make lint`.
- Unticked boxes: Spec 1121 lines 36, 202, 235, 236, 304, 433, 434, 599, 692, 694, 810, 813,
  814, 956, 959, 1054; Spec 0014 lines 1105 and 1544.
- Line 36 of the 1121 Spec, the by-hand check of 308.1, is satisfied by this run:
  `entity-glossary` carries `rules: ["[[rule-glossary]]"]` and `guppi lint` has no `ref` finding
  on the pair. The box is still open; only the `make lint` half of its text is blocked by the
  render failure.
- No ledger line of the walk went unapplied. The tree is clean after the commit of this run.

## Readings at the close

- `make test`: 548 passed, 2 skipped.
- `make lint`: exit 1 at its first step (`render --check`, `rule-atomicity`); `guppi lint` alone,
  85 findings.
- Pages: entities 4, rules 58, estimates 98, lessons 46, insights 16, decisions 464.
