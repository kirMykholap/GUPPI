# Brief — 2026-09-17, after session 2238 of 2026-09-16 (the sprint as a page and `guppi sprint`; the recut sets `method`; pre-task bound by the stamp; materialize lifts by the schema)

Written by the librarian from `raw/2026-09-16/2238/handoff.md`, the yamls of
`raw/2026-09-16/1034`, `1651`, `1955` and `2238`, and the index Greps.

## Where things stand

- Cases 209–216, 221, 222 ratified and built in code in session 2238: `guppi/sprint.py` (new,
  `guppi sprint` in `cli.py`, `tests/test_sprint.py`), `guppi/generate.py` (211.1, 211.2: an
  Estimate `update` whose `set` carries `method` drops `## Context` and `## Method`; a
  `sections.Criterion` on a page without `method` and no `set.method` fails alone),
  `guppi/lint.py` (212), `guppi/pretask.py` (213.1, 213.2, 221: `--session <stamp>`),
  `guppi/materialize.py` (214.1: fields lifted by the category's `schema.yaml`, a stray key
  `unknown`). Tests 396 → 411, all green; `make style` clean; `render --check` 0. Commit
  `a4c3509` on `migration`.
- One-off in the session: the stray `ref` field removed from 15 Estimate pages by a script
  (210); the 21 open task lines of `raw/2026-09-16/1955/spec.md` ticked by hand (216).
- Rule-class by hand: `index.md` §1 and §7, `glossary.md` (the Sprint row),
  `case-schema.md` (`set.method` on a recut), `rules/schema.md` (`governs` on a `check`
  rule), `estimates/schema.md` and `schema.yaml`.
- Readings in the ledger, all `passed`: `estimate-materialize-marks-superseded`,
  `-end-of-work-order`, `-brief-written` (the 1955 brief), `-case-protocol-loaded`,
  `-permissions`, `-generate-writes`, `-generate-fails-alone`, `-lint-catches`,
  `-pretask-checks-the-plan`, `-pretask-hook-gates`, `-materialize-assembles` — 12 lines.
  One lesson. Cases 217, 218, 219, 220, 223 deferred.
- Not done in the session: every page create and update (this run), the three renders
  (this run), the first `guppi sprint` (this run), the readings listed below,
  `rule-carry-over`'s stray `ref` (defer 223). `sprint.md` was not edited by hand.
- This run. `materialize` walked four units: 1034, 1651, 1955 extended with 0 entries (the
  1034 and 1955 yamls gained `superseded_by: 222` on the entries of cases 192 and 205), 2238
  written with 55 entries, no `unknown`, no `incomplete`, no `failed`. Two synthesis entries
  appended (57). `generate`: 67 pages written or changed from 2238, 0 from the three others;
  stderr empty; exit 0; every entry `applied`. Counts of the 2238 yaml:
  - `create`: 1 rule (`rule-sprint`, `ref: rule-documentation`, `enforcement: check`,
    `governs: vault/wiki/sprint.md`); 1 entity (`entity-sprint-migration`, MOC, the first
    live page under `entities/`); 4 estimates (`estimate-sprint-renders-the-backlog`,
    `estimate-sprint-migration-lint-clean`, `-leftovers-gone`, `-merges`); 1 lesson
    (`lesson-ledger-block-followed-by-a-tool-call`, `error`); 27 Decision pages (209,
    209.1–209.7, 211.1–211.4, 212, 213.1–213.4, 214.1, 214.2, 215, 217–223). New tag
    `sprint` in `tags.md`.
  - `update`: 3 rule pages (`rule-documentation` 209.5, `rule-brief` 209.6, `rule-pretask`
    213.3); 17 Estimate entries on 12 pages (`estimate-documentation-completes` 209.5,
    `-brief-written` 209.6, `-generate-writes` 211.1 and 211.3, `-generate-fails-alone`
    211.2, `-generate-walks-dates`, `-lint-catches` 211.3 and 212, `-pretask-reconciles`
    211.3 and 213.3, `-materialize-assembles` 211.3 and 214.1, `-pretask-checks-the-plan`
    213.1 and 221, `-pretask-hook-gates` 213.2, `-permissions` 215); 4 Insight entries on 2
    pages (213.4, 214.2, 222 twice with `supersedes` 205 and 192); 7 Rule-class file entries
    printed "a Rule-class file, applied by hand".
  - `defer`: 7 targets in 5 Cases — `rule-page-generation` (217), `rule-work-mode` and
    `rule-subagent-guppi` (218), `rule-spec-box` (219), `rule-git-context` and
    `rule-github-issues` (220), `rule-carry-over` (223); all `exists`, `deferred_by`
    appended, no placeholder.
  - `estimate`: 12 reading entries, all `passed`. `lesson`: 1.
  - Synthesis: 2 entries `librarian: synthesis` (Flags).
  - Cascade: `rule-end-of-work` and `rule-materialize` `draft` → `built`;
    `rule-documentation`, `rule-page-generation`, `rule-pretask` `built` → `draft` (an
    Estimate of each recut to `pending`); `insight-ledger-hi-tied-to-its-session-by-position`
    `actioned` (`addressed_by: decision-case-213.1`), `deferred_by` cleared, severity 0;
    `insight-materialize-lift-loses-a-schema-field` `actioned` (`addressed_by:
    decision-case-214.1`), severity 0; `decision-case-192` and `decision-case-205`
    `superseded`; `lesson-pretask-check-session-fallback-stops-at-midnight` and
    `lesson-materialize-item-ref-lifted-as-a-page-field` `archived` (their siblings were
    archived by earlier runs).
  - `cleanup`: 4 pages moved to `archive/migration/2026-09-17/2238/` — `decisions/
    decision-case-192`, `decisions/decision-case-205`, the two lessons above. `render`:
    `.claude/agents/librarian-guppi.md` (209.5, step 5), `.claude/skills/pre-task/SKILL.md`
    (213.3); `render --check` exit 0.
  - `guppi sprint` (step 5, the first render): exit 0, stderr empty; `vault/wiki/sprint.md`
    written whole from `entity-sprint-migration` — the three Done-when lines `pending`, the
    backlog of Slices 3b, 4, 5 with six unticked items and the status and `deferred_by` of
    each page (`rule-work-mode`, `rule-subagent-guppi`, `rule-spec-box` `draft`; the three
    Estimates `pending`), the Closed section from the page.
  - `deferred_by` now: `rule-work-mode`, `rule-subagent-guppi` by `decision-case-183`, `-206`,
    `-218`; `rule-spec-box` by `-207`, `-219`; `rule-page-generation` by `-217`;
    `rule-git-context`, `rule-github-issues` by `-220`; `rule-carry-over` by `-223`.

## Readings due

Nine Estimates stand `pending`, none `failed`. The 2238 Spec carries a `- [ ] read <slug>`
line for seven of them, the slug alone; the place is the page's `method` in every case.

- `estimate-sprint-renders-the-backlog` — `rule-sprint` (`draft`); read: `pytest
  tests/test_sprint.py` (5 tests, green in the session), plus one reading of the rendered
  `sprint.md` after the librarian's run. Facts of this run: `guppi sprint` exit 0, no
  stderr, `sprint.md` rewritten whole (45 lines changed), six backlog items each with the
  status of its page; the reading is the next session's line.
- `estimate-documentation-completes` — `rule-documentation` (`draft`); read: `make
  test-documentation`, plus the live reading by hand. Facts of this run: materialize, index
  check, synthesis, generate, cleanup, render, sprint, brief, archive, commit, in that
  order; no stderr from any script. The page keeps its five `### case` blocks by the
  Case's word (counted by `unmigrated`).
- `estimate-brief-written` — `rule-brief` (`draft`); read: one reading by hand after the
  first librarian run, recorded in the estimate line — this brief, written without a
  sprint edit.
- `estimate-pretask-reconciles` — `rule-pretask` (`draft`); read: one reading by hand,
  written into the estimate line — the next `/pre-task` with `--session <stamp>`.
- `estimate-generate-walks-dates` — `rule-page-generation` (`draft`); read:
  `tests/test_generate.py` with two dated folders; live, the librarian's first run. Set
  `pending` by the recut of 211.3 (`set.method`); not in the handoff's list of readings due;
  no `- [ ] read` line in the Spec.
- `estimate-carry-over-writes` — `rule-carry-over` (`draft`); read: pytest over the skill's
  render, plus one live reading of a carried-over session — a live `/carry`, none yet.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` (`draft`); read:
  `make lint` exit 0, or only `unread` lines on the Estimates of `entity-sprint-migration`;
  the close of the sprint.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` (`draft`); read:
  one reading of the tree by hand at the close of the sprint, each path and decision named
  in the estimate line (`vault/parked/`, the 2026-08 documents, the old archive root, the
  empty raw date folders; decisions 11.1 and 11.2 taken again — defer 220).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` (`draft`); read: `make
  test` on the last commit of `migration`, then `git log` of `main` after the merge.

## Deferred

1. **`insight-ledger-hook-reads-only-the-final-text`** — `open`, severity 1, reopened by
   this run (was `actioned` by `decision-case-137`); fifth child
   `lesson-ledger-block-followed-by-a-tool-call`. Pattern: the ledger writer sees the last
   text of a turn, not the turn; a LEDGER block anywhere else in the turn is never written.
   Proposal: read `guppi/ledger.py` (`transcript_texts` and the filter that picks the main
   agent's messages) against a transcript and settle whether an intermediate assistant text
   is in the transcript at all; if present, collect every assistant text of the `hi` window
   instead of the last one, if absent, the writer needs a second event beside `Stop`; either
   way count back blocks seen against lines written and show it at `/hi`. In Plan Mode a
   Case whose `recommend` starts from that Proposal, ending in an `update` of the Insight
   (`status: actioned`, `addressed_by`), a rejection written the same way, or a `defer` with
   the Insight as its target. (stood in 1 brief)
2. **`rule-work-mode`** — cases 183, 206, 218, Slice 3b: "Work Mode: the Spec as tasks with
   code, the ticked boxes in spec.md, the test of each Estimate written first and turned
   green; who ticks which task line (case 217); the Plan Mode of a session of its own, the
   first open Slice of the sprint page." Placeholder, `draft`; lint: `deferred: 15 times
   since case 29`. (stood in 19 briefs)
3. **`rule-subagent-guppi`** — cases 183, 206, 218, Slice 3b: "what a subagent may do in Work
   Mode, and the fork that comes back to the main agent as a Case; with rule-work-mode, the
   next session." Placeholder, `draft`; lint: `deferred: 15 times since case 29`. (stood in
   19 briefs)
4. **`rule-spec-box`** — cases 207, 219, after Slice 3b: "the Spec box of case 207 — a
   conserved Spec run in a worktree on its own branch, Work Mode only, the librarian once
   after the merge; its open questions as 207 left them: the skill and its conditions, the
   ledger hook and guppi gate inside a worktree, the cut of a Spec into boxes, a third end
   of a session, subagent or session." Placeholder, `draft`. (stood in 2 briefs)
5. **`rule-page-generation`** — case 217, with Slice 3b: "generate ticks, in the session's
   spec.md, the task line under the entry's Case whose kind and slug it names — `- [ ]
   create <slug>` / `update <slug>` / `defer <slug>` — once the entry applied, and the
   librarian's render step ticks its `guppi render` line the same way; a line not found is
   no error; the lines on code, tests, migrations and readings stay the agent's; the script
   reads the Spec, not the librarian — said in the Criterion; a one-off tick of the older
   Specs is case 216, not this; with Slice 3b, which fixes who ticks what." `draft`. (stood
   in 1 brief)
6. **`rule-git-context`** — case 220, the close of the sprint: "the pull without an upstream
   at /hi — set the upstream of `migration`, or keep the printed failure as the decision
   11.1 made it; at the close of the sprint, read by
   estimate-sprint-migration-leftovers-gone." `built`. (stood in 1 brief)
7. **`rule-github-issues`** — case 220, the close of the sprint: "gh not logged in, no GitHub
   remote — log in and add the remote, or keep the printed line as decision 11.2 made it; at
   the close of the sprint, read by estimate-sprint-migration-leftovers-gone." `built`.
   (stood in 1 brief)

Over the cap of seven: `rule-carry-over` — case 223, the next Plan Mode: "drop the stray
`ref` field from `rule-carry-over`, a one-off like case 210 — a script run once by path and
a History line with the pointer." `draft`, `deferred_by: decision-case-223`; also Flags,
item 1 of the handoff. Retired from the previous brief:
`insight-ledger-hi-tied-to-its-session-by-position` (`actioned` by 213.4; its defers 192 and
205 superseded by 222) and `insight-materialize-lift-loses-a-schema-field` (`actioned` by
214.2).

## Flags

- Entries: no `incomplete`, `failed`, `near` or `unparsed` in the four yamls; no `unknown`
  key. Index check: `rule-sprint` against the 49 lines of the rules Grep — nothing the
  same; the closest by mechanism is `rule-render-harness` (a page rendered into a governed
  file), whose subject is the harness files, not the sprint — not near.
  `entity-sprint-migration` against the entities Grep (2 lines, both schema examples) —
  nothing.
- Synthesis, against 31 lesson lines and 13 insight lines:
  `lesson-ledger-block-followed-by-a-tool-call` clustered under
  `insight-ledger-hook-reads-only-the-final-text` — the same condition, the block not the
  last text of the turn (a ToolSearch call followed it). The Insight was `actioned`
  (`addressed_by: decision-case-137`): set `open` again, severity 0 → 1, `addressed_by`
  stays, its four earlier children stay archived. The handoff expected the lesson alone,
  no cluster.
- Handoff flags, each a Case of the next Plan Mode:
  1. `rule-carry-over` carries a stray `ref: rule-end-of-work` field (defer 223, over the
     cap above).
  2. `generate` ticking the page lines of a Spec (defer 217, with Slice 3b).
  3. Whether `sprint.md` should also be checked at `SessionStart` like `render --sync` —
     not in case 209.
  4. The unticked page lines of the 2238 Spec: 36 unticked `- [ ]` lines by grep, 7 of them
     `read` lines (the handoff counts 35 page lines); they stay open by case 217 and are not
     debt for the next Retro.
- `estimate-generate-walks-dates` `pending` after the recut of 211.3 and absent from the
  handoff's list of readings due (Readings due above); `rule-page-generation` `draft` by it.
- `estimate-case-protocol-loaded` read `passed` on the first turn of 2238, which stated
  the two rules; the person accepted the 1955 reading and this one (handoff).
- `estimate-documentation-completes` keeps five `### case` blocks beside its `method`
  field (209.5, by the Case's word); counted by `unmigrated`.
- `rule-spec-box` (placeholder): lint `schema: missing field kind`, `missing field
  estimates`, `orphan: no other live page names it in its frontmatter`.
- Stale defers: `rule-work-mode` and `rule-subagent-guppi`, `deferred: 15 times since case
  29` (lint), 19 briefs.
- Contradictions: none named by lint this run; the `method` finding on
  `estimate-plan-mode-names-its-estimates` left in Work Mode; the `ref: body names slug`
  finding on `estimate-lint-catches` left with its new Result, as the handoff said.
- MOC candidates: none. `entities/` holds one live page, `entity-sprint-migration` (MOC).
- Lint at the close of the run, 78 findings (74 after the previous run):
  - 62 × `decisions/decision-case-<1–28>: schema: missing section ## Context` /
    `## Problem` (31 pages, the Cases 1–28 — `estimate-sprint-migration-lint-clean`).
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`,
    `orphan: no other live page names it in its frontmatter` (3).
  - `rules/rule-subagent-guppi: deferred: 15 times since case 29`
  - `rules/rule-work-mode: deferred: 15 times since case 29`
  - `estimates/estimate-brief-written`, `-carry-over-writes`, `-documentation-completes`,
    `-generate-walks-dates`, `-pretask-reconciles`, `-sprint-migration-leftovers-gone`,
    `-sprint-migration-lint-clean`, `-sprint-migration-merges`,
    `-sprint-renders-the-backlog`: `unread: pending` (9).
  - `estimates: unmigrated: 34 pages in the shape before case 193`

## Readings at the close

- `make test`: 411 passed.
- `make lint`: 78 findings, exit 1 (the list above).
- Live pages: rules 43, estimates 63, lessons 28, insights 11, decisions 310, entities 1.
  Archived this run: 2 decision pages (`decision-case-192`, `decision-case-205`), 2 lessons
  (`lesson-pretask-check-session-fallback-stops-at-midnight`,
  `lesson-materialize-item-ref-lifted-as-a-page-field`).
