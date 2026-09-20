# Brief — 2026-09-20, after session 1308 of 2026-09-20 (the tick on a reading by 270, the Case schema as a Render of `rule-case-protocol` by 273, `rule-language` and `rule-agent-writing` out of `rule-claude-md` by 272, `reword` by 274, Slice 3b deferred to 276)

Written by the librarian from `raw/2026-09-20/1308/handoff.md`, the yamls of
`raw/2026-09-20/1308`, `raw/2026-09-20/0958`, `raw/2026-09-20/0740` and
`raw/2026-09-20/0527`, and the Greps of the indexes.

## Where things stand

- Code, commit `10baf3d` on `migration`: `guppi/generate.py` — `READ_LINE`, `tick_read`,
  `raw_specs`, `Vault.tick` on estimate entries and folded creates (270.1);
  `REWORD_CATEGORIES`, `REWORD_FIELDS`, `Vault.owner_text`, `reword_text`, `reword_pairs`,
  `reword` among the update keys (274.1). `guppi/materialize.py` — `reword` carried as a
  list of pairs, `incomplete: [reword]` otherwise (274.3). Tests: `tests/test_generate.py`
  +6 and +5, `tests/test_materialize.py` +1, `tests/test_render.py` +1. 455 green, style
  clean. By hand: `vault/wiki/index.md` (8 places), `glossary.md` (3 rows), `rules/schema.md`
  (3), `entities/schema.md` (2), `estimates/schema.md` (1), `decisions/schema.md` (1),
  `case-schema.md` (the tick sentence of 270.2, two `pre-spec`; overwritten by the render
  with the same words). W5: the boxes of 0958 lines 191, 249, 432 and 0740 line 172 ticked
  by hand.
- Closed in the session: 270.1–270.3, 271, 272.1–272.3, 273.1–273.3, 274.1, 274.3, 275,
  277.1–277.6; 274.2 superseded by 277.4; 276 the defer of Slice 3b (`rule-work-mode`,
  `rule-subagent-guppi`, the twelfth). Readings `passed`, all in the 1308 ledger:
  `estimate-documentation-completes`, `estimate-brief-written`, `estimate-hi-writes-frontier`
  (W1–W3 of 0958), `estimate-generate-ticks-the-spec`, `estimate-materialize-assembles`,
  `estimate-case-protocol-case-form` (Retro, two departures named in the line). Lessons:
  `lesson-work-mode-check-widened-the-list-and-the-agent-acted` (error),
  `lesson-reword-pairs-signed-before-the-places-were-read` (error).
- Not done by the session's own account: the pages, the renders and `guppi sprint` — this
  run; the readings of Readings due — the next session; `estimate-generate-rewords` — the
  first `reword`, no `reword` in this yaml (274.2 superseded); the `grep` checks of Spec 1308
  lines 783, 863, 1028 and the diff of the first rendered `case-schema.md` (line 575) — the
  next session; Slice 3b — defer 276.
- Four units in the walk. `raw/2026-09-20/1308`: 57 entries, all applied or superseded —
  decisions: 21 pages written (270.1–277.6), 1 of them archived by cleanup
  (`decision-case-274.2`, superseded); rules: 2 created (`rule-language`,
  `rule-agent-writing`, both `draft`, children of `rule-claude-md`), 16 `update` entries on
  12 pages (`rule-page-generation` 270.1 then 274.1, `rule-case-protocol` 270.2 then 273.1,
  `rule-claude-md` 272.1 then 273.3, `rule-materialize` 274.3 then 277.1, `rule-retro`,
  `rule-documentation`, `rule-plan-mode`, `rule-internal-context`, `rule-ledger-write`,
  `rule-ask`, `rule-index-check`, `rule-brief`), 2 deferred (`rule-work-mode`,
  `rule-subagent-guppi` by 276); estimates: 3 created (`estimate-language-followed`,
  `estimate-agent-writing-followed`, `estimate-generate-rewords`, all `pending`), 11 `update`
  entries on 9 pages (`estimate-case-protocol-loaded` 270.2 then 273.1,
  `estimate-claude-md-rendered` 272.1 then 273.3, `estimate-generate-ticks-the-spec`,
  `estimate-retro-loads`, `estimate-documentation-completes`, `estimate-internal-context-loaded`,
  `estimate-materialize-assembles`, `estimate-case-protocol-case-form`,
  `estimate-case-protocol-ledger-line-form`), 6 reading lines applied on 6 pages (lines 8–10,
  53–55, all `passed`); lessons: 2 created (`new`), 1 updated
  (`lesson-spec-change-text-quotes-a-wikilink-bare`, 275); entities: 1 updated
  (`entity-sprint-migration`, 277.4); 9 Rule-class file entries marked applied by hand
  (`case-schema`, `glossary` ×2, `index` ×2, `rules-schema`, `entities-schema`,
  `estimates-schema`, `decisions-schema`); the 4 entries of 274.2 `superseded_by: 277.4`,
  none applied. 56 pages written or changed. `0958`, `0740`, `0527`: 0 new entries. Cleanup
  moved 1 page.
- The order the handoff named held: `rule-claude-md` carries
  `children: [rule-language, rule-agent-writing]`, `rule-case-protocol` carries
  `governs: vault/wiki/case-schema.md`, `render_mode: full`, `parent: rule-plan-mode`;
  `rule-plan-mode`'s `children` end in `rule-case-protocol`. `render` wrote nothing to
  stderr.
- Statuses computed by `generate`: `rule-brief` and `rule-skill-hi` `draft → built` (W2, W3
  `passed`); `rule-case-protocol`, `rule-retro`, `rule-claude-md`, `rule-internal-context`,
  `rule-page-generation` `built → draft` (one Estimate each `pending`); `rule-documentation`
  stays `draft` (its reading `passed` at line 8, then 271 replaced the Criterion and set it
  `pending` again); `rule-materialize`, `rule-plan-mode`, `rule-ledger-write`, `rule-ask`,
  `rule-index-check`, `rule-prespec` stand `built`. `deferred_by` of `rule-work-mode` and
  `rule-subagent-guppi` now ends at `decision-case-276`.
- `guppi render` wrote `CLAUDE.md` (58 lines), `.claude/agents/librarian-guppi.md`,
  `.claude/skills/hi/SKILL.md`, `.claude/skills/retro/SKILL.md` and, for the first time
  from a Rule page, `vault/wiki/case-schema.md` (136 lines) — the five the handoff named,
  no other; `uv run guppi render --check` after it exits 0. `guppi sprint` rewrote
  `vault/wiki/sprint.md`: Slice 3b current, both items `draft`, their defers ending at 276.
- The `read` lines after `generate`: ticked by this run — 0958 lines 488
  (`estimate-brief-written`) and 544 (`estimate-hi-writes-frontier`); 1308 lines 56
  (`estimate-generate-ticks-the-spec`), 188 (`estimate-documentation-completes`), 829
  (`estimate-materialize-assembles`), 1063 (`estimate-case-protocol-case-form`). Not
  ticked: 0958 line 308 (`estimate-documentation-completes`, W1) — see Flags.
- Tests: 455 green (`make test`), style clean at `10baf3d`.

## Readings due

- `estimate-documentation-completes` — `rule-documentation` stands `draft` — read at line
  308 of `raw/2026-09-20/0958/spec.md`: `make test-documentation`; live — the librarian's run
  of this session, read in the next. This run is that reading's object; the Criterion is the
  one 271 replaced.
- `estimate-case-protocol-loaded` — `rule-case-protocol` stands `draft` — read at lines 98
  and 577 of `raw/2026-09-20/1308/spec.md`: the first turn after the `/hi` of the next
  session, by hand; `tests/test_ledger.py`. One reading; the second line closes by hand at
  the next Retro.
- `estimate-case-protocol-ledger-line-form` — `rule-case-protocol` stands `draft` — read at
  line 1090 of the 1308 Spec: `case-schema.md` and `index.md` §4 after the render, by hand.
- `estimate-retro-loads` — `rule-retro` stands `draft` — read at line 132 of the 1308 Spec:
  the first `/retro` after the render, by hand.
- `estimate-claude-md-rendered` — `rule-claude-md` stands `draft` — read at lines 259 and
  693 of the 1308 Spec: `uv run guppi render` and `--check` after the build; the next session
  start, by hand. One reading; the second line closes by hand at the next Retro. Fact of this
  run: `render --check` exit 0.
- `estimate-language-followed` — `rule-language` stands `draft` — read at line 313 of the
  1308 Spec: the next session, by hand — the section in `CLAUDE.md`, the commit, the Spec and
  the chat of the session.
- `estimate-agent-writing-followed` — `rule-agent-writing` stands `draft` — read at line 367
  of the 1308 Spec: the next session, by hand — the section in `CLAUDE.md` and one reply of
  the agent against it.
- `estimate-internal-context-loaded` — `rule-internal-context` stands `draft` — read at line
  627 of the 1308 Spec: the `/hi` of the next session, by hand.
- `estimate-generate-rewords` — `rule-page-generation` stands `draft` — read at line 745 of
  the 1308 Spec: pytest now; live — the first `reword` applied, in a later session (case
  277.4). No date.
- `estimate-sprint-migration-lint-clean` — `entity-sprint-migration` — by its `method`:
  `make lint`, exit 0 — or only unread lines on the Estimates of `entity-sprint-migration`.
- `estimate-sprint-migration-leftovers-gone` — `entity-sprint-migration` — by its `method`:
  one reading of the tree by hand at the close of the sprint, each path and decision named in
  the estimate line.
- `estimate-sprint-migration-merges` — `entity-sprint-migration` — by its `method`:
  `make test` on the last commit of `migration`, then `git log` of `main` after the merge.

No Estimate stands `failed`.

## Deferred

Nothing stands in the list.

Left out, the sprint page names them (case 229.4): `rule-work-mode` and
`rule-subagent-guppi` (defer 276 this walk, the twelfth; 183, 206, 218, 231, 242, 248,
252, 254, 260, 263, 269 before — Slice 3b, the current milestone);
`insight-workflow-code-live-before-the-page-it-reads` (`open`, severity 2, defer 238; in the
text of the `rule-work-mode` item); `rule-git-context`, `rule-github-issues` (defers 220,
243; Slice 5); `rule-spec-box` (defers 207, 219, 232; Slice 5); `rule-morph` (defer 239;
Slice 5).

## Flags

- The `read` line 308 of `raw/2026-09-20/0958/spec.md` (`estimate-documentation-completes`,
  W1) stays `[ ]` after this run; the handoff expected it ticked. The reading (1308 ledger
  line 8) ticked line 188 of the 1308 Spec instead — the first unticked `read` line of that
  slug in the Spec beside the yaml, which the text of 270.1 takes first, then the other
  sessions of `raw/`. One reading, one tick; the 0958 line was the second. The Estimate is
  `pending` again by 271, so line 308 is also its Readings due line. Not repaired.
- The other five `read` lines the handoff named were ticked by `generate` (0958 lines 488,
  544; 1308 lines 56, 829, 1063 — the handoff's 1060). The mechanism of 270.1 ran live for
  the first time.
- Two `read` lines each for `estimate-case-protocol-loaded` (1308 lines 98, 577) and
  `estimate-claude-md-rendered` (259, 693), all four `[ ]`: one reading each, the second line
  closes by hand at the next Retro (from the handoff).
- 274.2: its four entries (`rule-prespec`, `index`, `entities-schema`, `estimates-schema`)
  carry `superseded_by: 277.4`, none applied; `decision-case-274.2` written `superseded` and
  moved by cleanup to `vault/archive/migration/2026-09-20/1308/decisions/`. No `reword`
  applied this run; `estimate-generate-rewords` `pending`, `rule-page-generation` `draft`.
- Index check: the Grep `^(purpose|deferred_by):` over `vault/wiki/rules/` returned 54
  lines; no line names the language of the repository or the agent's writing; `rule-claude-md`
  ("the system prompt holding a line nobody ratified") is the parent, not the same or near.
  `rule-language` and `rule-agent-writing` stand as creates; no `near`.
- Synthesis: the Greps `^(root_cause|deferred_by):` over `vault/wiki/lessons/` (42 lines)
  and `^(pattern|deferred_by):` over `vault/wiki/insights/` (16 lines).
  `lesson-work-mode-check-widened-the-list-and-the-agent-acted` against
  `lesson-agent-memory-is-not-the-product`: the causes differ — a preference put into a
  per-machine memory against a Case, and a check whose outcome widened the ratified list and
  the agent acted on the fork; no live lesson on a fork returning as a Case stands in the
  index; `insight-workflow-contract-change-leaves-its-derived-text-stale` (a dependent text
  no step names) is about the stale text, not the agent's act.
  `lesson-reword-pairs-signed-before-the-places-were-read` against
  `lesson-spec-change-text-quotes-a-wikilink-bare` (its Trigger and Root cause read): the
  wikilink lesson's cause is one string of the agent's own writing left unchecked; the reword
  lesson's is every place found by count and none read for meaning — a word is not a slug.
  Not the same cause; the candidate "the place the Case is about and not the others" does
  not hold for the second, where every place was found. `lesson-pretask-dispatch-summarized-the-plan-and-ask-guppi-judged-the-summary`
  (a judgment on a paraphrase) is the nearest by shape, its cause the dispatch's form and the
  reading of `rule-ask`. No cluster; both lessons stay `new`.
- `estimate-documentation-completes`: its reading of this walk `passed` (line 8) and 271's
  `update` replaced the Criterion after it in the same run, so the page stands `pending` with
  a `passed` Result of the old Criterion in its History. `estimate-generate-ticks-the-spec`,
  `estimate-materialize-assembles`, `estimate-case-protocol-case-form`: the `update` set
  `pending` and the reading of the same session passed it in one run — `passed`.
- Two `exists` marks on the defers of 276 (expected: a `defer` with a `ref`). No entry
  marked `incomplete`, `failed` or `unparsed` in the four yamls; no failed Estimate; no MOC
  candidate.
- The render changed `.claude/agents/librarian-guppi.md` during this run; this run ran by
  the frame it was dispatched with, the next run by the rendered one.
- Lint, gone since the previous brief: the `ref` finding on
  `lesson-spec-change-text-quotes-a-wikilink-bare` (275 applied). `unmigrated` 25 → 23.
- Standing: the defer of 238 on `insight-workflow-code-live-before-the-page-it-reads`
  without a `purpose`; `estimate-hi-no-read-calls` in the shape before case 193 by choice;
  `rule-spec-box` placeholder findings (`kind`, `estimates`, orphan).
- Stale defers by lint: `rule-work-mode` and `rule-subagent-guppi` 24 times since case 29;
  `rule-morph` 1 time since case 239.
- Lint, 81 findings: 2 `rules/rule-spec-box` schema (`kind`, `estimates`) and 1 orphan;
  62 `decisions/decision-case-<1–28>` missing `## Context` and `## Problem` (31 pages,
  Slice 5); 3 deferred (`rule-morph` 1, `rule-subagent-guppi` 24, `rule-work-mode` 24);
  12 unread pending (the Readings due); `estimates: unmigrated: 23 pages in the shape
  before case 193`.

## Next session

Cases

- Slice 3b — `rule-work-mode`, `rule-subagent-guppi` (defer 276, "the first item of the next
  session"), with the sentence of `insight-workflow-code-live-before-the-page-it-reads`
  written into `rule-work-mode`; from the handoff and the sprint page.
- Which `read` line a reading closes when two Specs carry one for the same Estimate: this
  run ticked 1308 line 188 and left 0958 line 308, the line the handoff expected — from the
  Flags of this run; a contract question on 270.1 or a by-hand tick.
- A line in `rule-claude-md` that the agent writes no local memory — from the previous
  brief and `lesson-agent-memory-is-not-the-product`; not among the Cases of 1308.
- The agent's behaviour after the Case schema left `CLAUDE.md` (273): the handoff names a
  change as an `error` lesson and a Case, not a repair — from the handoff; a Case only if the
  reading of `estimate-case-protocol-loaded` finds one.

Work

- Read `estimate-case-protocol-loaded` (1308 lines 98, 577), `estimate-internal-context-loaded`
  (627), `estimate-language-followed` (313), `estimate-agent-writing-followed` (367),
  `estimate-claude-md-rendered` (259, 693), `estimate-case-protocol-ledger-line-form` (1090),
  `estimate-retro-loads` (132), `estimate-documentation-completes` (0958 line 308).
- Read `estimate-generate-rewords` at the first `reword` (1308 line 745); no date.
- Read `estimate-sprint-migration-lint-clean`, `estimate-sprint-migration-leftovers-gone`,
  `estimate-sprint-migration-merges` — at the close of the sprint, by their `method`.
- The unticked boxes of the 1308 Spec named by the handoff for the next session: the `grep`
  checks of lines 783, 863, 1028 and the diff of the first rendered `case-schema.md` (575);
  the second `read` lines 577 and 693 at the next Retro.
- No ledger line of the walk left unapplied; the tree is clean after the commit of this run.

## Readings at the close

- `make test`: 455 passed.
- `make lint`: 81 findings, exit 1 (the list above).
- Pages: entities 2, rules 46, estimates 72, lessons 40, insights 14, decisions 390.
