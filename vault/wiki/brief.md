# Brief — 2026-09-18, after session 1119 of 2026-09-17 (the ledger Insight settled; the Spec ticked by the scripts; the sprint as milestones; the categories discussion deferred)

Written by the librarian from `raw/2026-09-17/1119/handoff.md`, the yamls of
`raw/2026-09-16/2238` and `raw/2026-09-17/1119`, and the index Greps.

## Where things stand

- Ratified in session 1119: 224.1–224.3, 225, 226.1, 226.2, 227, 229.1–229.4, 233.1–233.5,
  234; deferred 230 (`index`), 231 (`rule-work-mode`, `rule-subagent-guppi`), 232
  (`rule-spec-box`). Readings `passed` in the ledger: `estimate-generate-walks-dates`,
  `estimate-documentation-completes`, `estimate-pretask-reconciles`,
  `estimate-ledger-write-lifts`. Three lessons.
- Code, commit `d64a399` on `migration`: `guppi/gate.py` (the advice), `guppi/generate.py`
  (`tick_spec`, `SECTION_ORDER`), `guppi/render.py` (`tick_render_lines`), `guppi/sprint.py`
  (`--check`, the render by milestone, the plain line), `Makefile` (`lint` — three steps);
  tests 411 → 424, all green; `make style` clean.
- One-off: the `ref` field removed from `rule-carry-over` by a script (225). Rule-class by
  hand: `entities/schema.md` and `schema.yaml`, `index.md` (the `sprint.md` row, §2),
  `glossary.md` (the Sprint row), `case-schema.md`.
- Not done in the session: every page create and update (this run); the five renders (this
  run); the first `guppi sprint` on the milestones page (this run); the readings below;
  Slice 3b; the definitions of the categories (230).
- This run. `materialize` walked two units: 2238 extended with 0 entries (its entries of
  cases 217 and 223 gained `superseded_by` 226.1 and 225), 1119 written with 43 entries, no
  `unknown`, no `incomplete`, no `failed`, `unparsed: []`. Three synthesis entries appended
  (46). `generate`: 61 pages written or changed from 1119, 0 from 2238; stderr empty; exit
  0; every entry `applied`. Counts of the 1119 yaml:
  - `create`: 3 estimates (`estimate-generate-ticks-the-spec` on `rule-page-generation`,
    `estimate-render-harness-ticks-the-spec` on `rule-render-harness`,
    `estimate-sprint-checks-the-file` on `rule-sprint`); 3 lessons
    (`lesson-transcript-keeps-the-text-before-a-tool-call` knowledge,
    `lesson-hi-substitution-refused-when-the-permission-classifier-is-unavailable`
    knowledge, `lesson-work-mode-check-reads-a-page-the-same-spec-changes` error); 1
    insight by synthesis (`insight-workflow-code-live-before-the-page-it-reads`); 20
    Decision pages (224.1–224.3, 225, 226.1, 226.2, 227, 229.1–229.4, 230, 231, 232,
    233.1–233.5, 234). No new tag.
  - `update`: 13 rule entries on 11 pages (`rule-ledger-write` 224.1, `rule-case-protocol`
    224.2, `rule-carry-over` 225 and 233.4, `rule-page-generation` 226.1,
    `rule-render-harness` 226.2, `rule-sprint` 227 and 229.2, `rule-lint` 227,
    `rule-skill-hi` 229.3, `rule-brief` 229.4, `rule-harness` 233.1, `rule-retro` 233.2);
    9 Estimate entries (`estimate-ledger-write-lifts` 224.1, `-case-protocol-loaded` 224.2,
    `-sprint-renders-the-backlog` 229.2, `-hi-writes-frontier` 229.3, `-brief-written`
    229.4, `-harness-pipeline` 233.1, `-retro-loads` 233.2, `-carry-over-writes` 233.4,
    `-sprint-migration-lint-clean` 233.5); 1 entity (`entity-sprint-migration` 229.1,
    `## Milestones` and `## Backlog`); 1 insight (`insight-ledger-hook-reads-only-the-final-text`
    224.3, `actioned`, `addressed_by: decision-case-224.3`, the `pattern` set); 2 lessons by
    synthesis; 6 Rule-class file entries printed "a Rule-class file, applied by hand"
    (`entities-schema` 229.1, `index`, `glossary`, `case-schema` 233.3, `entities-schema-yaml`
    234).
  - `defer`: 4 targets in 3 Cases — `index` (230, a Rule-class file, no page, the Decision
    page alone), `rule-work-mode` and `rule-subagent-guppi` (231), `rule-spec-box` (232);
    the three rules `exists`, `deferred_by` appended, no placeholder.
  - `estimate`: 4 reading entries, all `passed`. `lesson`: 3.
  - Cascade: `rule-documentation` and `rule-pretask` `draft` → `built`;
    `rule-case-protocol`, `rule-harness`, `rule-render-harness`, `rule-retro`,
    `rule-skill-hi` `built` → `draft` (an Estimate of each recut to `pending`);
    `rule-page-generation`, `rule-sprint`, `rule-brief`, `rule-carry-over` stay `draft`;
    `insight-ledger-hook-reads-only-the-final-text` `actioned`, severity 1 → 0;
    `lesson-ledger-block-followed-by-a-tool-call` `archived` (its Insight actioned);
    `decision-case-217` and `decision-case-223` `superseded`; `deferred_by` cleared on
    `rule-page-generation` and `rule-carry-over`.
  - The Spec `raw/2026-09-17/1119/spec.md`: `generate` ticked 27 page lines (the first live
    tick, 226.1); `render` ticked 5 render lines here and 3 in the 2238 Spec, plus one
    reading line (Flags).
  - `cleanup`: 3 pages moved to `archive/migration/2026-09-18/1119/` —
    `decisions/decision-case-217`, `decisions/decision-case-223`,
    `lessons/lesson-ledger-block-followed-by-a-tool-call`. `render`: `CLAUDE.md` (224.2),
    `.claude/skills/hi/SKILL.md` (229.3), `.claude/agents/librarian-guppi.md` (229.4),
    `.claude/skills/retro/SKILL.md` (233.2), `.claude/skills/carry/SKILL.md` (233.4);
    `render --check` exit 0.
  - `guppi sprint` (step 5): exit 0, stderr empty; `vault/wiki/sprint.md` written from the
    milestones page — Slice 3b whole (two items, `draft`, four `deferred_by` each), Slices 4
    and 5 one line each, the Backlog two plain lines, the three Done-when lines `pending`.
    `make lint`'s `sprint --check` step is green after this run.
  - `deferred_by` now: `rule-work-mode`, `rule-subagent-guppi` by `decision-case-183`, `-206`,
    `-218`, `-231`; `rule-spec-box` by `-207`, `-219`, `-232`; `rule-git-context`,
    `rule-github-issues` by `-220`.

## Readings due

Thirteen Estimates stand `pending`, none `failed`. The 1119 Spec carries a `- [ ] read <slug>`
line for eight of them; for the other five the place is the page's `method`.

- `estimate-case-protocol-loaded` — `rule-case-protocol` (`draft`); read: the first turn of
  the next session, by hand (Spec line).
- `estimate-generate-ticks-the-spec` — `rule-page-generation` (`draft`); read: pytest, plus
  the page lines of the 1119 Spec ticked by this run — 27 ticked (Spec line).
- `estimate-render-harness-ticks-the-spec` — `rule-render-harness` (`draft`); read: pytest,
  plus the `guppi render` lines of the 1119 Spec ticked by this run — 5 ticked, and the read
  line itself was ticked by the render (Flags); the Spec line stands `[x]` although the
  reading is not taken.
- `estimate-sprint-checks-the-file` — `rule-sprint` (`draft`); read: pytest, plus `make lint`
  after this run — no `sprint:` line: this run's `make lint` printed none (Spec line).
- `estimate-sprint-renders-the-backlog` — `rule-sprint` (`draft`); read: pytest, plus
  `sprint.md` after this run (Spec line).
- `estimate-hi-writes-frontier` — `rule-skill-hi` (`draft`); read: the first `/hi` of the
  next session — a Frontier without Slices 4 and 5 (Spec line).
- `estimate-brief-written` — `rule-brief` (`draft`); read: this brief — `rule-work-mode`,
  `rule-subagent-guppi`, `rule-spec-box` not in Deferred (Spec line).
- `estimate-harness-pipeline` — `rule-harness` (`draft`); read: `make test-harness`,
  `make lint` after the build of 227 (Spec line).
- `estimate-retro-loads` — `rule-retro` (`draft`); read: the `/retro` of this session (Spec
  line, written before the session's own Retro; the next `/retro`).
- `estimate-carry-over-writes` — `rule-carry-over` (`draft`); read: pytest over the skill's
  render, plus one live reading of a carried-over session — a live `/carry`, none yet
  (`method`).
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` (`draft`); read: `make
  lint` exit 0, or only `unread` lines on the Estimates of `entity-sprint-migration`; the
  close of the sprint (`method`).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` (`draft`); read:
  one reading of the tree by hand at the close of the sprint, each path and decision named
  in the estimate line (`method`).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` (`draft`); read: `make test`
  on the last commit of `migration`, then `git log` of `main` after the merge (`method`).

## Deferred

1. **`insight-workflow-code-live-before-the-page-it-reads`** — `open`, severity 2, created
   by this run over `lesson-reader-changed-before-its-writer-closed-the-live-session` (case
   111) and `lesson-work-mode-check-reads-a-page-the-same-spec-changes` (session 1119).
   Pattern: a Case changes a reader in code and the text it reads in a page or a governed
   file; the code of the working tree runs at once, the page lands at the librarian's run
   and the file at the render, so the reader refuses or goes red in between, by
   construction. Proposal: one sentence in `rule-work-mode` (Slice 3b, defer 231) — a check
   that reads a page or a file the same Spec updates is read after the librarian's run or
   the render, its red in Work Mode is an expectation named in the handoff, not a finding;
   a reader that drops an old form keeps it as a fallback until its writer is measured
   live. In Plan Mode a Case whose `recommend` starts from that Proposal, ending in an
   `update` of the Insight (`status: actioned`, `addressed_by`), a rejection written the
   same way, or a `defer` with the Insight as its target. (stood in 1 brief)
2. **`rule-git-context`** — case 220, the close of the sprint: "the pull without an upstream
   at /hi — set the upstream of `migration`, or keep the printed failure as the decision
   11.1 made it; at the close of the sprint, read by
   estimate-sprint-migration-leftovers-gone." `built`. (stood in 2 briefs)
3. **`rule-github-issues`** — case 220, the close of the sprint: "gh not logged in, no GitHub
   remote — log in and add the remote, or keep the printed line as decision 11.2 made it; at
   the close of the sprint, read by estimate-sprint-migration-leftovers-gone." `built`.
   (stood in 2 briefs)
4. **`index`** — case 230, the next session, a Rule-class file without a page: "the
   definitions of Entity, Rule and Estimate for development — or the category set as data of
   the project; from raw/2026-09-17/1119/categories-discussion.md; the next session."
   `decision-case-230`. (stood in 1 brief)

Left out by case 229.4, the sprint page names them: `rule-work-mode` and
`rule-subagent-guppi` (defers 183, 206, 218, 231; Slice 3b, the first open milestone),
`rule-spec-box` (defers 207, 219, 232; Slice 5). Retired from the previous brief:
`insight-ledger-hook-reads-only-the-final-text` (`actioned` by 224.3),
`rule-page-generation` (defer 217 superseded by 226.1), `rule-carry-over` (defer 223
superseded by 225).

## Flags

- Entries: no `incomplete`, `failed`, `near` or `unparsed` in the two yamls; no `unknown`
  key. Index check: the three creates are Estimates, which have no index — no Grep run for
  them.
- Synthesis, against 30 lesson lines and 12 insight lines:
  - `lesson-work-mode-check-reads-a-page-the-same-spec-changes` and
    `lesson-reader-changed-before-its-writer-closed-the-live-session` (`new`, case 111)
    share the cause — the code of the working tree is live in the session that writes it,
    the page or file it reads lands later; no Insight had it. Created
    `insight-workflow-code-live-before-the-page-it-reads` (Deferred item 1), both lessons
    `clustered`. The handoff expected the lesson alone and one sentence for
    `rule-work-mode` in Slice 3b; the Proposal says that.
  - `lesson-transcript-keeps-the-text-before-a-tool-call` not clustered, as the handoff
    said: its cause is the opposite of the old pattern of
    `insight-ledger-hook-reads-only-the-final-text`; the Insight's `pattern` was set by
    224.3 and it stays `actioned`. Stays `new`.
  - `lesson-hi-substitution-refused-when-the-permission-classifier-is-unavailable` — no
    lesson or Insight with the cause (the closest by subject,
    `insight-retro-typed-command-is-never-a-tool-call`, is about the Skill tool, not the
    permission classifier). Stays `new`.
- `render` ticked a reading line: `- [ ] read estimate-render-harness-ticks-the-spec: pytest,
  plus the `guppi render` lines of this Spec …` holds `guppi render` in a code span and
  `tick_render_lines` took it for a render line. The Estimate stands `pending`; the Spec
  line is `[x]` without a reading. The handoff expected 5 render ticks; 6 were made in the
  1119 Spec, and 3 in the 2238 Spec (its yaml applied whole). A Case of the next Plan Mode
  (`rule-render-harness`, the Criterion of 226.2).
- Contradiction: `lesson-transcript-keeps-the-text-before-a-tool-call` (knowledge, session
  1119) states the opposite of `lesson-transcript-omits-text-emitted-before-tool-calls`
  (archived, a child of `insight-ledger-hook-reads-only-the-final-text`); settled by 224
  in favour of the new one, the old lesson stays archived as it is.
- Handoff flags, each a Case of the next Plan Mode:
  1. The definitions of the categories — defer 230, the record in
     `raw/2026-09-17/1119/categories-discussion.md` (Deferred item 4).
  2. One sentence for `rule-work-mode` on a check that reads a page the Spec updates —
     Slice 3b, defer 231 (the Proposal of Deferred item 1).
  3. `schema-prose` in lint reads one section per table row of a `schema.md` — three
     sections in one cell gave two false findings; the row was split in the session.
  4. `render --sync` at `/hi` refused by the permission classifier once — the lesson
     `lesson-hi-substitution-refused-when-the-permission-classifier-is-unavailable`.
  5. `rule-git-context` / `rule-github-issues` (defer 220) still at the close of the
     sprint (Deferred items 2, 3).
- `estimate-ledger-write-lifts`: recut to `pending` by 224.1 and read `passed` in the same
  session (ledger line 40); the page ends `passed`, `rule-ledger-write` `built`.
- `estimate-generate-walks-dates`: read `passed` against the Criterion as recut by 211.3
  (the `method` fields), not against "walks dates"; the person accepted (handoff).
- `rule-spec-box` (placeholder): lint `schema: missing field kind`, `missing field
  estimates`, `orphan: no other live page names it in its frontmatter`.
- Stale defers: `rule-work-mode` and `rule-subagent-guppi`, `deferred: 16 times since case
  29` (lint), 20 briefs; on the sprint page, not in Deferred (229.4).
- The archive folder of this run is `archive/migration/2026-09-18/1119/`: the run's clock
  passed midnight, the unit is `raw/2026-09-17/1119`.
- MOC candidates: none. `entities/` holds one live page, `entity-sprint-migration` (MOC).
- Lint at the close of the run, 81 findings (78 after the previous run):
  - 62 × `decisions/decision-case-<1–28>: schema: missing section ## Context` /
    `## Problem` (31 pages, the Cases 1–28 — `estimate-sprint-migration-lint-clean`).
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`,
    `orphan: no other live page names it in its frontmatter` (3).
  - `rules/rule-subagent-guppi: deferred: 16 times since case 29`
  - `rules/rule-work-mode: deferred: 16 times since case 29`
  - `estimates/estimate-brief-written`, `-carry-over-writes`, `-case-protocol-loaded`,
    `-generate-ticks-the-spec`, `-harness-pipeline`, `-hi-writes-frontier`,
    `-render-harness-ticks-the-spec`, `-retro-loads`, `-sprint-checks-the-file`,
    `-sprint-migration-leftovers-gone`, `-sprint-migration-lint-clean`,
    `-sprint-migration-merges`, `-sprint-renders-the-backlog`: `unread: pending` (13).
  - `estimates: unmigrated: 29 pages in the shape before case 193` (34 before this run).
  - No `render:` line and no `sprint:` line: the first two steps of `make lint` are green.

## Readings at the close

- `make test`: 424 passed.
- `make lint`: 81 findings, exit 1 (the list above).
- Live pages: rules 43, estimates 66, lessons 30, insights 12, decisions 328, entities 1.
  Archived this run: 2 decision pages (`decision-case-217`, `decision-case-223`), 1 lesson
  (`lesson-ledger-block-followed-by-a-tool-call`).
