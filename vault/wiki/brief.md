# Brief — 2026-09-20, after session 1749 of 2026-09-20 (the readings due of 1308; the form of a render line named in the schema by 279.1 and refused by pre-spec by 279.2; the skip of a later Case's read line by 280; the lines of a superseded Case out of the Retro count by 282; Slice 3b deferred to 281)

Written by the librarian from `raw/2026-09-20/1749/handoff.md`, the yamls of
`raw/2026-09-20/1749`, `raw/2026-09-20/1308`, `raw/2026-09-20/0958`, `raw/2026-09-20/0740`
and `raw/2026-09-20/0527`, and the Greps of the indexes.

## Where things stand

- Code, commit `3f53aa6` on `migration` (then `5b15281`, one ledger line): `guppi/prespec.py` —
  `OFF_FORM_LINE`, the finding `case N: render line off form: <line>` in `check_tasks`;
  `tests/test_prespec.py` +4. `guppi/generate.py` — `tick_read(specs, slug, skip)`,
  `later_cases`, `Vault.entries`, the skip in `Vault.tick` for `estimate` entries only;
  `tests/test_generate.py` +3. 462 green, style clean. By hand in `raw/2026-09-20/1308/spec.md`:
  the nine `render` lines (97, 131, 187, 258, 312, 366, 575, 626, 692), the checks 863, 575,
  1031, the second `read` lines 577 and 693 — all `[x]`.
- Closed in the session: 278 (superseded by 279.1), 279.1, 279.2, 280, 282; 281 the defer of
  Slice 3b (`rule-work-mode`, `rule-subagent-guppi`, the thirteenth). Readings in the 1749
  ledger, `passed`: `estimate-internal-context-loaded`, `estimate-claude-md-rendered`,
  `estimate-case-protocol-ledger-line-form`, `estimate-agent-writing-followed`,
  `estimate-documentation-completes`, `estimate-prespec-catches-a-command-line-off-form`,
  `estimate-retro-loads`, `estimate-language-followed`; `failed`:
  `estimate-case-protocol-loaded` (line 6, the one Criterion line on the agent restating two
  rules at `/hi`; the line removed by 279.1). Lesson:
  `lesson-spec-render-line-form-unmatched-by-the-ticker` (error).
- Not done by the session's own account: the pages, the three renders and `guppi sprint` —
  this run; the readings of Readings due — the next session; Slice 3b — defer 281.
- Five units in the walk. `raw/2026-09-20/1749`: 22 entries — 20 lifted from the ledger
  (line 19, the reading of `estimate-prespec-catches-a-command-line-off-form`, folded into
  the `create` of line 12) and 2 added at synthesis; all applied but the one `superseded_by`.
  Decisions: 6 pages written (278, 279.1, 279.2, 280, 281, 282), `decision-case-278`
  `superseded` by 279.1 and moved by cleanup to
  `vault/archive/migration/2026-09-20/1749/decisions/`. Rules: 4 updated
  (`rule-case-protocol` 279.1, `rule-prespec` 279.2, `rule-page-generation` 280, `rule-retro`
  282), 2 deferred (`rule-work-mode`, `rule-subagent-guppi` by 281, both marked `exists`).
  Estimates: 1 created (`estimate-prespec-catches-a-command-line-off-form`, `passed` by its
  folded reading), 3 `update` entries applied (`estimate-case-protocol-loaded` 279.1,
  `estimate-generate-ticks-the-spec` 280, `estimate-retro-loads` 282), the `update` of 278
  `superseded_by: 279.1` and not applied, 9 reading lines applied on 9 pages (8 `passed`,
  1 `failed`). Lessons: 1 created, then `clustered` by synthesis. Insights: 1 updated
  (`insight-session-vault-knowledge-not-loaded`, `actioned → open`, `severity` 1). 29 pages
  written or changed. `1308`, `0958`, `0740`, `0527`: 0 new entries. Cleanup moved 1 page.
- The check the handoff asked first held: the entry of 278 carries `superseded_by: '279.1'`
  and stays unapplied; the entry of 279.1 carries the whole Criterion (the text of 278 plus
  the line on the form of the render and sprint lines) and `set.purpose`; only 279.1's
  Decision page and Criterion stand on `estimate-case-protocol-loaded`.
- Statuses computed by `generate`: `rule-agent-writing`, `rule-claude-md`, `rule-documentation`,
  `rule-internal-context`, `rule-language`, `rule-retro` `draft → built` (their Estimates
  `passed`); `rule-case-protocol` stays `draft` (`estimate-case-protocol-loaded` `pending` by
  279.1); `rule-page-generation` stays `draft` (`estimate-generate-ticks-the-spec` `pending`
  by 280, `estimate-generate-rewords` `pending`); `rule-prespec` `built`. `deferred_by` of
  `rule-work-mode` and `rule-subagent-guppi` now ends at `decision-case-281`.
- `guppi render` wrote `vault/wiki/case-schema.md` (279.1), `.claude/skills/pre-spec/SKILL.md`
  (279.2) and `.claude/skills/retro/SKILL.md` (282) — the three the handoff named, no other;
  `uv run guppi render --check` after it exits 0. `guppi sprint` rewrote `vault/wiki/sprint.md`:
  Slice 3b current, both items `draft`, their defers ending at 281.
- The `read` lines ticked by this run's `generate`, the first live run of 280: 1308 line 98
  (`estimate-case-protocol-loaded`, the `failed` reading of line 6 — the line of 279.1 in the
  1749 Spec, line 88, stays `[ ]`); 0958 line 308 (`estimate-documentation-completes`, line 5);
  1308 lines 259, 313, 367, 627, 1090 (`estimate-claude-md-rendered`,
  `estimate-language-followed`, `estimate-agent-writing-followed`,
  `estimate-internal-context-loaded`, `estimate-case-protocol-ledger-line-form`); 1749 line 129
  (`estimate-prespec-catches-a-command-line-off-form`, folded) and line 220
  (`estimate-retro-loads`, line 20) — see Flags for the last.
- Tests: 462 green (`make test`), style clean at `3f53aa6`.

## Readings due

- `estimate-case-protocol-loaded` — `rule-case-protocol` stands `draft` — read at line 88 of
  `raw/2026-09-20/1749/spec.md`: the `/hi` of the next session, by hand; `tests/test_ledger.py`.
  The Criterion is the one of 279.1; the reading of this walk (line 6) `failed` on the line
  279.1 removed, then the `update` set `pending`. Line 39 of the same Spec, under the
  superseded 278, is not its line (282).
- `estimate-generate-ticks-the-spec` — `rule-page-generation` stands `draft` — read at line 179
  of `raw/2026-09-20/1749/spec.md`: pytest; live — the librarian's run of this session. The
  facts of this run stand under Flags.
- `estimate-generate-rewords` — `rule-page-generation` stands `draft` — read at line 745 of
  `raw/2026-09-20/1308/spec.md`: pytest now; live — the first `reword` applied, in a later
  session (case 277.4). No `reword` in this walk. No date.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — by its `method`:
  `make lint`, exit 0 — or only unread lines on the Estimates of `entity-sprint-migration`.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — by its `method`:
  one reading of the tree by hand at the close of the sprint, each path and decision named in
  the estimate line.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — by its `method`:
  `make test` on the last commit of `migration`, then `git log` of `main` after the merge.

No Estimate stands `failed` after `generate`.

## Deferred

1. `insight-session-vault-knowledge-not-loaded` — `severity` 1, `open` (reopened from
   `actioned` this run, the sixth child added), 1 brief. Pattern: a fact the vault holds does
   not reach the session that needs it; only `brief.md`, `CLAUDE.md`, the skills and the agent
   frames are loaded, and everything else waits for a read the agent must first think to make.
   Proposal, as the page has it: a second channel beside the brief — the ledger tail at `/hi`
   (done, 101.2) and a way for a Rule page to name the lessons that bear on it (rejected by
   134: a text to remember is the channel that failed). The new child put the missing fact
   into the loaded text itself (279.1); in Plan Mode a Case whose `recommend` starts from
   the Proposal, ending in an `update` of the Insight (`status: actioned`, `addressed_by`), a
   rejection written the same way, or a `defer` with the Insight as its target.

Left out, the sprint page names them (case 229.4): `rule-work-mode` and
`rule-subagent-guppi` (defer 281 this walk, the thirteenth; 183, 206, 218, 231, 242, 248,
252, 254, 260, 263, 269, 276 before — Slice 3b, the current milestone);
`insight-workflow-code-live-before-the-page-it-reads` (`open`, severity 2, defer 238; in the
text of the `rule-work-mode` item); `rule-git-context`, `rule-github-issues` (in the text of
the `estimate-sprint-migration-merges` item, Slice 5); `rule-spec-box` (Slice 5); `rule-morph`
(Slice 5).

## Flags

- The reading of `estimate-retro-loads` (1749 ledger line 20) ticked line 220 of the 1749 Spec,
  under Case 282, and left line 132 of the 1308 Spec `[ ]`; the handoff expected the reverse,
  "L20, before 282's decision lines". In the yaml the entries of 282 stand at lines 17 and 18,
  before the reading at line 20, so 282 is not a later Case by the rule of 280 (`later_cases`:
  the first decision entry with a `line` greater than the reading's), and its `read` line is
  the first unticked one in the Spec beside the yaml. The three expectations written into the
  Criterion line 179 of the 1749 Spec held: 1308:98 ticked, 1749:88 open, 0958:308 ticked.
  Not repaired.
- `estimate-retro-loads` stands `passed`, not `pending` as the handoff expected: the `update`
  of 282 (yaml line 18) replaced the Criterion and set `pending`, and the reading of line 20,
  applied after it in the same run, set `passed` — the Result measures the Criterion of 270.3
  while the page carries the Criterion of 282. `rule-retro` moved `draft → built` on it. The
  same shape as `estimate-generate-ticks-the-spec` after the last run; 1308 line 132 stays
  `[ ]` for a reading of the new Criterion.
- `estimate-case-protocol-loaded`: `failed` by the reading of line 6, then `pending` by the
  `update` of 279.1 in the same run; the History carries both. The `failed` was on the one
  Criterion line 279.1 removed (the agent restating two rules at `/hi`); no lesson, by the
  handoff: a stale line, not an act of the agent.
- Index check: the one `create` with an index is the lesson; the Grep
  `^(root_cause|deferred_by):` over `vault/wiki/lessons/` returned 42 lines. None names the
  form of a task line or a fact held by one Rule page and absent from the text the Spec is
  written from; the nearest by subject, `lesson-spec-change-text-quotes-a-wikilink-bare` (one
  string of the agent's writing left unchecked) and
  `lesson-spec-change-line-with-a-colon-breaks-the-then-block` (a YAML form error of the
  `then` block), are other causes. The lesson stands as a `create`; no `near`.
- Synthesis: the Greps `^(root_cause|deferred_by):` over `vault/wiki/lessons/` (42 lines) and
  `^(pattern|deferred_by):` over `vault/wiki/insights/` (16 lines).
  `insight-session-vault-knowledge-not-loaded` (page read: Pattern and History) — the same
  pattern: the form of a render line is fixed in `rule-render-harness` (case 235), a page the
  vault holds, and in no text the agent writes the Spec from; clustered — the Insight reopened
  `actioned → open`, `children` plus the lesson, the lesson `clustered` with `insight` set.
  `insight-workflow-contract-change-leaves-its-derived-text-stale` (page read: Pattern) — not
  the same: its children are one contract in two places with one changed; the render form
  never changed and the schema paragraph was written without it. Both entries carry
  `librarian: synthesis`; `generate` applied both, no stderr.
- The five older children of `insight-session-vault-knowledge-not-loaded` are archived
  (the cascade of 134); `severity` is 1, the live child alone. The `addressed_by` of 134
  stands on the page beside `status: open`.
- Two `exists` marks on the defers of 281 (expected: a `defer` with a `ref`). No entry marked
  `incomplete`, `failed` or `unparsed` in the five yamls; no failed Estimate; no MOC candidate.
- The lines 779–783 of the 1308 Spec (`[ ]`) belong to the superseded 274.2 and are not debt
  (282, from the handoff); the lines 38–39 of the 1749 Spec belong to the superseded 278, the
  same. Line 745 of 1308 waits for the first `reword`.
- The handoff's note on `guppi/generate.py`: the working copy holds CRLF, the committed blob
  LF; a diff of line endings only is that.
- Lint, gone since the previous brief: 6 `unread: pending` (the readings of this walk).
  `unmigrated` stays 23.
- Standing: the defer of 238 on `insight-workflow-code-live-before-the-page-it-reads` without a
  `purpose`; `estimate-hi-no-read-calls` in the shape before case 193 by choice;
  `rule-spec-box` placeholder findings (`kind`, `estimates`, orphan).
- Stale defers by lint: `rule-work-mode` and `rule-subagent-guppi` 25 times since case 29;
  `rule-morph` 1 time since case 239.
- Lint, 75 findings: 2 `rules/rule-spec-box` schema (`kind`, `estimates`) and 1 orphan;
  62 `decisions/decision-case-<1–28>` missing `## Context` and `## Problem` (31 pages,
  Slice 5); 3 deferred (`rule-morph` 1, `rule-subagent-guppi` 25, `rule-work-mode` 25);
  6 unread pending (`estimate-case-protocol-loaded`, `estimate-generate-rewords`,
  `estimate-generate-ticks-the-spec`, the three sprint Estimates);
  `estimates: unmigrated: 23 pages in the shape before case 193`.

## Next session

Cases

- Slice 3b — `rule-work-mode`, `rule-subagent-guppi` (defer 281, the thirteenth), with the
  sentence of `insight-workflow-code-live-before-the-page-it-reads` written into
  `rule-work-mode`; from the handoff and the sprint page.
- `estimate-retro-loads` `passed` on the Criterion of 270.3 while the page carries the
  Criterion of 282, and `rule-retro` `built` on it — from the Flags of this run; whether the
  reading at 1308 line 132 settles it or the order of an `update` and a reading of one session
  in `generate` is a contract question.
- The handoff's expectation on the tick of `estimate-retro-loads` (1308:132) against the yaml's
  order (282 at lines 17–18, the reading at 20) — from the Flags; a fact for the reading of
  `estimate-generate-ticks-the-spec`, a Case only if that reading finds the rule of 280 wrong.
- `insight-session-vault-knowledge-not-loaded` `open` again (Deferred, item 1): a Case from its
  Proposal, or a rejection or a `defer` — from the synthesis of this run.

Work

- Read `estimate-case-protocol-loaded` at the `/hi` (1749 line 88),
  `estimate-generate-ticks-the-spec` by this run's ticks (1749 line 179).
- Read `estimate-retro-loads` at the first `/retro` after this render (1308 line 132, the
  line left `[ ]`).
- Read `estimate-generate-rewords` at the first `reword` (1308 line 745); no date.
- Read `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-leftovers-gone`,
  `estimate-sprint-migration-merges` — at the close of the sprint, by their `method`.
- No ledger line of the walk left unapplied; the tree is clean after the commit of this run.

## Readings at the close

- `make test`: 462 passed.
- `make lint`: 75 findings, exit 1 (the list above).
- Pages: entities 2, rules 46, estimates 73, lessons 41, insights 14, decisions 395.
