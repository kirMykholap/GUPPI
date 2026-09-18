# Brief — 2026-09-18, after session 1252 of 2026-09-18 (the definitions of the categories; the sprint as a kind; the render line opens with the command; the collapsed milestone names its items; Slice 3b deferred again)

Written by the librarian from `raw/2026-09-18/1252/handoff.md`, the yamls of
`raw/2026-09-17/1119` and `raw/2026-09-18/1252`, and the index Greps.

## Where things stand

- Ratified in session 1252: 235, 236, 237, 239, 240.1–240.3, 241, 244; deferred 238
  (`insight-workflow-code-live-before-the-page-it-reads`), 242 (`rule-work-mode`,
  `rule-subagent-guppi`), 243 (`rule-git-context`, `rule-github-issues`). Readings `passed`
  in the ledger: `estimate-case-protocol-loaded`, `-hi-writes-frontier`, `-brief-written`,
  `-permissions`, `-generate-ticks-the-spec`, `-sprint-checks-the-file`,
  `-harness-pipeline`, `-retro-loads`. Four lessons.
- Code, commit `6843c93` on `migration`: `guppi/render.py` (`RENDER_LINE`), `guppi/sprint.py`
  (`item_name`, the collapsed line); tests 424 → 425; `make style` clean; `sprint.md`
  rewritten by `guppi sprint`.
- Rule-class by hand: `entities/schema.md`, `rules/schema.md` (the definition and a
  paragraph at the end of `### Enforcement`), `estimates/schema.md`, `glossary.md` (rows
  MOC, Leaf, Entity, Rule, Estimate, Sprint), `index.md` §6 (two paragraphs).
- One-off: `children: []` removed from `entity-sprint-migration`; the reading line of
  `estimate-render-harness-ticks-the-spec` in `raw/2026-09-17/1119/spec.md` back to `[ ]`.
- Not done in the session: every page create, update and defer of the Spec (this run); the
  readings below; `estimate-sprint-migration-lint-clean` (the close);
  `estimate-carry-over-writes` (a live `/carry`, none yet); Slice 3b (defer 242, the next
  session's first item); `rule-git-context` / `rule-github-issues` (defer 243, the close).
- This run. `materialize` walked two units: 1119 extended with 0 entries (its entry of case
  230 gained `superseded_by` 240.1), 1252 written with 38 entries, `unparsed: []`, no
  `failed`, one `incomplete` (Flags). Three synthesis entries appended (41). `generate`: 47
  pages written or changed from 1252, 0 from 1119; stderr empty; exit 0; every entry
  `applied`. Counts of the 1252 yaml:
  - `create`: 1 entity (`entity-sprint`, MOC, 241, `children` `[[entity-sprint-migration]]`);
    4 lessons (`lesson-hi-substitution-fails-when-the-login-has-lapsed` knowledge,
    `lesson-permissions-reading-taken-by-the-agent-who-cannot-see-the-prompt` error,
    `lesson-lint-schema-body-table-one-section-per-row` error,
    `lesson-pretask-session-flag-takes-the-id-not-the-hi-line` knowledge); 1 insight by
    synthesis (`insight-hi-skill-substitution-checked-by-a-model-call`); 1 placeholder rule
    (`rule-morph`, defer 239 without `ref`, `draft`); 12 Decision pages (235, 236, 237, 238,
    239, 240.1–240.3, 241, 242, 243, 244). No new tag.
  - `update`: 4 rule entries on 3 pages (`rule-render-harness` 235, `rule-sprint` 236 and
    241, `rule-permissions` 237); 4 Estimate entries (`estimate-render-harness-ticks-the-spec`
    235, `-sprint-renders-the-backlog` 236, `-permissions` 237,
    `-sprint-migration-lint-clean` 244, its Criterion under `sections: Criterion`); 2
    entity entries on `entity-sprint-migration` (239 `replace` on Slice 5 and the Backlog —
    the Backlog holds one line after; 241 `kind: Leaf`, `parent: [[entity-sprint]]`); 2
    lessons by synthesis (`clustered`); 9 Rule-class file entries printed "a Rule-class
    file, applied by hand" (`entities-schema`, `rules-schema`, `estimates-schema`,
    `glossary` ×4, `index` ×2; the handoff counted 8).
  - `defer`: 6 targets in 4 Cases — `insight-workflow-code-live-before-the-page-it-reads`
    (238), `rule-morph` (239, no page: a placeholder written), `rule-work-mode` and
    `rule-subagent-guppi` (242), `rule-git-context` and `rule-github-issues` (243); the five
    that exist got `deferred_by` appended.
  - `estimate`: 8 reading entries, all `passed`. `lesson`: 4.
  - Cascade: `rule-brief`, `rule-case-protocol`, `rule-harness`, `rule-page-generation`,
    `rule-retro`, `rule-skill-hi` `draft` → `built`; `rule-render-harness` and `rule-sprint`
    stay `draft` (an Estimate of each recut to `pending`); `rule-permissions` stays `built`
    (`estimate-permissions` `pending` by 237 and `passed` by the estimate line, `checked`
    2026-09-18); `decision-case-230` `superseded` by 240.1 (`index` has no page, nothing to
    clear); `entity-sprint-migration` `draft`, `kind: Leaf`; `entity-sprint` `draft`.
  - The Spec `raw/2026-09-18/1252/spec.md`: `generate` ticked 12 page lines; the Spec holds
    no `uv run guppi render` line, so `render` ticked nothing; three `- [ ] read` lines
    stand unticked (Readings due). The read line of the 1119 Spec (line 260, returned to
    `[ ]` in the session) stands `[ ]` after this render.
  - `cleanup`: 1 page moved to `archive/migration/2026-09-18/1252/` —
    `decisions/decision-case-230`. `render`: exit 0, stderr empty, no governed file changed
    (`CLAUDE.md` and `.claude/` clean after the run).
  - `guppi sprint` (step 5): exit 0, stderr empty; `vault/wiki/sprint.md` — Slice 3b whole
    (two items, `draft`, five `deferred_by` each), Slice 4 one line with its one item named,
    Slice 5 one line with four names, `[[rule-morph]]` the fourth; the Backlog one line;
    the three Done-when lines `pending`.
  - `deferred_by` now: `rule-work-mode`, `rule-subagent-guppi` by `decision-case-183`,
    `-206`, `-218`, `-231`, `-242`; `rule-spec-box` by `-207`, `-219`, `-232`;
    `rule-git-context`, `rule-github-issues` by `-220`, `-243`; `rule-morph` by `-239`;
    `insight-workflow-code-live-before-the-page-it-reads` by `-238`.

## Readings due

Six Estimates stand `pending`, none `failed`. The 1252 Spec carries a `- [ ] read <slug>`
line for three of them; for the other three the place is the page's `method`.

- `estimate-render-harness-ticks-the-spec` — `rule-render-harness` (`draft`); read: pytest,
  plus this session's Spec after the librarian's run — the `uv run guppi render` lines
  ticked, this reading line not (Spec line 45). Fact of this run: the 1252 Spec has no
  render line; the read line of the 1119 Spec, returned to `[ ]`, was not ticked by
  `render`.
- `estimate-sprint-renders-the-backlog` — `rule-sprint` (`draft`); read: pytest, plus
  `sprint.md` after the librarian's run — the lines of Slice 4 and Slice 5 with the names of
  their items (Spec line 89). Fact of this run: `sprint.md` above.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` (`draft`); read: `make
  lint` at the close of the sprint (Spec line 417).
- `estimate-carry-over-writes` — `rule-carry-over` (`draft`); read: pytest over the skill's
  render, plus one live reading of a carried-over session — a live `/carry`, none yet
  (`method`).
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` (`draft`); read:
  one reading of the tree by hand at the close of the sprint, each path and decision named
  in the estimate line (`method`).
- `estimate-sprint-migration-merges` — `entity-sprint-migration` (`draft`); read: `make test`
  on the last commit of `migration`, then `git log` of `main` after the merge (`method`).

## Deferred

1. **`insight-workflow-code-live-before-the-page-it-reads`** — `open`, severity 2, deferred
   by case 238 (`decision-case-238`; the defer's `purpose` is missing in the yaml, Flags).
   Children `lesson-reader-changed-before-its-writer-closed-the-live-session` and
   `lesson-work-mode-check-reads-a-page-the-same-spec-changes`. Pattern: a Case changes a
   reader in code and the text it reads in a page or a governed file; the code of the
   working tree runs at once, the page lands at the librarian's run and the file at the
   render, so the reader refuses or goes red in between, by construction. Proposal: one
   sentence in `rule-work-mode` (Slice 3b, defer 242) — a check that reads a page or a file
   the same Spec updates is read after the librarian's run or the render, its red in Work
   Mode is an expectation named in the handoff, not a finding; a reader that drops an old
   form keeps it as a fallback until its writer is measured live. In Plan Mode a Case whose
   `recommend` starts from that Proposal, ending in an `update` of the Insight (`status:
   actioned`, `addressed_by`), a rejection written the same way, or a `defer` with the
   Insight as its target. (stood in 2 briefs)
2. **`insight-hi-skill-substitution-checked-by-a-model-call`** — `open`, severity 2, created
   by this run over `lesson-hi-substitution-refused-when-the-permission-classifier-is-unavailable`
   (session 1119) and `lesson-hi-substitution-fails-when-the-login-has-lapsed` (session
   1252). Pattern: a `!` command of a skill is checked by a model call before it runs; when
   that call fails — a lapsed login, reported as the model unavailable — the substitution is
   refused and the Render: line comes back empty, while the SessionStart hook is not
   affected. Proposal: one sentence in `rule-skill-hi` — a refused `!` substitution at `/hi`
   is a lapsed login; the cure is `/login` and `/hi` again, not `render --check` by hand and
   not an allow entry for the command. In Plan Mode a Case whose `recommend` starts from
   that Proposal, ending in an `update` of the Insight (`status: actioned`, `addressed_by`),
   a rejection written the same way, or a `defer` with the Insight as its target. (stood in
   1 brief)
3. **`rule-git-context`** — case 243 (after 220), the close of the sprint: "the pull without
   an upstream at /hi — set the upstream of migration, or keep the printed failure as
   decision 11.1 made it; at the close of the sprint, read by
   estimate-sprint-migration-leftovers-gone." `built`. (stood in 3 briefs)
4. **`rule-github-issues`** — case 243 (after 220), the close of the sprint: "gh not logged
   in, no GitHub remote — log in and add the remote, or keep the printed line as decision
   11.2 made it; at the close of the sprint, read by
   estimate-sprint-migration-leftovers-gone." `built`. (stood in 3 briefs)

Left out by case 229.4, the sprint page names them: `rule-work-mode` and
`rule-subagent-guppi` (defers 183, 206, 218, 231, 242; Slice 3b, the first open milestone),
`rule-spec-box` (defers 207, 219, 232; Slice 5), `rule-morph` (defer 239; Slice 5, the
placeholder). Retired from the previous brief: `index` (defer 230 superseded by 240.1).

## Flags

- `incomplete`: the defer of case 238 (`insight-workflow-code-live-before-the-page-it-reads`)
  — `incomplete: [purpose]`, `unknown: [purpose]`: the `## Deferred` Case of the Spec
  carries no `purpose`. `deferred_by` was appended; the Decision page holds no purpose. The
  entry stands as it is. No `failed`, no `near`, `unparsed: []` in the two yamls.
- Index check: one create outside estimates, `entity-sprint`, against the Grep
  `^(purpose|deferred_by):` over `wiki/entities/` — 3 lines, one live page
  (`entity-sprint-migration`, the sprint of one id) and two schema examples. Not the same
  page and not a near one: the migration page is the child the entry names. No page
  opened.
- Synthesis, against 32 lesson lines (30 live pages, 2 schema examples) and 13 insight lines
  (12 live, 1 schema example):
  - `lesson-hi-substitution-fails-when-the-login-has-lapsed` and
    `lesson-hi-substitution-refused-when-the-permission-classifier-is-unavailable` (`new`,
    session 1119) share the cause — the `!` command of a skill is checked by a model call,
    and the call fails; the new lesson names the login as the cause the old one saw as
    the classifier's model. No Insight had it. Created
    `insight-hi-skill-substitution-checked-by-a-model-call` (Deferred item 2), both
    lessons `clustered`. The handoff expected this cluster.
  - `lesson-permissions-reading-taken-by-the-agent-who-cannot-see-the-prompt` — no lesson
    or Insight with the cause. Stays `new`.
  - `lesson-lint-schema-body-table-one-section-per-row` — no lesson or Insight with the
    cause. Stays `new`.
  - `lesson-pretask-session-flag-takes-the-id-not-the-hi-line` — no lesson or Insight with
    the cause (`insight-ledger-hi-tied-to-its-session-by-position` is about the event log's
    window, not the flag). Stays `new`.
- Contradiction: `lesson-plan-mode-frontier-refused-on-the-client-text` (root cause: the
  allow list of `settings.json` for `frontier.md`, `spec.md`, `handoff.md` exists "for
  exactly this" and nothing in the harness refuses the write) against
  `lesson-permissions-reading-taken-by-the-agent-who-cannot-see-the-prompt` and case 237
  (in Plan Mode the client asks before every edit outside the plan file, and the allow
  list does not lift that). Both stand `new`; 237 settled the promise in
  `estimate-permissions`, the old lesson is as it was.
- `estimate-permissions`: recut to `pending` by 237 and read `passed` in the same session
  from the person's word (ledger line 12); the page ends `passed`, `checked` 2026-09-18,
  `rule-permissions` `built`. The Result records a prompt in Plan Mode, approved.
- `rule-morph`: the defer of 239 carried no `ref` and the scripts wrote the placeholder page
  `rules/rule-morph.md` (`draft`, `deferred_by: decision-case-239`); the handoff expected
  "a placeholder, no page today". Lint: `deferred: 1 time since case 239`; no schema line
  on it.
- Handoff flags, each a Case of the next Plan Mode:
  1. Slice 3b — `rule-work-mode`, `rule-subagent-guppi` (defer 242, the next session's
     first item), with the sentence of Deferred item 1 written into `rule-work-mode`.
  2. The Proposal of Deferred item 2 — one sentence in `rule-skill-hi` on the refused `!`
     substitution.
  3. `rule-git-context` / `rule-github-issues` (defer 243) at the close of the sprint
     (Deferred items 3, 4).
  4. The person's doubt on the Rule / Entity-Estimate criterion of 240.2, noted in the
     handoff as a caveat, not a change.
- `rule-spec-box` (placeholder): lint `schema: missing field kind`, `missing field
  estimates`, `orphan: no other live page names it in its frontmatter`.
- Stale defers: `rule-work-mode` and `rule-subagent-guppi`, `deferred: 17 times since case
  29` (lint), 21 briefs; on the sprint page, not in Deferred (229.4).
- MOC candidates: none new. `entity-sprint` (MOC, one child) was created by 241.
- The `entities/entity-sprint-migration: schema: missing field children (given kind MOC)`
  line the handoff expected between the one-off and this run is gone after the 241 `set`.
- Lint at the close of the run, 75 findings (81 after the previous run):
  - 62 × `decisions/decision-case-<1–28>: schema: missing section ## Context` /
    `## Problem` (31 pages, the Cases 1–28 — `estimate-sprint-migration-lint-clean`).
  - `rules/rule-spec-box: schema: missing field kind`, `missing field estimates`,
    `orphan: no other live page names it in its frontmatter` (3).
  - `rules/rule-morph: deferred: 1 time since case 239`
  - `rules/rule-subagent-guppi: deferred: 17 times since case 29`
  - `rules/rule-work-mode: deferred: 17 times since case 29`
  - `estimates/estimate-carry-over-writes`, `-render-harness-ticks-the-spec`,
    `-sprint-migration-leftovers-gone`, `-sprint-migration-lint-clean`,
    `-sprint-migration-merges`, `-sprint-renders-the-backlog`: `unread: pending` (6).
  - `estimates: unmigrated: 29 pages in the shape before case 193` (29 before this run).
  - No `render:` line and no `sprint:` line: the first two steps of `make lint` are green.

## Readings at the close

- `make test`: 425 passed.
- `make lint`: 75 findings, exit 1 (the list above).
- Live pages: rules 44, estimates 66, lessons 34, insights 13, decisions 339, entities 2.
  Archived this run: 1 decision page (`decision-case-230`).
